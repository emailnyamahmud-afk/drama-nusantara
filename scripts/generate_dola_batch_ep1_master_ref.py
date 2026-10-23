#!/usr/bin/env python3
"""
Generate dola-batch-EP1-master-ref.json — single phase T2I untuk master ref EP1.

12 job:
- 8 K karakter (5-angle horizontal grid, 16:9)
- 4 A artefak (macro 1:1 square)

Reuse dari existing era 3B (3 file):
- 3B-K001-sultan-trenggana.txt (reuse untuk Pangeran Trenggana)
- 3B-L001-demak.txt (reuse untuk Demak lokasi)
- 3B-S001-pendapa-demak.txt (reuse untuk Pendapa Demak scene)
Plus dari era 3A (2 file):
- 3A-K003-sunan-kalijaga.txt (reuse untuk Sunan Kalijaga)
- 3A-L002-malaka.txt (reuse untuk Malaka lokasi)

Total asset untuk EP1: 12 baru + 5 reuse = 17 master ref
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
PROMPTS_DIR_3B = ROOT / "produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts"
PROMPTS_DIR_3A = ROOT / "produksi/master-reff-t2i-prompts/3A-islamisasi-awal/prompts"
OUT = ROOT / "produksi/pra-produksi/jaka-tingkir-series/dola-batch-EP1-master-ref.json"


def read_prompt(filename, prompts_dir):
    path = prompts_dir / filename
    return path.read_text(encoding="utf-8").strip()


# ============================================================
# 12 NEW prompts (baru di-generate)
# ============================================================
new_jobs = [
    # Karakter (K-type, 16:9 horizontal)
    {"asset_id": "EP1-C001", "asset_name": "Raden Patah (Sultan I)", "asset_type": "character",
     "prompt_file": "3B-K007-raden-patah.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Sultan Demak I, tua bijak, jenggot putih"},
    
    {"asset_id": "EP1-C002", "asset_name": "Raden Yunus (Sultan II)", "asset_type": "character",
     "prompt_file": "3B-K008-raden-yunus.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Pangeran muda ambisius, gagal serang Malaka 1512, Sultan II 1518-1521"},
    
    {"asset_id": "EP1-C003", "asset_name": "Raden Suryawiyata", "asset_type": "character",
     "prompt_file": "3B-K009-raden-suryawiyata.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Adipati Jipang Panolan, pro Putihan, akan dibunuh EP2"},
    
    {"asset_id": "EP1-C004", "asset_name": "Sunan Kudus", "asset_type": "character",
     "prompt_file": "3B-K010-sunan-kudus.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Penasehat Agung Demak, pro Putihan, dendam ke Pangeran Prawata"},
    
    {"asset_id": "EP1-C005", "asset_name": "Sunan Giri Dalem", "asset_type": "character",
     "prompt_file": "3B-K011-sunan-giri-dalem.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Pimpinan Dewan Wali Sangha, waskita"},
    
    {"asset_id": "EP1-C006", "asset_name": "Hang Tuah", "asset_type": "character",
     "prompt_file": "3B-K012-hang-tuah.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Laksamana Malaka, gugur 1511 saat jatuh ke Portugis"},
    
    {"asset_id": "EP1-C007", "asset_name": "Prajurit Demak", "asset_type": "character",
     "prompt_file": "3B-K013-prajurit-demak.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Pasukan Demak abad 16, armor kulit + tombak"},
    
    {"asset_id": "EP1-C008", "asset_name": "Prajurit Portugis", "asset_type": "character",
     "prompt_file": "3B-K014-prajurit-portugis.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "16:9",
     "include_inspiration": False, "notes": "Soldado Português abad 16, armor baja + matchlock musket"},
    
    # Artefak (A-type, 1:1 square macro)
    {"asset_id": "EP1-P001", "asset_name": "Keris Kyai Naga Sasra", "asset_type": "prop",
     "prompt_file": "3B-A004-keris-kyai-naga-sasra.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "1:1",
     "include_inspiration": False, "notes": "Keris pusaka yang 'menggigit' punggung Raden Yunus hingga wafat"},
    
    {"asset_id": "EP1-P002", "asset_name": "Singgasana Demak", "asset_type": "prop",
     "prompt_file": "3B-A005-singgasana-demak.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "1:1",
     "include_inspiration": False, "notes": "Singgasana kayu jati berukir, mahkota sultan, 3 level"},
    
    {"asset_id": "EP1-P003", "asset_name": "Mahkota Sultan Demak", "asset_type": "prop",
     "prompt_file": "3B-A006-mahkota-sultan-demak.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "1:1",
     "include_inspiration": False, "notes": "Mahkota emas + zamrud + bulan sabit, 7 points simbol wali"},
    
    {"asset_id": "EP1-P004", "asset_name": "Bendera Surya Majapahit", "asset_type": "prop",
     "prompt_file": "3B-A007-bendera-surya-majapahit.txt", "prompts_dir": PROMPTS_DIR_3B, "aspect_ratio": "1:1",
     "include_inspiration": False, "notes": "Bendera Demak gabungan Surya Majapahit + kaligrafi Arab"},
]

# ============================================================
# Build jobs
# ============================================================
jobs = []
for nj in new_jobs:
    job = {
        "job_id": f"ref-{nj['asset_id']}",
        "phase": "master_ref",
        "asset_id": nj["asset_id"],
        "asset_name": nj["asset_name"],
        "asset_type": nj["asset_type"],
        "prompt_file": nj["prompt_file"],
        "prompt": read_prompt(nj["prompt_file"], nj["prompts_dir"]),
        "model": "seedream-4.5",
        "aspect_ratio": nj["aspect_ratio"],
        "include_inspiration": nj["include_inspiration"],
        "ref_image_inputs": [],
        "output_path": f"produksi/t2i-output/jaka-tingkir-ep1/master-ref/{nj['asset_id']}-{nj['prompt_file'].replace('.txt','')}.jpg",
        "notes": nj["notes"]
    }
    jobs.append(job)


# ============================================================
# Compile batch JSON
# ============================================================
batch = {
    "schema_version": "1.0",
    "project": {
        "id": "JT-S1-EP1-MASTER-REF",
        "title": "Jaka Tingkir EP1 — Master Reference Image Batch",
        "era": "3B Demak-Pajang (Pajang Awal, 1499-1550 M)",
        "type": "master_ref_batch",
        "episode": "EP1: Demak Berdiri, Malaka Jatuh",
        "duration_target_seconds": 720,
        "resolution": "1920x1080",
        "fps": 24,
        "style": "cinematic realistic, Javanese period drama, dark-fantasy tones",
        "date_created": "2026-10-23"
    },
    "instructions_for_agent": {
        "purpose": "Generate 12 master reference images untuk EP1 Jaka Tingkir Series. Single phase, no dependency, parallel.",
        "phase_master_ref": {
            "description": "Generate 12 image (8 karakter 5-angle + 4 artefak macro). Tidak ada dependency antar job — boleh parallel semua.",
            "count": len(jobs),
            "input": "text prompt only (no image input)",
            "output": "save each image to output_path",
            "aspect_ratio_rule": "16:9 untuk karakter (K), 1:1 untuk artefak (A)",
            "model_hint": "seedream-4.5 (atau best available)"
        },
        "execution_order": "single_phase_parallel",
        "output_organization": {
            "master_ref": "produksi/t2i-output/jaka-tingkir-ep1/master-ref/"
        },
        "reuse_note": "EP1 juga akan pakai 5 master ref yang SUDAH ADA (tidak perlu generate ulang): 3B-K001-sultan-trenggana (Pangeran Trenggana), 3A-K003-sunan-kalijaga (Sunan Kalijaga), 3B-L001-demak (Demak lokasi), 3B-S001-pendapa-demak (Pendapa scene), 3A-L002-malaka (Malaka lokasi).",
        "qc_check": {
            "aspect_ratio_check": "8 K harus 16:9 (1920x1080), 4 A harus 1:1 (1080x1080)",
            "konsistensi_karakter": "5-angle dalam 1 K image harus menunjukkan karakter yang sama",
            "no_modern_elements": "Tidak boleh ada modern elements (kabel, aspal, building modern, electric lights)"
        }
    },
    "phases": [{
        "phase_id": "phase_master_ref_ep1",
        "name": "Generate Master Reference Images untuk EP1",
        "parallel": True,
        "depends_on": None,
        "jobs": jobs
    }],
    "total_jobs": len(jobs),
    "summary": {
        "total_images": len(jobs),
        "new_prompts": 12,
        "reuse_existing": 5,
        "characters": 8,
        "artifacts": 4,
        "estimasi_dola_time": "5-10 menit untuk 12 image parallel"
    },
    "reuse_existing_assets": [
        {"asset_id": "EP1-C009", "name": "Pangeran Trenggana", "prompt_file": "3B-K001-sultan-trenggana.txt", "notes": "Reuse dari era 3B"},
        {"asset_id": "EP1-C010", "name": "Sunan Kalijaga", "prompt_file": "3A-K003-sunan-kalijaga.txt", "notes": "Reuse dari era 3A"},
        {"asset_id": "EP1-L001", "name": "Demak Bintara (lokasi)", "prompt_file": "3B-L001-demak.txt", "notes": "Reuse dari era 3B"},
        {"asset_id": "EP1-L002", "name": "Malaka (lokasi)", "prompt_file": "3A-L002-malaka.txt", "notes": "Reuse dari era 3A"},
        {"asset_id": "EP1-S001", "name": "Pendapa Demak (scene)", "prompt_file": "3B-S001-pendapa-demak.txt", "notes": "Reuse dari era 3B"}
    ]
}

# Write
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

size_kb = OUT.stat().st_size / 1024
print(f"✅ Written: {OUT}")
print(f"   Size: {size_kb:.1f} KB")
print(f"   Total jobs: {batch['total_jobs']}")
print()
print("=== 12 NEW JOBS (PARALLEL) ===")
for j in jobs:
    ar = "16:9" if j["asset_type"] == "character" else "1:1"
    print(f"  {j['job_id']:12s} [{j['asset_type']:9s}] {ar:5s} {j['asset_name']:30s} → {j['output_path'].split('/')[-1]}")
print()
print("=== 5 REUSE EXISTING (tidak perlu generate) ===")
for r in batch["reuse_existing_assets"]:
    print(f"  {r['asset_id']:12s} {r['name']:30s} ← {r['prompt_file']}")
print()
print("Workflow:")
print("  1. User: review + edit naskah EP1 (parallel, fokus dialog Jawa)")
print("  2. User: upload dola-batch-EP1-master-ref.json ke Dola → trigger skill")
print("  3. Setelah keduanya selesai → AI bikin storyboard frame prompts + JSON final")
