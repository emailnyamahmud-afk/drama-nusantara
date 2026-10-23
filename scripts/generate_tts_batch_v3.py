#!/usr/bin/env python3
"""
Generate 6 TTS per segmen dari prototype-30s-v3.json
Rate: +25% (1.25x) — ideal setelah user feedback
Output: produksi/tts-output/prototype-30s-v3/*.mp3
"""
import asyncio
import edge_tts
import json
import os
import subprocess
from pathlib import Path

ROOT = Path("/home/z/my-project")
JSON_PATH = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.json"
OUT_DIR = ROOT / "produksi/tts-output/prototype-30s-v3"
OUT_DIR.mkdir(parents=True, exist_ok=True)

async def generate_tts_for_segment(seg):
    """Generate 1 TTS file untuk 1 segmen."""
    tts = seg["tts"]
    text = tts["text"]
    voice = tts["edge_tts_voice"]
    rate = tts["rate"]
    pitch = tts["pitch"]
    output_path = OUT_DIR / f"{seg['segment_id']}.mp3"
    
    print(f"  Generating: {seg['segment_id']}")
    print(f"    voice: {voice}, rate: {rate}, pitch: {pitch}")
    print(f"    text: {text[:80]}{'...' if len(text) > 80 else ''}")
    
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(str(output_path))
    
    # Get duration
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(output_path)],
        capture_output=True, text=True
    )
    duration = float(result.stdout.strip()) if result.stdout.strip() else 0
    size = output_path.stat().st_size
    
    print(f"    ✅ Saved: {output_path.name} ({duration:.2f}s, {size // 1024} KB)")
    print(f"    Target SRT duration: {seg['srt_timing']['duration_seconds']}s")
    
    if duration > seg["srt_timing"]["duration_seconds"]:
        print(f"    ⚠️  TTS lebih panjang {duration - seg['srt_timing']['duration_seconds']:.2f}s dari SRT target")
    elif duration < seg["srt_timing"]["duration_seconds"]:
        print(f"    ℹ️  TTS lebih pendek {seg['srt_timing']['duration_seconds'] - duration:.2f}s (akan di-pad silence)")
    print()
    
    return {
        "segment_id": seg["segment_id"],
        "tts_path": str(output_path),
        "duration": duration,
        "target_duration": seg["srt_timing"]["duration_seconds"],
        "size_kb": size // 1024
    }

async def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"=== GENERATE TTS BATCH (rate +25% = 1.25x) ===")
    print(f"Source JSON: {JSON_PATH}")
    print(f"Output dir: {OUT_DIR}")
    print(f"Total segments: {len(data['segments'])}")
    print()
    
    results = []
    for seg in data["segments"]:
        result = await generate_tts_for_segment(seg)
        results.append(result)
    
    print("=" * 70)
    print("TTS BATCH COMPLETE")
    print("=" * 70)
    print(f"{'Segment':15s} {'Duration':10s} {'Target':10s} {'Status':10s} {'Size':8s}")
    print("-" * 60)
    total_duration = 0
    for r in results:
        total_duration += r["duration"]
        status = "OK" if abs(r["duration"] - r["target_duration"]) < 1 else ("LONG" if r["duration"] > r["target_duration"] else "SHORT")
        print(f"{r['segment_id']:15s} {r['duration']:.2f}s{' ':>4} {r['target_duration']}s{' ':>6} {status:10s} {r['size_kb']}KB")
    print("-" * 60)
    print(f"{'TOTAL':15s} {total_duration:.2f}s")
    print()
    
    # Save results to JSON for next step (ffmpeg stitch)
    results_path = OUT_DIR / "_tts_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved: {results_path}")

if __name__ == "__main__":
    asyncio.run(main())
