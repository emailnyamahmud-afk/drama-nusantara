# Workflow Paralel — EP1 Jaka Tingkir

**Tujuan**: User review naskah sambil AI generate T2I secara paralel, supaya waktu total produksi EP1 efisien.

---

## 🎯 Konsep Paralel

Naskah dan T2I memiliki **sensitifitas berbeda terhadap perubahan**:

| Jenis | Tergantung Naskah? | Bisa Mulai Sekarang? |
|---|---|---|
| **Master ref** (karakter, lokasi, artefak) | ❌ Tidak (karakter fisik stabil) | ✅ YA — paralel |
| **Storyboard frame** (visual per segmen) | ✅ Ya (visual spec di naskah) | ⏳ Tunggu naskah final |

**Insight**: Master ref (8 karakter + 4 artefak) bisa langsung di-generate sekarang, terlepas dari edit naskah. Karakter seperti Raden Patah, Raden Yunus, Sunan Kudus — deskripsi fisik mereka tidak akan berubah meski dialog Jawa di-edit.

---

## 📋 Workflow Paralel (Sekarang)

```
┌──────────────────────────────────────────────────────────────────┐
│ PARALLEL TRACK A — USER                                          │
│                                                                  │
│ Review + edit naskah EP1 di:                                     │
│ produksi/pra-produksi/jaka-tingkir-series/EP1-NASKAH.md          │
│                                                                  │
│ Fokus review:                                                    │
│ - Dialog Bahasa Jawa (Raden Patah, Raden Yunus)                  │
│ - Story flow 7 scene                                            │
│ - Tone entertainment                                             │
│ - Cliffhanger ending                                             │
│                                                                  │
│ Estimasi waktu: 30-60 menit                                      │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ PARALLEL TRACK B — AI + DOLA                                     │
│                                                                  │
│ 1. ✅ AI sudah generate 12 master ref prompt .txt baru            │
│    Lokasi: produksi/master-reff-t2i-prompts/3B-demak-pajang/    │
│           prompts/3B-K007 s/d 3B-K014 + 3B-A004 s/d 3B-A007    │
│                                                                  │
│ 2. ✅ AI sudah generate dola-batch-EP1-master-ref.json (35.8 KB) │
│    Lokasi: produksi/pra-produksi/jaka-tingkir-series/           │
│           dola-batch-EP1-master-ref.json                         │
│                                                                  │
│ 3. ⏳ User upload JSON ke Dola AI → trigger skill                 │
│    "jalankan batch storyboard"                                   │
│                                                                  │
│ 4. ⏳ Dola generate 12 image (8 K + 4 A), parallel, ~5-10 mnt    │
│                                                                  │
│ 5. ⏳ User download 12 image, save ke:                            │
│    produksi/t2i-output/jaka-tingkir-ep1/master-ref/              │
└──────────────────────────────────────────────────────────────────┘

Setelah DUA-DUANYA selesai:
┌──────────────────────────────────────────────────────────────────┐
│ MERGE FASE — AI                                                  │
│                                                                  │
│ 1. AI: bikin 17 storyboard frame prompts                         │
│    (pakai visual spec dari naskah FINAL + master ref image      │
│    yang sudah jadi)                                              │
│                                                                  │
│ 2. AI: generate dola-batch-EP1-storyboard-frame.json             │
│                                                                  │
│ 3. User: upload ke Dola → generate 17 storyboard frame           │
│                                                                  │
│ 4. AI: compile semua → JSON final v3.1 EP1                       │
│                                                                  │
│ 5. User: review JSON final → approve                             │
└──────────────────────────────────────────────────────────────────┘

Setelah JSON final approved:
┌──────────────────────────────────────────────────────────────────┐
│ PRODUKSI — AI                                                    │
│                                                                  │
│ 1. Generate TTS adaptive (rate +25%) per segmen                  │
│ 2. Stitch via ffmpeg Ken Burns                                   │
│ 3. Output: jaka-tingkir-ep1.mp4 (12 menit, 1920x1080)           │
│                                                                  │
│ Estimasi: 2 jam setelah JSON final approved                      │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📁 File yang Sudah Siap

### Untuk User Review Naskah:
- **`produksi/pra-produksi/jaka-tingkir-series/EP1-NASKAH.md`** — naskah lengkap 7 scene, 17 segmen

### Untuk Upload ke Dola (Track B):
- **`produksi/pra-produksi/jaka-tingkir-series/dola-batch-EP1-master-ref.json`** (35.8 KB) — 12 job T2I master ref

### Master Ref Prompts Baru (12 file .txt):
Lokasi: `produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts/`

| File | Karakter/Artefak |
|---|---|
| 3B-K007-raden-patah.txt | Raden Patah (Sultan I) |
| 3B-K008-raden-yunus.txt | Raden Yunus (Sultan II) |
| 3B-K009-raden-suryawiyata.txt | Raden Suryawiyata |
| 3B-K010-sunan-kudus.txt | Sunan Kudus |
| 3B-K011-sunan-giri-dalem.txt | Sunan Giri Dalem |
| 3B-K012-hang-tuah.txt | Hang Tuah |
| 3B-K013-prajurit-demak.txt | Prajurit Demak |
| 3B-K014-prajurit-portugis.txt | Prajurit Portugis |
| 3B-A004-keris-kyai-naga-sasra.txt | Keris Kyai Naga Sasra |
| 3B-A005-singgasana-demak.txt | Singgasana Demak |
| 3B-A006-mahkota-sultan-demak.txt | Mahkota Sultan Demak |
| 3B-A007-bendera-surya-majapahit.txt | Bendera Surya Majapahit |

### Master Ref yang Sudah Ada (Reuse, 5 file):
- `3B-K001-sultan-trenggana.txt` → Pangeran Trenggana
- `3A-K003-sunan-kalijaga.txt` → Sunan Kalijaga
- `3B-L001-demak.txt` → Lokasi Demak
- `3A-L002-malaka.txt` → Lokasi Malaka
- `3B-S001-pendapa-demak.txt` → Pendapa Demak (scene)

---

## 🚀 Cara Mulai Track B (Upload ke Dola)

### Opsi 1 — Pakai skill Dola yang sudah ada
1. Buka Dola AI (sesi yang sama dengan prototype 30s)
2. Upload `dola-batch-EP1-master-ref.json`
3. Ketik: `jalankan batch storyboard`
4. Skill `batch-storyboard-generator` akan auto-trigger
5. Tunggu 5-10 menit untuk 12 image parallel
6. Download 12 image + contact sheet

### Opsi 2 — Manual copy-paste (kalau skill Dola tidak support batch besar)
1. Buka Dola AI
2. Untuk tiap file .txt di `produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts/3B-K007` s/d `3B-A007` (12 file):
   - Buka file .txt
   - Copy seluruh isi
   - Paste ke chat Dola
   - Generate 1 image
   - Download
3. Save ke `produksi/t2i-output/jaka-tingkir-ep1/master-ref/`

---

## 📊 Estimasi Timeline Paralel

| Track | Mulai | Selesai | Durasi |
|---|---|---|---|
| A: User review naskah | Sekarang | +45 menit | ~45 menit |
| B: AI prompt (done) + User upload Dola + Dola generate | Sekarang | +15 menit | ~15 menit |
| B: User download 12 image | Setelah Dola selesai | +5 menit | 5 menit |
| **PARALLEL TOTAL** | - | **+45 menit** | (maks A atau B, mana yang lebih lama) |
| Merge: AI bikin storyboard frame prompts | Setelah naskah + master ref ready | +30 menit | 30 menit |
| Merge: User upload + Dola generate 17 frame | Setelah prompts ready | +15 menit | 15 menit |
| Merge: AI compile JSON final | Setelah frame ready | +15 menit | 15 menit |
| User review JSON final | Setelah JSON ready | +20 menit | 20 menit |
| Produksi: AI TTS + ffmpeg stitch | Setelah JSON approved | +120 menit | 2 jam |
| **TOTAL EP1 production** | - | - | **~4 jam** |

**Tanpa paralel** (sequential): ~6 jam
**Dengan paralel**: ~4 jam (hemat ~2 jam)

---

## ❓ Pertanyaan untuk User

1. **Mulai paralel sekarang?**
   - Track A: User buka `EP1-NASKAH.md`, review + edit dialog Jawa
   - Track B: User upload `dola-batch-EP1-master-ref.json` ke Dola

2. **Mau saya commit + push dulu supaya bisa download dari GitHub?**

3. **Kalau ada masalah dengan skill Dola**, mau pakai Opsi 2 (manual copy-paste 12 prompt)?

Saran: mulai keduanya sekarang. Sambil user review naskah, Dola generate master ref di background.
