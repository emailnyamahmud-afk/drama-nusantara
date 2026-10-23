# Optimasi Workflow Dola — Pindah ke Dola Drive & Alternatif Lain

**Tanggal**: 2026-10-23
**Status**: Skill `batch-storyboard-generator` sudah jalan, Phase 1 + 2 selesai, sedang QC file
**Pertanyaan user**: Maksud "download" ke mana? Optimasi apa yang bisa dilakukan?

---

## 1. Klarifikasi: "Download" yang Dola Maksud

**Bukan ke MacBook Anda**, tapi ke **VM sandbox Dola** (cloud).

### Alur saat ini:

```
Dola generate image (di cloud Dola)
  ↓
Image disimpan ke VM working directory Dola (sementara, sesi-scope)
  ↓
Dola run QC + contact sheet (di VM)
  ↓
NotifyHuman: kirim 12 image + contact-sheet sebagai ATTACHMENT CHAT
  ↓
User click download di chat Dola → file masuk MacBook lokal
```

### Konsekuensi:
- VM Dola = **persistent selama sesi aktif** saja. Kalau sesi ditutup, file hilang.
- Image di VM **tidak langsung tersimpan** di Dola Drive 10GB atau MacBook.
- User harus **download manual** via attachment chat kalau mau simpan permanen.

---

## 2. Opsi Optimasi (5 alternatif)

### Opsi A — Output Langsung ke Dola Drive 10GB ⭐ RECOMMENDED

**Modifikasi skill**: ganti `output_root` dari `./batch-output/` (VM) jadi `/drive/drama-nusantara/prototype-30s/` (Dola Drive).

**Keuntungan**:
- ✅ Persistent storage (10GB cukup untuk ratusan image)
- ✅ Bisa akses dari device lain (web Dola di mana saja)
- ✅ Tidak hilang saat sesi Dola ditutup
- ✅ Bisa organize folder per produksi

**Cara implementasi**:
- Edit SKILL.md bagian "Ingest and validate" step 3:
  ```
  Original: Create an output root dir (e.g. ./batch-output/)
  Modified: Use Dola Drive path /drive/drama-nusantara/<project-id>/
  ```
- Atau tambahkan parameter di `dola-batch.json`:
  ```json
  "output_root": "/drive/drama-nusantara/prototype-30s/"
  ```
- Skill akan create folder di Dola Drive kalau belum ada, lalu save image ke sana.

**Estimasi effort modifikasi skill**: 30-60 menit

### Opsi B — Install Dola Desktop App di MacBook

**Apa yang desktop app kasih**:
- ✅ Local sync folder (otomatis sync Dola Drive ↔ folder MacBook)
- ✅ Notifikasi desktop saat skill selesai
- ✅ Lebih stabil dari browser Brave (no tab close accident)
- ✅ Background process — bisa tutup browser tanpa hentikan skill

**Cara**:
- Download "Dola for Mac" dari button kanan-atas di web Dola
- Install → login dengan akun yang sama
- Aktifkan sync folder

**Kontra**:
- Desktop app mungkin masih beta
- Perlu setup sync folder manual

### Opsi C — Manual Download via NotifyHuman Attachment (DEFAULT saat ini)

**Yang terjadi sekarang** (tanpa modifikasi):
- Skill deliver via NotifyHuman dengan attachment
- User click download tiap image satu per satu
- Atau download all as zip (kalau Dola support)

**Keuntungan**:
- ✅ Tidak perlu modifikasi skill
- ✅ Bisa pilih image mana yang mau disimpan (hemat space)

**Kontra**:
- ❌ Manual, lambat untuk 12 image
- ❌ Harus download ulang kalau hilang
- ❌ Tidak persistent kalau chat Dola di-clear

### Opsi D — Webhook Auto-Push ke GitHub (Advanced)

**Modifikasi skill**: tambah step di akhir workflow:
1. Setelah image jadi, upload ke GitHub via API
2. Save ke `produksi/t2i-output/master-reff/2C/` dan `prototype-30s/` di repo

**Keuntungan**:
- ✅ Auto-versioned di Git (bisa rollback)
- ✅ Backup permanen
- ❌ **TAPI**: t2i-output di-gitignore (aset lokal saja by design)
- ❌ GitHub limit 50MB per file (cukup untuk JPG, tapi tidak untuk video nanti)

**Implementasi**:
- Butuh GitHub token (PAT) di Dola env
- Tambah script `push_to_github.py` di skill
- Edit SKILL.md: tambah step 7 "Deliver to GitHub"

**Kontra**:
- ❌ Kompleks, butuh setup credential
- ❌ Bypass aturan "aset lokal saja" di repo kita
- ❌ GitHub bukan tempat aset media besar

### Opsi E — Hybrid: Dola Drive + Auto-Download Script

**Workflow**:
1. Skill output ke Dola Drive (Opsi A)
2. User install `rclone` atau script Python di MacBook
3. Script auto-pull dari Dola Drive ke folder lokal `produksi/t2i-output/`

**Keuntungan**:
- ✅ Persistent di Dola Drive
- ✅ Auto-sync ke MacBook
- ✅ Tidak manual download

**Kontra**:
- Butuh setup script di MacBook
- Butuh Dola Drive API access atau rclone config

---

## 3. Rekomendasi: Opsi A (Dola Drive)

**Kenapa**:
1. Dola Drive 10GB sudah ada, gratis, tinggal pakai
2. Modifikasi skill minimal (1 baris di SKILL.md atau 1 field di JSON)
3. Persistent — bisa akses dari mana saja
4. Bisa organize per produksi: `/drive/drama-nusantara/prototype-30s/`, `/drive/drama-nusantara/pilot-panji-3min/`, dll

**Estimasi effort**: 30-60 menit modifikasi skill di Dola AI

---

## 4. Pertanyaan untuk User

Sebelum modifikasi skill, perlu konfirmasi:

1. **Apakah Dola AI skill bisa write ke Dola Drive?** (perlu cek dokumentasi Dola)
2. **Apakah path `/drive/...` accessible dari VM skill?**
3. **Skill bisa create folder baru di Dola Drive?**

Kalau 3 jawabannya **YA**, lanjut Opsi A. Kalau **TIDAK**, fallback ke:
- Opsi C (manual download, gak efisien tapi work)
- Atau Opsi D (GitHub, tapi butuh PAT)

---

## 5. Workflow Ideal ke Depan

```
[Z.ai chat] generate dola-batch.json
  ↓
[User] upload JSON ke Dola AI + trigger skill
  ↓
[Dola skill] generate 12 image → save ke Dola Drive
  ↓
[Dola Drive] /drama-nusantara/prototype-30s/
  ├── master-reff/2C/*.jpg (6 file)
  └── storyboard-frame/*.jpg (6 file) + contact-sheet.png
  ↓
[User] browse Dola Drive di Brave → download zip folder
  ↓ atau
[Optional] install Dola desktop app → auto-sync ke MacBook
  ↓
[MacBook lokal] produksi/t2i-output/prototype-30s/ (synced)
  ↓
[User] share 3 sample ke Z.ai untuk review
  ↓
[Z.ai] iterate prompt → re-generate kalau perlu
```

**Target akhir**: 1 upload JSON → output otomatis di Dola Drive → sync ke MacBook → review.

---

## 6. Yang Bisa Dilakukan Sekarang

**Sambil nunggu Dola skill selesai QC**:

1. **Cek dokumentasi Dola** (Help / Settings) — apakah ada info tentang:
   - Path Dola Drive dari VM skill
   - Cara skill write ke Dola Drive
   - API endpoint untuk Dola Drive

2. **Install Dola desktop app** (button kanan-atas di web Dola) — coba dulu, kalau bagus pertahankan, kalau tidak uninstall.

3. **Tunggu hasil skill saat ini** dulu — setelah 12 image + contact sheet jadi, share ke saya. Baru kita modifikasi skill untuk Dola Drive.

---

## 7. Catatan Penting

**Jangan modifikasi skill sekarang** — biarkan yang berjalan selesai dulu supaya kita punya baseline hasil. Kalau hasilnya bagus, baru modifikasi untuk optimasi storage. Kalau hasilnya jelek, fokus iterate prompt dulu, bukan optimasi storage.
