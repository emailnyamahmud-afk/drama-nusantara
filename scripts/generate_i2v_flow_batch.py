#!/usr/bin/env python3
"""
Generate i2v-flow-batch.json — untuk Google Flow Veo
+ i2v-flow-prompts.txt — plain text prompts untuk manual copy-paste di Flow

Google Flow constraints:
- Resolution: 360p / 720p (no 480p option)
- Duration: 4s / 6s / 8s / 10s (no 5s option)
- Credits: 360p@4s=4cr, 360p@6s=6cr, 720p@4s=7cr, 720p@6s=10cr
- Free: 50cr/day
- Includes SFX (audio native)
- NO watermark
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
STORYBOARD = ROOT / "produksi/pra-produksi/prototype-30s/storyboard.json"
OUT_JSON = ROOT / "produksi/pra-produksi/prototype-30s/i2v-flow-batch.json"
OUT_TXT = ROOT / "produksi/pra-produksi/prototype-30s/i2v-flow-prompts.txt"


def read_storyboard():
    with open(STORYBOARD, encoding="utf-8") as f:
        return json.load(f)


sb = read_storyboard()

# Strategy: 360p + 4s untuk hemat credits
# Kalau hasil bagus, nanti bisa iterate dengan 720p untuk critical frames
RESOLUTION = "360p"
DURATION_S = 4  # Google Flow option: 4s
CREDITS_PER_VIDEO = 4  # 360p @ 4s

i2v_jobs = []
for act in sb["acts"]:
    for scene in act["scenes"]:
        for seg in scene["segments"]:
            input_image_path = f"produksi/t2i-output/prototype-30s/{seg['id']}.jpg"
            
            i2v_jobs.append({
                "job_id": f"i2v-flow-{seg['id']}",
                "phase": "i2v_flow",
                "segment_id": seg["id"],
                "scene_id": scene["id"],
                "scene_title": scene["judul"],
                "segment_notes": seg.get("notes", ""),
                "input_image_path": input_image_path,
                "motion_prompt": seg.get("motion", {}).get("prompt", ""),
                "motion_camera": seg.get("motion", {}).get("camera", ""),
                "motion_speed": seg.get("motion", {}).get("speed", "medium"),
                "audio_context": seg.get("audio", {}),
                "duration_seconds": DURATION_S,  # Google Flow option 4s
                "fps": 24,
                "resolution": RESOLUTION,
                "credits_per_video": CREDITS_PER_VIDEO,
                "output_path": f"produksi/i2v-output/prototype-30s/flow-{seg['id']}.mp4",
                "model": "google-veo-flow",
                "notes": f"I2V Google Flow untuk {seg['id']} — 360p 4s {CREDITS_PER_VIDEO}cr"
            })

batch = {
    "schema_version": "1.0",
    "platform": "google_flow",
    "project": {
        "id": sb["episode"]["id"],
        "title": sb["episode"]["judul"] + " — I2V Google Flow",
        "era": sb["episode"]["era"],
        "duration_target_seconds": 24,  # 6 segmen × 4s (bukan 30s karena Flow tidak support 5s)
        "resolution": "640x360",  # 360p
        "fps": 24,
        "style": sb["episode"]["style"],
        "date_created": sb["episode"]["tanggal_dibuat"]
    },
    "instructions_for_agent": {
        "purpose": "Batch I2V generation via Google Flow Veo — 6 segmen × 4s = 24s total",
        "platform_constraints": {
            "resolution_options": ["360p", "720p"],
            "duration_options_seconds": [4, 6, 8, 10],
            "credits_per_video": {
                "360p_4s": 4,
                "360p_6s": 6,
                "360p_8s": 8,
                "720p_4s": 7,
                "720p_6s": 10,
                "720p_8s": 15
            },
            "free_daily_limit": 50,
            "audio_native": True,
            "watermark": False,
            "notes": "Resolusi rendah (360p) tidak masalah — bisa di-upscale di akhir via ffmpeg/Real-ESRGAN"
        },
        "execution_strategy": "Manual upload one-by-one di Google Flow web UI (tidak ada batch API)",
        "estimated_credits": f"{len(i2v_jobs)} × {CREDITS_PER_VIDEO} = {len(i2v_jobs) * CREDITS_PER_VIDEO}cr",
        "free_credit_balance_after": f"{50 - len(i2v_jobs) * CREDITS_PER_VIDEO}cr remaining untuk iterate"
    },
    "phases": [{
        "phase_id": "phase_i2v_flow",
        "name": "Generate Video Clips via Google Flow Veo",
        "parallel": False,
        "depends_on": None,
        "jobs": i2v_jobs
    }],
    "total_jobs": len(i2v_jobs),
    "summary": {
        "total_clips": len(i2v_jobs),
        "total_duration_seconds": len(i2v_jobs) * DURATION_S,
        "resolution": RESOLUTION,
        "duration_per_video": DURATION_S,
        "credits_per_video": CREDITS_PER_VIDEO,
        "total_credits": len(i2v_jobs) * CREDITS_PER_VIDEO,
        "free_daily_limit": 50,
        "remaining_credits_after": 50 - len(i2v_jobs) * CREDITS_PER_VIDEO,
        "audio_native": True,
        "watermark": False
    }
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

# ============================================================
# Plain text prompts untuk manual copy-paste di Google Flow
# ============================================================
prompts_txt = []
prompts_txt.append("=" * 80)
prompts_txt.append("GOOGLE FLOW VEO — I2V PROMPTS UNTUK 6 SEGMEN")
prompts_txt.append("=" * 80)
prompts_txt.append("")
prompts_txt.append("Settings di Google Flow (sama untuk semua segmen):")
prompts_txt.append(f"  - Resolution: {RESOLUTION}")
prompts_txt.append(f"  - Duration: {DURATION_S}s (4 detik — pilihan terdekat dengan target 5s)")
prompts_txt.append(f"  - Estimasi credits per video: {CREDITS_PER_VIDEO}cr")
prompts_txt.append(f"  - Total 6 video: {len(i2v_jobs) * CREDITS_PER_VIDEO}cr (sisa {50 - len(i2v_jobs) * CREDITS_PER_VIDEO}cr untuk iterate)")
prompts_txt.append(f"  - Audio native: YA (SFX included)")
prompts_txt.append(f"  - Watermark: TIDAK ADA")
prompts_txt.append("")
prompts_txt.append("Workflow per segmen:")
prompts_txt.append("  1. Buka https://flow.google.com")
prompts_txt.append("  2. Upload image dari produksi/t2i-output/prototype-30s/{segment_id}.jpg")
prompts_txt.append("  3. Copy-paste motion prompt di bawah")
prompts_txt.append(f"  4. Set Resolution = {RESOLUTION}, Duration = {DURATION_S}s")
prompts_txt.append("  5. Generate → download .mp4")
prompts_txt.append(f"  6. Save ke: produksi/i2v-output/prototype-30s/flow-{{segment_id}}.mp4")
prompts_txt.append("")
prompts_txt.append("Note: durasi 4s vs target 5s = -1s per video. Total video 24s bukan 30s.")
prompts_txt.append("Solusi: pakai slow-motion di ffmpeg untuk extend ke 30s, atau trim TTS narasi jadi 24s.")
prompts_txt.append("")

for i, job in enumerate(i2v_jobs, 1):
    prompts_txt.append("=" * 80)
    prompts_txt.append(f"[SEGMENT {i}/6] {job['segment_id']} — {job['segment_notes']}")
    prompts_txt.append("=" * 80)
    prompts_txt.append(f"Input image: {job['input_image_path']}")
    prompts_txt.append(f"Camera direction: {job['motion_camera']}")
    prompts_txt.append(f"Speed: {job['motion_speed']}")
    prompts_txt.append(f"Output: {job['output_path']}")
    prompts_txt.append(f"Credits: {job['credits_per_video']}cr")
    prompts_txt.append("")
    prompts_txt.append("MOTION PROMPT (copy-paste):")
    prompts_txt.append(job["motion_prompt"])
    prompts_txt.append("")
    prompts_txt.append("AUDIO CONTEXT (kalau perlu tambah ke prompt untuk SFX native):")
    audio = job["audio_context"]
    if audio.get("bgm"):
        prompts_txt.append(f"  BGM: {audio['bgm']}")
    if audio.get("sfx"):
        prompts_txt.append(f"  SFX: {audio['sfx']}")
    if audio.get("tts_text"):
        prompts_txt.append(f"  Dialogue: \"{audio['tts_text']}\"")
    prompts_txt.append("")

prompts_txt.append("=" * 80)
prompts_txt.append("STRATEGI ITERASI (kalau perlu improve)")
prompts_txt.append("=" * 80)
prompts_txt.append(f"")
prompts_txt.append(f"Sisa credits setelah 6 video: {50 - len(i2v_jobs) * CREDITS_PER_VIDEO}cr")
prompts_txt.append(f"")
prompts_txt.append("Kalau ada video yang perlu iterate:")
prompts_txt.append(f"  - 360p 4s = {CREDITS_PER_VIDEO}cr per video, sisa bisa iterate {50 // CREDITS_PER_VIDEO - len(i2v_jobs)} video lagi")
prompts_txt.append(f"  - Atau upgrade ke 720p 4s = 7cr untuk critical frames (mis. seg04 prophecy)")
prompts_txt.append(f"")
prompts_txt.append("Critical frames untuk iterate dengan 720p (jika perlu):")
prompts_txt.append("  ⭐ seg04 (Prophecy — 2 karakter, paling kompleks)")
prompts_txt.append("  ⭐ seg05 (Epiphany — snap zoom, motion unik)")
prompts_txt.append("  seg01 (Chase — sudah ada Dola version untuk comparison)")

OUT_TXT.write_text("\n".join(prompts_txt), encoding="utf-8")

print(f"✅ JSON: {OUT_JSON} ({OUT_JSON.stat().st_size // 1024} KB)")
print(f"✅ TXT:  {OUT_TXT} ({OUT_TXT.stat().st_size // 1024} KB)")
print()
print("=" * 70)
print("STRATEGI GOOGLE FLOW — SUMMARY")
print("=" * 70)
print(f"  Resolution: {RESOLUTION}")
print(f"  Duration: {DURATION_S}s per video (Flow tidak ada opsi 5s)")
print(f"  Credits per video: {CREDITS_PER_VIDEO}cr")
print(f"  Total 6 video: {len(i2v_jobs) * CREDITS_PER_VIDEO}cr (limit 50cr/day)")
print(f"  Sisa credits: {50 - len(i2v_jobs) * CREDITS_PER_VIDEO}cr (untuk iterate atau critical frame 720p)")
print(f"  Audio: NATIVE SFX ✅")
print(f"  Watermark: NONE ✅")
print(f"  Total duration: {len(i2v_jobs) * DURATION_S}s (target awal 30s)")
print(f"  Note: 4s vs 5s = -1s per video. Bisa slow-mo atau trim TTS di ffmpeg.")
