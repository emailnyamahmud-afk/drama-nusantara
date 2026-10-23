#!/usr/bin/env python3
"""
Nusantara Render v2 — TUI untuk user awam
Features:
  - Menu berwarna, progress bar, panel informatif
  - Generate TTS (edge-tts, free unlimited)
  - Stitch image + TTS + BGM auto-fill (no silent gaps!)
  - Render final MP4
  - Preview per segmen
  - Re-render single segmen (iterate)

Setup:
    pip3 install edge-tts rich
    brew install ffmpeg

Run:
    cd drama-nusantara
    python3 scripts/nusantara-render.py
"""
import json
import subprocess
import os
import sys
import asyncio
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.layout import Layout
from rich.text import Text

console = Console()

# ============================================================
# Paths
# ============================================================
ROOT = Path(__file__).parent.parent
TTS_DIR = ROOT / "produksi/tts-output"
FINAL_DIR = ROOT / "produksi/final"
IMAGE_DIR = ROOT / "produksi/t2i-output"
BGM_DIR = ROOT / "produksi/bgm-library"
TEMP_DIR = ROOT / "download/temp-render"

for d in [TTS_DIR, FINAL_DIR, BGM_DIR, TEMP_DIR]:
    d.mkdir(parents=True, exist_ok=True)


# ============================================================
# Helpers
# ============================================================
def find_jsons():
    """Cari semua JSON di produksi/pra-produksi/."""
    files = list(ROOT.glob("produksi/pra-produksi/**/*v3*.json"))
    files += list(ROOT.glob("produksi/pra-produksi/**/*final*.json"))
    return sorted(set(files), key=lambda p: p.name)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True
    )
    return float(r.stdout.strip()) if r.stdout.strip() else 0


def ken_burns_filter(effect, dur, w=1920, h=1080):
    frames = int(dur * 24)
    if effect == "zoom_in_slow":
        return f"scale={w*2}:{h*2}:force_original_aspect_ratio=increase,crop={w*2}:{h*2},zoompan=z='min(zoom+0.0008,1.10)':d={frames}:s={w}x{h}:fps=24,format=yuv420p"
    elif effect == "zoom_in_fast":
        return f"scale={w*2}:{h*2}:force_original_aspect_ratio=increase,crop={w*2}:{h*2},zoompan=z='min(zoom+0.0025,1.25)':d={frames}:s={w}x{h}:fps=24,format=yuv420p"
    elif effect == "zoom_out_slow":
        return f"scale={w*2}:{h*2}:force_original_aspect_ratio=increase,crop={w*2}:{h*2},zoompan=z='if(eq(on,0),1.15,max(zoom-0.0008,1.0))':d={frames}:s={w}x{h}:fps=24,format=yuv420p"
    elif effect == "pan_right_slow":
        return f"scale={w*2}:{h*2}:force_original_aspect_ratio=increase,crop={w*2}:{h*2},zoompan=z=1.0:x='iw/2-{w}/2+(iw-{w})*on/{frames}/2':y='ih/2-{h}/2':d={frames}:s={w}x{h}:fps=24,format=yuv420p"
    else:
        return f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},format=yuv420p"


def check_deps():
    """Cek dependencies terinstall."""
    deps = []
    # edge-tts
    try:
        import edge_tts
        deps.append(("edge-tts", True))
    except ImportError:
        deps.append(("edge-tts", False))
    # ffmpeg
    r = subprocess.run(["which", "ffmpeg"], capture_output=True, text=True)
    deps.append(("ffmpeg", bool(r.stdout.strip())))
    return deps


# ============================================================
# TTS Generation
# ============================================================
async def gen_tts_one(text, voice, rate, pitch, output):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(output))


async def gen_tts_batch(data, tts_dir):
    segments = data.get("segments", [])
    voices = data.get("voice_profiles", {})
    tts_dir.mkdir(parents=True, exist_ok=True)

    results = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TextColumn("[bold]{task.completed}/{task.total}"),
        console=console,
    ) as prog:
        task = prog.add_task("Generating TTS...", total=len(segments))
        for seg in segments:
            sid = seg["segment_id"]
            tts = seg.get("tts", {})
            text = tts.get("text", "")
            speaker = tts.get("speaker", "narrator")
            vp = voices.get(speaker, voices.get(tts.get("voice_profile", "narrator"), {}))
            voice = vp.get("edge_tts_voice", "id-ID-ArdiNeural")
            rate = vp.get("default_rate", "+25%")
            pitch = vp.get("default_pitch", "+0Hz")
            out = tts_dir / f"{sid}.mp3"

            if text.strip():
                prog.update(task, description=f"TTS: {sid} ({speaker})")
                await gen_tts_one(text, voice, rate, pitch, out)
                dur = get_duration(out)
                results.append({"seg": sid, "dur": dur, "path": str(out), "ok": True})
            else:
                results.append({"seg": sid, "dur": 0, "path": None, "ok": False})
            prog.advance(task)

    # Summary table
    table = Table(title="TTS Results", show_header=True)
    table.add_column("Segment", style="cyan")
    table.add_column("Duration", justify="right", style="green")
    table.add_column("Status")
    for r in results:
        status = "[green]✓" if r["ok"] else "[red]✗ (no text)"
        table.add_row(r["seg"], f"{r['dur']:.1f}s", status)
    console.print(table)
    return results


# ============================================================
# BGM Library
# ============================================================
def show_bgm_library():
    """Tampilkan BGM yang tersedia."""
    bgms = list(BGM_DIR.glob("*.mp3")) + list(BGM_DIR.glob("*.wav"))
    if not bgms:
        console.print(Panel(
            "[yellow]Belum ada BGM di folder:[/]\n"
            f"  {BGM_DIR}\n\n"
            "[bold]Cara download BGM:[/]\n"
            "  1. Buka https://studio.youtube.com → Audio Library\n"
            "  2. Filter: No attribution required\n"
            "  3. Search: gamelan, ambient, cinematic, tribal\n"
            "  4. Download MP3\n"
            "  5. Save ke folder bgm-library/\n\n"
            "Atau dari Pixabay Music:\n"
            "  https://pixabay.com/music/\n"
            "  (free, no attribution)",
            title="🎵 BGM Library Kosong", border_style="yellow"
        ))
        return []
    
    table = Table(title="BGM Library", show_header=True)
    table.add_column("#", style="cyan")
    table.add_column("File", style="white")
    table.add_column("Duration", justify="right", style="green")
    for i, b in enumerate(bgms, 1):
        dur = get_duration(b)
        table.add_row(str(i), b.name, f"{dur:.0f}s")
    console.print(table)
    return bgms


def select_bgm_for_scene(scene_name, bgms):
    """User pilih BGM untuk scene tertentu."""
    if not bgms:
        return None
    console.print(f"\n[cyan]Pilih BGM untuk scene: {scene_name}[/]")
    for i, b in enumerate(bgms, 1):
        console.print(f"  [{i}] {b.name}")
    console.print(f"  [0] Skip (no BGM)")
    choice = IntPrompt.ask("[yellow]Nomor", default=0)
    if 1 <= choice <= len(bgms):
        return bgms[choice - 1]
    return None


# ============================================================
# Stitch with BGM
# ============================================================
def build_segment_with_bgm(seg, tts_path, tts_dur, image_path, output_path, bgm_path=None, bgm_vol=0.15):
    """Build 1 segment: image (Ken Burns) + TTS + BGM fill."""
    cue_dur = seg.get("srt_timing", {}).get("cue_duration", seg.get("srt_timing", {}).get("duration_seconds", 30))
    kb = seg.get("image", seg.get("t2i", {})).get("ken_burns", "zoom_in_slow")
    vf = ken_burns_filter(kb, cue_dur)

    if bgm_path and bgm_path.exists():
        # TTS + BGM: mix 3 layers
        # [1:a] = TTS (vol 1.0), [2:a] = BGM (vol 0.15, loop, fade)
        af = (f"[1:a]volume=1.0,apad=whole_dur={cue_dur}[tts];"
              f"[2:a]aloop=loop=-1:size=2e9,volume={bgm_vol},"
              f"afade=t=in:st=0:d=2.0,afade=t=out:st={cue_dur-2.0}:d=2.0,"
              f"atrim=duration={cue_dur}[bgm];"
              f"[tts][bgm]amix=inputs=2:duration=first:dropout_transition=0[a]")
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", str(image_path),
            "-i", str(tts_path),
            "-i", str(bgm_path),
            "-filter_complex", f"[0:v]{vf}[v];{af}",
            "-map", "[v]", "-map", "[a]",
            "-t", str(cue_dur),
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k",
            str(output_path)
        ]
    else:
        # TTS only: pad silence
        af = f"[1:a]apad=whole_dur={cue_dur}[a]"
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", str(image_path),
            "-i", str(tts_path),
            "-filter_complex", f"[0:v]{vf}[v];{af}",
            "-map", "[v]", "-map", "[a]",
            "-t", str(cue_dur),
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k",
            str(output_path)
        ]

    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0


def concat_mp4s(paths, output):
    list_file = output.parent / "concat_list.txt"
    with open(list_file, "w") as f:
        for p in paths:
            f.write(f"file '{p}'\n")
    r = subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(output)],
        capture_output=True, text=True
    )
    list_file.unlink()
    return r.returncode == 0


# ============================================================
# Menu Functions
# ============================================================
def show_banner():
    console.print(Panel(
        "[bold cyan]🏠 Nusantara Render v2[/]\n"
        "[dim]TTS + Stitch + BGM → MP4 untuk DaVinci Resolve[/]\n"
        "[dim]Pipeline: JSON → TTS → ffmpeg → MP4[/]",
        border_style="cyan", padding=1
    ))


def show_status(data, json_path):
    """Tampilkan status asset."""
    ep_id = data.get("episode", {}).get("id", "?")
    segs = data.get("segments", [])
    tts_dir = TTS_DIR / ep_id
    img_dirs = list(IMAGE_DIR.glob("*/storyboard-frame/"))
    
    tts_count = len(list(tts_dir.glob("*.mp3"))) if tts_dir.exists() else 0
    img_count = sum(len(list(d.glob("*.jpg"))) for d in img_dirs) if img_dirs else 0
    bgm_count = len(list(BGM_DIR.glob("*.mp3"))) + len(list(BGM_DIR.glob("*.wav")))
    
    table = Table(title="📊 Status", show_header=True, header_style="bold")
    table.add_column("Asset", style="cyan")
    table.add_column("Count", justify="right")
    table.add_column("Status")
    table.add_row("JSON", f"{len(segs)} segmen", f"[green]{json_path.name}")
    table.add_row("TTS MP3", f"{tts_count}/{len(segs)}", "[green]✓" if tts_count >= len(segs) else "[red]✗")
    table.add_row("Image JPG", f"{img_count}", "[green]✓" if img_count >= len(segs) else "[red]✗")
    table.add_row("BGM tracks", f"{bgm_count}", "[green]✓" if bgm_count > 0 else "[yellow]⚠ (opsional)")
    console.print(table)


def menu_tts(data, json_path):
    """[1] Generate TTS."""
    ep_id = data.get("episode", {}).get("id", "unknown")
    tts_dir = TTS_DIR / ep_id
    console.print(f"\n[bold green]🎵 Generate TTS untuk {ep_id}[/]")
    console.print(f"   Output: {tts_dir}")
    console.print(f"   Voice: edge-tts (free, native Jawa)\n")
    asyncio.run(gen_tts_batch(data, tts_dir))


def menu_stitch(data, json_path):
    """[2] Stitch image + TTS (+ BGM jika ada)."""
    ep_id = data.get("episode", {}).get("id", "unknown")
    segs = data.get("segments", [])
    tts_dir = TTS_DIR / ep_id
    temp_dir = TEMP_DIR / ep_id
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Find images
    img_dirs = list(IMAGE_DIR.glob("*/storyboard-frame/"))
    if not img_dirs:
        console.print("[red]❌ Tidak ada image di produksi/t2i-output/*/storyboard-frame/")
        return None
    img_dir = img_dirs[0]
    
    # BGM selection
    bgms = list(BGM_DIR.glob("*.mp3")) + list(BGM_DIR.glob("*.wav"))
    use_bgm = False
    bgm_path = None
    if bgms:
        console.print(f"\n[yellow]BGM tersedia: {len(bgms)} tracks[/]")
        if Confirm.ask("[yellow]Pakai BGM untuk fill silent gaps?", default=True):
            use_bgm = True
            bgm_path = bgms[0]  # Default: pakai track pertama
            if len(bgms) > 1:
                bgm_path = select_bgm_for_scene("all segments", bgms) or bgm_path
            console.print(f"   [green]BGM: {bgm_path.name}")
    else:
        console.print("\n[yellow]⚠ Tidak ada BGM. Silent gaps akan tetap ada.")
        console.print("   Download BGM ke produksi/bgm-library/ untuk fix silent gaps.")
    
    console.print(f"\n[bold green]🎬 Stitch {len(segs)} segmen[/]")
    console.print(f"   Image: {img_dir}")
    console.print(f"   TTS: {tts_dir}")
    if use_bgm:
        console.print(f"   BGM: {bgm_path.name} (vol 0.15, loop, fade in/out)")
    
    seg_paths = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TextColumn("[bold]{task.completed}/{task.total}"),
        console=console,
    ) as prog:
        task = prog.add_task("Stitching...", total=len(segs))
        for seg in segs:
            sid = seg["segment_id"]
            img = img_dir / f"{sid}.jpg"
            tts = tts_dir / f"{sid}.mp3"
            out = temp_dir / f"{sid}.mp4"
            
            if not img.exists():
                prog.update(task, description=f"[red]Missing: {sid}.jpg")
                prog.advance(task)
                continue
            if not tts.exists():
                prog.update(task, description=f"[red]Missing: {sid}.mp3")
                prog.advance(task)
                continue
            
            tts_dur = get_duration(tts)
            prog.update(task, description=f"Stitch: {sid} ({tts_dur:.1f}s)")
            
            ok = build_segment_with_bgm(seg, tts, tts_dur, img, out, bgm_path if use_bgm else None)
            if ok:
                seg_paths.append(out)
            prog.advance(task)
    
    console.print(f"\n[green]✓ {len(seg_paths)}/{len(segs)} segmen selesai")
    return seg_paths


def menu_render(data, seg_paths=None):
    """[3] Render final MP4."""
    ep_id = data.get("episode", {}).get("id", "unknown")
    
    if not seg_paths:
        temp_dir = TEMP_DIR / ep_id
        seg_paths = sorted(temp_dir.glob("*.mp4"))
    
    if not seg_paths:
        console.print("[red]❌ Belum ada segmen. Run Stitch dulu.")
        return
    
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    output = FINAL_DIR / f"{ep_id}.mp4"
    
    console.print(f"\n[bold green]📦 Render final: {len(seg_paths)} segmen → {output.name}")
    
    if concat_mp4s(seg_paths, output):
        dur = get_duration(output)
        size_mb = output.stat().st_size / 1024 / 1024
        console.print(Panel(
            f"[bold green]✓ Final MP4 ready![/]\n\n"
            f"  📁 File: {output}\n"
            f"  ⏱ Duration: {dur:.1f}s ({dur/60:.1f} menit)\n"
            f"  💾 Size: {size_mb:.1f} MB\n\n"
            f"  [bold]Next step:[/]\n"
            f"  → Import ke DaVinci Resolve untuk fine-tune\n"
            f"  → Atau langsung pakai jika sudah OK",
            title="🎬 Render Complete", border_style="green"
        ))
    else:
        console.print("[red]❌ Render gagal!")


def menu_preview(data):
    """[4] Preview single segmen."""
    segs = data.get("segments", [])
    console.print("\n[bold cyan]📋 Pilih segmen:")
    for i, s in enumerate(segs, 1):
        tts = s.get("tts", {})
        text = tts.get("text", "")[:60]
        console.print(f"  [{i:2d}] {s['segment_id']:25s} {text}...")
    
    choice = IntPrompt.ask("[yellow]Nomor segmen", default=1)
    if 1 <= choice <= len(segs):
        seg = segs[choice - 1]
        tts = seg.get("tts", {})
        console.print(Panel(
            f"[bold]{seg['segment_id']}[/]\n\n"
            f"  Speaker: {tts.get('speaker', 'narrator')}\n"
            f"  Text: {tts.get('text', '')[:200]}\n"
            f"  Ken Burns: {seg.get('image', seg.get('t2i', {})).get('ken_burns', 'none')}\n"
            f"  SRT: {seg.get('srt_timing', {}).get('start', '?')} → {seg.get('srt_timing', {}).get('end', '?')}",
            title="Preview", border_style="cyan"
        ))


def menu_bgm():
    """[5] BGM Library management."""
    show_bgm_library()
    if Confirm.ask("\n[yellow]Buka folder bgm-library/ di Finder?", default=True):
        subprocess.run(["open", str(BGM_DIR)])
        console.print("[green]Folder dibuka. Download BGM ke sini.")


# ============================================================
# Main
# ============================================================
def main():
    # Check deps
    deps = check_deps()
    missing = [d[0] for d in deps if not d[1]]
    if missing:
        console.print(Panel(
            f"[red]❌ Dependencies belum terinstall:[/]\n"
            f"  Missing: {', '.join(missing)}\n\n"
            f"[bold]Install:[/]\n"
            f"  pip3 install edge-tts rich\n"
            f"  brew install ffmpeg",
            title="Setup Required", border_style="red"
        ))
        return
    
    show_banner()
    
    # Select JSON
    jsons = find_jsons()
    if not jsons:
        console.print("[red]❌ Tidak ada JSON di produksi/pra-produksi/")
        return
    
    console.print("\n[bold cyan]📋 Pilih JSON (Source of Truth):[/]")
    for i, j in enumerate(jsons, 1):
        console.print(f"  [{i}] {j.relative_to(ROOT)}")
    
    choice = IntPrompt.ask("[yellow]Nomor", default=1)
    if not (1 <= choice <= len(jsons)):
        return
    json_path = jsons[choice - 1]
    data = load_json(json_path)
    
    seg_paths = None
    
    # Main loop
    while True:
        console.print("\n" + "─" * 60)
        show_status(data, json_path)
        console.print("\n[bold]🏠 Menu:[/]")
        console.print("  [1] 🎵 Generate TTS (edge-tts, free)")
        console.print("  [2] 🎬 Stitch image + TTS (+ BGM fill)")
        console.print("  [3] 📦 Render final MP4")
        console.print("  [4] 👁 Preview segmen")
        console.print("  [5] 🎵 BGM Library (download/manage)")
        console.print("  [Q] ❌ Quit")
        
        choice = Prompt.ask("\n[yellow]Pilih menu", default="q").lower()
        
        if choice == "1":
            menu_tts(data, json_path)
        elif choice == "2":
            seg_paths = menu_stitch(data, json_path)
        elif choice == "3":
            menu_render(data, seg_paths)
        elif choice == "4":
            menu_preview(data)
        elif choice == "5":
            menu_bgm()
        elif choice == "q":
            console.print("[bold cyan]👋 Bye! Selamat produktif![/]")
            break


if __name__ == "__main__":
    main()
