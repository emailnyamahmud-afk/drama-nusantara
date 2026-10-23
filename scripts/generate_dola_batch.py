#!/usr/bin/env python3
"""
Generate dola-batch.json — 1 file berisi semua prompt untuk Dola AI mode agen.

Struktur:
  - Phase 1 (master_ref): 6 job generate master ref image (no dependency)
  - Phase 2 (storyboard_frame): 6 job generate storyboard frame (depends on phase 1 output)

User upload JSON ini ke Dola AI mode agen → agen otomatis:
  1. Eksekusi phase 1 — generate 6 ref image, save ke path
  2. Setelah phase 1 selesai, eksekusi phase 2 — generate 6 storyboard frame
     pakai ref image dari phase 1 sebagai input (yang include_inspiration=true)
  3. Output: 12 image di t2i-output/

Workflow:
  User: upload dola-batch.json ke Dola agen
  Dola agen: baca JSON, generate all image otomatis
  User: download 12 image, taruh di folder sesuai output_path
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
PROMPTS_DIR = ROOT / "produksi/master-reff-t2i-prompts/2C-singasari-kediri/prompts"
STORYBOARD = ROOT / "produksi/pra-produksi/prototype-30s/storyboard.json"
OUT = ROOT / "produksi/pra-produksi/prototype-30s/dola-batch.json"


def read_prompt(filename):
    return (PROMPTS_DIR / filename).read_text(encoding="utf-8").strip()


def read_storyboard():
    with open(STORYBOARD, encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# Build batch
# ============================================================
sb = read_storyboard()

# --- PHASE 1: MASTER REF ---
# Map asset_id → prompt file
ref_jobs = []

# Characters
for c in sb["characters"]:
    ref_id = c.get("ref_k_id")
    if not ref_id:
        continue
    ref_jobs.append({
        "job_id": f"ref-{c['id']}",
        "phase": "master_ref",
        "asset_id": c["id"],
        "asset_name": c["nama"],
        "asset_type": "character",
        "prompt_file": f"{ref_id}.txt",
        "prompt": read_prompt(f"{ref_id}.txt"),
        "model": "seedream-4.5",
        "aspect_ratio": "16:9",
        "include_inspiration": False,  # ref image tidak butuh ref input
        "ref_image_inputs": [],
        "output_path": f"produksi/t2i-output/master-reff/2C/{c['id']}-{ref_id}.jpg",
        "notes": f"Character ref sheet 5-angle horizontal untuk {c['nama']}"
    })

# Locations
for l in sb["locations"]:
    ref_id = l.get("ref_l_id")
    if not ref_id:
        continue
    ref_jobs.append({
        "job_id": f"ref-{l['id']}",
        "phase": "master_ref",
        "asset_id": l["id"],
        "asset_name": l["nama"],
        "asset_type": "location",
        "prompt_file": f"{ref_id}.txt",
        "prompt": read_prompt(f"{ref_id}.txt"),
        "model": "seedream-4.5",
        "aspect_ratio": "16:9",
        "include_inspiration": False,
        "ref_image_inputs": [],
        "output_path": f"produksi/t2i-output/master-reff/2C/{l['id']}-{ref_id}.jpg",
        "notes": f"Location ref (no people) untuk {l['nama']}"
    })

# Props
for p in sb["props"]:
    ref_id = p.get("ref_a_id")
    if not ref_id:
        continue
    ref_jobs.append({
        "job_id": f"ref-{p['id']}",
        "phase": "master_ref",
        "asset_id": p["id"],
        "asset_name": p["nama"],
        "asset_type": "prop",
        "prompt_file": f"{ref_id}.txt",
        "prompt": read_prompt(f"{ref_id}.txt"),
        "model": "seedream-4.5",
        "aspect_ratio": "1:1",  # A-type macro square
        "include_inspiration": False,
        "ref_image_inputs": [],
        "output_path": f"produksi/t2i-output/master-reff/2C/{p['id']}-{ref_id}.jpg",
        "notes": f"Prop macro ref untuk {p['nama']}"
    })

# --- PHASE 2: STORYBOARD FRAME ---
frame_jobs = []
seg_count = 0
for act in sb["acts"]:
    for scene in act["scenes"]:
        for seg in scene["segments"]:
            # Determine ref inputs: hanya yang include_inspiration=true
            ref_inputs = []
            for aid in seg.get("linked_asset_ids", []):
                # find asset
                asset = None
                for c in sb["characters"]:
                    if c["id"] == aid and c.get("include_inspiration_in_image_gen"):
                        asset = c
                        break
                if not asset:
                    for l in sb["locations"]:
                        if l["id"] == aid:
                            asset = l
                            break
                if not asset:
                    for p in sb["props"]:
                        if p["id"] == aid:
                            asset = p
                            break
                if asset:
                    ref_field = {"character": "ref_k_id", "location": "ref_l_id", "prop": "ref_a_id"}.get(asset.get("asset_type") or ("character" if "physical_characteristics" in asset and "backstory" in asset else "location" if "time_of_day" in asset else "prop"))
                    # simpler: just use the actual ref_*_id field
                    ref_id_value = asset.get("ref_k_id") or asset.get("ref_l_id") or asset.get("ref_a_id")
                    if ref_id_value:
                        # Check include flag (only characters have it, default true for char, false for others)
                        include_flag = asset.get("include_inspiration_in_image_gen", False)
                        if include_flag:
                            ref_inputs.append({
                                "asset_id": aid,
                                "asset_name": asset.get("nama"),
                                "ref_image_path": f"produksi/t2i-output/master-reff/2C/{aid}-{ref_id_value}.jpg",
                                "role": "character_consistency" if "ref_k_id" in asset else "location_context" if "ref_l_id" in asset else "prop_detail"
                            })

            frame_jobs.append({
                "job_id": f"frame-{seg['id']}",
                "phase": "storyboard_frame",
                "segment_id": seg["id"],
                "scene_id": scene["id"],
                "scene_title": scene["judul"],
                "segment_notes": seg.get("notes", ""),
                "prompt": seg["visual"]["prompt"],
                "motion_prompt": seg.get("motion", {}).get("prompt", ""),  # for future I2V use
                "model": "seedream-4.5",
                "aspect_ratio": "16:9",
                "include_inspiration": True,  # frame memakai ref image
                "ref_image_inputs": ref_inputs,
                "output_path": f"produksi/t2i-output/prototype-30s/{seg['id']}.jpg",
                "duration_seconds": seg["durasi"],
                "depends_on": [r["asset_id"] for r in ref_inputs],
                "notes": f"Storyboard frame untuk segment {seg['id']} (durasi {seg['durasi']}s)"
            })
            seg_count += 1


# ============================================================
# COMPILE BATCH JSON
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
        "purpose": "Batch generate all images untuk prototype 30 detik. 2 phase berurutan dengan dependency.",
        "phase_1_master_ref": {
            "description": "Generate 6 master reference images. Tidak ada dependency — boleh parallel.",
            "count": len(ref_jobs),
            "input": "text prompt only (no image input)",
            "output": "save each image to its output_path",
            "model_setting": "Seedream 4.5, aspect_ratio per job"
        },
        "phase_2_storyboard_frame": {
            "description": "Generate 6 storyboard frames. Setiap frame butuh ref image dari phase 1 sebagai input.",
            "count": len(frame_jobs),
            "input": "text prompt + ref images (upload ref images yang sesuai ref_image_inputs)",
            "ref_image_rule": "Hanya asset dengan include_inspiration_in_image_gen=true yang perlu diupload sebagai ref. Karakter utama = true (konsistensi wajah). Prop sekunder = false (hemat token).",
            "output": "save each image to its output_path",
            "depends_on_phase": "phase_1_master_ref (must complete first)"
        },
        "execution_order": "phase_1_master_ref (parallel) → phase_2_storyboard_frame (parallel after phase 1 done)",
        "output_organization": {
            "master_ref": "produksi/t2i-output/master-reff/2C/",
            "storyboard_frame": "produksi/t2i-output/prototype-30s/"
        }
    },
    "phases": [
        {
            "phase_id": "phase_1_master_ref",
            "name": "Generate Master Reference Images",
            "parallel": True,
            "depends_on": None,
            "jobs": ref_jobs
        },
        {
            "phase_id": "phase_2_storyboard_frame",
            "name": "Generate Storyboard Frames",
            "parallel": True,
            "depends_on": "phase_1_master_ref",
            "jobs": frame_jobs
        }
    ],
    "total_jobs": len(ref_jobs) + len(frame_jobs),
    "summary": {
        "characters": len(sb["characters"]),
        "locations": len(sb["locations"]),
        "props": len(sb["props"]),
        "segments": seg_count,
        "total_ref_images": len(ref_jobs),
        "total_frame_images": len(frame_jobs),
        "total_images": len(ref_jobs) + len(frame_jobs)
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
print(f"   Total jobs: {batch['total_jobs']} ({len(ref_jobs)} ref + {len(frame_jobs)} frame)")
print(f"   Phases: 2 (phase 1 no-dep, phase 2 depends-on phase 1)")
print()
print("=== PHASE 1 — MASTER REF (no dependency, parallel) ===")
for j in ref_jobs:
    print(f"  {j['job_id']:18s} {j['asset_type']:10s} {j['asset_name']:25s} → {j['aspect_ratio']} → {Path(j['output_path']).name}")
print()
print("=== PHASE 2 — STORYBOARD FRAME (depends on phase 1) ===")
for j in frame_jobs:
    deps = ",".join(j["depends_on"]) if j["depends_on"] else "(none)"
    print(f"  {j['job_id']:25s} dur={j['duration_seconds']}s deps=[{deps}] → {Path(j['output_path']).name}")
