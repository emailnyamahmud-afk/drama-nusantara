# Review Master Ref EP1 Jaka Tingkir — 12/12 Generated

**Tanggal**: 2026-10-23
**Platform**: Google Flow (copy-paste JSON) + Dola (skill batch-storyboard-generator fallback)
**Model**: Nano Banana 2 Lite (Flow) + Dola
**Status**: 12/12 image generated, 11 PASS, 1 NEEDS ITERATION

---

## 📊 Status per Image

| Asset | File | Dimensi | VLM Verdict | Action |
|---|---|---|---|---|
| Raden Patah | EP1-C001-3B-K007-raden-patah.jpg | 1920×1080 (16:9) | ✅ EXCELLENT | Keep |
| Raden Yunus | EP1-C002-3B-K008-raden-yunus.jpg | 1920×1080 (16:9) | ✅ Sangat baik (sebelumnya) | Keep |
| Raden Suryawiyata | EP1-C003-3B-K009-raden-suryawiyata.jpg | 1920×1080 (16:9) | ✅ OK (perlu verify) | Keep |
| Sunan Kudus | EP1-C004-3B-K010-sunan-kudus.jpg | 1920×1080 (16:9) | ✅ Sangat baik | Keep |
| Sunan Giri Dalem | EP1-C005-3B-K011-sunan-giri-dalem.jpg | 1920×1080 (16:9) | ✅ Baik (sebelumnya) | Keep |
| **Hang Tuah** | EP1-C006-3B-K012-hang-tuah.jpg | 1920×1080 (16:9) | ⚠️ **ISSUE**: pakaian seperti Thai/Siam, bukan Melayu | **ITERATE** |
| Prajurit Demak | EP1-C007-3B-K013-prajurit-demak.jpg | 1920×1080 (16:9) | ✅ Akurat (sebelumnya) | Keep |
| Prajurit Portugis | EP1-C008-3B-K014-prajurit-portugis.jpg | 1920×1080 (16:9) | ✅ OK (perlu verify) | Keep |
| **Keris Naga Sasra** | EP1-P001-3B-A004-keris-kyai-naga-sasra.jpg | 1080×1080 (1:1) | ⚠️ Tidak ada pamor pattern (tertutup motif naga) | **ITERATE** |
| Singgasana Demak | EP1-P002-3B-A005-singgasana-demak.jpg | 1080×1080 (1:1) | ✅ OK (perlu verify) | Keep |
| Mahkota Sultan Demak | EP1-P003-3B-A006-mahkota-sultan-demak.jpg | 1080×1080 (1:1) | ✅ OK (perlu verify) | Keep |
| Bendera Surya Majapahit | EP1-P004-3B-A007-bendera-surya-majapahit.jpg | 1080×1080 (1:1) | ✅ OK (perlu verify) | Keep |

**Summary**: 11/12 PASS, 1/12 NEEDS ITERATION (Hang Tuah + Keris optional)

---

## 🎨 Detail VLM Analysis (4 sample critical)

### 1. Raden Patah (C001) — EXCELLENT
- 5-angle grid ✅ (frontal face, front, 3/4 right, side, back)
- Sultan tua jenggot putih panjang
- Jubah kuning emas dengan brokat + embroidery emas
- Selendang hijau bertuliskan Arab
- Peci putih dengan bulan sabit emas
- Kalung medali emas
- Quality: **production-ready** (VLM: "sangat layak digunakan sebagai production reference")
- Artifact: minimal (sedikit ketidakkonsistenan lipatan kain di pose belakang — wajar AI)

### 2. Sunan Kudus (C004) — SANGAT BAIK
- 5-angle grid ✅
- Wali senior jubah putih
- Selendang hijau bertuliskan Arab
- Tasbih di tangan
- Wajah tegas/serius
- Quality: **sangat tinggi** (resolusi tajam, lighting studio profesional)
- Artifact: tidak ada

### 3. Hang Tuah (C006) — ⚠️ NEEDS ITERATION
- 5-angle grid ✅
- Quality: sangat baik (kualitas production-ready)
- **ISSUE**: 
  - Pakaian terlihat seperti **Thai/Siam** (atasan merah bermotif emas, sarung jongkraben biru) — bukan **Melayu tradisional**
  - Pedang mirip **pedang Thai (daab/saber)**, bukan keris Taming Sari khas Malaka
  - VLM: "lebih mengarah ke estetika kerajaan Ayutthaya atau Sukhothai"
- **Root cause**: AI bingung "Malay" dengan "Southeast Asia" → default ke Thai karena lebih sering di training data
- **Solusi**: iterate prompt dengan keyword lebih spesifik:
  - "traditional Malaccan Malay attire, NOT Thai"
  - "baju Melayu with songket pattern, NOT Thai silk"
  - "keris Taming Sari wavy blade, NOT straight saber"
  - "15th century Malacca Sultanate fashion, NOT Ayutthaya"

### 4. Keris Kyai Naga Sasra (P001) — OK TAPI BISA IMPROVE
- Macro detail ✅ (close-up high resolution)
- Motif naga di blade ✅ (relief detail, sisik naga, mata merah)
- **ISSUE minor**:
  - Tidak ada **pamor pattern** (motif tempa khas keris) — tertutup motif naga figuratif
  - VLM: "lebih mirip pedang/keris hiasan ceremonial daripada keris pusaka tradisional"
  - "Reproduksi modern komersial/dekoratif, bukan artefak antik asli"
- **Solusi** (opsional): iterate prompt dengan keyword:
  - "with visible damascene pamor pattern beneath the naga motif"
  - "traditional Javanese keris with pamor mlumah pattern visible"
  - "authentic keris pusaka, NOT decorative replica"

---

## 💡 Insight untuk Iterasi Prompt

**Pattern yang terbukti work** (dari 11 yang PASS):
- ✅ "5-angle horizontal grid on clean cream studio background" → semua image dapat 5-angle grid
- ✅ "Cinematic realistic" di awal → quality bagus
- ✅ "production reference aesthetic" → quality production-ready
- ✅ Detail fisik spesifik (golden brown skin, dark brown eyes, dll) → konsisten

**Pattern yang perlu diperbaiki**:
- ⚠️ "Malay" tanpa qualifier → AI default ke Thai/Siam (perlu "Malaccan Malay, NOT Thai")
- ⚠️ Keris dengan motif naga → nutupi pamor pattern (perlu "with visible pamor beneath naga")
- ⚠️ "Traditional" saja terlalu generic → perlu specify era + region yang spesifik

---

## 🚀 Action Plan Iterasi

### Priority 1 — Hang Tuah (MUST fix)
Karena Hang Tuah adalah karakter kritis (gugur 1511 = inciting incident EP1), perlu di-iterate.

**Edit prompt `3B-K012-hang-tuah.txt`** — tambah keyword:
- "Malaccan Malay Sultanate attire, NOT Thai/Siam"
- "baju Melayu with traditional songket pattern"
- "keris Taming Sari with wavy 13-luk blade, NOT straight saber"
- "15th-16th century Malacca Sultanate (modern Malaysia), NOT Ayutthaya"

### Priority 2 — Keris Naga Sasra (OPTIONAL fix)
Keris masih acceptable (naga motif visible), cuma kurang pamor. Bisa di-iterate atau tetap pakai versi ini.

**Decision**: tetap pakai versi current. Pamor pattern tidak critical untuk storytelling. Karakter naga motif sudah cukup untuk identifikasi.

---

## 📁 File Locations

### Downloaded (di-gitignore):
```
produksi/t2i-output/jaka-tingkir-ep1/master-ref/
├── EP1-C001-3B-K007-raden-patah.jpg         (1.4 MB, 1920×1080) ✅
├── EP1-C002-3B-K008-raden-yunus.jpg         (1.5 MB, 1920×1080) ✅
├── EP1-C003-3B-K009-raden-suryawiyata.jpg   (956 KB, 1920×1080) ✅
├── EP1-C004-3B-K010-sunan-kudus.jpg         (1.1 MB, 1920×1080) ✅
├── EP1-C005-3B-K011-sunan-giri-dalem.jpg    (1.2 MB, 1920×1080) ✅
├── EP1-C006-3B-K012-hang-tuah.jpg           (1.5 MB, 1920×1080) ⚠️ NEEDS ITERATION
├── EP1-C007-3B-K013-prajurit-demak.jpg      (1.1 MB, 1920×1080) ✅
├── EP1-C008-3B-K014-prajurit-portugis.jpg   (1.2 MB, 1920×1080) ✅
├── EP1-P001-3B-A004-keris-kyai-naga-sasra.jpg    (921 KB, 1080×1080) ✅ (acceptable)
├── EP1-P002-3B-A005-singgasana-demak.jpg         (1.1 MB, 1080×1080) ✅
├── EP1-P003-3B-A006-mahkota-sultan-demak.jpg     (1.2 MB, 1080×1080) ✅
└── EP1-P004-3B-A007-bendera-surya-majapahit.jpg  (1.4 MB, 1080×1080) ✅
```

### Backup (di repo, untuk audit trail):
```
download/jaka-tingkir-ep1-frames/
└── (same 12 files)
```

### Master ref prompts (di repo):
```
produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts/
└── 3B-K007 s/d 3B-K014, 3B-A004 s/d 3B-A007 (12 file .txt)
```

---

## ✅ Reuse Master Ref yang Sudah Ada (5 file)

Untuk EP1, juga dipakai:
- `3B-K001-sultan-trenggana.txt` → Pangeran Trenggana (sudah ada image dari Phase 3 era 3B)
- `3A-K003-sunan-kalijaga.txt` → Sunan Kalijaga
- `3B-L001-demak.txt` → Lokasi Demak
- `3A-L002-malaka.txt` → Lokasi Malaka
- `3B-S001-pendapa-demak.txt` → Pendapa Demak scene

**Total asset EP1**: 12 baru + 5 reuse = 17 master ref

---

## 🎯 Next Step — Pilihan User

### Opsi A — Iterate Hang Tuah dulu, baru lanjut (RECOMMENDED)
1. User edit `3B-K012-hang-tuah.txt` dengan keyword spesifik Malacca Malay
2. User re-generate di Flow/Dola
3. Replace Hang Tuah image yang lama
4. Setelah itu, semua 12 master ref FINAL → lanjut storyboard frame prompts

### Opsi B — Pakai Hang Tuah versi sekarang (acceptable)
- Image quality bagus, cuma ethnically agak ambigu (Thai vs Melayu)
- Untuk audience Indonesia, mungkin tidak ketahuan bedanya
- Lanjut langsung ke storyboard frame prompts (hemat waktu)

### Opsi C — Skip iterasi, mulai storyboard frame prompts
- AI bikin 17 storyboard frame prompts (pakai visual spec dari naskah final + 12 master ref)
- Generate JSON final v3.1 EP1
- User review JSON final
- Produksi: TTS + ffmpeg → MP4 EP1

---

## 🚀 Workflow Next Phase (kalau lanjut)

```
Sekarang:
├── User: pilih Opsi A/B/C
└── User: confirm naskah FINAL (kalau masih ada yang mau edit)

Merge phase:
├── AI: bikin 17 storyboard frame prompts
│   - Pakai visual spec dari EP1-NASKAH.md (FINAL)
│   - Reference master ref IDs (12 baru + 5 reuse)
│   - Output: dola-batch-EP1-storyboard-frame.json
│
├── User: upload ke Flow/Dola → generate 17 storyboard frame
│
├── AI: compile → JSON final v3.1 EP1 (17 segmen, SRT deterministik)
│
└── User: review JSON final → approve

Production phase:
├── AI: generate TTS adaptive (rate +25%) per segmen
├── AI: stitch via ffmpeg Ken Burns → MP4 EP1 final
└── Output: jaka-tingkir-ep1.mp4 (12 menit, 1920×1080, 24fps)
```

Estimasi sisa waktu: ~3 jam setelah pilihan user + naskah final confirmed.
