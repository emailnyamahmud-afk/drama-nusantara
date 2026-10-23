# Review Hasil I2V Google Flow — Segment S001_seg04 (Prophecy)

**Tanggal**: 2026-10-23
**Platform**: Google Flow Veo
**Source video**: `upload/Men_speaking_about_prophecy_20261023085011.mp4`
**Saved**: `produksi/i2v-output/prototype-30s/flow-S001_seg04.mp4`

---

## 📊 Video Specs

| Spec | Expected | Actual | Status |
|---|---|---|---|
| Duration | 4s (Flow option) | **4.00s** | ✅ Perfect |
| Resolution | 360p (640×360) | **640×360** | ✅ Perfect sesuai request |
| FPS | 24 | **24** | ✅ Perfect |
| Codec | H.264 | **H.264/AVC High Profile** | ✅ Standard web |
| Bitrate | ~1-2 Mbps | **1.56 Mbps** | ✅ Reasonable |
| File size | ~500KB-1MB | **837 KB** | ✅ Kecil, web-friendly |
| Audio | Native SFX + dialogue | ✅ **AAC 48kHz stereo 128kbps** | ⭐ NATIVE DIALOGUE! |
| Watermark | None | ✅ **NONE** | ⭐ Clean video! |

**Comparison dengan Dola Seedance 2.5**:

| Spec | Dola seg01 | Flow seg04 |
|---|---|---|
| Resolution | 1248×704 (more detail) | 640×360 (360p) |
| File size | 2.65 MB | 837 KB |
| Codec | H.265/HEVC | H.264/AVC |
| Audio | NONE | ✅ Native AAC |
| Watermark | ❌ ADA | ✅ NONE |
| Dialogue native | ❌ | ✅ Ya (meskipun terpotong) |

---

## 🎨 Hasil VLM Analysis (3 frame: t=0, t=2, t=3s)

### Frame Awal (t=0s) — Two-shot composition
| Kriteria | Hasil |
|---|---|
| 2 karakter terlihat | ✅ Ya |
| Karakter 1 (kiri) = Lohgawe (jubah putih, jenggot putih) | ✅ Sesuai |
| Karakter 2 (kanan) = Ken Arok (golden brown, topknot, leather armor) | ✅ Sesuai |
| Two-shot composition | ✅ Keduanya terlihat jelas |
| Hutan + god rays background | ✅ Ada |

### Frame Tengah (t=2s) — Camera still in two-shot
| Kriteria | Hasil |
|---|---|
| Komposisi masih two-shot | ✅ Ya, frontal two-shot |
| Karakter konsisten vs awal | ✅ Identical (kostum, atribut, proporsi) |
| Arc rotation terlihat? | ⚠️ Belum signifikan — kamera masih locked-off |

### Frame Akhir (t=3s) — Over-shoulder shot! ⭐
| Kriteria | Hasil |
|---|---|
| Berhasil jadi over-shoulder shot | ✅ **YA, BERHASIL!** |
| Bahu Lohgawe di foreground | ✅ Ya (rambut abu-abu, jenggot, tongkat) |
| Wajah Ken Arok di background | ✅ Ya (muda, kumis, rompi kulit, keris) |
| Ken Arok stunned reaction | ✅ Mata melotot lebar, alis terangkat, mulut sedikit terbuka |
| Camera arc rotation berhasil | ⭐ **YA, dari two-shot → over-shoulder** |
| Fokus emosional ke reaction Ken Arok | ✅ Tercipta dengan baik |

---

## 🎯 Overall Verdict: ⭐ EXCELLENT — BEST I2V RESULT SO FAR

### Yang Berhasil (STRENGTHS):
1. ⭐ **Camera arc rotation BERHASIL** — dari two-shot → over-shoulder shot, sesuai prompt!
2. ⭐ **2-karakter konsistensi maintained** — Lohgawe + Ken Arok sama di semua frame
3. ⭐ **Native audio included** — AAC stereo 48kHz (SFX + dialogue)
4. ⭐ **NO watermark** — clean video, langsung pakai
5. ⭐ **Stunned reaction Ken Arok terlihat jelas** — emotion conveyed
6. ✅ **Durasi 4.00s exact** — sesuai Flow option
7. ✅ **Resolution 360p sesuai request** — bisa upscale di akhir via Real-ESRGAN
8. ✅ **File size kecil** (837 KB) — web-friendly, hemat storage
9. ✅ **Codec H.264 standard** — compatible semua player/editor

### Yang Perlu Diiterasi (WEAKNESSES):
1. ⚠️ **Dialog native TERPOTONG**:
   - Original: "Aku tidak menaruh kasihan, Ken Arok. Aku menaruh ramalan. Dewa Wisnu tidak mengirimmu ke dunia fana hanya untuk menjadi pencuri rendahan."
   - Generated: "Ken Arok, aku menaruh ramalan, kau..."
   - **Penyebab**: Durasi 4s terlalu pendek untuk dialog lengkap
   - **Solusi**: Pakai 6s atau 8s untuk segmen dengan dialog panjang
   - **Atau**: Mute audio video + pakai edge-tts untuk dialog lengkap (Phase 7)

2. ⚠️ **Camera movement baru terlihat di akhir** (t=3s):
   - Frame t=0 dan t=2 masih statis
   - Arc rotation baru terlihat di akhir video
   - **Penyebab**: Mungkin Flow perlu build-up momentum
   - **Solusi**: Bisa pakai 6s untuk arc movement yang lebih gradual

---

## 📊 Perbandingan 2 Platform — Verdict Final

| Kriteria | Dola Seedance 2.5 | Google Flow Veo | Winner |
|---|---|---|---|
| Camera movement sesuai prompt | ❌ Tidak (seg01) | ✅ Ya (seg04 arc) | **Flow** ⭐ |
| Karakter konsistensi | ✅ Ya | ✅ Ya | Tie |
| Audio native | ❌ NONE | ✅ AAC stereo | **Flow** ⭐ |
| Watermark | ❌ ADA | ✅ NONE | **Flow** ⭐ |
| Resolution | 720p (better) | 360p (lower) | Dola |
| File size | 2.65 MB | 837 KB | Flow |
| Cost | 3cr/hari (2 hari) | 50cr/hari (1 hari) | **Flow** ⭐ |
| Speed | 1-3 menit | 1-3 menit | Tie |
| **Total** | 2 win | **6 win** | **GOOGLE FLOW WIN** |

**Keputusan**: Lanjut pakai Google Flow untuk 5 segmen sisanya.

---

## 🚀 Strategi Lanjutan untuk 5 Segmen Sisanya

### Sekarang: User sudah pakai 4cr (seg04). Sisa 46cr.

### Opsi A — Pakai 360p 4s untuk semua segmen (24cr total, sisa 26cr)
**Pro**: Hemat, konsisten dengan strategi awal
**Kontra**: Dialog terpotong seperti seg04

### Opsi B — Mixed strategy berdasarkan dialog ⭐ RECOMMENDED
| Seg | Duration | Reason | Credits |
|---|---|---|---|
| seg01 Chase | 4s | Tidak ada dialog | 4cr |
| seg02 Taunt | 6s | Dialog pendek ("Hanya segitu...") | 6cr |
| seg03 Sage appears | 4s | Tidak ada dialog | 4cr |
| seg04 Prophecy | ✅ DONE | - | (4cr used) |
| seg05 Epiphany | 4s | Tidak ada dialog | 4cr |
| seg06 Title card | 6s | Title card + ambient | 6cr |
| **Total** | - | - | **24cr** |

Sisa 22cr untuk iterate critical frames dengan 720p.

### Opsi C — All 6s untuk better camera movement + dialog (36cr)
- Total 36cr, sisa 14cr untuk iterate
- Camera arc lebih gradual, dialog lebih lengkap
- Trade-off: more credits used

---

## 💡 Rekomendasi Saya

**Opsi B (Mixed strategy)** — paling balanced:
- Segmen tanpa dialog → 4s (hemat)
- Segmen dengan dialog → 6s (dialog lebih lengkap)
- Total 24cr (sama dengan opsi A)
- Sisa 22cr untuk iterate critical frames kalau perlu

### Action items untuk user:
1. Lanjut generate 5 segmen sisanya di Flow (pilih duration sesuai tabel di atas)
2. Setelah semua 6 video jadi, share ke saya untuk review menyeluruh
3. Kalau ada yang kurang, iterate dengan credits sisa

---

## 📁 File Saved

```
produksi/i2v-output/prototype-30s/
├── flow-S001_seg04.mp4    (837 KB, 4s, 360p, AAC audio) ⭐ BEST RESULT
└── S001_seg01.mp4          (2.65 MB, 5.04s, 720p, no audio) — Dola version
```

Plus 4 extracted frames di `download/flow-i2v-seg04-frames/` untuk VLM analysis reference.

---

## 🏆 Milestone Update

| Phase | Status |
|---|---|
| Phase 1-4 (Riset + Master Era + T2I Prompt + Pra-produksi JSON) | ✅ |
| Phase 5 (T2I Production) | ✅ 12 image generated Dola |
| **Phase 6 (I2V Production)** | 🔄 **2/6 video done** — seg01 Dola + seg04 Flow |
| Phase 7 (TTS) | ⏳ Next — edge-tts untuk narasi/dialog |
| Phase 8 (Stitch) | ⏳ Next — ffmpeg 6 clips + TTS |

**Status**: 
- ✅ Dola I2V tested (seg01) — quality OK, ada watermark
- ⭐ **Flow I2V tested (seg04) — quality EXCELLENT, no watermark, native audio**
- Flow menang untuk strategi utama, Dola backup kalau Flow credits habis
