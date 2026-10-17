# Phase 2 — Penulisan Naskah & Storyboard

**Status**: ⏳ Belum dimulai (pending Phase 1 finalisasi)

## Tujuan

Mengubah riset sejarah Phase 1 menjadi **ratusan ide drama Nusantara** yang siap diproduksi. Setiap drama = 1 folder terstruktur berisi naskah + storyboard + aset daftar (karakter, lokasi, wardrobe) untuk dipakai di Phase 3 (LoRA) dan Phase 4 (produksi).

## Struktur Folder (direncanakan)

```
phase-2-naskah-storyboard/
├── README.md                              ← file ini
├── _template/                             (template kosong untuk drama baru)
│   ├── naskah.md                          (template naskah)
│   ├── storyboard.yaml                    (template storyboard)
│   ├── characters.yaml                    (daftar karakter + voice ref)
│   ├── locations.yaml                     (daftar lokasi + LoRA ref)
│   ├── wardrobe.yaml                      (daftar kostum + LoRA ref)
│   └── README.md                          (instruksi pengisian)
│
├── drama-01-pralaya-mataram/             (1016 M)
├── drama-02-ken-arok/                    (1222-1227 M)
├── drama-03-peristiwa-bubat/             (1357 M)
├── drama-04-walisongo/                   (1475-1548 M)
├── drama-05-sultan-agung-batavia/        (1628-1629 M)
├── drama-06-diponegoro/                  (1825-1830 M)
├── drama-07-proklamasi/                  (1945 M)
├── drama-08-g30s-pki/                    (1965 M)
└── drama-09-reformasi-1998/              (1998 M)
```

## 9 Drama Anchor (Draft Pilihan)

| # | Judul | Era | Periode | Hook Dramatik | Durasi |
|---|-------|-----|---------|--------------|--------|
| 1 | Pralaya Mataram | 1 | 1016 M | Airlangga lari dari istana terbakar, bangun Kahuripan | 12 min |
| 2 | Ken Arok: Tirani & Karma | 2 | 1222-1227 M | Pengkhianat suci — bunuh Tunggul Ametung, kawin Ken Dedes, dibunuh Anusapati | 15 min |
| 3 | Peristiwa Bubat | 3 | 1357 M | Gajah Mada bunuh rombongan Pajajaran, Dyah Pitaloka tewas | 10 min |
| 4 | Walisongo: Sembilan Cahaya | 4 | 1475-1548 M | Sunan Kalijaga & Raden Patah — Islamisasi Jawa lewat budaya | 15 min |
| 5 | Sultan Agung Serang Batavia | 6 | 1628-1629 M | Mataram Islam gagal serang VOC 2x — heroisme tragis | 12 min |
| 6 | Pangeran Diponegoro | 7 | 1825-1830 M | Pangeran sufi perang melawan Belanda 5 tahun, ditangkap tipu | 15 min |
| 7 | Proklamasi | 8 | 1945 M | Soekarno-Hatta proklamasi 17 Agustus — harapan & revolusi | 10 min |
| 8 | G30S: Malam Panjang | 9 | 30 Sep 1965 | Penculikan 7 jenderal, Pembantaian PKI | 15 min |
| 9 | Reformasi: 9 Hari Mei | 10 | 12-21 Mei 1998 | Trisakti → Kerusuhan → Soeharto mundur dalam 9 hari | 12 min |

## Format Storyboard YAML (draft struktur)

```yaml
drama:
  id: "drama-01-pralaya-mataram"
  title: "Pralaya Mataram"
  era: 1
  periode: "1016 M"
  duration_minutes: 12
  total_scenes: 24
  aspect_ratio: "16:9"
  resolution: "1920x1080"
  fps: 24
  art_style: "cinematic hyperrealistic, warm earth tones, candlelight"

characters:
  - id: "airlangga"
    name: "Airlangga"
    age: 16
    lora_ref: "../../phase-3-lora-assets/characters/airlungga/"
    voice_ref: "edge-tts:id-ID-ArdiNeural"

locations:
  - id: "istana_bedulu"
    name: "Istana Bedulu, Bali"
    lora_ref: "../../phase-3-lora-assets/locations/istana-bali/"

scenes:
  - id: 1
    title: "Airlangga di Bali, malam"
    location: "istana_bedulu"
    time: "1016 M, malam"
    characters_present: ["airlungga", "dharmodayana"]
    shot_type: "medium shot, eye-level, candlelight"
    action: "Airlangga (16) berdiskusi dengan ayahnya raja Bali"
    dialog:
      - speaker: "dharmodayana"
        text: "Putraku, ada kabar gelisah dari Jawa."
        voice: "edge-tts:id-ID-ArdiNeural"
    prompt_t2i: >
      Cinematic scene, 1016 CE Balinese palace interior at night...
    prompt_i2v: >
      Subtle head turn toward father, slight lip movement during
      dialogue, candle flicker, 4 seconds
    voice_over: "Tahun 1016 Masehi. Sebuah cahaya padam di Jawa..."
    duration_seconds: 8
    music_mood: "tense, low drone with gamelan"
```

## Workflow per Drama (direncanakan)

1. Pilih drama anchor dari 9 pilihan di atas
2. Buat folder `drama-XX-nama/` (copy dari `_template/`)
3. Tulis `naskah.md` (5-15 menit, ~10-30 scenes)
4. Generate `storyboard.yaml` dari naskah
5. Daftar `characters.yaml` + `locations.yaml` + `wardrobe.yaml` yang dibutuhkan
6. ( Lanjut ke Phase 3 untuk LoRA dataset )

## Catatan

- Folder ini akan diisi setelah Phase 1 finalisasi dan disepakati untuk lanjut
- Storyboard YAML adalah **sumber kebenaran** untuk pipeline Phase 4 (T2I + TTS + I2V + ffmpeg)
- Format voice_ref: `edge-tts:id-ID-ArdiNeural` (laki-laki dewasa), `id-ID-GadisNeural` (perempuan dewasa), `id-ID-ArdiNeural` (laki-laki muda)
