# Phase 4 — Produksi Film (T2I + TTS + I2V + Compose)

**Status**: ⏳ Belum dimulai (menunggu Phase 2 storyboard + Phase 3 LoRA siap)

## Tujuan

Pipeline end-to-end untuk mengubah `storyboard.yaml` (dari Phase 2) menjadi video MP4 final dengan aset LoRA (dari Phase 3).

Pipeline:
```
storyboard.yaml
       ↓
[T2I] Generate image per scene dengan LoRA
       ↓
[TTS] Generate voice per dialog dengan Edge TTS
       ↓
[I2V] Animate image dengan motion prompt
       ↓
[Compose] ffmpeg: gabung image+voice+music+SFX → MP4
       ↓
final_drama.mp4
```

## Struktur Folder (direncanakan)

```
phase-4-produksi/
├── README.md                              ← file ini
├── pipeline/
│   ├── generate_image.py                 (SDXL/Flux + LoRA via API)
│   ├── generate_voice.py                  (Edge TTS via Python)
│   ├── animate_image.py                   (I2V: Kling/Runway/LTX/CogVideoX)
│   ├── compose_video.py                   (ffmpeg compose all assets)
│   ├── utils/
│   │   ├── storyboard_loader.py          (parse storyboard.yaml)
│   │   ├── lora_resolver.py               (resolve LoRA paths)
│   │   └── progress_tracker.py            (log progress per scene)
│   └── requirements.txt                   (Python deps)
│
├── projects/                              (per-drama working files)
│   ├── drama-01-pralaya-mataram/
│   │   ├── storyboard.yaml               (copy dari phase-2)
│   │   ├── generated_images/             (PNG per scene)
│   │   ├── generated_voices/             (MP3 per dialog)
│   │   ├── generated_clips/              (MP4 per scene animated)
│   │   ├── music/                        (background music MP3)
│   │   ├── sfx/                          (sound effects MP3)
│   │   └── final_drama-01-pralaya-mataram.mp4
│   ├── drama-02-ken-arok/
│   └── ... (9 drama total)
│
├── output/                                (final MP4 files untuk distribusi)
│   ├── drama-01-pralaya-mataram_v1.mp4
│   ├── drama-02-ken-arok_v1.mp4
│   └── ...
│
└── logs/                                  (production logs per run)
    └── 2026-10-17_drama-01.log
```

## Pipeline Detail

### 1. generate_image.py (T2I)

```python
import yaml, requests, os, base64

def generate_scene_image(scene, drama, output_path):
    prompt = scene['prompt_t2i']
    character_loras = [c['lora_ref'] for c in drama['characters']
                       if c['id'] in scene['characters_present']]
    location_lora = drama['locations'][scene['location']]['lora_ref']

    # Panggil SDXL WebUI API (Automatic1111 / ComfyUI)
    response = requests.post("http://localhost:7860/sdapi/v1/txt2img", json={
        "prompt": prompt,
        "negative_prompt": "lowres, bad anatomy, deformed, ugly, low quality",
        "loras": character_loras + [location_lora],
        "steps": 30,
        "cfg_scale": 7.5,
        "width": 1920, "height": 1080,
        "sampler_name": "DPM++ 2M Karras"
    })
    image_data = base64.b64decode(response.json()['images'][0])
    with open(output_path, 'wb') as f:
        f.write(image_data)
```

### 2. generate_voice.py (TTS dengan Edge TTS)

```python
import edge_tts, asyncio, yaml

async def generate_dialog_voice(dialog_line, output_path):
    voice = dialog_line['voice']
    text = dialog_line['text']
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

async def generate_voice_over(text, output_path):
    voice = "id-ID-ArdiNeural"  # voice over default
    communicate = edge_tts.Communicate(text, voice, rate="-15%")
    await communicate.save(output_path)

async def main():
    with open('storyboard.yaml') as f:
        sb = yaml.safe_load(f)
    for scene in sb['scenes']:
        if 'voice_over' in scene:
            await generate_voice_over(
                scene['voice_over'],
                f"voices/scene_{scene['id']}_vo.mp3"
            )
        for dialog in scene.get('dialog', []):
            await generate_dialog_voice(
                dialog,
                f"voices/scene_{scene['id']}_dialog_{dialog['speaker']}.mp3"
            )

asyncio.run(main())
```

### 3. animate_image.py (I2V)

```python
import requests, os

def animate_scene_image(image_path, scene, output_path):
    prompt_i2v = scene.get('prompt_i2v', 'subtle motion, breathing')
    duration = scene.get('duration_seconds', 4)

    # Opsi engine I2V:
    # - Kling AI (komersial, kualitas tinggi, ~$5 per video)
    # - Runway Gen-3 Alpha (komersial)
    # - LTX-Video (open source, lokal, gratis)
    # - CogVideoX (open source, lokal, gratis)

    # Contoh: LTX-Video lokal
    response = requests.post("http://localhost:7861/generate", json={
        "image": image_path,
        "prompt": prompt_i2v,
        "duration": duration,
        "fps": 24,
        "resolution": "1920x1080"
    })
    with open(output_path, 'wb') as f:
        f.write(response.content)
```

### 4. compose_video.py (ffmpeg)

```python
import subprocess, os, yaml

def compose_final_video(drama_folder, output_mp4):
    # 1. Concat semua animated clips
    scenes_file = os.path.join(drama_folder, 'scenes.txt')
    with open(scenes_file, 'w') as f:
        for clip in sorted(os.listdir(f"{drama_folder}/generated_clips")):
            f.write(f"file 'generated_clips/{clip}'\n")

    # 2. Concat semua voice + music + sfx
    audio_file = os.path.join(drama_folder, 'audio.txt')
    # ... (logika sinkronisasi audio per scene)

    # 3. ffmpeg compose
    cmd = f"""ffmpeg -y \
        -f concat -safe 0 -i {scenes_file} \
        -i {drama_folder}/music/background.mp3 \
        -i {drama_folder}/audio_full.wav \
        -filter_complex "[1:a]volume=0.3[bg];[2:a][bg]amix=inputs=2:duration=longest[aout]" \
        -map 0:v -map "[aout]" \
        -c:v libx264 -c:a aac -b:a 192k \
        {output_mp4}"""

    subprocess.run(cmd, shell=True, check=True)
```

## Tools yang Direncanakan

| Tool | Fungsi | Lisensi | Setup |
|------|--------|---------|-------|
| **SDXL / Flux** | T2I image generation | Open source | Local GPU / RunPod / Colab |
| **Automatic1111 / ComfyUI** | T2I WebUI + API | Open source | Local |
| **Kohya_ss** | LoRA training | Open source | Local GPU |
| **Edge TTS** | Voice synthesis (Microsoft) | Gratis (no API key) | Python package |
| **LTX-Video** | I2V open source | Open source (Apache 2.0) | Local GPU |
| **CogVideoX** | I2V open source | Open source | Local GPU (heavy) |
| **Kling AI** | I2V komersial | Bayar per video | API |
| **Runway Gen-3** | I2V komersial | Bayar per video | API |
| **ffmpeg** | Video compose | Open source | Local |

## Catatan

- Folder ini akan diisi setelah Phase 2 + Phase 3 siap
- File output besar (MP4, dataset LoRA) TIDAK di-commit ke GitHub
- Yang di-commit: `pipeline/*.py` (script), `projects/*/storyboard.yaml`, `logs/*.log`
- File output disimpan di storage lokal (Google Drive / OneDrive / NAS)
