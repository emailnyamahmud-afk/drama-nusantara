#!/usr/bin/env python3
"""
Extract 36 segmen prompts dari storyboard-pilot.json ke file .txt terpisah.
Setiap file siap copy-paste ke Google Flow (flow.google.com).

Output: produksi/panji/pre-produksi/prompts/segments/SXX_segYY.txt
"""

import json
from pathlib import Path

STORYBOARD_PATH = Path(
    "/home/z/my-project/produksi/panji/pre-produksi/storyboard-pilot.json"
)
OUTPUT_DIR = Path("/home/z/my-project/produksi/panji/pre-produksi/prompts/segments")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    print(f"Membaca: {STORYBOARD_PATH}")
    with open(STORYBOARD_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Build character ref mapping untuk info di header file
    char_names = {c["id"]: c["nama"] for c in data.get("characters", [])}
    loc_names = {l["id"]: l["nama"] for l in data.get("locations", [])}

    count = 0
    for act in data.get("acts", []):
        act_id = act.get("id", "")
        act_title = act.get("judul", "")
        for scene in act.get("scenes", []):
            scene_id = scene.get("id", "")
            scene_title = scene.get("judul", "")
            scene_loc = scene.get("lokasi", "")
            scene_mood = scene.get("mood", "")
            for seg in scene.get("segments", []):
                seg_id = seg.get("id", "")
                prompt = seg.get("visual", {}).get("prompt", "")
                negative = seg.get("visual", {}).get("negative_prompt", "")
                camera = seg.get("visual", {}).get("camera", "")
                char_refs = seg.get("characters_present", [])
                audio = seg.get("audio", {})
                tts_text = audio.get("tts_text", "")
                tts_voice = audio.get("tts_voice", "")
                notes = seg.get("notes", "")

                # Build file content dengan metadata + prompt murni
                content = f"""# {seg_id}
# Act: {act_id} - {act_title}
# Scene: {scene_id} - {scene_title}
# Lokasi: {scene_loc} - {loc_names.get(scene_loc, '?')}
# Mood: {scene_mood}
# Camera: {camera}
# Karakter: {', '.join(f'{c}={char_names.get(c, '?')}' for c in char_refs) if char_refs else 'none'}
# Notes: {notes}

# === T2I PROMPT (copy ke Google Flow) ===

{prompt}

# === NEGATIVE PROMPT (jika Flow support field terpisah) ===

{negative}

# === AUDIO METADATA ===

TTS Voice: {tts_voice or 'none'}
TTS Text: {tts_text or 'none'}

"""
                output_path = OUTPUT_DIR / f"{seg_id}.txt"
                output_path.write_text(content, encoding="utf-8")
                count += 1
                print(f"  ✅ {seg_id}.txt")

    print(f"\nTotal: {count} segmen prompt di-extract ke {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
