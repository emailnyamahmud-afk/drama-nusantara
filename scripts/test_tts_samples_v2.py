#!/usr/bin/env python3
"""
Test TTS samples dengan rate +50% (1.5x speed) sesuai feedback user.
Plus strategy: tiap segmen akan ada BGM + SFX dari YouTube (free, no copyright).
"""
import asyncio
import edge_tts
import os
from pathlib import Path

OUT_DIR = Path("/home/z/my-project/download/tts-samples-v2")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Updated voice profiles dengan rate +50% (1.5x)
# Pitch tetap, hanya rate yang dinaikkan karena user bilang tempo lambat
samples = [
    # (voice, text, filename, rate, pitch, description)
    (
        "id-ID-ArdiNeural",
        "Tahun 1222 masa Saka. Seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel, membawa hasil curian dari istana.",
        "v2_narrator_id.mp3",
        "+50%", "+0Hz",  # 1.5x speed
        "Narrator Indonesia 1.5x speed"
    ),
    (
        "jv-ID-DimasNeural",
        "Aku ora nyuwun pangapura, Dang Hyang. Aku mung nunggu prajanjen. Gusti Wisnu ora ngutus aku menyang donya fana mung kanggo dadi maling cilik.",
        "v2_ken_arok_jv.mp3",
        "+50%", "+2Hz",  # muda + confident + cepat
        "Ken Arok (muda, confident, 1.5x) - Jawa"
    ),
    (
        "jv-ID-DimasNeural",
        "Aku ora ngetokake welas asih, Ken Arok. Aku ngetokake ramalan. Dewa Wisnu ora ngutus kau menyang donya fana mung kanggo dadi maling cilik.",
        "v2_lohgawe_jv.mp3",
        "+20%", "-4Hz",  # tua + bijak + sedikit cepat (not too slow)
        "Dang Hyang Lohgawe (tua, 1.2x - not too slow) - Jawa"
    ),
    (
        "jv-ID-SitiNeural",
        "Sampun, Gusti. Sabar iku kuncine. Sanadyan atiku kobls, aku tansah eling marang Gusti.",
        "v2_ken_dedes_jv.mp3",
        "+40%", "-3Hz",  # perempuan + melancholic + cukup cepat
        "Ken Dedes (perempuan, 1.4x) - Jawa"
    ),
    # Tambahan: test extreme speed untuk dialog panjang
    (
        "jv-ID-DimasNeural",
        "Tunggul Ametung lirih ngandika: 'Apa kowe ngerti sapa sing nglakoni iki?' Ken Arok mung ndhingkluk, ora wani mlayu.",
        "v2_dialog_fast_jv.mp3",
        "+60%", "-2Hz",  # dialog cepat untuk scene tense
        "Dialog cepat (1.6x) - Jawa untuk scene tense"
    ),
    # Tambahan: narrator cepat untuk narasi action
    (
        "id-ID-ArdiNeural",
        "Begitu Ken Arok melangkah keluar dari pendopo, langkah malamnya langsung membawa ia ke bengkel Empu Gandring di pinggir hutan.",
        "v2_narrator_action_id.mp3",
        "+60%", "+0Hz",  # narrator action cepat
        "Narrator action (1.6x) - Indonesia"
    ),
]

async def generate_all():
    print(f"Output dir: {OUT_DIR}")
    print(f"Total samples: {len(samples)}")
    print()
    for voice, text, filename, rate, pitch, desc in samples:
        print(f"Generating: {filename}")
        print(f"  desc: {desc}")
        print(f"  voice: {voice}, rate: {rate}, pitch: {pitch}")
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        out_path = OUT_DIR / filename
        await communicate.save(str(out_path))
        size = out_path.stat().st_size
        print(f"  ✅ Saved: {out_path.name} ({size // 1024} KB)")
        print()

if __name__ == "__main__":
    asyncio.run(generate_all())
    print("=" * 70)
    print("ALL V2 SAMPLES GENERATED (rate +50% / 1.5x speed)")
    print("=" * 70)
    for f in sorted(OUT_DIR.glob("*.mp3")):
        size = f.stat().st_size
        # Get duration via ffprobe
        import subprocess
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(f)],
            capture_output=True, text=True
        )
        duration = float(result.stdout.strip()) if result.stdout.strip() else 0
        print(f"  {f.name:35s}  {duration:.1f}s  {size // 1024} KB")
