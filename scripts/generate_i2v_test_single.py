#!/usr/bin/env python3
"""
Generate i2v-test-single.json — 1 segment only untuk quality test cepat.
Plus extract prompt plain text untuk manual copy-paste ke platform I2V.

Strategy: Test seg01 dulu (chase, motion paling jelas, cepat kelihatan kualitas).
Kalau OK → lanjut 5 segmen lainnya.
Kalau jelek → coba model/resolusi lain.
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
STORYBOARD = ROOT / "produksi/pra-produksi/prototype-30s/storyboard.json"
OUT_SINGLE = ROOT / "produksi/pra-produksi/prototype-30s/i2v-test-single.json"
OUT_PROMPT_TXT = ROOT / "produksi/pra-produksi/prototype-30s/i2v-test-seg01-prompt.txt"


def read_storyboard():
    with open(STORYBOARD, encoding="utf-8") as f:
        return json.load(f)


sb = read_storyboard()

# Ambil seg01 — chase scene, paling dynamic untuk test quality
target_seg_id = "S001_seg01"
target_seg = None
target_scene = None
for act in sb["acts"]:
    for scene in act["scenes"]:
        for seg in scene["segments"]:
            if seg["id"] == target_seg_id:
                target_seg = seg
                target_scene = scene
                break

# Bikin single-job JSON
single_job = {
    "job_id": f"i2v-test-{target_seg_id}",
    "phase": "i2v",
    "segment_id": target_seg_id,
    "scene_id": target_scene["id"],
    "scene_title": target_scene["judul"],
    "segment_notes": target_seg.get("notes", ""),
    "input_image_path": f"produksi/t2i-output/prototype-30s/{target_seg_id}.jpg",
    "motion_prompt": target_seg.get("motion", {}).get("prompt", ""),
    "motion_camera": target_seg.get("motion", {}).get("camera", ""),
    "motion_speed": target_seg.get("motion", {}).get("speed", "medium"),
    "audio_context": target_seg.get("audio", {}),
    "duration_seconds": target_seg["durasi"],
    "fps": 24,
    "output_path": f"produksi/i2v-output/prototype-30s/test-{target_seg_id}.mp4",
    "model_suggestion": "kling-3.0-480p",  # 480p — user bilang OK
    "resolution": "854x480",  # 480p (lebih hemat lagi)
    "notes": f"TEST single segment — {target_seg_id} (chase, fast motion) — 480p untuk hemat credits"
}

batch = {
    "schema_version": "1.0",
    "project": {
        "id": sb["episode"]["id"],
        "title": sb["episode"]["judul"] + " — I2V Test Single",
        "era": sb["episode"]["era"],
        "duration_target_seconds": 5,  # single segment only
        "resolution": "854x480",  # 480p test
        "fps": 24,
        "style": sb["episode"]["style"],
        "date_created": sb["episode"]["tanggal_dibuat"]
    },
    "instructions_for_agent": {
        "purpose": "TEST single I2V generation untuk evaluate kualitas 480p sebelum commit ke full 6 video batch.",
        "phase_i2v_test": {
            "description": "Generate 1 video clip dari storyboard frame seg01 (chase scene).",
            "count": 1,
            "input": "image + motion_prompt",
            "output": ".mp4 480p 5s",
            "model_hint": "kling-3.0-480p atau model 480p lainnya (paling hemat credits). 480p OK untuk test quality."
        },
        "qc_check": "Cek: durasi 5s, character consistency (Ken Arok wajah), motion blur (chase feel), file size > 500KB"
    },
    "phases": [{
        "phase_id": "phase_i2v_test",
        "name": "Test I2V Single Segment",
        "parallel": False,
        "depends_on": None,
        "jobs": [single_job]
    }],
    "total_jobs": 1,
    "summary": {
        "total_clips": 1,
        "total_duration_seconds": 5,
        "estimasi_credits": "1-5 credits tergantung model (480p paling hemat)",
        "platform_rekomendasi": "Higgsfield (Kling 3.0 480p ~3-5cr) atau Google Flow (5-10cr) atau ReelCine (free test)"
    }
}

with open(OUT_SINGLE, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"✅ Single-test JSON: {OUT_SINGLE}")
print(f"   Size: {OUT_SINGLE.stat().st_size // 1024} bytes")
print(f"   Job: {single_job['job_id']}")
print(f"   Segment: {target_seg_id} (chase, fast motion)")
print(f"   Duration: 5s")
print(f"   Resolution: 480p (hemat credits)")
print()

# ============================================================
# Bikin plain text prompt untuk manual copy-paste
# ============================================================
prompt_txt = f"""# I2V TEST — {target_seg_id} (Chase Through Dense Woods)

## Input Image
Path: {single_job['input_image_path']}
Deskripsi: Ken Arok sprint di hutan, 3 prajurit kejar dengan tombak, motion blur, god rays

## Motion Prompt (COPY-PASTE ke platform I2V)
{single_job['motion_prompt']}

## Camera Direction
{single_job['motion_camera']}

## Settings
- Duration: 5 seconds
- FPS: 24
- Resolution: 480p (854×480) atau 720p (1280×720) — pilih hemat
- Speed: {single_job['motion_speed']}

## Model Options (urut paling hemat credits)
1. Higgsfield Kling 3.0 480p — ~3-5 credits per 5s
2. Higgsfield Seedance 1.5 480p — ~1 credit per 5s (paling hemat, quality lebih rendah)
3. Higgsfield Kling 3.0 720p — ~7 credits per 5s (quality lebih bagus)
4. Google Flow Veo Fast — ~5-10 credits per 5s (50cr/hari free)
5. ReelCine Seedance 2.5 — free no signup (limit unclear, test dulu)
6. Dola Seedance 2.5 — cek credits di akun

## QC Checklist
- [ ] Durasi video 5 detik (±0.5s)
- [ ] Karakter Ken Arok konsisten vs input image (wajah, costum)
- [ ] Motion blur terlihat (chase feel)
- [ ] 3 prajurit dengan tombak di background (tidak hilang)
- [ ] File size > 500KB (tidak corrupt)
- [ ] Audio (kalau native): panting + twig snaps + soldier shouts

## Audio Context (kalau model support native audio)
Type: ambience
BGM: tense tribal percussion building, fast tempo matching footstep rhythm
SFX: heavy panting, twigs snapping, distant shouting soldiers, metallic armor rattle

## Notes
- Test ini untuk evaluate kualitas I2V sebelum commit ke full 6 video
- Kalau 480p bagus → lanjut 5 segmen lainnya dengan 480p (paling hemat)
- Kalau 480p jelek → coba 720p (Kling 3.0 720p ~7cr)
- Kalau masih jelek → coba model lain (Seedance 2.0 / Veo)
"""

OUT_PROMPT_TXT.write_text(prompt_txt, encoding="utf-8")
print(f"✅ Plain text prompt: {OUT_PROMPT_TXT}")
print(f"   Size: {OUT_PROMPT_TXT.stat().st_size} bytes")
print()
print("=" * 80)
print("CARA PAKAI — PILIH 1 DARI 4 OPSI")
print("=" * 80)
print()
print("OPSI A — Higgsfield (signup fresh account, paling hemat)")
print("  1. Buka https://higgsfield.ai → signup email baru")
print("  2. Dapat 150 credits free")
print("  3. Upload image: produksi/t2i-output/prototype-30s/S001_seg01.jpg")
print("  4. Copy motion prompt dari file .txt di atas")
print("  5. Pilih model: Kling 3.0 480p (3-5cr) atau Seedance 1.5 480p (1cr)")
print("  6. Generate → download .mp4")
print("  7. Share ke Z.ai untuk review")
print()
print("OPSI B — Google Flow (kalau 50cr hari ini belum dipakai)")
print("  1. Buka https://flow.google.com")
print("  2. Upload image: S001_seg01.jpg")
print("  3. Paste motion prompt")
print("  4. Pilih model: Veo Fast 480p (~5cr)")
print("  5. Generate → download")
print()
print("OPSI C — ReelCine (free no signup, test limit)")
print("  1. Buka https://reelcine.org")
print("  2. Pilih Seedance 2.5")
print("  3. Upload image + paste motion prompt")
print("  4. Generate → cek apakah benar-benar free")
print("  5. Kalau OK → download")
print()
print("OPSI D — Dola AI (kalau ada free I2V credits)")
print("  1. Buka https://dola.com → login")
print("  2. Cek credits I2V available")
print("  3. Upload i2v-test-single.json + ketik 'jalankan batch i2v test'")
print("     (butuh skill baru — bisa pakai prompt plain text dulu untuk test cepat)")
print("  4. Atau manual: upload image + paste motion prompt di chat")
print()
print("ESTIMASI CREDITS:")
print("  - Higgsfield Kling 3.0 480p: 3-5cr")
print("  - Higgsfield Seedance 1.5 480p: 1cr (paling hemat, quality rendah)")
print("  - Google Flow Veo Fast: 5-10cr")
print("  - ReelCine: free (kalau limit OK)")
print("  - Dola: cek credits akun")
