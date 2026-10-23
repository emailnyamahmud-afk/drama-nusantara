#!/usr/bin/env python3
"""
Nusantara Render — TUI Tool untuk MacBook
Generate TTS + stitch image via ffmpeg → MP4 final.

Usage:
    cd drama-nusantara
    python3 scripts/nusantara-render.py

Dependencies:
    pip3 install edge-tts rich
    brew install ffmpeg

Input: JSON v3.1 (source of truth) di produksi/pra-produksi/
Output: TTS MP3 + MP4 final di produksi/tts-output/ + produksi/final/
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
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# ============================================================
# Config
# ============================================================
ROOT = Path(__file__).parent.parent  # drama-nusantara/
TTS_OUTPUT = ROOT / "produksi/tts-output"
FINAL_OUTPUT = ROOT / "produksi/final"
TEMP_SEGMENTS = ROOT / "download/temp-render"
IMAGE_DIR = ROOT / "produksi/t2i-output"

# Find JSON files
JSON_FILES = list(ROOT.glob("produksi/pra-produksi/**/ep*-final*.json"))
if not JSON_FILES:
    JSON_FILES = list(ROOT.glob("produksi/pra-produksi/**/prototype*.json"))


def find_json():
    """Find available JSON source of truth files."""
    files = list(ROOT.glob("produksi/pra-produksi/**/*v3*.json"))
    files += list(ROOT.glob("produksi/pra-produksi/**/*final*.json"))
    return sorted(set(files), key=lambda p: p.name)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_tts_duration(mp3_path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)],
        capture_output=True, text=True
    )
    return float(r.stdout.strip()) if r.stdout.strip() else 0


def get_ken_burns_filter(effect, duration_sec, target_w=1920, target_h=1080):
    frames = int(duration_sec * 24)
    if effect == "zoom_in_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0008,1.10)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_in_fast":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0025,1.25)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_out_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='if(eq(on,0),1.15,max(zoom-0.0008,1.0))':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "pan_right_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z=1.0:x='iw/2-{target_w}/2+(iw-{target_w})*on/{frames}/2':y='ih/2-{target_h}/2':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    else:
        return f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},format=yuv420p"


# ============================================================
# TTS Generation (edge-tts)
# ============================================================
async def generate_tts(text, voice, rate, pitch, output_path):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(str(output_path))


async def generate_tts_batch(json_data, tts_dir):
    """Generate TTS per segmen dari JSON."""
    segments = json_data.get("segments", [])
    voice_profiles = json_data.get("voice_profiles", {})
    
    tts_dir.mkdir(parents=True, exist_ok=True)
    
    results = []
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("Generating TTS...", total=len(segments))
        
        for seg in segments:
            seg_id = seg["segment_id"]
            tts = seg.get("tts", {})
            speaker = tts.get("speaker", "narrator")
            text = tts.get("text", "")
            voice_profile = tts.get("voice_profile", speaker)
            
            # Get voice settings
            profile = voice_profiles.get(voice_profile, {})
            voice = profile.get("edge_tts_voice", "id-ID-ArdiNeural")
            rate = profile.get("default_rate", "+25%")
            pitch = profile.get("default_pitch", "+0Hz")
            
            output_path = tts_dir / f"{seg_id}.mp3"
            
            if text:
                progress.update(task, description=f"TTS: {seg_id} ({speaker})")
                await generate_tts(text, voice, rate, pitch, output_path)
                dur = get_tts_duration(output_path)
                results.append({"seg_id": seg_id, "duration": dur, "path": str(output_path)})
            else:
                progress.update(task, description=f"Skip: {seg_id} (no TTS)")
                results.append({"seg_id": seg_id, "duration": 0, "path": None})
            
            progress.advance(task)
    
    return results


# ============================================================
# Stitch (ffmpeg Ken Burns)
# ============================================================
def build_segment(seg, tts_path, tts_duration, image_path, output_path, buffer_seconds=2.0):
    """Build 1 segment MP4: image (Ken Burns) + TTS audio."""
    cue_duration = tts_duration + buffer_seconds
    
    kb = seg.get("image", {}).get("ken_burns", "zoom_in_slow")
    video_filter = get_ken_burns_filter(kb, cue_duration)
    
    # Audio: TTS + pad silence to cue_duration
    audio_filter = f"[1:a]apad=whole_dur={cue_duration}[a]"
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(image_path),
        "-i", str(tts_path),
        "-filter_complex", f"[0:v]{video_filter}[v];{audio_filter}",
        "-map", "[v]", "-map", "[a]",
        "-t", str(cue_duration),
        "-c:v", "libx264", "-preset", "medium", "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        str(output_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0, cue_duration


def concat_segments(segment_paths, output_path):
    """Concat MP4 files."""
    list_path = output_path.parent / "concat_list.txt"
    with open(list_path, "w") as f:
        for p in segment_paths:
            f.write(f"file '{p}'\n")
    
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path), "-c", "copy", str(output_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    list_path.unlink()
    return result.returncode == 0


# ============================================================
# Menu
# ============================================================
def menu_select_json():
    """Pilih JSON source of truth."""
    files = find_json()
    if not files:
        console.print("[red]No JSON files found in produksi/pra-produksi/")
        return None
    
    console.print("\n[bold cyan]Select JSON Source of Truth:[/]")
    table = Table()
    table.add_column("#", style="cyan")
    table.add_column("File", style="white")
    table.add_column("Size", style="green")
    for i, f in enumerate(files, 1):
        table.add_row(str(i), str(f.relative_to(ROOT)), f"{f.stat().st_size // 1024}KB")
    console.print(table)
    
    choice = IntPrompt.ask("[yellow]Select number", default=1)
    if 1 <= choice <= len(files):
        return files[choice - 1]
    return None


def menu_generate_tts(json_path):
    """Menu 1: Generate TTS."""
    data = load_json(json_path)
    episode_id = data.get("episode", {}).get("id", "unknown")
    tts_dir = TTS_OUTPUT / episode_id
    
    console.print(f"\n[bold green]Generate TTS for {episode_id}[/]")
    console.print(f"Output: {tts_dir}")
    
    asyncio.run(generate_tts_batch(data, tts_dir))
    console.print("[green]TTS generation complete!")


def menu_stitch(json_path):
    """Menu 2: Stitch image + TTS → segments."""
    data = load_json(json_path)
    episode_id = data.get("episode", {}).get("id", "unknown")
    segments = data.get("segments", [])
    
    tts_dir = TTS_OUTPUT / episode_id
    temp_dir = TEMP_SEGMENTS / episode_id
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Find image directory
    image_dirs = list(IMAGE_DIR.glob(f"*/storyboard-frame/"))
    if not image_dirs:
        console.print("[red]No storyboard images found in produksi/t2i-output/")
        return
    
    image_dir = image_dirs[0]
    console.print(f"\n[bold green]Stitch {len(segments)} segments")
    console.print(f"Images: {image_dir}")
    console.print(f"TTS: {tts_dir}")
    
    seg_paths = []
    total_dur = 0
    
    for i, seg in enumerate(segments, 1):
        seg_id = seg["segment_id"]
        image_path = image_dir / f"{seg_id}.jpg"
        tts_path = tts_dir / f"{seg_id}.mp3"
        output_path = temp_dir / f"{seg_id}.mp4"
        
        if not image_path.exists():
            console.print(f"  [red]Missing image: {seg_id}")
            continue
        if not tts_path.exists():
            console.print(f"  [red]Missing TTS: {seg_id}")
            continue
        
        tts_dur = get_tts_duration(tts_path)
        console.print(f"  [{i}/{len(segments)}] {seg_id} (tts={tts_dur:.1f}s)")
        
        ok, cue_dur = build_segment(seg, tts_path, tts_dur, image_path, output_path)
        if ok:
            seg_paths.append(output_path)
            total_dur += cue_dur
            console.print(f"    [green]✓ {cue_dur:.1f}s")
        else:
            console.print(f"    [red]✗ Failed")
    
    console.print(f"\n[bold]Total: {len(seg_paths)} segments, {total_dur:.1f}s ({total_dur/60:.1f} min)")
    return seg_paths


def menu_render_final(json_path, seg_paths=None):
    """Menu 3: Render final MP4."""
    data = load_json(json_path)
    episode_id = data.get("episode", {}).get("id", "unknown")
    
    if not seg_paths:
        temp_dir = TEMP_SEGMENTS / episode_id
        seg_paths = sorted(temp_dir.glob("*.mp4"))
    
    if not seg_paths:
        console.print("[red]No segments found. Run stitch first.")
        return
    
    FINAL_OUTPUT.mkdir(parents=True, exist_ok=True)
    output = FINAL_OUTPUT / f"{episode_id}.mp4"
    
    console.print(f"\n[bold green]Render final: {len(seg_paths)} segments → {output.name}")
    
    if concat_segments(seg_paths, output):
        dur = get_tts_duration(output)
        size_mb = output.stat().st_size / 1024 / 1024
        console.print(Panel(
            f"[green]✓ Final MP4 ready!\n\n"
            f"  File: {output}\n"
            f"  Duration: {dur:.1f}s ({dur/60:.1f} min)\n"
            f"  Size: {size_mb:.1f} MB\n\n"
            f"  Next: Import to DaVinci Resolve → add BGM/SFX → export final",
            title="Render Complete", border_style="green"
        ))
    else:
        console.print("[red]Render failed!")


def menu_preview(json_path):
    """Menu 4: Preview single segmen."""
    data = load_json(json_path)
    segments = data.get("segments", [])
    
    console.print("\n[bold cyan]Select segment to preview:")
    for i, seg in enumerate(segments, 1):
        console.print(f"  [{i}] {seg['segment_id']}")
    
    choice = IntPrompt.ask("[yellow]Segment number", default=1)
    if 1 <= choice <= len(segments):
        seg = segments[choice - 1]
        console.print(f"\n[yellow]Preview: {seg['segment_id']}")
        console.print(f"  Speaker: {seg.get('tts', {}).get('speaker', 'narrator')}")
        console.print(f"  Text: {seg.get('tts', {}).get('text', '')[:100]}...")
        console.print(f"  Ken Burns: {seg.get('image', {}).get('ken_burns', 'none')}")


def main():
    console.print(Panel(
        "[bold cyan]Nusantara Render[/]\n"
        "TTS + ffmpeg stitch tool untuk MacBook\n"
        "Pipeline: JSON → TTS → stitch → MP4 → DaVinci Resolve",
        title="🏠 Nusantara Render", border_style="cyan"
    ))
    
    # Select JSON
    json_path = menu_select_json()
    if not json_path:
        return
    
    data = load_json(json_path)
    episode_id = data.get("episode", {}).get("id", "unknown")
    segments = data.get("segments", [])
    
    console.print(f"\n[green]Loaded: {json_path.name}")
    console.print(f"  Episode: {episode_id}")
    console.print(f"  Segments: {len(segments)}")
    
    seg_paths = None
    
    while True:
        console.print("\n[bold]Menu:")
        console.print("  [1] Generate TTS (edge-tts)")
        console.print("  [2] Stitch image + TTS (ffmpeg Ken Burns)")
        console.print("  [3] Render final MP4 (concat all)")
        console.print("  [4] Preview segment")
        console.print("  [5] Re-render single segment (iterate)")
        console.print("  [Q] Quit")
        
        choice = Prompt.ask("[yellow]Select", default="q").lower()
        
        if choice == "1":
            menu_generate_tts(json_path)
        elif choice == "2":
            seg_paths = menu_stitch(json_path)
        elif choice == "3":
            menu_render_final(json_path, seg_paths)
        elif choice == "4":
            menu_preview(json_path)
        elif choice == "5":
            console.print("[yellow]Re-render: edit JSON first, then run stitch for that segmen")
        elif choice == "q":
            console.print("[bold]Bye! 🎬")
            break


if __name__ == "__main__":
    main()
