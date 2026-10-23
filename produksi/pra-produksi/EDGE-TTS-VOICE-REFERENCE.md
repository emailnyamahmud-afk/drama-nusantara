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
