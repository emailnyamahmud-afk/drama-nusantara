#!/usr/bin/env python3
"""
Demo: Audio layering — TTS + BGM + SFX
Verify konsep bahwa TTS (v2 dengan rate cepat) bisa di-mix dengan BGM dan SFX.

Menggunakan sample TTS yang sudah ada + simulate BGM/SFX via ffmpeg generated tones.
"""
import subprocess
import os
from pathlib import Path

TTS_DIR = Path("/home/z/my-project/download/tts-samples-v2")
OUT_DIR = Path("/home/z/my-project/download/audio-layer-demo")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# Generate dummy BGM (tense percussion loop) via ffmpeg
# ============================================================
def generate_dummy_bgm(output_path, duration_seconds=10):
    """Generate simple tense ambient BGM via ffmpeg sine wave."""
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"sine=frequency=80:duration={duration_seconds}",
        "-f", "lavfi", "-i", f"sine=frequency=120:duration={duration_seconds}",
        "-filter_complex",
        "[0:a][1:a]amix=inputs=2:duration=longest:weights=0.7 0.3,volume=0.3,"
        f"afade=t=in:st=0:d=1,afade=t=out:st={duration_seconds-1}:d=1",
        "-t", str(duration_seconds),
        "-c:a", "libmp3lame", "-b:a", "96k",
        str(output_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✅ BGM generated: {output_path.name}")
    else:
        print(f"  ❌ BGM failed: {result.stderr[-200:]}")
    return output_path

# ============================================================
# Generate dummy SFX (footstep + twig snap) via ffmpeg noise
# ============================================================
def generate_dummy_sfx(output_path, duration_seconds=3):
    """Generate simple footstep SFX via ffmpeg noise bursts."""
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"anoisesrc=d={duration_seconds}:c=pink:a=0.5",
        "-filter_complex",
        "volume=0.4,"
        f"afade=t=in:st=0:d=0.1,afade=t=out:st={duration_seconds-0.2}:d=0.2",
        "-t", str(duration_seconds),
        "-c:a", "libmp3lame", "-b:a", "96k",
        str(output_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✅ SFX generated: {output_path.name}")

# ============================================================
# Mix TTS + BGM + SFX
# ============================================================
def mix_audio(tts_path, bgm_path, sfx_path, output_path, tts_volume=1.0, bgm_volume=0.2, sfx_volume=0.3):
    """Mix TTS (loud) + BGM (subtle) + SFX (medium) into 1 audio file."""
    inputs = ["-i", str(tts_path)]
    if bgm_path and bgm_path.exists():
        inputs += ["-i", str(bgm_path)]
    if sfx_path and sfx_path.exists():
        inputs += ["-i", str(sfx_path)]
    
    # Build filter
    amix_inputs = []
    if bgm_path and bgm_path.exists() and sfx_path and sfx_path.exists():
        filter_str = f"[1:a]volume={bgm_volume}[b];[2:a]volume={sfx_volume}[s];[0:a][b][s]amix=inputs=3:duration=first:dropout_transition=0[a]"
    elif bgm_path and bgm_path.exists():
        filter_str = f"[1:a]volume={bgm_volume}[b];[0:a][b]amix=inputs=2:duration=first:dropout_transition=0[a]"
    else:
        filter_str = "[0:a]anull[a]"
    
    cmd = [
        "ffmpeg", "-y"
    ] + inputs + [
        "-filter_complex", filter_str,
        "-map", "[a]",
        "-c:a", "libmp3lame", "-b:a", "128k",
        str(output_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✅ Mixed: {output_path.name}")
    else:
        print(f"  ❌ Mix failed: {result.stderr[-300:]}")

# ============================================================
# Main demo
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("AUDIO LAYERING DEMO: TTS + BGM + SFX")
    print("=" * 70)
    
    # Pick Ken Arok TTS (muda, confident, 1.5x) for demo
    tts_file = TTS_DIR / "v2_ken_arok_jv.mp3"
    print(f"\nTTS source: {tts_file.name}")
    
    # Get TTS duration
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(tts_file)],
        capture_output=True, text=True
    )
    tts_duration = float(result.stdout.strip())
    print(f"TTS duration: {tts_duration:.1f}s")
    
    # Generate BGM same duration
    bgm_path = OUT_DIR / "demo_bgm.mp3"
    print(f"\n[1/3] Generate BGM (tense ambient drone)...")
    generate_dummy_bgm(bgm_path, tts_duration + 2)
    
    # Generate SFX (footsteps)
    sfx_path = OUT_DIR / "demo_sfx.mp3"
    print(f"\n[2/3] Generate SFX (footstep ambient)...")
    generate_dummy_sfx(sfx_path, min(tts_duration, 4))
    
    # Mix them
    print(f"\n[3/3] Mix TTS + BGM + SFX...")
    mixed_path = OUT_DIR / "demo_ken_arok_mixed.mp3"
    mix_audio(tts_file, bgm_path, sfx_path, mixed_path,
              tts_volume=1.0, bgm_volume=0.15, sfx_volume=0.25)
    
    print(f"\n{'='*70}")
    print(f"DEMO COMPLETE — All audio files:")
    print(f"{'='*70}")
    for f in sorted(OUT_DIR.glob("*.mp3")):
        size = f.stat().st_size
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(f)],
            capture_output=True, text=True
        )
        dur = float(result.stdout.strip()) if result.stdout.strip() else 0
        print(f"  {f.name:35s}  {dur:.1f}s  {size // 1024} KB")
    
    print()
    print("Note: BGM dan SFX di sini DUMMY (generated via ffmpeg).")
    print("Production: akan pakai BGM+SFX asli dari YouTube Audio Library (free, no copyright).")
