# README — Sumber Primer Supplementary

Folder ini berisi sumber sekunder yang **tidak termasuk** dalam 5 jilid buku Kemenbud 2025 (yang ada di folder `jilid-1` sampai `jilid-5`).

## Aturan Pakai

1. **Sumber primer utama** = 83 file MD Jilid I-V Kemenbud 2025 (folder `jilid-1` sampai `jilid-5`).
2. **Sumber primer supplementary** = dokumen tambahan di folder ini, untuk topik yang tidak tercakup di 5 jilid utama (mis. Jaka Tingkir, era Mataram Islam akhir, dll).
3. **Untuk produksi series entertainment**: sumber supplementary cukup dipakai sebagai baseline cerita. Creative freedom boleh untuk adaptasi dramatis.
4. **Untuk dokumenter akademis** (kalau diperlukan): perlu verifikasi dengan sumber orisinal (Babad Tanah Jawi, Serat Kandha, dll) yang tidak tersedia di repo ini.

## Isi Folder

### `jaka-tingkir-damar-shashangka/`

5 file MD berisi kisah Jaka Tingkir (5 bagian) yang diterjemahkan + diinterpretasi oleh Damar Shashangka di blog Puri Damar Shashangka (2010).

**Sumber asli**: https://damar-shashangka.blogspot.com/2010/06/jaka-tingkir-1.html sampai `jaka-tingkir-5.html`

**Penulis**: Damar Shashangka

**Sumber yang disitir Damar Shashangka**:
1. Babad Tanah Jawi
2. Babad Tanah Jawi Demakan
3. Serat Kandha
4. Kronik Tionghoa Klenteng Sam Po Kong Semarang
5. Cerita tutur masyarakat Jawa
6. Baboning Kitab Primbon (Sadu Budi, Solo)

**Periode**: 1499-1550 M (Pajang Awal / Akhir Demak)

**Tokoh utama**: Mas Karebet / Jaka Tingkir / Adipati Adiwijaya

**Master era**: `master-era/JAKA-TINGKIR-damar-shashangka.md`

**Series plan**: `produksi/pra-produksi/jaka-tingkir-series/SERIES-PLAN.md`

**Catatan duel**:
- Duel di Pegunungan Prawata (EP6) = Jaka Tingkir vs **Kebo Andanu** (gerilyawan yang membangkang), BUKAN vs Arya Penangsang.
- Duel maut Jaka Tingkir vs Arya Penangsang terjadi di Pajang akhir (~1554 M), ada di sequel series "Arya Penangsang" yang sumbernya BELUM ada di repo (perlu cari dari Damar Shashangka).

## Cara Tambah Sumber Supplementary Baru

Kalau menemukan sumber supplementary lain (mis. kisah Panji, Arya Penangsang, babad lain, blog sejarah lain), buat subfolder baru dengan format:

```
supplementary/
├── README.md (file ini)
└── {nama-topik-slug}/
    ├── {bagian-1}.md
    ├── {bagian-2}.md
    └── ...
```

Lalu bikin master-era di `master-era/{NAMA-TOPIK}.md` dengan format sama dengan `JAKA-TINGKIR-damar-shashangka.md`.

