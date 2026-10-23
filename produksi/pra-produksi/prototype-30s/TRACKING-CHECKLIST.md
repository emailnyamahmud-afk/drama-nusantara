# Prototype 30s — Tracking Checklist

**Status**: Dola AI skill sedang dibuat & dieksekusi
**Source**: `dola-batch.json` (24.9 KB, 12 job total)
**Output target**: 12 image di `produksi/t2i-output/`

---

## Phase 1 — Master Reference (6 job, parallel, no dependency)

Setelah phase 1 selesai, cek tiap image:

### ref-C001 Ken Arok
- [ ] Image tersimpan: `master-reff/2C/C001-2C-K002-ken-arok.jpg`
- [ ] Aspect 16:9 horizontal (1920×1080)
- [ ] 5 angle dalam 1 frame (frontal face + full body front + side profile + side full + back)
- [ ] Wajah KONSISTEN di semua 5 angle
- [ ] Costum: leather chest armor, woven kain, topknot, scar di pipi kiri
- [ ] Background clean cream studio (no environment)

### ref-C002 Dang Hyang Lohgawe
- [ ] Image tersimpan: `master-reff/2C/C002-2C-K007-dang-hyang-lohgawe.jpg`
- [ ] Aspect 16:9 horizontal
- [ ] 5 angle dalam 1 frame
- [ ] Pria 60-an, jenggot putih panjang, rambut besi topknot
- [ ] Jubah katun putih lusuh, kalung rudraksha
- [ ] Background clean cream studio

### ref-L001 Hutan Tumapel
- [ ] Image tersimpan: `master-reff/2C/L001-2C-L008-hutan-tumapel.jpg`
- [ ] Aspect 16:9 horizontal
- [ ] NO people, NO characters (empty location ref)
- [ ] Hutan jati tropis, pohon tinggi, kulit kayu kering
- [ ] God rays menembus kanopi (midday)
- [ ] Tanah kering + lumpur, batang pohon tumbang berlumut

### ref-L002 Pendopo Akuwu Tumapel
- [ ] Image tersimpan: `master-reff/2C/L002-2C-L009-pendopo-akuwu-tumapel.jpg`
- [ ] Aspect 16:9 horizontal
- [ ] NO people
- [ ] Pendopo dengan pilar kayu jati berukir, atap ijuk
- [ ] Singgasana di latar belakang
- [ ] Obor api + god rays dari samping

### ref-P001 Sekantung Beras
- [ ] Image tersimpan: `master-reff/2C/P001-2C-A004-sekantung-beras.jpg`
- [ ] Aspect **1:1 square** (1080×1080) — BEDA dengan yang lain
- [ ] Macro shot, kantung goni cokelat
- [ ] Detail weave serat jute terlihat
- [ ] Beras putih menyembul di sambungan
- [ ] NO people, NO hands

### ref-P002 Tombak Prajurit
- [ ] Image tersimpan: `master-reff/2C/P002-2C-A005-tombak-prajurit.jpg`
- [ ] Aspect **1:1 square**
- [ ] Macro shot, mata tombak perunggu daun memanjang
- [ ] Shaft kayu jati gelap
- [ ] Kerah kuningan + jumbai rambut kuda merah
- [ ] NO people, NO hands

---

## Phase 2 — Storyboard Frame (6 job, parallel, depends on phase 1)

### frame-S001_seg01 (5s) — Chase Through Dense Woods
- [ ] Image tersimpan: `prototype-30s/S001_seg01.jpg`
- [ ] Aspect 16:9 horizontal
- [ ] Ken Arok sprint di hutan (KONSISTEN dengan ref-C001)
- [ ] 3 prajurit di background dengan tombak (KONSISTEN dengan ref-P002)
- [ ] God rays + motion blur
- [ ] Mood: tense, adrenaline

### frame-S001_seg02 (5s) — Arok Taunts Pursuers
- [ ] Image tersimpan: `prototype-30s/S001_seg02.jpg`
- [ ] Ken Arok di atas batang pohon tumbang (KONSISTEN)
- [ ] Ekspresi menantang (arrogant grin)
- [ ] Prajurit di background dengan tombak
- [ ] Low-angle shot

### frame-S001_seg03 (5s) — Brahmana Halts Conflict
- [ ] Image tersimpan: `prototype-30s/S001_seg03.jpg`
- [ ] Dang Hyang Lohgawe muncul dari balik pohon banyan (KONSISTEN dengan ref-C002)
- [ ] Tangan kanan terangkat (peace gesture)
- [ ] Prajurit menundukkan senjata
- [ ] Mood shift: tense → sacred

### frame-S001_seg04 (5s) — Prophecy Unveiled (CRITICAL FRAME)
- [ ] Image tersimpan: `prototype-30s/S001_seg04.jpg`
- [ ] **2 karakter sekaligus**: Ken Arok + Dang Hyang Lohgawe (KEDUANYA KONSISTEN)
- [ ] Lohgawe berdiri dekat Ken Arok, mata menembus
- [ ] Ken Arok paralyzed, ekspresi disbelief
- [ ] Soft warm sunlight di antara mereka
- [ ] Slow arc shot framing

### frame-S001_seg05 (5s) — Arok Struck by Lightning
- [ ] Image tersimpan: `prototype-30s/S001_seg05.jpg`
- [ ] Extreme close-up mata Ken Arok (KONSISTEN)
- [ ] Refleksi cahaya keemasan di mata
- [ ] Background blur dreamlike
- [ ] Snap zoom effect

### frame-S001_seg06 (5s) — Title Card
- [ ] Image tersimpan: `prototype-30s/S001_seg06.jpg`
- [ ] Ken Arok walking away through forest (KONSISTEN)
- [ ] Camera crane up revealing sun breaking through canopy
- [ ] Title text overlay: "KEN AROK: TAKDIR DARI TUMAPEL" (kalau Dola bisa render text)
- [ ] Mood: dramatic resolution

---

## Quality Checklist Keseluruhan

### Karakter Konsistensi (HARUS PASS)
- [ ] Ken Arok di frame 1, 2, 4, 5, 6 → wajah SAMA (bandingkan dengan ref-C001)
- [ ] Dang Hyang Lohgawe di frame 3, 4 → wajah SAMA (bandingkan dengan ref-C002)
- [ ] Jika ada inkonsistensi → regenerate frame tersebut dengan ref image yang lebih jelas

### Lokasi Konsistensi
- [ ] Hutan Tumapel di frame 1, 2, 3, 4 → tone warna + jenis pohon SAMA
- [ ] Tidak ada modern elements (jalan aspal, kabel, building modern)

### Aspect Ratio
- [ ] 4 ref K/L = 16:9 (1920×1080)
- [ ] 2 ref A (P001, P002) = 1:1 (1080×1080)
- [ ] 6 storyboard frame = 16:9 (1920×1080)

### Style Konsistensi
- [ ] All 12 image → "cinematic realistic, Javanese period drama"
- [ ] Color grade: warm earthy tones dengan golden highlights
- [ ] Tidak ada anime/cartoon/3D render look

---

## Iteration Tracking

Jika ada image yang perlu di-regenerate:

| Job ID | Attempt | Status | Issue | Action |
|---|---|---|---|---|
| ref-C001 | 1 | ⏳ | - | - |
| ref-C002 | 1 | ⏳ | - | - |
| ref-L001 | 1 | ⏳ | - | - |
| ref-L002 | 1 | ⏳ | - | - |
| ref-P001 | 1 | ⏳ | - | - |
| ref-P002 | 1 | ⏳ | - | - |
| frame-S001_seg01 | 1 | ⏳ | - | - |
| frame-S001_seg02 | 1 | ⏳ | - | - |
| frame-S001_seg03 | 1 | ⏳ | - | - |
| frame-S001_seg04 | 1 | ⏳ | - | - |
| frame-S001_seg05 | 1 | ⏳ | - | - |
| frame-S001_seg06 | 1 | ⏳ | - | - |

**Status legend**: ⏳ pending / ✅ pass / ❌ fail / 🔄 regenerating

---

## Setelah 12 Image Selesai

1. **Save all** ke folder lokal (struktur sesuai `output_path`):
   ```
   produksi/t2i-output/
   ├── master-reff/2C/
   │   ├── C001-2C-K002-ken-arok.jpg
   │   ├── C002-2C-K007-dang-hyang-lohgawe.jpg
   │   ├── L001-2C-L008-hutan-tumapel.jpg
   │   ├── L002-2C-L009-pendopo-akuwu-tumapel.jpg
   │   ├── P001-2C-A004-sekantung-beras.jpg
   │   └── P002-2C-A005-tombak-prajurit.jpg
   └── prototype-30s/
       ├── S001_seg01.jpg
       ├── S001_seg02.jpg
       ├── S001_seg03.jpg
       ├── S001_seg04.jpg
       ├── S001_seg05.jpg
       └── S001_seg06.jpg
   ```

2. **Share 3 sample** ke AI Z.ai untuk review:
   - ref-C001 (Ken Arok) — karakter utama
   - frame-S001_seg04 (Prophecy) — critical frame dengan 2 karakter
   - frame-S001_seg06 (Title card) — closing shot

3. **Iterasi**: kalau ada yang kurang, edit prompt di `.txt` atau di `storyboard.json` → regenerate `dola-batch.json` → upload ulang ke Dola.

4. **Lanjut Phase 6 (I2V)** — kalau semua image sudah pass:
   - Pakai `motion.prompt` di setiap segmen untuk input ke I2V
   - Opsi: Dola video / Flow / Kling / Runway / LTX
   - Output 6 clip 5-detik

5. **Phase 7 (TTS)** — voice over narasi:
   - edge-tts voice id-ID-Ardi
   - Audio: 6 segment narasi/dialog dari `audio.tts_text`

6. **Phase 8 (Stitch)** — final 30s video:
   - ffmpeg composite 6 clips + TTS audio + title card overlay
