#!/usr/bin/env python3
"""
Generate karakter ref via Google Nano Banana (gemini-nano-banana-2.1).

Penggunaan:
  python scripts/generate_character_ref.py              # generate semua 4 karakter
  python scripts/generate_character_ref.py C001          # generate 1 karakter
  python scripts/generate_character_ref.py C001 C002     # generate 2 karakter

Iterasi multi-turn:
  python scripts/iterate_character_ref.py C001 "Make the lighting more dramatic, increase contrast to 6:1"

Setup:
  1. pip install google-genai python-dotenv Pillow
  2. Dapatkan API key dari https://aistudio.google.com/apikey
  3. Buat file .env: GEMINI_API_KEY=AIzaSy...
"""

import os
import sys
import base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Cek API key
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: GEMINI_API_KEY tidak ditemukan di .env")
    print("Dapatkan API key dari https://aistudio.google.com/apikey")
    print("Lalu buat file .env dengan isi: GEMINI_API_KEY=AIzaSy...")
    sys.exit(1)

from google import genai

client = genai.Client(api_key=API_KEY)

# Konfigurasi
MODEL_ID = "gemini-nano-banana-2.1"  # Workhorse utama Oktober 2026
PROMPT_DIR = Path("/home/z/my-project/produksi/panji/pre-produksi/prompts")
REF_DIR = Path("/home/z/my-project/produksi/panji/refs")
REF_DIR.mkdir(parents=True, exist_ok=True)


def load_prompt(char_id: str) -> str:
    """Load prompt murni dari file .txt"""
    prompt_files = {
        "C001": "C001_panji.txt",
        "C002": "C002_candra_kirana.txt",
        "C003": "C003_patih.txt",
        "C004": "C004_mpu_dharmaja.txt",
    }
    if char_id not in prompt_files:
        raise ValueError(f"Unknown char_id: {char_id}. Must be one of {list(prompt_files)}")

    prompt_path = PROMPT_DIR / prompt_files[char_id]
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")


def generate_character(
    char_id: str,
    aspect_ratio: str = "9:16",
    resolution: str = "2K",
) -> Path:
    """Generate karakter ref baru via Nano Banana 2.1"""
    prompt = load_prompt(char_id)
    output_path = REF_DIR / f"{char_id}_base.png"

    print(f"[{char_id}] Generating with model {MODEL_ID}...")
    print(f"  Prompt length: {len(prompt)} chars")
    print(f"  Aspect ratio: {aspect_ratio}")
    print(f"  Resolution: {resolution}")

    try:
        interaction = client.interactions.create(
            model=MODEL_ID,
            input=prompt,
            config={
                "aspect_ratio": aspect_ratio,
                "resolution": resolution,
            },
        )

        # Save image
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(interaction.output_image.data))

        print(f"  ✅ Saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        raise


def main():
    if len(sys.argv) > 1:
        # Generate karakter spesifik
        char_ids = sys.argv[1:]
    else:
        # Generate semua 4 karakter
        char_ids = ["C001", "C002", "C003", "C004"]

    print(f"\n=== Generate {len(char_ids)} karakter ref via {MODEL_ID} ===\n")

    success = 0
    failed = 0
    for char_id in char_ids:
        try:
            generate_character(char_id)
            success += 1
        except Exception as e:
            print(f"  ❌ {char_id}: {e}")
            failed += 1
        print()

    print(f"=== Summary ===")
    print(f"  ✅ Success: {success}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📁 Output: {REF_DIR}")


if __name__ == "__main__":
    main()
