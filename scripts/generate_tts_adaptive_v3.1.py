#!/usr/bin/env python3
"""
Generate TTS ADAPTIVE untuk v3.1 — TTS rate auto-adjust supaya FIT ke SRT cue.

Logic:
1. Generate TTS dengan default rate (+25%)
2. Cek actual duration vs cue_duration
3. Kalau TTS > cue → hitung rate baru = (tts_actual / cue) × 1.25, capped at 2.0 (max +100%)
4. Re-generate dengan rate baru
5. Kalau TTS < cue → pakai default, nanti di-pad silence saat stitch
6. Final: TTS duration ≤ cue_duration (no cut, no overlap)
"""
import asyncio
import edge_tts
import json
import subprocess
from pathlib import Path

ROOT = Path("/home/z/my-project")
JSON_PATH = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.1.json"
OUT_DIR = ROOT / "produksi/tts-output/prototype-30s-v3.1"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def rate_to_multiplier(rate_str):
    """Convert '+25%' to 1.25, '-10%' to 0.9, etc."""
    if rate_str.startswith("+"):
        return 1 + float(rate_str[1:-1]) / 100
    elif rate_str.startswith("-"):
        return 1 - float(rate_str[1:-1]) / 100
    return 1.0


def multiplier_to_rate(mult):
    """Convert 1.5 to '+50%', 0.9 to '-10%'."""
    pct = (mult - 1) * 100
    if pct >= 0:
        return f"+{pct:.0f}%"
    else:
        return f"{pct:.0f}%"


def get_tts_duration(mp3_path):
    """Get MP3 duration via ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip()) if result.stdout.strip() else 0


async def generate_tts(text, voice, rate, pitch, output_path):
    """Generate 1 TTS file."""
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(str(output_path))


async def generate_adaptive(seg):
    """Generate TTS dengan adaptive rate supaya fit ke cue_duration."""
    tts = seg["tts"]
    text = tts["text"]
    voice = tts["edge_tts_voice"]
    pitch = tts["pitch"]
    cue_dur = seg["srt_timing"]["cue_duration"]
    
    default_rate = tts["default_rate"]
    max_rate = tts["max_rate"]
    max_mult = rate_to_multiplier(max_rate)
    
    output_path = OUT_DIR / f"{seg['segment_id']}.mp3"
    
    print(f"\n[{seg['segment_id']}] cue={cue_dur}s")
    print(f"  text: {text[:70]}{'...' if len(text) > 70 else ''}")
    
    # Step 1: Generate dengan default rate
    print(f"  Step 1: Generate dengan default rate={default_rate}")
    await generate_tts(text, voice, default_rate, pitch, output_path)
    actual_dur = get_tts_duration(output_path)
    print(f"  → TTS actual duration: {actual_dur:.2f}s")
    
    # Step 2: Check fit
    # Beri buffer 0.2s supaya tidak mepet ke cue
    target_max = cue_dur - 0.2
    pad_silence = 0
    
    if actual_dur <= cue_dur:
        # TTS fit di cue (dengan atau tanpa pad)
        if actual_dur < target_max:
            pad_silence = cue_dur - actual_dur
            print(f"  ✅ TTS FIT, pad silence = {pad_silence:.2f}s")
        else:
            print(f"  ✅ TTS FIT (mepet), no pad needed")
        final_rate = default_rate
        final_dur = actual_dur
    else:
        # TTS too long → calculate adaptive rate
        default_mult = rate_to_multiplier(default_rate)
        # Rate baru supaya TTS = target_max
        # actual_dur / (new_mult / default_mult) = target_max
        # new_mult = actual_dur × default_mult / target_max
        new_mult = (actual_dur * default_mult) / target_max
        
        if new_mult > max_mult:
            # Tidak muat walau max rate → SPLIT needed (rare case)
            print(f"  ⚠️  TIDAK MUAT walau rate {max_rate}!")
            print(f"     Actual: {actual_dur:.2f}s, target: {target_max:.2f}s")
            print(f"     Needed rate mult: {new_mult:.2f}, max allowed: {max_mult:.2f}")
            print(f"     Solution: SPLIT cue jadi 2 (akan di-handle manual)")
            # Untuk sekarang, pakai max rate aja, audio akan di-trim dengan fade out
            new_rate = max_rate
            await generate_tts(text, voice, new_rate, pitch, output_path)
            final_dur = get_tts_duration(output_path)
            final_rate = new_rate
            # Mark untuk split kalau perlu
            print(f"  → Pakai max rate {max_rate}, durasi={final_dur:.2f}s")
            print(f"  → Audio akan di-fade out di akhir saat stitch (trim dengan grace)")
        else:
            # Adaptive rate works
            new_rate = multiplier_to_rate(new_mult)
            print(f"  Step 2: Re-generate dengan adaptive rate={new_rate} (mult={new_mult:.2f})")
            await generate_tts(text, voice, new_rate, pitch, output_path)
            final_dur = get_tts_duration(output_path)
            final_rate = new_rate
            print(f"  ✅ TTS FIT: durasi={final_dur:.2f}s (target ≤ {target_max:.2f}s)")
    
    # Update JSON
    tts["actual_rate"] = final_rate
    tts["actual_duration"] = final_dur
    tts["pad_silence_seconds"] = pad_silence
    
    return {
        "segment_id": seg["segment_id"],
        "cue_duration": cue_dur,
        "tts_duration": final_dur,
        "actual_rate": final_rate,
        "pad_silence": pad_silence,
        "output_path": str(output_path)
    }


async def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)
    
    print("=" * 70)
    print("TTS ADAPTIVE BATCH — rate auto-adjust supaya FIT ke SRT cue")
    print("=" * 70)
    print(f"JSON: {JSON_PATH.name}")
    print(f"Default rate: +25% (1.25x)")
    print(f"Max rate: +100% (2.0x)")
    print(f"Total cue: 30s exact (SRT ground truth)")
    print()
    
    results = []
    for seg in data["segments"]:
        result = await generate_adaptive(seg)
        results.append(result)
    
    print()
    print("=" * 70)
    print("TTS ADAPTIVE BATCH COMPLETE")
    print("=" * 70)
    print(f"{'Segment':15s} {'Cue':>5s} {'TTS':>7s} {'Rate':>8s} {'Pad':>6s} {'Status':>10s}")
    print("-" * 60)
    for r in results:
        if r["tts_duration"] <= r["cue_duration"]:
            status = "FIT ✅"
        else:
            status = "OVER ⚠️"
        pad_str = f"{r['pad_silence']:.2f}s" if r["pad_silence"] > 0 else "-"
        print(f"{r['segment_id']:15s} {r['cue_duration']:>4.0f}s {r['tts_duration']:>6.2f}s {r['actual_rate']:>8s} {pad_str:>6s} {status:>10s}")
    
    total_tts = sum(r["tts_duration"] for r in results)
    total_pad = sum(r["pad_silence"] for r in results)
    print("-" * 60)
    print(f"{'TOTAL':15s} {'30s':>5s} {total_tts:>6.2f}s {'':>8s} {total_pad:>5.2f}s")
    print()
    print(f"Total TTS audio: {total_tts:.2f}s")
    print(f"Total silence pad: {total_pad:.2f}s")
    print(f"Total video: {total_tts + total_pad:.2f}s (target: 30s)")
    print()
    
    # Save results to JSON
    results_path = OUT_DIR / "_tts_adaptive_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results: {results_path}")
    
    # Update JSON v3.1 dengan actual_rate dan actual_duration
    for seg in data["segments"]:
        for r in results:
            if r["segment_id"] == seg["segment_id"]:
                seg["tts"]["actual_rate"] = r["actual_rate"]
                seg["tts"]["actual_duration"] = r["tts_duration"]
                seg["tts"]["pad_silence_seconds"] = r["pad_silence"]
    
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON updated: {JSON_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
