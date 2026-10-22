#!/usr/bin/env python3
"""
Generate prototype-30s/storyboard.json — schema v2 dengan adopsi Google Flow.

Prototype: KEN AROK short (30 detik, 6 segmen × 5s)
Era: 2C Singasari-Kediri (abad 11-13 M)
Sumber: master-era/2C-singasari-kediri.md + jilid-2/11-bab-4.md (Bharatayuddha context)
Asset link: produksi/master-reff-t2i-prompts/2C-singasari-kediri/prompts/
"""

import json
from pathlib import Path
from datetime import datetime

# ============================================================
# EPISODE META
# ============================================================
episode = {
    "id": "P002-PROTOTYPE-30S",
    "judul": "Ken Arok: Takdir dari Tumapel — Prototype 30s",
    "era": "2C Singasari-Kediri (abad 11-13 M)",
    "jilid_sumber": "2",
    "sumber_tambahan": "master-era/2C-singasari-kediri.md (rewrite lengkap) + Pararaton (Mpu Panuluh)",
    "durasi_target": 30,
    "resolusi": "1920x1080",  # 16:9 horizontal (adopsi #8)
    "fps": 24,
    "style": "cinematic realistic, Javanese period drama, dark-fantasy tones",
    "tanggal_dibuat": datetime.now().strftime("%Y-%m-%d"),
    "schema_version": "2.0",  # ★ adopsi Flow schema
    "catatan": "Prototype 30 detik untuk validasi end-to-end pipeline (T2I → I2V → TTS → stitch). 6 segmen × 5 detik. Babak pembuka — Ken Arok menemui takdirnya."
}

# ============================================================
# CHARACTERS — adopsi #1 (3-field schema) + #4 (include_inspiration flag)
# ============================================================
characters = [
    {
        "id": "C001",
        "nama": "Ken Arok",
        "peran": "Protagonis — pemuda pencuri yang ditakdirkan jadi raja",
        "physical_characteristics": "Pria Jawa 25 tahun, tubuh atletis tangguh, kulit cokelat keemasan, rahang tegas, mata cokelat amber melirik predator, rambut hitam ikal panjang berantakan",
        "clothing_accessories": "Ikat kepala kain crimson lusuh, rompi cokelat tanpa lengan di atas dada telanjang, sarung batik indigo di atas lutut diikat tali hemp, gelang tali dipergelangan tangan, kaki telanjang berlumpur",
        "backstory": "Yatim piatu yang dibesarkan jadi pencuri dan bandit di hutan Tumapel. Bertemu Dang Hyang Lohgawe yang meramalkan dia sebagai penjelmaan Wisnu yang ditakdirkan jadi raja",
        "voice": "id-ID-Ardi",
        "include_inspiration_in_image_gen": True,  # ★ adopsi #4 — karakter utama
        "ref_k_id": "2C-K002-ken-arok",
        "status": "draft"
    },
    {
        "id": "C002",
        "nama": "Dang Hyang Lohgawe",
        "peran": "Brahmana tua — peramal takdir",
        "physical_characteristics": "Pria Asia Tenggara 60-an, tubuh kurus berotot, kulit sawo matang terpanggang matahari, tulang pipi menonjol, mata cokelat gelap menembus, rambut besi panjang diikat topknot, jenggot putih sepanjang kerah",
        "clothing_accessories": "Jubah katun putih lusuh melilit bahu kiri (gaya Brahmana), dhoti sebatas betis, kalung tasbih rudraksha cokelat, sandal jangkar kulit tua",
        "backstory": "Resi Hindu dari India yang mengembara ke Jawa mencari raja yang ditakdirkan. Melihat Ken Arok bukan pencuri rendahan, tapi avatar Wisnu",
        "voice": "id-ID-Ardi",  # bisa ganti ke voice berbeda
        "include_inspiration_in_image_gen": True,
        "ref_k_id": "2C-K007-dang-hyang-lohgawe",  # ★ generated in Phase 3 v2.1
        "status": "draft"
    }
]

# ============================================================
# LOCATIONS — adopsi #1 (fisik saja) + #5 (time_of_day)
# ============================================================
locations = [
    {
        "id": "L001",
        "nama": "Hutan Tumapel",
        "physical_characteristics": "Hutan jati tropis luas dengan pohon-pohon tinggi berkulit kering, semak berduri lebat, batang pohon tumbang berlumut di jalur tanah kering. Bebatuan kapur berserakan. God rays menembus kanopi",
        "time_of_day": "midday",  # ★ adopsi #5
        "ref_l_id": "2C-L008-hutan-tumapel",  # ★ generated in Phase 3 v2.1
        "status": "draft"
    },
    {
        "id": "L002",
        "nama": "Pendopo Kediaman Akuwu Tumapel",
        "physical_characteristics": "Interior pendopo batu dengan lantai berukiran kuno, pilar kayu jati berukir, atap ijuk tinggi, obor api memberi cahaya dramatis, singgasana kayu berukir di tengah",
        "time_of_day": "day",
        "ref_l_id": "2C-L009-pendopo-akuwu-tumapel",  # ★ generated in Phase 3 v2.1
        "status": "draft"
    }
]

# ============================================================
# PROPS — array BARU (adopsi dari Flow, tidak ada di pilot Panji lama)
# ============================================================
props = [
    {
        "id": "P001",
        "nama": "Sekantung Beras",
        "physical_characteristics": "Kantung goni cokelat kasar diikat leher dengan tali hemp fray, noda lumpur, beberapa butir beras putih menyembul di sambungan",
        "include_inspiration_in_image_gen": False,  # prop sekunder
        "ref_a_id": "2C-A004-sekantung-beras",  # ★ generated in Phase 3 v2.1
        "status": "draft"
    },
    {
        "id": "P002",
        "nama": "Tombak Prajurit",
        "physical_characteristics": "Tombak infantri: batang kayu jati gelap 8 kaki, mata tombak perunggu daun memanjang dengan bevel tajam, kerah kawat kuningan dan jumbai rambut kuda merah",
        "include_inspiration_in_image_gen": False,
        "ref_a_id": "2C-A005-tombak-prajurit",  # ★ generated in Phase 3 v2.1
        "status": "draft"
    }
]

# ============================================================
# ACTS / SCENES / SEGMENTS — adopsi #2 (motion.prompt) + #3 (linked_asset_ids) + #7 (image_history)
# ============================================================
acts = [
    {
        "id": "A1",
        "judul": "Ramalan di Hutan Tumapel",
        "scenes": [
            {
                "id": "S001",
                "judul": "Pengejaran di Hutan",
                "lokasi": "L001",
                "mood": "tegas, menantang, penuh adrenalin",
                "segments": [
                    # ============ SEG 1 (0-5s) ============
                    {
                        "id": "S001_seg01",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic extreme wide tracking shot, young Javanese man Ken Arok sprints through dense tropical teak forest at midday, holding rough jute rice sack against chest, bare feet kicking up dust, three armored Tumapel soldiers chase in distant background with raised spears. Golden god rays cut through canopy, depth of field, motion blur on foliage, 50mm lens, 16:9 horizontal"
                        },
                        "motion": {  # ★ adopsi #2
                            "camera": "rapid backward tracking, ahead of subject",
                            "prompt": "Camera tracks rapidly backward ahead of Ken Arok, keeping him centered as foliage whips past frame edges",
                            "speed": "fast"
                        },
                        "audio": {
                            "type": "ambience",
                            "tts_text": "",  # tidak ada narasi
                            "tts_voice": None,
                            "bgm": "tense tribal percussion building, fast tempo matching footstep rhythm",
                            "sfx": "heavy panting, twigs snapping, distant shouting soldiers, metallic armor rattle"
                        },
                        "linked_asset_ids": ["C001", "L001", "P001", "P002"],  # ★ adopsi #3
                        "image_history": [],  # ★ adopsi #7
                        "notes": "Opening hook — establish chase & character"
                    },
                    # ============ SEG 2 (5-10s) ============
                    {
                        "id": "S001_seg02",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic medium low-angle shot, Ken Arok lands on mossy fallen log, pivots to face camera with arrogant grin, one hand grips jute rice sack, other gestures dismissively. Three soldiers in background with spears leveled, panting. Forest midday sun, dappled shadows, 35mm lens, 16:9 horizontal"
                        },
                        "motion": {
                            "camera": "low-angle medium, slight pan up as subject lands",
                            "prompt": "Low-angle medium shot pans slightly up as Ken Arok lands on log, emphasizing agile stance and height advantage over pursuers",
                            "speed": "medium"
                        },
                        "audio": {
                            "type": "dialogue",
                            "tts_text": "Hanya segitu kecepatan prajurit istana? Kura-kura di rawa pun masih bisa mendahului kalian!",
                            "tts_voice": "id-ID-Ardi",
                            "bgm": "percussion drops to sparse, anticipatory",
                            "sfx": "subject's confident exhale, soldiers' guttural grunts"
                        },
                        "linked_asset_ids": ["C001", "L001", "P001", "P002"],
                        "image_history": [],
                        "notes": "Establish Ken Arok's defiant character"
                    },
                    # ============ SEG 3 (10-15s) ============
                    {
                        "id": "S001_seg03",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic medium shot, old Brahmin sage Dang Hyang Lohgawe emerges calmly from behind massive banyan tree, weathered white robes glowing in dappled sunlight, right hand raised in peaceful commanding gesture. Soldiers in background lowering weapons in awe. Forest midday, ethereal soft light, 50mm lens, 16:9 horizontal"
                        },
                        "motion": {
                            "camera": "slow stately tilt up from hem of robes to serene face and raised hand",
                            "prompt": "Slow tilt-up from hem of Lohgawe's robes revealing his serene face and raised hand, establishing dominant spiritual presence",
                            "speed": "slow"
                        },
                        "audio": {
                            "type": "dialogue",
                            "tts_text": "Hentikan amarah kalian. Darah anak muda ini bukan untuk tumpah di tanah berlumpur ini.",
                            "tts_voice": "id-ID-Ardi",  # nanti ganti ke voice lebih berat/berat untuk Brahmana
                            "bgm": "ambient drone fades in, percussion silences",
                            "sfx": "wind hushes through leaves, soldiers' footsteps stop"
                        },
                        "linked_asset_ids": ["C002", "L001", "P002"],
                        "image_history": [],
                        "notes": "Pivot moment — sage halts conflict, shifts tone"
                    },
                    # ============ SEG 4 (15-20s) ============
                    {
                        "id": "S001_seg04",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic slow two-shot arc, Dang Hyang Lohgawe stands close to Ken Arok, piercing eyes into young rebel's soul. Ken Arok paralyzed in disbelief, defiant posture softening. Soft warm sunlight between two men, ancient forest canopy behind. Slow arc around them, 85mm lens, shallow depth of field, 16:9 horizontal"
                        },
                        "motion": {
                            "camera": "slow tense two-shot arc, rotates around the two men",
                            "prompt": "Slow tense two-shot arc gently rotates around the two men, ending framed over Lohgawe's shoulder onto Ken Arok's stunned reaction",
                            "speed": "slow"
                        },
                        "audio": {
                            "type": "dialogue",
                            "tts_text": "Aku tidak menaruh kasihan, Ken Arok. Aku menaruh ramalan. Dewa Wisnu tidak mengirimmu ke dunia fana hanya untuk menjadi pencuri rendahan.",
                            "tts_voice": "id-ID-Ardi",
                            "bgm": "low ethereal drone swells, all other ambient cut",
                            "sfx": "subject's breath catches, heartbeat subtly thumps"
                        },
                        "linked_asset_ids": ["C001", "C002", "L001"],
                        "image_history": [],
                        "notes": "The prophecy moment — turning point of Ken Arok's life"
                    },
                    # ============ SEG 5 (20-25s) ============
                    {
                        "id": "S001_seg05",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic extreme close-up on Ken Arok's eyes, wide and astonished, reflecting golden light. Jaw clenched, breath caught. Background forest dissolves into shallow dreamlike blur. Snap zoom punch-in effect, 85mm lens, 16:9 horizontal"
                        },
                        "motion": {
                            "camera": "rapid snap zoom punch-in to pupils, freeze, then subtle handheld tremble",
                            "prompt": "Rapid snap zoom punch-in directly into Ken Arok's pupils, freezing momentarily before settling with subtle trembling handheld framing",
                            "speed": "fast"
                        },
                        "audio": {
                            "type": "ambience",
                            "tts_text": "",
                            "tts_voice": None,
                            "bgm": "heartbeat thump loud, sub-bass pulse, ethereal chime",
                            "sfx": "muffled heartbeat, subtle whoosh mirroring thunderous shock"
                        },
                        "linked_asset_ids": ["C001"],
                        "image_history": [],
                        "notes": "Internal epiphany — ambition ignited"
                    },
                    # ============ SEG 6 (25-30s) ============
                    {
                        "id": "S001_seg06",
                        "durasi": 5,
                        "status": "draft",
                        "visual": {
                            "prompt": "Cinematic realistic wide pull-back shot rising higher, Ken Arok walks away through forest, camera cranes up revealing sun breaking through canopy. Title text overlay 'KEN AROK: TAKDIR DARI TUMAPEL' in elegant serif gold, fade-in. Forest midday god rays, 24mm lens, 16:9 horizontal"
                        },
                        "motion": {
                            "camera": "slow pull-back rising higher, crane up revealing sun",
                            "prompt": "Slow pull-back shot rising higher, re-establishing wide composition as Ken Arok walks away into god rays, title fades in",
                            "speed": "slow"
                        },
                        "audio": {
                            "type": "title_card",
                            "tts_text": "",
                            "tts_voice": None,
                            "bgm": "swelling orchestral strings + gamelan motif, dramatic resolution",
                            "sfx": "wind through canopy, distant bird call"
                        },
                        "linked_asset_ids": ["C001", "L001"],
                        "image_history": [],
                        "notes": "Closing title card — prototype end"
                    }
                ]
            }
        ]
    }
]

# ============================================================
# RENDER STATUS
# ============================================================
render_status = {
    "total_segments": 6,
    "draft": 6,
    "approved": 0,
    "image_generated": 0,
    "audio_generated": 0,
    "video_generated": 0,
    "rendered": 0,
    "failed": 0,
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
}

# ============================================================
# COMPILE + WRITE
# ============================================================
storyboard = {
    "episode": episode,
    "characters": characters,
    "locations": locations,
    "props": props,
    "acts": acts,
    "render_status": render_status
}

out_path = Path("/home/z/my-project/produksi/pra-produksi/prototype-30s/storyboard.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(storyboard, f, ensure_ascii=False, indent=2)

# Stats
size_kb = out_path.stat().st_size / 1024
total_durasi = sum(s["durasi"] for act in acts for sc in act["scenes"] for s in sc["segments"])
print(f"✅ Written: {out_path}")
print(f"   Size: {size_kb:.1f} KB (target < 500 KB)")
print(f"   Segments: {render_status['total_segments']}")
print(f"   Total durasi: {total_durasi}s = {total_durasi/60:.1f} menit")
print(f"   Characters: {len(characters)}")
print(f"   Locations: {len(locations)}")
print(f"   Props: {len(props)}")
print(f"   Schema version: 2.0 (adopsi Flow #1-#7)")

# Verify adopsi items
print("\n=== VERIFIKASI ADOPSI ===")
seg1 = acts[0]["scenes"][0]["segments"][0]
checks = [
    ("#1 Asset 3-field (physical/clothing/backstory)", 
     all(k in characters[0] for k in ["physical_characteristics","clothing_accessories","backstory"])),
    ("#2 motion.prompt field", "motion" in seg1 and "prompt" in seg1["motion"]),
    ("#3 linked_asset_ids (multi-asset)", "linked_asset_ids" in seg1 and len(seg1["linked_asset_ids"]) > 1),
    ("#4 include_inspiration_in_image_gen flag", 
     all("include_inspiration_in_image_gen" in c for c in characters)),
    ("#5 location.time_of_day", all("time_of_day" in l for l in locations)),
    ("#7 image_history per segment", "image_history" in seg1),
    ("#8 16:9 horizontal (1920x1080)", episode["resolusi"] == "1920x1080")
]
for name, ok in checks:
    print(f"   {'✅' if ok else '❌'} {name}")
