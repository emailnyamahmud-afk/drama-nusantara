# Insight — Pivot T2I ke Google Flow (Nano Banana 2 Lite)

**Tanggal**: 2026-10-23
**Status**: User test pakai Google Flow berhasil. Dola skill lambat.

---

## 🔄 Pivot T2I: Dola → Google Flow

**User test**:
- ❌ Dola skill `batch-storyboard-generator` — lambat
- ✅ Google Flow (copy-paste JSON) — langsung jadi

**Model yang dipakai di Flow**:
- **Nano Banana 2 Lite** (default, free unlimited) ⭐
- Nano Banana 2.1, Nano Banana Pro (alternatif)
- Seedream-4.5 tidak available di Flow

**Status generate EP1**:
- ✅ 4/12 image sudah jadi:
  - Prajurit Demak
  - Raden Yunus
  - Raden Patah
  - Sunan Giri Dalem
- ⏳ 8 image pending (Suryawiyata, Sunan Kudus, Hang Tuah, Prajurit Portugis + 4 artefak)

---

## 🎨 Hasil VLM Analysis (4 image pertama)

**Overall**: 85% siap pakai untuk production reference

| Karakter | Status | Notes VLM |
|---|---|---|
| Prajurit Demak | ✅ Akurat | iket kepala, baju tanpa lengan, sarung batik, armor ringan di dada |
| Raden Yunus | ✅ Sangat baik | iket hijau, kemeja batik/tenun, sampur, celana surjan |
| Raden Patah | ⚠️ Cukup akurat | jubah kuning emas, ikat kepala putih, tongkat. Minor: potongan jubah terlalu lurus/modern |
| Sunan Giri Dalem | ✅ Baik | baju hijau dengan bordir emas, peci/ikat khas santri, janggut putih |

**Konsistensi 5-angle grid**: ✅ Semua 4 karakter menampilkan 5-angle grid yang benar.

**Artifact AI**: Minor pada area tangan (jari sedikit meleleh — typical AI generation).

**Rekomendasi**:
- 85% siap pakai untuk pre-production
- Bisa langsung dipakai sebagai master ref untuk storyboard frame (Phase berikutnya)
- Kalau perlu improve → iterate prompt dengan detail tambahan

---

## 💡 Insight untuk Workflow

### JSON tetap kompatibel antar platform
- Schema `dola-batch-EP1-master-ref.json` (35.8 KB) tetap sama untuk Dola + Flow
- Field yang penting: `prompt`, `aspect_ratio`, `output_path` — semua di-parse sama
- Cuma beda di eksekusi: Dola pakai skill auto-trigger, Flow manual copy-paste JSON

### Model preferensi untuk produksi:
| Platform | Model Default | Quality | Speed |
|---|---|---|---|
| Google Flow | Nano Banana 2 Lite | 85% production-ready | Cepat |
| Google Flow | Nano Banana Pro | Lebih bagus | Sedang |
| Dola | Seedream 4.5 | 90% production-ready | Lambat (kalau batch besar) |

**Untuk EP1 Jaka Tingkir**: pakai Google Flow + Nano Banana 2 Lite. Cukup bagus, cepat, free.

---

## 📁 Update Asset Status EP1

### Master Ref Generated (4/12)
| Asset | Status | File Output |
|---|---|---|
| Raden Patah | ✅ Generated | EP1-C001-3B-K007-raden-patah.jpg |
| Raden Yunus | ✅ Generated | EP1-C002-3B-K008-raden-yunus.jpg |
| Sunan Giri Dalem | ✅ Generated | EP1-C005-3B-K011-sunan-giri-dalem.jpg |
| Prajurit Demak | ✅ Generated | EP1-C007-3B-K013-prajurit-demak.jpg |

### Master Ref Pending (8/12)
| Asset | Status |
|---|---|
| Raden Suryawiyata | ⏳ Pending |
| Sunan Kudus | ⏳ Pending |
| Hang Tuah | ⏳ Pending |
| Prajurit Portugis | ⏳ Pending |
| Keris Kyai Naga Sasra | ⏳ Pending |
| Singgasana Demak | ⏳ Pending |
| Mahkota Sultan Demak | ⏳ Pending |
| Bendera Surya Majapahit | ⏳ Pending |

### Reuse Existing (5 file, tidak perlu generate)
- Pangeran Trenggana (3B-K001)
- Sunan Kalijaga (3A-K003)
- Lokasi Demak (3B-L001)
- Lokasi Malaka (3A-L002)
- Pendapa Demak scene (3B-S001)

---

## 🚀 Next Step

1. **User lanjut generate 8 image sisanya** di Google Flow (copy-paste JSON atau per-prompt)
2. **User lanjut edit naskah** kalau masih ada dialog yang mau diperhalus
3. **Setelah keduanya selesai**, AI bikin:
   - 17 storyboard frame prompts (pakai visual spec dari naskah final + ref dari 12 master ref)
   - dola-batch-EP1-storyboard-frame.json (untuk upload ke Flow lagi, phase 2)
4. **User upload ke Flow** → generate 17 storyboard frame
5. **AI compile JSON final v3.1** EP1
6. **User review JSON final** → approve
7. **Produksi**: AI TTS + ffmpeg stitch → MP4 EP1 final

Estimasi sisa waktu: ~3 jam setelah naskah + 12 image ready.
