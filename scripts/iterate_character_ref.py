#!/usr/bin/env python3
"""
Iterasi karakter ref via multi-turn editing (text + image input).

Penggunaan:
  python scripts/iterate_character_ref.py C001 "Make the lighting more dramatic"
  python scripts/iterate_character_ref.py C002 "The face looks too Chinese, make nose broader"
  python scripts/iterate_character_ref.py C001 "Change batik pattern to parang rusak diagonal"

Workflow:
  1. Load karakter ref sebelumnya dari refs/C00X_base.png
  2. Backup ke refs/C00X_base_prev.png
  3. Send ke Nano Banana dengan: [text feedback] + [previous image]
  4. Save hasil baru ke refs/C00X_base.png
"""

import os
import sys
import base64
import shutil
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: GEMINI_API_KEY tidak ditemukan di .env")
    sys.exit(1)

from google import genai

client = genai.Client(api_key=API_KEY)

MODEL_ID = "gemini-nano-banana-2.1"
REF_DIR = Path("/home/z/my-project/produksi/panji/refs")


def iterate_character(
    char_id: str,
    feedback: str,
    aspect_ratio: str = "9:16",
    resolution: str = "2K",
) -> Path:
    """Iterasi karakter ref dengan multi-turn editing"""
    current_ref = REF_DIR / f"{char_id}_base.png"

    if not current_ref.exists():
        raise FileNotFoundError(
            f"Previous ref not found: {current_ref}\n"
            f"Run `python scripts/generate_character_ref.py {char_id}` first."
        )

    # Backup previous version
    backup_path = REF_DIR / f"{char_id}_base_prev.png"
    shutil.copy2(current_ref, backup_path)
    print(f"[{char_id}] Backed up previous to {backup_path}")

    # Read current image as base64
    with open(current_ref, "rb") as f:
        image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    print(f"[{char_id}] Iterating with feedback:")
    print(f"  \"{feedback}\"")
    print(f"  Aspect: {aspect_ratio}, Resolution: {resolution}")

    try:
        interaction = client.interactions.create(
            model=MODEL_ID,
            input=[
                {"type": "text", "text": feedback},
                {
                    "type": "image",
                    "data": image_b64,
                    "mime_type": "image/png",
                },
            ],
            config={
                "aspect_ratio": aspect_ratio,
                "resolution": resolution,
            },
        )

        # Save new version (overwrite)
        with open(current_ref, "wb") as f:
            f.write(base64.b64decode(interaction.output_image.data))

        print(f"  ✅ Refined ref saved to {current_ref}")
        print(f"  💾 Previous version: {backup_path}")
        return current_ref

    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        # Restore previous
        shutil.copy2(backup_path, current_ref)
        print(f"  ↩️  Restored previous version")
        raise


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    char_id = sys.argv[1]
    feedback = sys.argv[2]

    if char_id not in ["C001", "C002", "C003", "C004"]:
        print(f"ERROR: char_id must be C001, C002, C003, or C004")
        sys.exit(1)

    iterate_character(char_id, feedback)


if __name__ == "__main__":
    main()
