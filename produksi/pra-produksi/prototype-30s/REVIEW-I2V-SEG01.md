# Review Hasil I2V Test — Segment S001_seg01 (Chase Scene)

**Tanggal**: 2026-10-23
**Platform**: Dola AI (Seedance 2.5)
**Source video**: `upload/S001_seg01.mp4`
**Saved**: `produksi/i2v-output/prototype-30s/S001_seg01.mp4`

---

## 📊 Video Specs

| Spec | Expected | Actual | Status |
|---|---|---|---|
| Duration | 5s | **5.04s** | ✅ Perfect |
| Resolution | 480p (854×480) | **1248×704** (~16:9) | ⚠️ Lebih besar dari yang diminta (bagus!) |
| FPS | 24 | **24** | ✅ Perfect |
| Codec | H.264 / H.265 | **H.265/HEVC** | ✅ Modern codec |
| Bitrate | ~2-4 Mbps | **4.3 Mbps** | ✅ Quality bagus |
| File size | ~1-3 MB | **2.65 MB** | ✅ Reasonable |
| Audio | Native kalau support | **NONE** | ⚠️ Perlu Phase 7 TTS |

**Insight penting**: Dola kasih 1248×704 (hampir 720p) walaupun diminta 480p. Lebih bagus dari yang diharapkan! Plus 5.04s, lebih akurat dari yang diminta.

---

## 🎨 Hasil VLM Analysis (4 frame: t=0, t=2, t=5s)

### Frame Awal (t=0s)
| Kriteria | Hasil |
|---|---|
| Ken Arok di tengah frame | ✅ Ya, focal point |
| Karakter konsisten vs T2I ref (golden brown, topknot, leather armor) | ✅ Sesuai |
| 3 prajurit di background | ✅ Jelas terlihat |
| Hutan + god rays | ✅ Ada |
| Motion blur (chase feel) | ✅ Ada di debu + ujung anggota tubuh |

### Frame Tengah (t=2s)
| Kriteria | Hasil |
|---|---|
| Ken Arok masih di tengah | ✅ Ya |
| Background hutan + 3 prajurit | ✅ Masih ada |
| Komposisi berubah (camera backward)? | ⚠️ **Tidak signifikan** — frontal view stabil |
| Motion blur masih ada | ⚠️ **Tidak** — frame ini tampak tajam/statis |

### Frame Akhir (t=5s)
| Kriteria | Hasil |
|---|---|
| Ken Arok masih di tengah | ✅ Ya |
| Komposisi berubah drastis (camera sudah backward)? | ⚠️ **Tidak signifikan** — framing stabil medium shot |
| Motion blur ada? | ✅ Ya di kaki + debu + ujung tombak |
| 3 prajurit masih kelihatan | ✅ Ya, semua terlihat |

---

## 🎯 Overall Verdict: **PASS — Good for Prototype**

### Yang Berhasil (STRENGTHS):
1. ✅ **Durasi 5.04s** — sesuai spec (target 5s, hanya +0.04s)
2. ✅ **Karakter konsisten** — Ken Arok dengan topknot, leather armor, golden brown skin
3. ✅ **3 prajurit terlihat** — semua frame menampilkan 3 prajurit dengan tombak
4. ✅ **Hutan + god rays** — mood cinematic terjaga
5. ✅ **Motion blur natural** — di kaki, debu, ujung tombak (chase feel ada)
6. ✅ **Resolution lebih bagus dari permintaan** — dapat 1248×704 padahal diminta 480p
7. ✅ **File size wajar** — 2.65 MB untuk 5s 720p HEVC

### Yang Kurang (WEAKNESSES):
1. ⚠️ **Camera tidak benar-benar backward tracking** — komposisi frame stabil, tidak ada perspective shift yang menunjukkan camera mundur
2. ⚠️ **Frame tengah tidak ada motion blur** — mungkin ini frame "pas" yang kebetulan tajam
3. ⚠️ **Tidak ada audio native** — perlu Phase 7 TTS terpisah

### Insight: Motion prompt tidak sepenuhnya dipatuhi
- Diminta: "camera tracks rapidly backward, foliage whips past frame edges"
- Aktual: Karakter + prajurit tetap di posisi yang sama sepanjang 5 detik, hanya motion blur di kaki + debu yang jalan
- **Bukan masalah besar** — motion feel masih ada, tapi bukan "backward tracking" yang dimaksud

---

## 💡 Rekomendasi untuk Segmen Lainnya

### Opsi A — Lanjut 5 segmen sisanya dengan Dola (3 credits/hari)
- Hari ini: seg01 ✅ + **2 credits tersisa**
- Besok: 3 credits untuk segmen lain

**Saran urutan prioritas** (berdasarkan motion complexity):
1. ✅ seg01 (chase, fast) — DONE
2. **seg04 (prophecy, slow arc, 2 karakter)** ⭐ paling kompleks, prioritas tinggi
3. **seg05 (epiphany, snap zoom fast)** — motion unik
4. seg02 (taunt, medium pan up)
5. seg03 (sage appears, slow tilt up)
6. seg06 (title card, slow pull back) — paling simple

### Opsi B — Iterate prompt untuk improve motion
Kalau mau motion yang lebih akurat (beneran backward tracking):
- Tambah keyword eksplisit: "camera dolly backward, foliage moves toward viewer, depth of field changes"
- Atau pakai camera motion tool kalau Dola support (image-to-video with motion brush)

### Opsi C — Pakai platform lain untuk motion lebih akurat
- Higgsfield punya "Motion Control" models (Kling 2.6 Motion Control 720p) — 5cr per 5s
- Google Flow Veo mungkin lebih control
- Tapi untuk prototype 30s, motion Dola sudah cukup

---

## 🚀 Next Step Recommendation

### Skenario 1 — Iterasi seg01 dulu untuk improve motion (KALAU MAU)
- Edit motion prompt di `storyboard.json`: tambah keyword eksplisit "dolly backward, perspective shift, foreground elements pass camera"
- Re-generate seg01 (1 credit Dola)
- Compare dengan versi sekarang

### Skenario 2 — Lanjut segmen lain (RECOMMENDED) ⭐
- Lanjut generate seg04 (prophecy) — paling kompleks, paling penting untuk test 2-karakter motion
- Pakai 1 dari 2 credits tersisa hari ini
- Quality seg01 sudah pass — enough untuk prototype

### Skenario 3 — Scale up pakai platform lain
- Untuk 5 segmen sisanya, pakai Higgsfield (paling hemat: Kling 3.0 720p = 7cr × 5 = 35cr)
- Atau pakai Google Flow (50cr/hari free)
- Skill Dola I2V tidak perlu dibuat — cukup manual untuk prototype

---

## 📁 File Saved

```
produksi/i2v-output/prototype-30s/
└── S001_seg01.mp4  (2.65 MB, 5.04s, 1248×704, 24fps, HEVC)
```

Plus 6 extracted frames di `download/dola-i2v-frames/` untuk VLM analysis reference.

---

## 🏆 Milestone Update

| Phase | Status |
|---|---|
| Phase 1-4 (Riset + Master Era + T2I Prompt + Pra-produksi JSON) | ✅ |
| Phase 5 (T2I Production) | ✅ 12 image generated Dola |
| **Phase 6 (I2V Production)** | 🔄 **TEST 1 SEGMENT SUCCESS** — seg01 pass QC |
| Phase 7 (TTS) | ⏳ Next — edge-tts untuk 6 segmen |
| Phase 8 (Stitch) | ⏳ Next — ffmpeg 6 clips + TTS |

**Status**: Pipeline Phase 6 I2V terbukti jalan. Tinggal scaling untuk 5 segmen sisanya.
