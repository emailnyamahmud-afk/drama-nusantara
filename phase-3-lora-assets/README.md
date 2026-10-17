# Phase 3 — LoRA Assets (Karakter, Lokasi, Wardrobe)

**Status**: ⏳ Belum dimulai (menunggu Phase 2 selesai)

## Tujuan

Membangun **dataset LoRA** untuk karakter, lokasi, dan wardrobe yang dibutuhkan oleh drama-drama di Phase 2. LoRA (Low-Rank Adaptation) memungkinkan konsistensi visual karakter/lokasi lintas scene tanpa retraining full model.

## Struktur Folder (direncanakan)

```
phase-3-lora-assets/
├── README.md                              ← file ini
├── characters/                            (20-30 tokoh LoRA)
│   ├── airlungga/
│   │   ├── dataset/
│   │   │   ├── 001.jpg                   (close-up, front)
│   │   │   ├── 002.jpg                   (close-up, side profile)
│   │   │   ├── 003.jpg                   (medium shot, standing)
│   │   │   ├── 004.jpg                   (full body, walking)
│   │   │   ├── 005.jpg                   (with crown)
│   │   │   └── ... 30-50 images
│   │   ├── captions.txt                  (caption per image)
│   │   ├── trigger_word.txt              ("airlungga_prince")
│   │   ├── config.json                   (training: SDXL base, 1500 steps, lr 1e-4)
│   │   └── README.md                     (instruksi training dengan Kohya_ss)
│   ├── ken-arok/
│   ├── ken-dedes/
│   ├── gajah-mada/
│   ├── hayam-wuruk/
│   ├── raden-patah/
│   ├── sunan-kalijaga/
│   ├── sultan-agung/
│   ├── diponegoro/
│   ├── soekarno/
│   ├── soeharto/
│   └── gus-dur/
│
├── locations/                             (15-20 lokasi LoRA)
│   ├── borobudur-9ce/
│   ├── prambanan-9ce/
│   ├── trowulan-14ce/
│   ├── demak-mosque-16ce/
│   ├── keraton-mataram-17ce/
│   ├── yogyakarta-1945/
│   ├── lubang-buaya-1965/
│   ├── bca-plaza-1998/
│   └── trisakti-1998/
│
├── wardrobe/                              (10-15 kostum LoRA)
│   ├── baju-syailendra-priest/
│   ├── kebaya-kontemporer-tien/
│   ├── baju-safari-soeharto/
│   ├── seragam-loreng-tni-orba/
│   ├── jas-kolonial-belanda/
│   └── busana-walisongo/
│
└── style/                                  (5-10 style LoRA)
    ├── batik-jawa-kuno/
    ├── wayang-style/
    ├── cinematic-historic-lighting/
    └── javanese-temple-relief/
```

## Tokoh Prioritas (10 LoRA Karakter Pertama)

| # | Tokoh | Era | Usia di Drama | Voice Ref (Edge TTS) |
|---|-------|-----|---------------|---------------------|
| 1 | Airlangga | 1 (1016 M) | 16 | id-ID-ArdiNeural (muda) |
| 2 | Ken Arok | 2 (1222 M) | 30 | id-ID-ArdiNeural |
| 3 | Ken Dedes | 2 (1222 M) | 18 | id-ID-GadisNeural |
| 4 | Gajah Mada | 3 (1357 M) | 60 | id-ID-ArdiNeural (deep) |
| 5 | Hayam Wuruk | 3 (1357 M) | 33 | id-ID-ArdiNeural |
| 6 | Raden Patah | 4 (1500 M) | 50 | id-ID-ArdiNeural |
| 7 | Sunan Kalijaga | 4 (1500 M) | 60 | id-ID-ArdiNeural |
| 8 | Sultan Agung | 6 (1628 M) | 40 | id-ID-ArdiNeural |
| 9 | Pangeran Diponegoro | 7 (1825 M) | 42 | id-ID-ArdiNeural |
| 10 | Soekarno | 8 (1945 M) | 44 | id-ID-ArdiNeural |
| 11 | Soeharto | 10 (1965-98) | 50-77 | id-ID-ArdiNeural |
| 12 | Gus Dur | 10 (1990s) | 50-60 | id-ID-ArdiNeural |

## Lokasi Prioritas (10 LoRA Lokasi Pertama)

| # | Lokasi | Era | Tampilan |
|---|--------|-----|---------|
| 1 | Borobudur (abad 9) | 1 | candi Buddha terbesar, sunset golden |
| 2 | Prambanan (abad 9) | 1 | candi Hindu, silhouette malam |
| 3 | Trowulan (abad 14) | 3 | ibu kota Majapahit, batu bata merah |
| 4 | Demak Mosque (abad 16) | 4 | masjid kayu, tiang soko tatal |
| 5 | Keraton Mataram (abad 17) | 6 | istana Sultan Agung, gapura Semar Tinandhu |
| 6 | Yogyakarta 1945 | 8 | kota kolonial + Jalan Malioboro |
| 7 | Lubang Buaya 1965 | 9 | sumur tua + Monumen Pancasila Sakti |
| 8 | BCA Plaza 1998 | 10 | gedung tinggi Jakarta, kerusuhan |
| 9 | Trisakti 1998 | 10 | kampus Grogol, demonstrasi mahasiswa |
| 10 | Istana Negara | 7-10 | Istana Merdeka, kolonial Belanda |

## Workflow Training LoRA (direncanakan)

```
1. Collect 30-50 images karakter/lokasi/wardrobe
2. Caption setiap image (BLIP atau manual)
3. Trigger word: "<nama>_<periode>" (mis. "airlungga_prince")
4. Training dengan Kohya_ss / OneTrainer / sd-scripts
   - Base model: SDXL 1.0 atau Flux.dev
   - Steps: 1500-2000
   - Learning rate: 1e-4 (UNet), 5e-5 (Text Encoder)
   - Batch size: 1
   - Resolution: 1024x1024
   - Output: <nama>.safetensors (~100-300 MB)
5. Validasi: generate 5 test images, cek konsistensi
6. Iterasi: tambah dataset, retrain jika perlu
```

## Catatan

- LoRA output `.safetensors` TIDAK akan di-commit ke GitHub (terlalu besar, ~100-300 MB per file)
- Yang di-commit: `dataset/` (jika ukurannya kecil), `captions.txt`, `trigger_word.txt`, `config.json`, `README.md`
- LoRA disimpan di storage lokal (Google Drive / OneDrive) untuk akses pipeline Phase 4
- Folder ini akan diisi setelah Phase 2 selesai (karena daftar LoRA tergantung drama yang dipilih)
