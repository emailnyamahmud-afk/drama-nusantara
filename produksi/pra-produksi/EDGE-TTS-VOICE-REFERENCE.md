# Edge-TTS Voice Reference — Bahasa Indonesia & Jawa

**Tanggal**: 2026-10-23
**Sumber**: `edge-tts` v7.3.1 (Microsoft Azure TTS, free unlimited, no API key)
**Total voices available**: 322 voices di 100+ bahasa

---

## 🇮🇩 Bahasa Indonesia (id-ID) — 2 voices

| Voice ShortName | Gender | Friendly Name |
|---|---|---|
| `id-ID-ArdiNeural` | Male | Microsoft Ardi Online (Natural) |
| `id-ID-GadisNeural` | Female | Microsoft Gadis Online (Natural) |

**Penggunaan**:
- **ArdiNeural** — Default narrator (suara pria dewasa, netral). Cocok untuk narasi dokumenter.
- **GadisNeural** — Suara wanita dewasa, netral. Cocok untuk karakter perempuan Indonesia modern.

---

## 🏯 Bahasa Jawa (jv-ID) — 2 voices ⭐ NATIVE JAWA

| Voice ShortName | Gender | Friendly Name |
|---|---|---|
| `jv-ID-DimasNeural` | Male | Microsoft Dimas Online (Natural) |
| `jv-ID-SitiNeural` | Female | Microsoft Siti Online (Natural) |

**CATATAN PENTING** (koreksi dari dokumen sebelumnya):
- ❌ Salah: `jv-ID-MasNeural` (tidak ada di edge-tts)
- ✅ Benar: `jv-ID-DimasNeural` (laki-laki Jawa)

**Penggunaan**:
- **DimasNeural** — Laki-laki Jawa halus. Cocok untuk: Ken Arok, Dang Hyang Lohgawe, Tunggul Ametung, Empu Gandring, raja-raja Jawa lainnya.
- **SitiNeural** — Perempuan Jawa halus. Cocok untuk: Ken Dedes, permaisuri, putri Jawa.

---

## 🌍 Bahasa Daerah Indonesia Lainnya (for future productions)

| Bahasa | Locale | Voice Laki-laki | Voice Perempuan |
|---|---|---|---|
| **Sunda** | `su-ID` | `su-ID-JajangNeural` | `su-ID-TutiNeural` |
| **Melayu** | `ms-MY` | `ms-MY-OsmanNeural` | `ms-MY-YasminNeural` |

**Penggunaan untuk era lain**:
- Era 2D Majapahit → bisa pakai Jawa (jv-ID) karena Majapahit berbasis Jawa Kuno
- Era 3A-3C Islam Indonesia → bisa pakai Jawa (Mataram Islam) atau Melayu (Demak, Aceh)
- Era 4A VOC → mix Indonesia + Melayu (tergantung wilayah)
- Era 2B Sriwijaya → pakai Melayu Kuno (ms-MY paling mendekati)

---

## 🎭 Voice Profile Mapping untuk Ken Arok Series

Berdasarkan riset voice di atas, ini mapping yang recommended:

```json
{
  "voice_profiles": {
    "narrator": {
      "edge_tts_voice": "id-ID-ArdiNeural",
      "speed": "1.0",
      "pitch": "0",
      "emotion": "neutral",
      "language": "id",
      "purpose": "Narrator Indonesia modern — netral, mudah dipahami semua audience"
    },
    "ken_arok": {
      "edge_tts_voice": "jv-ID-DimasNeural",
      "speed": "1.05",
      "pitch": "+2",
      "emotion": "confident",
      "language": "jv",
      "purpose": "Pemuda Jawa ambisius — suara Jawa halus dengan pitch sedikit tinggi untuk kesan muda"
    },
    "dang_hyang_lohgawe": {
      "edge_tts_voice": "jv-ID-DimasNeural",
      "speed": "0.85",
      "pitch": "-4",
      "emotion": "wise",
      "language": "jv",
      "purpose": "Brahmana tua — suara Jawa halus, slow, pitch rendah untuk kesan bijak"
    },
    "tunggul_ametung": {
      "edge_tts_voice": "jv-ID-DimasNeural",
      "speed": "0.95",
      "pitch": "-2",
      "emotion": "cruel",
      "language": "jv",
      "purpose": "Akuwu zalim — suara Jawa halus, pitch rendah, agak lambat untuk kesan berkuasa"
    },
    "ken_dedes": {
      "edge_tts_voice": "jv-ID-SitiNeural",
      "speed": "0.95",
      "pitch": "-3",
      "emotion": "melancholic",
      "language": "jv",
      "purpose": "Putri yang ditawan — suara Jawa halus perempuan, slow, pitch rendah untuk kesan sedih"
    },
    "empu_gandring": {
      "edge_tts_voice": "jv-ID-DimasNeural",
      "speed": "0.9",
      "pitch": "-5",
      "emotion": "wise_old",
      "language": "jv",
      "purpose": "Emppu tua — suara Jawa halus, slow, pitch sangat rendah untuk kesan tua dan mistis"
    },
    "prajurit_tumapel": {
      "edge_tts_voice": "jv-ID-DimasNeural",
      "speed": "1.1",
      "pitch": "+1",
      "emotion": "aggressive",
      "language": "jv",
      "purpose": "Prajurit — suara Jawa kasar, cepat, pitch agak tinggi"
    }
  }
}
```

**Strategy voice**:
- ✅ Narrator pakai Indonesia (id-ID-ArdiNeural) — netral, mudah dipahami semua audience
- ✅ Dialog karakter pakai Jawa (jv-ID-DimasNeural/SitiNeural) — autentik untuk era Singasari
- ✅ Speed + pitch adjustment untuk differentiate karakter (muda vs tua vs zalim vs bijak)

---

## 📋 Cara Pakai edge-tts di Python

### Install:
```bash
pip install edge-tts
# atau kalau pakai venv:
uv pip install edge-tts --python /path/to/venv
```

### Basic usage — single voice:
```python
import asyncio
import edge_tts

async def generate_tts(text, voice, output_path, rate="+0%", pitch="+0Hz"):
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)
    print(f"Saved: {output_path}")

asyncio.run(generate_tts(
    text="Tahun 1222 masa Saka, seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel.",
    voice="id-ID-ArdiNeural",
    output_path="narrator_seg01.mp3"
))
```

### Batch generation dengan voice_profiles:
```python
import asyncio
import edge_tts
import json

async def generate_batch(json_path):
    with open(json_path) as f:
        data = json.load(f)
    
    voice_profiles = data["voice_profiles"]
    
    for seg in data["segments"]:
        tts = seg["tts"]
        profile = voice_profiles[tts["voice_profile"]]
        
        text = tts["text"]
        voice = profile["edge_tts_voice"]
        rate = f"+{int((float(profile.get('speed', 1.0)) - 1) * 100)}%"
        pitch = profile.get("pitch", "+0Hz").replace("+", "+").replace("-", "-")
        if not pitch.endswith("Hz"):
            pitch = f"{pitch}Hz"
        
        output = tts["tts_path"]
        
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(output)
        print(f"✅ {seg['segment_id']} → {output}")

asyncio.run(generate_batch("storyboard.json"))
```

---

## ⚡ Edge-TTS Pros & Cons

### Pros:
- ✅ **FREE unlimited** — no API key, no quota, no credit card
- ✅ **Native Jawa voice** — autentik untuk dialog historis
- ✅ **Quality bagus** — Neural TTS, suara natural
- ✅ **Adjustable** — speed, pitch, volume bisa di-tune
- ✅ **Multi-language** — 322 voices, 100+ bahasa
- ✅ **Easy install** — `pip install edge-tts`
- ✅ **Async support** — bisa batch generate paralel

### Cons:
- ⚠️ **Hanya 1 voice per gender per bahasa** — kalau butuh variasi lebih, harus pakai voice cloning (separate tool)
- ⚠️ **Tidak support custom voice** — kalau butuh voice aktor spesifik, harus pakai tool lain (ElevenLabs, dll — berbayar)
- ⚠️ **Emotion control terbatas** — hanya speed + pitch + volume, tidak ada emotion tag seperti Azure Premium
- ⚠️ **Online required** — butuh internet untuk fetch voice (Microsoft endpoint)

---

## 🎯 Rekomendasi Strategy Voice untuk Series

### Untuk Ken Arok Series (6 episode × 10 menit):
- **Narrator**: `id-ID-ArdiNeural` (Indonesia netral)
- **Dialog karakter Jawa**: `jv-ID-DimasNeural` (laki-laki) + `jv-ID-SitiNeural` (perempuan)
- Differentiate karakter via **speed + pitch adjustment** (lihat voice_profiles mapping di atas)

### Untuk era lain (future productions):
| Era | Bahasa Dialog | Voice |
|---|---|---|
| 1A-1D Prasejarah | Indonesia (narrator only) | id-ID-ArdiNeural |
| 2A-2C Hindu-Buddha | Jawa Kuno ( Dimas/Siti) | jv-ID-DimasNeural, jv-ID-SitiNeural |
| 2D Majapahit | Jawa Kuno | jv-ID-DimasNeural, jv-ID-SitiNeural |
| 3A Islamisasi awal | Melayu (untuk Aceh, Demak) + Jawa | ms-MY-OsmanNeural, ms-MY-YasminNeural, jv-ID-* |
| 3B-3C Mataram Islam | Jawa | jv-ID-DimasNeural, jv-ID-SitiNeural |
| 4A VOC | Indonesia modern | id-ID-ArdiNeural, id-ID-GadisNeural |
| 4B Kolonial 19 | Indonesia modern | id-ID-ArdiNeural, id-ID-GadisNeural |

---

## 📝 Update Schema v3.0 (Koreksi)

**Update dari dokumen sebelumnya** — koreksi `MasNeural` → `DimasNeural`:

```json
"voice_profiles": {
  "narrator": {
    "edge_tts_voice": "id-ID-ArdiNeural",
    "language": "id"
  },
  "ken_arok": {
    "edge_tts_voice": "jv-ID-DimasNeural",  // ⚠️ KOREKSI dari MasNeural
    "language": "jv"
  },
  "ken_dedes": {
    "edge_tts_voice": "jv-ID-SitiNeural",
    "language": "jv"
  }
}
```

---

## 🚀 Next Step

Sekarang voice reference sudah jelas. Next:
1. Update schema v3.0 dengan voice yang benar (DimasNeural, bukan MasNeural)
2. Bikin `scripts/generate_tts_batch.py` dengan voice_profiles mapping
3. Test generate 1 sample TTS untuk verifikasi voice Jawa
4. Lanjut ke produksi pertama (Ken Arok Series EP1)

Mau saya test generate sample TTS sekarang untuk verify voice Jawa-nya? Tinggal bilang.

---

## 15. USER FEEDBACK (2026-10-23) — Tempo Update + Audio Layering Strategy

### User feedback:
- ❌ **Tempo terlalu lambat** — sample v1 dengan rate +0% (1.0x) terlalu lambat
- ✅ **Pakai kecepatan 1.5x** (rate +50%) untuk default
- 🆕 **Tiap segmen akan punya BGM + SFX (dari YouTube)** — selain dialog TTS

### Updated voice profiles (rate +50% default):

| Karakter | Voice | Rate (lama → baru) | Pitch | Effect |
|---|---|---|---|---|
| Narrator default | id-ID-ArdiNeural | +0% → **+50%** (1.5x) | +0Hz | Netral tapi cepat |
| Narrator action | id-ID-ArdiNeural | **+60%** (1.6x) | +0Hz | Cepat untuk scene aksi |
| Ken Arok (muda) | jv-ID-DimasNeural | +5% → **+50%** (1.5x) | +2Hz | Muda, confident, cepat |
| Lohgawe (tua) | jv-ID-DimasNeural | -15% → **+20%** (1.2x) | -4Hz | Tua + bijak tapi tidak terlalu lambat |
| Tunggul Ametung (zalim) | jv-ID-DimasNeural | **+30%** (1.3x) | -2Hz | Berkuasa, agak cepat |
| Ken Dedes (perempuan) | jv-ID-SitiNeural | -5% → **+40%** (1.4x) | -3Hz | Melancholic tapi tidak lambat |
| Prajurit (agresif) | jv-ID-DimasNeural | **+70%** (1.7x) | +1Hz | Sangat cepat, kasar |
| Dialog tense | jv-ID-DimasNeural | **+60%** (1.6x) | -2Hz | Cepat untuk scene tegang |

### Sample v2 generated (rate updated):

Di `/home/z/my-project/download/tts-samples-v2/`:

| File | Voice | Rate | Durasi | Size | Karakter |
|---|---|---|---|---|---|
| `v2_narrator_id.mp3` | id-ID-ArdiNeural | +50% | 6.2s | 36 KB | Narrator 1.5x |
| `v2_narrator_action_id.mp3` | id-ID-ArdiNeural | +60% | 4.3s | 25 KB | Narrator action 1.6x |
| `v2_ken_arok_jv.mp3` | jv-ID-DimasNeural | +50% | 7.4s | 43 KB | Ken Arok muda confident 1.5x |
| `v2_lohgawe_jv.mp3` | jv-ID-DimasNeural | +20% | 9.3s | 54 KB | Lohgawe tua 1.2x (not too slow) |
| `v2_ken_dedes_jv.mp3` | jv-ID-SitiNeural | +40% | 6.6s | 38 KB | Ken Dedes 1.4x |
| `v2_dialog_fast_jv.mp3` | jv-ID-DimasNeural | +60% | 5.3s | 30 KB | Dialog tense 1.6x |

**Perbandingan durasi v1 vs v2** (sample Lohgawe):
- v1: 13.1s (rate -15%)
- v2: 9.3s (rate +20%)
- **Difference: ~30% lebih cepat** — sesuai feedback user

---

## 16. Audio Layering Strategy — TTS + BGM + SFX

### Per segmen akan punya 3 audio layer:

```
Layer 1: TTS (dialog/narasi)     — main audio, volume 1.0 (100%)
Layer 2: BGM (background music)  — subtle, volume 0.15-0.20 (15-20%)
Layer 3: SFX (sound effects)     — selective, volume 0.25-0.35 (25-35%)
```

### BGM Source — YouTube Audio Library (FREE, no copyright)

**YouTube Audio Library** = library musik gratis untuk creator:
- URL: https://studio.youtube.com (login Google account)
- Filter: Free, no attribution required (cari yang "No attribution required")
- Genre: ambient, cinematic, dramatic, world, percussion
- Download MP3 gratis, bebas pakai untuk konten YouTube

**Alternative BGM sources**:
- **Pixabay Music**: https://pixabay.com/music/ — free, no attribution
- **Free Music Archive**: https://freemusicarchive.org/ — Creative Commons
- **Incompetech**: https://incompetech.com/ — Kevin MacLeod, CC BY 4.0
- **Bensound**: https://www.bensound.com/ — free dengan attribution

**Recommended BGM tracks untuk Ken Arok Series** (search di YouTube Audio Library):
- "Tribal Percussion" / "Forest Ambience" — untuk scene hutan
- "Royal Court" / "Cinematic Drama" — untuk scene pendopo
- "Mystic East" / "Asian Ambience" — untuk scene spiritual/ramalan
- "Epic Battle" / "Tense Action" — untuk scene konflik

### SFX Source — YouTube Audio Library + Freesound

**YouTube Audio Library** juga punya SFX:
- Sound effects tab di YouTube Studio
- Categories: ambient, nature, human, impact, whoosh

**Freesound** = https://freesound.org/ — komunitas SFX:
- Free dengan akun
- Filter CC0 (no attribution) untuk kemudahan
- Search: footstep, twig snap, sword, fire, rain, wind

**Recommended SFX per scene**:
| Scene | SFX needed |
|---|---|
| Chase scene | footstep running, twig snap, distant shouting |
| Pendopo scene | fire crackle, goblet clink, fabric rustle |
| Bengkel Empu | hammer strike, bellows, fire crackle, metal scrape |
| Storm scene | thunder, rain, wind howling |
| Ramalan scene | heartbeat, breath catch, ethereal drone |

### Audio Mixing Strategy

**Per segmen, ffmpeg akan mix 3 layer**:
```bash
ffmpeg -y \
  -i seg01_tts.mp3 \
  -i seg01_bgm.mp3 \
  -i seg01_sfx.mp3 \
  -filter_complex "
    [1:a]volume=0.15[b];  # BGM 15% volume
    [2:a]volume=0.30[s];  # SFX 30% volume
    [0:a][b][s]amix=inputs=3:duration=first:dropout_transition=0[a]
  " \
  -map "[a]" \
  -c:a libmp3lame -b:a 128k \
  seg01_audio_mixed.mp3
```

**Volume reference**:
- TTS: 1.0 (always loudest — ini konten utama)
- BGM: 0.15-0.20 (subtle background)
- SFX: 0.25-0.35 (selective emphasis)

### JSON Schema v3.0 — Audio Field Update

```json
"audio_layers": {
  "tts": {
    "path": "produksi/tts-output/ep1/EP1-S001-SEG01.mp3",
    "volume": 1.0,
    "speaker": "ken_arok"
  },
  "bgm": {
    "path": "produksi/bgm-library/tense_tribal_percussion.mp3",
    "source": "youtube_audio_library",
    "volume": 0.15,
    "loop": true,  // loop kalau BGM lebih pendek dari segmen
    "fade_in": 1.0,  // fade in 1 detik
    "fade_out": 1.0
  },
  "sfx": {
    "path": "produksi/sfx-library/footstep_running.mp3",
    "source": "freesound",
    "volume": 0.30,
    "loop": true,
    "fade_in": 0.1,
    "fade_out": 0.2
  }
}
```

### Demo Audio Layering

Sample demo sudah di-generate di `/home/z/my-project/download/audio-layer-demo/`:
- `demo_bgm.mp3` — dummy BGM (ffmpeg sine wave, 9.4s)
- `demo_sfx.mp3` — dummy SFX (ffmpeg noise, 4s)
- `demo_ken_arok_mixed.mp3` — TTS + BGM + SFX mixed (7.4s)

**Note**: BGM/SFX di demo ini DUMMY (generated via ffmpeg). Production akan pakai BGM/SFX asli dari YouTube Audio Library + Freesound.

---

## 17. Updated Strategy — Workflow dengan Audio Layering

### Workflow revisi (4 step + audio layering):

```
Step 1: PRA-PRODUKSI JSON
   - Tambah field: audio_layers per segmen (TTS + BGM + SFX)
   - User approve per segmen, termasuk pilih BGM/SFX per scene
   ↓
Step 2: BATCH T2I + BATCH TTS + COLLECT BGM/SFX
   - T2I: Dola/Flow (reuse existing)
   - TTS: edge-tts dengan rate +50% (1.5x) default
   - BGM: download dari YouTube Audio Library
   - SFX: download dari Freesound
   ↓
Step 3: STITCH LOKAL via ffmpeg
   - Mix 3 audio layers per segmen (TTS loud, BGM subtle, SFX medium)
   - Composite image (Ken Burns) + mixed audio → segmen MP4
   - Concat semua segmen → episode MP4
   ↓
Step 4: DONE atau DaVinci Resolve untuk fine-tune
```

### Cost estimate per episode (10 menit):
- T2I: $0 (Dola/Flow free)
- TTS: $0 (edge-tts free)
- BGM: $0 (YouTube Audio Library free)
- SFX: $0 (Freesound free)
- ffmpeg: $0 (open source)
- **Total: $0 per episode**

**Estimasi effort per episode**:
- Download BGM+SFX: 1-2 jam (cari yang cocok per scene)
- Generate T2I: 10-15 menit (via skill Dola)
- Generate TTS: 5-10 menit (via script edge-tts)
- Mix audio + stitch video: 5-10 menit (via script ffmpeg)
- Review + iterate: 30-60 menit
- **Total: 2-4 jam per episode**
