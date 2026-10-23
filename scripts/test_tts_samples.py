#!/usr/bin/env python3
"""
Test generate sample TTS untuk verify edge-tts voice Bahasa Indonesia + Jawa.
Output: 4 .mp3 files di download/tts-samples/
"""
import asyncio
import edge_tts
import os
from pathlib import Path

OUT_DIR = Path("/home/z/my-project/download/tts-samples")
OUT_DIR.mkdir(parents=True, exist_ok=True)

samples = [
    # (voice, text, filename, rate, pitch, description)
    (
        "id-ID-ArdiNeural",
        "Tahun 1222 masa Saka. Seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel, membawa hasil curian dari istana.",
        "narrator_id.mp3",
        "+0%", "+0Hz",
        "Narrator Indonesia netral"
    ),
    (
        "jv-ID-DimasNeural",
        "Aku ora nyuwun pangapura, Dang Hyang. Aku mung nunggu prajanjen. Gusti Wisnu ora ngutus aku menyang donya fana mung kanggo dadi maling cilik.",
        "ken_arok_jv.mp3",
        "+5%", "+2Hz",
        "Ken Arok (muda, confident) - Jawa"
    ),
    (
        "jv-ID-DimasNeural",
        "Aku ora ngetokake welas asih, Ken Arok. Aku ngetokake ramalan. Dewa Wisnu ora ngutus kau menyang donya fana mung kanggo dadi maling cilik.",
        "lohgawe_jv.mp3",
        "-15%", "-4Hz",
        "Dang Hyang Lohgawe (tua, bijak, slow, low pitch) - Jawa"
    ),
    (
        "jv-ID-SitiNeural",
        "Sampun, Gusti. Sabar iku kuncine. Sanadyan atiku koblos, aku tansah eling marang Gusti.",
        "ken_dedes_jv.mp3",
        "-5%", "-3Hz",
        "Ken Dedes (perempuan, melancholic) - Jawa"
    ),
]

async def generate_all():
    print(f"Output dir: {OUT_DIR}")
    print(f"Total samples: {len(samples)}")
    print()
    for voice, text, filename, rate, pitch, desc in samples:
        print(f"Generating: {filename} ({desc})")
        print(f"  voice: {voice}")
        print(f"  rate: {rate}, pitch: {pitch}")
        print(f"  text: {text[:80]}...")
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        out_path = OUT_DIR / filename
        await communicate.save(str(out_path))
        size = out_path.stat().st_size
        print(f"  ✅ Saved: {out_path} ({size // 1024} KB)")
        print()

if __name__ == "__main__":
    asyncio.run(generate_all())
    print("=" * 70)
    print("ALL SAMPLES GENERATED")
    print("=" * 70)
    for f in sorted(OUT_DIR.glob("*.mp3")):
        print(f"  {f.name:30s}  {f.stat().st_size // 1024} KB")
