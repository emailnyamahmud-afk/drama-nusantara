#!/usr/bin/env python3
"""
Generate i2v-batch.json — 1 file berisi 6 I2V job untuk storyboard frame
yang sudah di-generate Dola.

Pattern reuse dari dola-batch.json (T2I):
- Phase-based, parallel jobs
- Output path per job
- Contact sheet (thumbnail grid bukan montage image)

PERBEDAAN dari T2I batch:
- Single phase (tidak ada dependency antar I2V job)
- Input: image path (bukan text)
- Output: .mp4 (bukan .jpg)
- Tambahan: duration_seconds, fps, motion_prompt
- QC: durasi + file size (bukan aspect ratio)
"""

import json
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/z/my-project")
STORYBOARD = ROOT / "produksi/pra-produksi/prototype-30s/storyboard.json"
OUT = ROOT / "produksi/pra-produksi/prototype-30s/i2v-batch.json"


def read_storyboard():
    with open(STORYBOARD, encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Build I2V batch
# ============================================================
sb = read_storyboard()

i2v_jobs = []
seg_count = 0
for act in sb["acts"]:
    for scene in act["scenes"]:
        for seg in scene["segments"]:
            # Input image = T2I output dari segmen ini
            input_image_path = f"produksi/t2i-output/prototype-30s/{seg['id']}.jpg"
            
            i2v_jobs.append({
                "job_id": f"i2v-{seg['id']}",
                "phase": "i2v",
                "segment_id": seg["id"],
                "scene_id": scene["id"],
                "scene_title": scene["judul"],
                "segment_notes": seg.get("notes", ""),
                
                # INPUT — image dari T2I output
                "input_image_path": input_image_path,
                
                # MOTION PROMPT — ditarik dari storyboard.json motion.prompt
                # (sebelumnya reserved di T2I skill, sekarang dipakai di I2V)
                "motion_prompt": seg.get("motion", {}).get("prompt", ""),
                "motion_camera": seg.get("motion", {}).get("camera", ""),
                "motion_speed": seg.get("motion", {}).get("speed", "medium"),
                
                # AUDIO CONTEXT (optional, kalau I2V support native audio)
                "audio_context": seg.get("audio", {}),
                
                # OUTPUT
                "duration_seconds": seg["durasi"],
                "fps": sb["episode"]["fps"],  # 24
                "output_path": f"produksi/i2v-output/prototype-30s/{seg['id']}.mp4",
                
                # MODEL — pilihan user, default Kling 3.0 720p (paling hemat di Higgsfield)
                "model_suggestion": "kling-3.0-720p",  # alternatives: seedance-2.0-720p, veo-3-fast
                "resolution": "1280x720",  # 720p default (hemat credit)
                
                # NOTES
                "notes": f"I2V untuk segment {seg['id']} — durasi {seg['durasi']}s, speed {seg.get('motion', {}).get('speed', 'medium')}"
            })
            seg_count += 1


# ============================================================
# COMPILE I2V BATCH JSON
# ============================================================
batch = {
    "schema_version": "1.0",
    "project": {
        "id": sb["episode"]["id"],
        "title": sb["episode"]["judul"],
        "era": sb["episode"]["era"],
        "duration_target_seconds": sb["episode"]["durasi_target"],
        "resolution": sb["episode"]["resolusi"],
        "fps": sb["episode"]["fps"],
        "style": sb["episode"]["style"],
        "date_created": sb["episode"]["tanggal_dibuat"]
    },
    "instructions_for_agent": {
        "purpose": "Batch generate 6 video clips dari storyboard frame yang sudah ada. Image-to-Video (I2V).",
        "phase_i2v": {
            "description": "Generate 6 video clips. Setiap job pakai image dari T2I output sebagai input, plus motion_prompt untuk arah gerakan.",
            "count": len(i2v_jobs),
            "input": "image (from input_image_path) + motion_prompt text",
            "output": "save each .mp4 to output_path",
            "model_hint": "field model_suggestion = rekomendasi model. User bisa override (kling-3.0-720p / seedance-2.0-720p / veo-3-fast). Pilih yang tersedia di platform.",
            "duration_rule": "duration_seconds = video length (5s default). Jangan override kalau tidak perlu.",
            "fps_rule": "fps = 24 (cinema standard). Keep this unless platform requires different."
        },
        "execution_order": "single_phase (all jobs parallel, no dependency between I2V jobs)",
        "output_organization": {
            "i2v_clips": "produksi/i2v-output/prototype-30s/",
            "contact_gif": "produksi/i2v-output/prototype-30s/contact-grid.gif (optional)"
        },
        "qc_check": {
            "duration_check": "Verify each .mp4 has duration close to duration_seconds (±0.5s)",
            "file_size_check": "Each .mp4 should be > 1MB (sanity check, not corrupt)",
            "audio_check": "If model supports native audio (e.g. Seedance 2.5), verify audio matches audio_context. If not, generate audio separately in Phase 7 (TTS)."
        }
    },
    "phases": [
        {
            "phase_id": "phase_i2v",
            "name": "Generate Video Clips (Image-to-Video)",
            "parallel": True,
            "depends_on": None,  # All jobs independent
            "jobs": i2v_jobs
        }
    ],
    "total_jobs": len(i2v_jobs),
    "summary": {
        "total_clips": len(i2v_jobs),
        "total_duration_seconds": sum(j["duration_seconds"] for j in i2v_jobs),
        "input_images": len(i2v_jobs),
        "model_suggestion": "kling-3.0-720p (default, ~7 credits per 5s di Higgsfield)",
        "estimasi_credits_higgsfield": "6 × 7 = 42 credits (Kling 3.0 720p)",
        "estimasi_credits_higgsfield_seedance": "6 × 22 = 132 credits (Seedance 2.0 720p)",
        "estimasi_credits_flow_veo": "6 × 5-10 = 30-60 credits (Google Flow, 50/hari)"
    }
}

# Write
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

# Stats
size_kb = OUT.stat().st_size / 1024
print(f"✅ Written: {OUT}")
print(f"   Size: {size_kb:.1f} KB")
print(f"   Total jobs: {batch['total_jobs']}")
print(f"   Total duration: {sum(j['duration_seconds'] for j in i2v_jobs)}s = {sum(j['duration_seconds'] for j in i2v_jobs)/60:.1f} menit")
print()
print("=== JOBS ===")
for j in i2v_jobs:
    print(f"  {j['job_id']:25s} dur={j['duration_seconds']}s model={j['model_suggestion']:25s} speed={j['motion_speed']}")
    print(f"    input: {j['input_image_path']}")
    print(f"    motion: {j['motion_prompt'][:80]}...")
    print(f"    output: {j['output_path']}")
    print()

# Summary
print("=== ESTIMASI CREDITS PER PLATFORM ===")
print(f"  Higgsfield Kling 3.0 720p: 6 × 7 = 42 credits (paling hemat)")
print(f"  Higgsfield Seedance 2.0 720p: 6 × 22 = 132 credits")
print(f"  Google Flow Veo: 6 × 5-10 = 30-60 credits (50/hari)")
print(f"  Dola Seedance 2.5: cek di akun user")
