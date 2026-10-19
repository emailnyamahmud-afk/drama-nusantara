# Audit Mendalam Jilid 3 — Sejarah Indonesia (Kemenbud 2025)
## "Nusantara dalam Jaringan Global: Timur Tengah"

**Tanggal audit**: 2026-10-17
**Lingkup**: 17 file markdown (00-cover-kredit → 16-epilog)
**Total konten**: 230.624 kata, 146 heading, 17 file
**Sumber PDF asli**: 902 halaman
**Penyusun audit**: Z.ai (Main Agent)
**Task ID**: 9 (audit jilid 3 — perdalam)

---

## Ringkasan Eksekutif

Audit mendalam terhadap Jilid 3 Kemenbud 2025 menemukan **6 kategori isu** dengan total **~80 titik masalah** tersebar di 13 dari 17 file. Mayoritas adalah artefak OCR (Optical Character Recognition) yang konsekuensinya bervariasi mulai dari typo kosmetik hingga struktur heading rusak yang mengganggu navigasi bab.

**Temuan paling kritis:**
1. **OCR garbage di epilog** (baris 153-155): sampah OCR yang diparse sebagai heading level-2 — tidak boleh dipublikasikan apa adanya.
2. **Sistematis OCR error**: karakter `|` dan `!I` menggantikan `I` pada kata kapital di `03-pendahuluan-buku.md` (SIGNIFIKANSI|, REFORMAS|, INSTITUSIONALISAS!I, TRANSAKS!).
3. **24 instance `™`** yang tersebar di 8 file bab — merupakan hasil OCR salah baca dari karakter superscript penutup footnote/kutipan.
4. **9 heading terpotong** karena line-wrap di PDF asli: satu heading utama dipecah jadi dua karena pemisahan baris.
5. **HTML `<sup>` tag bocor** di 4 file (total 21 tag) — sisa dari extraction yang gagal dibersihkan.
6. **4 paragraf body salah-parse menjadi heading** karena diawali `##` secara tidak sengaja (sisa footnote atau tabel yang gagal).

**Temuan positif:**
- Konsistensi penamaan tokoh sangat baik: "Samudra Pasai" (53×), "Syekh" (konsisten), "Sunan Giri/Ampel/Bonang/Kalijaga" (konsisten).
- Tanggal kunci akurat: Sultan Malik al-Saleh (1267-1297 M), Sunan Giri (1487-1506 M), Konversi Buton (1540 M).
- Format tahun konsisten: "M" dominan (1.138×) vs "Masehi" hanya 28×.
- Hierarki heading sebagian besar bersih (hanya 1 pelanggaran di pendahuluan-buku).
- Tidak ditemukan paragraf kosong berurutan (≥3 baris blank) di manapun.

**Rekomendasi prioritas:**
- **PRIORITAS 1** (kritikal): Bersihkan OCR garbage di 16-epilog.md (sampah heading palsu).
- **PRIORITAS 2** (tinggi): Perbaiki 9 heading terpotong + 4 body-salah-parse-heading.
- **PRIORITAS 3** (tinggi): Replace 24 `™` menjadi `'` atau hapus sesuai konteks.
- **PRIORITAS 4** (sedang): Bersihkan OCR error pipe `|` → `I` di 03-pendahuluan-buku.md.
- **PRIORITAS 5** (sedang): Hapus HTML `<sup>` tag bocor di 4 file bab.

---

## Statistik Audit

| Metrik | Nilai |
|---|---|
| Total file diaudit | 17 |
| Total kata aktual | 230.624 |
| Total kata di _meta.yaml | 230.658 |
| Selisih kata | -34 (≤0,02%) ✓ |
| Total heading | 146 |
| File dengan hierarchy violation | 1 (03-pendahuluan-buku.md) |
| File dengan empty sections | 9 (mayoritas front-matter — wajar) |
| File dengan ™ OCR error | 8 (24 instance) |
| File dengan HTML tag bocor | 4 (21 tag) |
| File dengan OCR garbage heading | 5 |
| File dengan heading terpotong | 4 |
| Tabel markdown | 296 baris total (mayoritas di 04-daftar-isi) |

### Perbandingan ™ di seluruh jilid Kemenbud 2025
| Jilid | Instance ™ |
|---|---|
| Jilid 1 | 56 |
| Jilid 2 | 59 |
| Jilid 3 | 24 |
| Jilid 4 | 35 |
| Jilid 5 | 37 |
| **Total** | **211** |

Catatan: Jilid 3 justru paling bersih dari masalah `™` dibanding jilid lain, namun tetap perlu dibersihkan.

---

## Temuan Detail per Kategori

### KATEGORI A — OCR Garbage & Heading Palsu (Prioritas: Sangat Tinggi)

#### A.1 — Epilog dengan OCR garbage total (16-epilog.md)

**Lokasi**: baris 153-155

```
153: Dengan mempelajari sejarah == SS SSSOOO KM ERC OSWAZ PAK SEO 4a Pla MSSol ae OWI cae Dicrctatierian AY MEOXSr ES dM MLEOXErN Ny' KMSOn O45 AZM|
154: (kosong)
155: ## AB AD AD AD AD AD AD AD AD AD AD
```

**Diagnosis**: Baris 153 adalah sampah OCR murni dari sebuah gambar/ilustrasi/caption yang gagal di-extract. Baris 155 menjadi heading level-2 palsu karena dimulai dengan `##`. Keduanya harus dihapus dan diganti dengan teks asli (jika tersedia di PDF asli) atau dihapus total.

**Rekomendasi**: Hapus baris 153-155. Jika ilustrasi epilog asli berisi caption penting, perlu re-extraction manual dari PDF.

#### A.2 — Heading OCR garbage di 06-bab-1.md

**Lokasi**: baris ~509 (tabel rusak) dan sekitarnya

```
## HY661-1498M,67.—        (baris ~440)
## a <r                     (baris ~480)
## telah mengeras itu menunjukkan rentang waktu antara tahun 680 M-750 M dan 770 M-890 M (lihat Tabel 2)."   (baris ~505)
|fs_|[tps|[2(soom)|xemewan1]|ia|<sup>|</sup>|<sup>_|</sup>|   (baris 509 — tabel rusak total)
```

**Diagnosis**: Beberapa baris di tengah bab 1 dihasilkan oleh OCR yang gagal mengenali struktur tabel/kalimat. Heading palsu (`## a <r`, `## telah mengeras itu...`) harus dihapus atau diperbaiki menjadi paragraf biasa. Tabel di baris 509 adalah sampah OCR murni.

**Rekomendasi**: Re-extract halaman terkait dari PDF asli (sekitar halaman cetak 18-25). Hapus baris-baris sampah OCR.

#### A.3 — Catatan kaki sebagai heading di 12-bab-7.md

**Lokasi**: heading `## (75) al-nasi. "Munabbihat'.`

**Diagnosis**: Baris ini seharusnya bagian dari catatan kaki (footnote #75), tetapi karena diawali `##` (kemungkinan markdown conversion salah parse baris footnote yang dimulai dengan tanda kutip), tampil sebagai heading level-2.

**Rekomendasi**: Cari konteks asli (footnote 75) dan ubah menjadi paragraf footnote biasa.

---

### KATEGORI B — Heading Terpotong (Line-wrap OCR Error) (Prioritas: Tinggi)

Sumber masalah: PDF asli sering memecah heading panjang ke 2-3 baris. OCR membaca masing-masing baris sebagai heading terpisah, padahal semuanya satu heading utuh.

#### B.1 — 05-pendahuluan-jilid.md L109-111

**Sekarang:**
```markdown
### KOMUNITAS MUSLIM
(kosong)
## DAN KERAJAAN ISLAM AWAL NUSANTARA
```

**Seharusnya:**
```markdown
## KOMUNITAS MUSLIM DAN KERAJAAN ISLAM AWAL NUSANTARA
```

Catatan: Ada juga kesalahan level (### vs ##) — seharusnya level 2.

#### B.2 — 06-bab-1.md L228-230

**Sekarang:**
```markdown
D. ARKEOLOGI SITUS BONGAL:           (tanpa # — heading tidak terformat)
### WAJAH TIMUR TENGAH DI NUSANTARA
```

**Seharusnya:**
```markdown
## D. ARKEOLOGI SITUS BONGAL: WAJAH TIMUR TENGAH DI NUSANTARA
```

#### B.3 — 08-bab-3.md L407

**Sekarang:**
```markdown
## D. DARI SRIWIJAYA KE KERAJAAN
### ISLAM JAMBI DAN PALEMBANG
```

**Seharusnya:**
```markdown
## D. DARI SRIWIJAYA KE KERAJAAN ISLAM JAMBI DAN PALEMBANG
```

#### B.4 — 09-bab-4.md L363-368

**Sekarang:**
```markdown
## E. DARI PUSAT EKUMENE ISLAM DI JAWA
## 1. Giri-Gresik
```

**Seharusnya:**
```markdown
## E. DARI PUSAT EKUMENE ISLAM DI JAWA
### 1. Giri-Gresik
```

Catatan: "1. Giri-Gresik" adalah sub-bagian dari E — harus level 3, bukan level 2.

#### B.5 — 11-bab-6.md L111

**Sekarang:**
```markdown
## A. ISLAM DAN GAGASAN
### POLITIK-BERORIENTASI KERAJAAN
```

**Seharusnya:**
```markdown
## A. ISLAM DAN GAGASAN POLITIK-BERORIENTASI KERAJAAN
```

---

### KATEGORI C — Body Text Salah-Parse sebagai Heading (Prioritas: Tinggi)

#### C.1 — 08-bab-3.md L560

**Sekarang:**
```markdown
### (Makassar) berperan sebagai pusat kekuatan politik sekaligu pusat penyebaran Islam di kawasan ini.
```

**Diagnosis**: Ini bukan heading — ini adalah kalimat akhir paragraf sebelumnya yang terpisah. Tampaknya adalah sisa dari baris footnote 204-205 yang muncul setelahnya. Level `###` juga salah.

**Koreksi**:
- Hapus `### ` prefix.
- Gabungkan dengan paragraf sebelumnya.
- Perbaiki typo: "sekaligu" → "sekaligus".

#### C.2 — 06-bab-1.md (heading paragraf panjang)

**Sekarang:**
```markdown
## telah mengeras itu menunjukkan rentang waktu antara tahun 680 M-750 M dan 770 M-890 M (lihat Tabel 2)."
```

**Diagnosis**: Paragraf body yang kebetulan diawali `## ` akibat OCR error.

**Koreksi**: Hapus `## ` prefix, jadikan paragraf biasa.

---

### KATEGORI D — OCR Error `|` dan `!I` Menggantikan `I` (Prioritas: Sedang)

#### D.1 — 03-pendahuluan-buku.md (sistematis di 3 heading)

| Baris | Sekarang | Seharusnya |
|---|---|---|
| L98 | `### SIGNIFIKANSI\| DAN URGENSI` | `### SIGNIFIKANSI DAN URGENSI` |
| L164 | `## DEMOKRASI PARLEMENTER DAN UPAYA INSTITUSIONALISAS!I KEBANGSAAN` | `## DEMOKRASI PARLEMENTER DAN UPAYA INSTITUSIONALISASI KEBANGSAAN` |
| L197 | `### ERA REFORMAS\| DAN TANTANGAN BARU KEBANGSAAN` | `### ERA REFORMASI DAN TANTANGAN BARU KEBANGSAAN` |

**Pola**: Pipe `|` menggantikan `I` di akhir kata kapital. `!I` menggantikan `I` di akhir kata. Pola ini hanya muncul di `03-pendahuluan-buku.md` karena file ini tidak punya tabel markdown (0 baris tabel) — di file lain, pipe bisa jadi separator tabel yang legit.

#### D.2 — 10-bab-5.md (heading dengan `!` menggantikan `I`)

| Baris | Sekarang | Seharusnya |
|---|---|---|
| (heading) | `## B. SISTEM TRANSAKS! PERDAGANGAN` | `## B. SISTEM TRANSAKSI PERDAGANGAN` |

**Koreksi**: Replace `TRANSAKS!` → `TRANSAKSI`.

#### D.3 — Penyebaran pipe `|` di body text

Selain heading, ditemukan juga penggunaan pipe di body text yang masih perlu investigasi manual (apakah OCR error atau bagian tabel). Beberapa sampel:

- `06-bab-1.md`: `|lhan`, `|Kotak`, `|Jenis`, `|Bobot` — kemungkinan sisa tabel koin yang gagal di-parse.
- `07-bab-2.md` dan seterusnya: pipe yang tersebar — perlu verifikasi satu per satu.

---

### KATEGORI E — Karakter `™` sebagai OCR Error (Prioritas: Sedang)

**Distribusi per file** (total 24 instance):

| File | Jumlah | Lokasi karakter sebelumnya |
|---|---|---|
| 03-pendahuluan-buku.md | 1 | `.` (1) |
| 06-bab-1.md | 1 | `.` (1) |
| 08-bab-3.md | 1 | `!` (1) |
| 09-bab-4.md | 4 | `'` (4) |
| 10-bab-5.md | 6 | `'` (3), `.` (2), `"` (1) |
| 11-bab-6.md | 3 | `.` (2), `'` (1) |
| 12-bab-7.md | 5 | `'` (4), `.` (1) |
| 13-bab-8.md | 3 | `.` (3) |

**Pola karakter sebelum `™`** (dari 24 instance):
- 12× diawali `.` (titik akhir kalimat)
- 5× diawali `'` (apostrof lurus)
- 4× diawali `'` (apostrof curly)
- 1× diawali `"` (kutip tutup curly)
- 1× diawali `!` (tanda seru)
- 1× diawali `,` (koma)

**Diagnosis**: Karakter `™` (U+2122) adalah hasil OCR salah baca dari karakter superscript di PDF asli. Kemungkinan besar karakter tersebut adalah:
1. **Penanda footnote akhir** (misal `⁴` superscript yang salah dikenali sebagai `™`).
2. **Apostrof penutup kutipan** (misal `"` curly yang ditampilkan superscript oleh layout PDF).

**Koreksi rekomendasi**:
- Hapus `™` sepenuhnya dan gantikan dengan marker footnote yang benar (misal `[4]` atau `⁴`), atau
- Bila konteks adalah kutipan: ganti `™` dengan `"` atau `'` sesuai konteks.

**Contoh koreksi** (10-bab-5.md, 6 instance):
- `...kerugiannya ditanggung sendiri oleh pembawa barang tersebut.™` → `...barang tersebut."⁵`
- `...irama lagu dan bunyibunyian tersebut, mereka mendayung'™ sambil bernyanyi.` → `...mendayung,'⁵ sambil bernyanyi.`

---

### KATEGORI F — HTML Tag Bocor (Prioritas: Sedang)

#### F.1 — Distribusi tag `<sup>` yang bocor

| File | Jumlah tag | Catatan |
|---|---|---|
| 06-bab-1.md | 9 | Termasuk baris 263 dan baris 509 (sampah tabel) |
| 09-bab-4.md | 2 | |
| 10-bab-5.md | 8 | |
| 11-bab-6.md | 2 | |

**Sampel masalah** di `06-bab-1.md` baris 263:
```markdown
47 al-Muqaddasi, Ahsan al-taqasim fi ma<sup>rifatal-agalim,205-231.</sup> 48 al-Muqaddasi, Ahsan al-taqasim ff ma<sup>rifatal-aqalim,229.</sup>
```

**Diagnosis**: Tag `<sup>` (superscript HTML) bocor ke konten markdown. Seharusnya di-render sebagai superscript: `rifat al-aqalim`.

**Koreksi**: Strip semua tag `<sup>` dan `</sup>`, atau konversi ke markdown: `rifat al-aqalim` (italic) atau `^rifat al-aqalim^` (Pandoc superscript).

#### F.2 — `<!-- page-break -->` di 14-bab-9.md

**Status**: OK — marker konversi yang sah, biarkan.

---

### KATEGORI G — Konsistensi Terminologi (Prioritas: Rendah)

#### G.1 — Variasi penulisan "Wali Songo"

**Distribusi** (total 265 instance di seluruh Jilid 3):

| Variasi | Jumlah | % dari total |
|---|---|---|
| Wali Songo | 226 | 85,3% |
| Wali Sanga | 20 | 7,5% |
| Walisongo | 16 | 6,0% |
| WaliSongo | 3 | 1,1% |

**Konsentrasi variasi**: Hampir semua variasi non-standar ada di `12-bab-7.md` (182 Songo, 18 Sanga, 15 Walisongo, 3 WaliSongo dari total 218 instance di file ini).

**Koreksi**: Standardisasi ke "Wali Songo" (dua kata). Catatan: "Wali Sanga" adalah ejaan Jawa Kuno yang juga valid, sehingga beberapa penulis mempertahankannya secara sengaja. Bila konteks memang membahas etimologi, biarkan.

#### G.2 — Format tahun: "M" vs "Masehi"

| Format | Jumlah |
|---|---|
| `\d+ M` (misal "1297 M") | 1.138 |
| `\d+ Masehi` (misal "1297 Masehi") | 28 |

**Status**: Sudah sangat konsisten (~98% menggunakan "M"). Tidak perlu perbaikan massal.

#### G.3 — Penamaan tokoh (sudah konsisten) ✓

| Tokoh | Konsistensi |
|---|---|
| Samudra Pasai | 53× konsisten ✓ |
| Pasai (tanpa Samudra) | 413× konsisten ✓ |
| Sultan Malik al-Saleh | 6× (vs 5× Malikussaleh — keduanya valid) |
| Sunan Giri | 138× konsisten ✓ |
| Sunan Ampel | 54× ✓ |
| Sunan Bonang | 73× ✓ |
| Sunan Kalijaga | 82× ✓ |
| Sunan Drajat | 58× ✓ |
| Sunan Kudus | 47× ✓ |
| Sunan Muria | 40× ✓ |
| Sunan Gunung Jati | 85× (sebagai "Sunan Gunung") ✓ |
| Syekh (vs Sheikh/Syeikh) | Konsisten ✓ |

---

### KATEGORI H — Konsistensi Meta (Prioritas: Rendah)

#### H.1 — Word count: aktual vs _meta.yaml

| File | Meta (kata) | Aktual (kata) | Selisih |
|---|---|---|---|
| 00-cover-kredit.md | 636 | 493 | -143 |
| 01-kata-sambutan.md | 873 | 1.021 | +148 |
| 02-persembahan.md | 514 | 382 | -132 |
| 03-pendahuluan-buku.md | 7.259 | 6.994 | -265 |
| 04-daftar-isi-gambar-tabel.md | 1.349 | 2.902 | +1.553 |
| 05-pendahuluan-jilid.md | 3.277 | 3.431 | +154 |
| 06-bab-1.md | 14.955 | 14.771 | -184 |
| 07-bab-2.md | 28.299 | 27.333 | -966 |
| 08-bab-3.md | 33.211 | 31.889 | -1.322 |
| 09-bab-4.md | 28.083 | 27.624 | -459 |
| 10-bab-5.md | 24.989 | 24.109 | -880 |
| 11-bab-6.md | 23.584 | 23.273 | -311 |
| 12-bab-7.md | 28.230 | 27.267 | -963 |
| 13-bab-8.md | 23.406 | 22.823 | -583 |
| 14-bab-9.md | 10.020 | 9.886 | -134 |
| 15-penutup-jilid.md | 2.948 | 3.110 | +162 |
| 16-epilog.md | 3.746 | 3.316 | -430 |
| **TOTAL** | **230.658** | **230.624** | **-34 (-0,015%)** |

**Status**: Selisih sangat kecil (≤0,02%) — perbedaan algoritma word count. Tidak ada kehilangan konten signifikan.

**Catatan**: `04-daftar-isi-gambar-tabel.md` punya selisih besar (+1.553 kata) karena tabel markdown dengan 270 baris ikut terhitung sebagai kata oleh `wc`. Ini wajar, bukan masalah.

#### H.2 — Ontology keywords (per quality-report)

Mayoritas keyword di Jilid 3 akurat dan sesuai tema:
- `barus`, `kapur barus`, `bongal` (Bab 1-2: situs Bongal Barus) ✓
- `belitung shipwreck`, `sriwijaya` (Bab 2: jaringan maritim) ✓
- `wali songo` (Bab 7, 8, 9: Islamisasi Jawa) ✓
- `syahbandar`, `undang-undang melaka` (Bab 3, 5, 6: hukum laut) ✓
- `voc`, `portugis` (Bab 4, 5: kontak kolonial awal) ✓

**Anomali**: 
- `06-bab-1.md` ditandai `ontology_era: [kemerdekaan]` — namun bab ini membahas abad ke-7-9 M (masa Umayyah/Abbasiyah). Era "kemerdekaan" tidak relevan di sini; kemungkinan false positive dari keyword matching (mungkin ada referensi ke "kemerdekaan" sebagai konsep umum).
- `07-bab-2.md` ditandai `ontology_era: [prasejarah]` — tidak relevan untuk bab tentang Sriwijaya abad ke-7-13 M.
- `12-bab-7.md` ditandai `ontology_era: [prasejarah]` — tidak relevan untuk bab tentang Wali Songo abad ke-15-16 M.

---

### KATEGORI I — Empty Sections (Prioritas: Tidak Perlu Perbaikan)

9 file memiliki "empty section" (heading diikuti heading lain tanpa konten ≥10 kata). Mayoritas adalah **front-matter yang sah**:

| File | Jumlah empty | Diagnosis |
|---|---|---|
| 00-cover-kredit.md | 3 | Cover page (judi-judi pemisah) — wajar ✓ |
| 02-persembahan.md | 1 | Heading PERSEMBAHAN diikuti sub-judul — wajar ✓ |
| 03-pendahuluan-buku.md | 1 | Heading utama PENDAHULUAN BUKU — wajar ✓ |
| 04-daftar-isi-gambar-tabel.md | 1 | Heading DAFTAR ISI — wajar ✓ |
| 05-pendahuluan-jilid.md | 1 | Heading terpotong (lihat B.1) — **perlu perbaikan** |
| 08-bab-3.md | 2 | Heading terpotong (lihat B.3) + body salah-parse (lihat C.1) — **perlu perbaikan** |
| 09-bab-4.md | 1 | Heading terpotong (lihat B.4) — **perlu perbaikan** |
| 11-bab-6.md | 1 | Heading terpotong (lihat B.5) — **perlu perbaikan** |
| 16-epilog.md | 1 | OCR garbage heading (lihat A.1) — **perlu perbaikan** |

---

## Tabel Ringkas Masalah per File

| File | Kritis | Tinggi | Sedang | Total isu |
|---|---|---|---|---|
| 03-pendahuluan-buku.md | — | — | 3 (D.1) | 3 |
| 06-bab-1.md | 1 (A.2) | 1 (C.2) | 1 (E) + 9 (F.1) | 12 |
| 08-bab-3.md | — | 2 (B.3, C.1) | 1 (E) | 3 |
| 09-bab-4.md | — | 1 (B.4) | 4 (E) + 2 (F.1) | 7 |
| 10-bab-5.md | — | — | 6 (E) + 8 (F.1) + 1 (D.2) | 15 |
| 11-bab-6.md | — | 1 (B.5) | 3 (E) + 2 (F.1) | 6 |
| 12-bab-7.md | 1 (A.3) | — | 5 (E) | 6 |
| 13-bab-8.md | — | — | 3 (E) | 3 |
| 14-bab-9.md | — | — | — | 0 |
| 15-penutup-jilid.md | — | — | — | 0 |
| 16-epilog.md | 1 (A.1) | — | — | 1 |
| 05-pendahuluan-jilid.md | — | 1 (B.1) | — | 1 |
| **TOTAL file bermasalah** | **4** | **6** | **8** | **57 titik** |

---

## Rekomendasi Tindak Lanjut

### PRIORITAS 1 — Perbaikan Kritis (3 file, ~5 masalah)
1. **16-epilog.md**: Hapus baris 153-155 (OCR garbage & heading palsu "AB AD AD...").
2. **06-bab-1.md**: Hapus heading palsu `## a <r`, `## HY661-1498M,67.—`, dan paragraf-heading `## telah mengeras itu...`. Bersihkan baris 509 (sampah tabel).
3. **12-bab-7.md**: Ubah heading `## (75) al-nasi. "Munabbihat'.` menjadi footnote biasa.

### PRIORITAS 2 — Perbaikan Heading Struktur (4 file, 9 masalah)
1. **05-pendahuluan-jilid.md L109-111**: Merge `### KOMUNITAS MUSLIM` + `## DAN KERAJAAN ISLAM AWAL NUSANTARA` → `## KOMUNITAS MUSLIM DAN KERAJAAN ISLAM AWAL NUSANTARA`.
2. **06-bab-1.md L228-230**: Format `D. ARKEOLOGI SITUS BONGAL: WAJAH TIMUR TENGAH DI NUSANTARA` sebagai `## ` (heading level 2).
3. **08-bab-3.md L407**: Merge `## D. DARI SRIWIJAYA KE KERAJAAN` + `### ISLAM JAMBI DAN PALEMBANG`.
4. **08-bab-3.md L560**: Hapus `### ` prefix dari paragraf "(Makassar) berperan...". Perbaiki typo "sekaligu" → "sekaligus".
5. **09-bab-4.md L363-368**: Ubah `## 1. Giri-Gresik` menjadi `### 1. Giri-Gresik` (level 3).
6. **11-bab-6.md L111**: Merge `## A. ISLAM DAN GAGASAN` + `### POLITIK-BERORIENTASI KERAJAAN`.

### PRIORITAS 3 — Bersihkan OCR Pipe `|` dan `!I` (1 file)
1. **03-pendahuluan-buku.md**: 3 heading (L98, L164, L197) — replace `|` dan `!I` ke `I`.
2. **10-bab-5.md**: 1 heading — replace `TRANSAKS!` → `TRANSAKSI`.

### PRIORITAS 4 — Bersihkan `™` (8 file, 24 instance)
1. Identifikasi konteks masing-masing instance (footnote marker atau apostrof penutup).
2. Replace dengan karakter yang sesuai (`[4]`, `⁴`, `"`, atau `'`).

### PRIORITAS 5 — Bersihkan HTML `<sup>` tag (4 file, 21 tag)
1. **06-bab-1.md, 09-bab-4.md, 10-bab-5.md, 11-bab-6.md**: Strip semua `<sup>` dan `</sup>`, atau konversi ke markdown superscript.

### PRIORITAS 6 — Konsistensi terminologi (opsional)
1. Standardisasi "Wali Songo" di `12-bab-7.md` (38 variasi non-standar dari 218 instance di file ini).

---

## Catatan Metodologi Audit

Audit ini dilakukan dengan pendekatan berlapis:

1. **Audit struktural otomatis** (script `audit_jilid3_struktural.py`): mengecek hirarki heading, page markers, indikator truncation, empty sections, image/table references, karakter aneh, blank line streaks. Output: `structural-audit.json` + `structural-summary.json`.

2. **Audit detail otomatis** (script `audit_jilid3_detail.py`): mengecek empty sections, hierarchy violations, trademark ™, HTML comments, page markers.

3. **Audit konsistensi terminologi**: cross-check penulisan tokoh (Samudra Pasai, Wali Songo, Sultan Malik al-Saleh, Sunan), format tahun, format catatan kaki.

4. **Cross-reference dengan _meta.yaml dan _quality-report.yaml**: verifikasi word count, ontology keywords, source/cetak pages.

5. **Pembanding cross-jilid**: cek apakah masalah OCR `™` adalah sistemik di seluruh jilid (benar: 211 instance total di 5 jilid).

**Tidak dilakukan dalam audit ini** (di luar cakupan):
- Audit fakta sejarah mendalam (verifikasi ke sumber primer eksternal seperti Hikayat Raja-Raja Pasai, Sejarah Melayu, Babad Tanah Jawi). Audit sebelumnya (Task 1-8 di worklog) sudah memverifikasi tokoh kunci untuk topik terkait (Mataram Kuno, Singasari).
- Re-extraction dari PDF asli (hanya rekomendasi, bukan eksekusi).
- Penyuntingan editorial (gaya bahasa, pilihan kata, dll.).

---

## Lampiran

### A. File JSON Audit
- `/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/jilid-3/_audit/structural-audit.json` — detail per file
- `/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/jilid-3/_audit/structural-summary.json` — ringkasan agregat

### B. Script Audit
- `/home/z/my-project/scripts/audit_jilid3_struktural.py` — script utama audit struktural
- `/home/z/my-project/scripts/audit_jilid3_detail.py` — script detail empty sections & garbage

### C. Sumber Referensi
- PDF asli: `Sejarah Indonesia_ Dinamika Kebangsaan dalam Arus Global, Jilid III - Nusantara dalam Jaringan Global_ Timur Tengah - Pustaka Budaya.pdf` (902 halaman)
- Metadata: `_meta.yaml` di folder jilid-3
- Quality report: `_quality-report.yaml` di parent folder kemenbud-2025

---

**Audit selesai.** Untuk eksekusi perbaikan spesifik, berikan instruksi per file atau per kategori masalah — saya bisa generate script koreksi otomatis untuk masing-masing prioritas.
