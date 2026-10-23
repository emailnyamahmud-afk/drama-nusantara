#!/usr/bin/env python3
"""
Generate 24 TTS adaptive untuk EP1 Jaka Tingkir.

Pola: rate +25% default, pitch sesuai karakter.
Voice: id-ID-ArdiNeural (narrator), jv-ID-DimasNeural (karakter Jawa).

Logic adaptive: cek TTS actual duration vs SRT cue, kalau > cue → re-generate dengan rate lebih cepat (capped at +100%).
"""
import asyncio
import edge_tts
import json
import subprocess
from pathlib import Path

ROOT = Path("/home/z/my-project")
OUT_DIR = ROOT / "produksi/tts-output/jaka-tingkir-ep1"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def rate_to_mult(rate_str):
    if rate_str.startswith("+"):
        return 1 + float(rate_str[1:-1]) / 100
    elif rate_str.startswith("-"):
        return 1 - float(rate_str[1:-1]) / 100
    return 1.0


def mult_to_rate(mult):
    pct = (mult - 1) * 100
    return f"+{pct:.0f}%" if pct >= 0 else f"{pct:.0f}%"


def get_duration(mp3_path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)],
        capture_output=True, text=True
    )
    return float(r.stdout.strip()) if r.stdout.strip() else 0


# ============================================================
# Voice profiles (rate +25% default, sesuai naskah EP1)
# ============================================================
VOICE_PROFILES = {
    "Narrator": {"voice": "id-ID-ArdiNeural", "rate": "+25%", "pitch": "+0Hz", "language": "id"},
    "Raden Patah": {"voice": "jv-ID-DimasNeural", "rate": "+15%", "pitch": "-3Hz", "language": "jv"},
    "Raden Yunus": {"voice": "jv-ID-DimasNeural", "rate": "+20%", "pitch": "+2Hz", "language": "jv"},
    "Sunan Kudus": {"voice": "jv-ID-DimasNeural", "rate": "+15%", "pitch": "-2Hz", "language": "jv"},
    "Sunan Kalijaga": {"voice": "jv-ID-DimasNeural", "rate": "+5%", "pitch": "-5Hz", "language": "jv"},
    "Pangeran Trenggana": {"voice": "jv-ID-DimasNeural", "rate": "+20%", "pitch": "+0Hz", "language": "jv"},
    "Raden Suryawiyata": {"voice": "jv-ID-DimasNeural", "rate": "+20%", "pitch": "-1Hz", "language": "jv"},
    "Sunan Giri Dalem": {"voice": "jv-ID-DimasNeural", "rate": "+15%", "pitch": "-2Hz", "language": "jv"},
}


# ============================================================
# 24 TTS jobs dari naskah EP1 (manual extraction)
# ============================================================
# Setiap segmen punya: cue_duration, speaker, text
TTS_JOBS = [
    # SCENE 1 — Pembuka: Demak Berdiri (1478 M)
    {
        "segment_id": "EP1-S001-SEG01",
        "cue_duration": 20,
        "speaker": "Narrator",
        "text": "Tahun seribu empat ratus tujuh puluh delapan Masehi. Di pesisir utara Pulau Jawa, sebuah kesultanan baru berdiri. Demak Bintara — pewaris dinasti Majapahit yang telah runtuh. Seorang pangeran berdarah biru, Raden Patah, naik tahta sebagai Sultan Syah Alam Akbar Jiem Boen-ningrat pertama."
    },
    {
        "segment_id": "EP1-S001-SEG02",
        "cue_duration": 35,
        "speaker": "Raden Patah",
        "text": "Wonten ngarsanipun, para wali lan para adipati. Demak sampun jumeneng. Majapahit sampun runtuh. Dhumateng Allah Ta'ala, mugi Panjenengan tansah kaluhuraken wonten salebeting dhiri. Dhumateng bebrayan agung, mugi tansah pinaringan kawilujengan."
    },
    # Narrator continuation in same segmen
    {
        "segment_id": "EP1-S001-SEG02-narrator",
        "cue_duration": 35,  # Same segmen, but separate TTS for narrator part
        "speaker": "Narrator",
        "text": "Empat putra Raden Patah berdiri di belakang tahta. Raden Yunus, sang sulung, gagah dan ambisius. Raden Suryawiyata, sang kedua, tenang namun tajam. Pangeran Trenggana, sang ketiga, berwawasan luas. Dan seorang putri yang kelak dinikahkan dengan bangsawan Pasai."
    },
    {
        "segment_id": "EP1-S001-SEG03",
        "cue_duration": 35,
        "speaker": "Narrator",
        "text": "Sunan Kalijaga, wali senior yang bermain di balik layar, menggembleng trah Tarub dari kejauhan. Sunan Kudus, sang Penasehat Agung, menjaga keseimbangan kekuasaan dengan tangan besi. Dua kekuatan yang nantinya akan membelah Demak dari dalam — Islam Putihan dan Islam Abangan — kini masih bersatu di bawah panji satu sultan."
    },
    # SCENE 2 — Empat Putra Raden Patah (1480-an)
    {
        "segment_id": "EP1-S002-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Raden Yunus, sang putra sulung, tumbuh menjadi pemuda gagah dengan ambisi menyeberang lautan. Sejak kecil, ia bercita-cita menandingi kejayaan Laksamana Hang Tuah dari Malaka. Sementara itu, Raden Suryawiyata, sang adik, lebih suka mempelajari siasat perang darat dan ilmu keris di Pesantren Kudus, di bawah bimbingan Sunan Kudus."
    },
    {
        "segment_id": "EP1-S002-SEG02",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Pangeran Trenggana, sang putra ketiga, lebih tenang dan berwawasan. Ia berguru kepada Raden Getas Pandhawa, cucu murid Sunan Kalijaga. Karena itu, hatinya lebih condong ke Islam Abangan — sinkretisme yang menghormati tradisi lama. Sementara Suryawiyata, di bawah asuhan Sunan Kudus, lebih ortodoks — pro Putihan."
    },
    {
        "segment_id": "EP1-S002-SEG03",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Dua aliran — Putihan dan Abangan — kini mulai bersaing diam-diam di balik tahta. Persaingan ini sempat mereda saat pemerintahan Raden Patah. Namun api yang dipendam itu, akan menyala berkobar ketika sang Sultan wafat. Dan hari itu, tak lama lagi."
    },
    # SCENE 3 — Malaka Jatuh (1511 M)
    {
        "segment_id": "EP1-S003-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Tahun seribu lima ratus sebelas Masehi. Tiga puluh tiga tahun setelah Demak berdiri, kabar duka tiba dari seberang Selat Malaka. Malaka — kota suci perdagangan Islam di Asia Tenggara, pusat rempah-rempah dunia — jatuh ke tangan armada Portugis di bawah pimpinan Alfonso d'Albuquerque."
    },
    {
        "segment_id": "EP1-S003-SEG02",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Malaka dipimpin oleh Sultan Mahmud Syah. Laksamana handalnya, Hang Tuah — sang pahlawan legendaris yang konon tidak pernah kalah dalam duel — gugur dalam pertempuran terakhir. Malaka jatuh. Darah menggenangi pelabuhan yang dulu menjadi jantung perdagangan Islam Nusantara."
    },
    {
        "segment_id": "EP1-S003-SEG03",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Penyerangan ini dipicu oleh semangat Reconquista — dendam bangsa Eropa terhadap kekuasaan Islam di mana pun berada. Jatuhnya Constantinopel ke tangan Turki Utsmani tahun seribu empat ratus lima puluh tiga telah menutup perdagangan di Laut Tengah. Bangsa Eropa berlomba mencari jalur baru ke rempah-rempah. Dan Malaka menjadi sasaran utama."
    },
    {
        "segment_id": "EP1-S003-SEG04",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Kabar ini sampai ke Demak Bintara. Raden Patah, sang Sultan tua, murka. Malaka adalah jalur utama perdagangan Nusantara. Jika Portugis bercokol di sana, perekonomian umat Islam akan mati. Namun Raden Patah sudah tua. Tindakan harus diambil oleh generasi muda."
    },
    # SCENE 4 — Raden Yunus Serang Malaka (1512 M)
    {
        "segment_id": "EP1-S004-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Atas fatwa Dewan Wali Sangha, Raden Patah mengutus putra sulungnya, Raden Yunus, memimpin armada laut Demak untuk menyerang Malaka. Ribuan kapal berlayar menuju selat, dengan persenjataan lengkap. Peperangan akan terjadi. Malaka, sekali lagi, akan menjadi ajang pertumpahan darah."
    },
    {
        "segment_id": "EP1-S004-SEG02",
        "cue_duration": 30,
        "speaker": "Raden Yunus",
        "text": "Para prajurit Demak! Malaka sampun dipuncepeng dening wong kafir! Panjenengan sedaya lan kula badhe mbedah malih Malaka saking tanganipun! Surya Majapahit badhe mubeng malih ing langit Jawa!"
    },
    {
        "segment_id": "EP1-S004-SEG03",
        "cue_duration": 40,
        "speaker": "Narrator",
        "text": "Peperangan pun pecah. Portugis mati-matian membendung serangan besar-besaran Lasykar Jawa. Pasukan Demak begitu dahsyatnya — beberapa wilayah Malaka berhasil diduduki. Namun sayang, penyerangan ini tidak disertai dukungan penuh dari pihak Malaka sendiri."
    },
    {
        "segment_id": "EP1-S004-SEG04",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Malaka diam-diam mempersulit gerak laju Lasykar Jawa. Mereka takut — jika Portugis berhasil dipukul mundur, maka sekali lagi, Malaka akan jatuh ke tangan orang-orang Jawa, seperti saat Majapahit berkuasa dulu. Alasan klasik dan ironis. Karena kecurigaan ini, kekuatan gabungan pecah dari dalam."
    },
    {
        "segment_id": "EP1-S004-SEG05",
        "cue_duration": 20,
        "speaker": "Narrator",
        "text": "Pada akhirnya, Portugis berhasil memukul mundur Lasykar Demak Bintara dari Malaka. Kekalahan telak bagi Demak. Sisa-sisa pasukan laut Demak bertolak kembali ke Jawa — membawa rasa malu dan dendam."
    },
    # SCENE 5 — Raden Patah Wafat (1518 M)
    {
        "segment_id": "EP1-S005-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Lima tahun setelah penyerangan Malaka, tepat tahun seribu lima ratus delapan belas Masehi, Raden Patah wafat. Sang pendiri Demak Bintara pergi meninggalkan tahta yang belum stabil. Untuk menggantikan sang ramanda, Dewan Wali Sangha memilih Raden Yunus — sang pangeran yang gagal membebaskan Malaka — sebagai Sultan kedua."
    },
    {
        "segment_id": "EP1-S005-SEG02",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Raden Yunus naik tahta dengan gelar Sultan Syah Alam Akbar Jiem Boen-ningrat kedua. Begitu memegang tampuk pemerintahan, politik garis keras Islam semakin ekstrem ia terapkan. Hal ini terpicu oleh masuknya bangsa Eropa ke Nusantara. Namun efek baliknya — para bangsawan Majapahit yang masih berpegang pada keyakinan Shiwa Buddha ikut terkena imbasnya."
    },
    {
        "segment_id": "EP1-S005-SEG03",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Tiga tahun kemudian, tepat tahun seribu lima ratus dua puluh satu Masehi, dendam berbuah. Raden Yunus terbunuh oleh sisa-sisa lasykar Majapahit yang merasa semakin tersudutkan."
    },
    # SCENE 6 — Kematian Raden Yunus (Detail)
    {
        "segment_id": "EP1-S006-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Berbagai versi beredar tentang kematian Raden Yunus. Dalam cerita tradisional, dikisahkan Keris Kyai Naga Sasra — pusaka sakti — menggigit punggung sang Sultan hingga wafat. Dari Kronik Tionghoa klenteng Sam Po Kong Semarang, diceritakan Dipati Yunus wafat karena menderita bengkak paru-paru. Sedangkan berita dari Portugis, Adipati Yunus wafat karena tusukan kerissteek."
    },
    {
        "segment_id": "EP1-S006-SEG02",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Apapun versi yang benar, satu hal yang pasti — Raden Yunus wafat tanpa meninggalkan putra. Hal ini mengakibatkan Dewan Wali Sangha harus menunjuk adiknya untuk memegang tampuk pemerintahan Demak. Dan di sinilah, perpecahan besar dimulai."
    },
    {
        "segment_id": "EP1-S006-SEG03",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Dewan Wali Sangha terpecah menjadi dua kubu. Sebagian mengusulkan Raden Suryawiyata, putra kedua Raden Patah, sebagai pengganti. Sebagian yang lain mengusulkan Pangeran Trenggana, putra ketiga, sebagai penggantinya. Kala itu, Dewan Wali Sangha dipimpin oleh Sunan Giri Dalem."
    },
    {
        "segment_id": "EP1-S006-SEG04",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Kala itu, banyak para wali sepuh yang sudah wafat dan digantikan oleh para wali muda. Namun ada dua orang wali yang masih hidup dan sangat-sangat disegani. Keduanya adalah Sunan Kalijaga dan Sunan Kudus. Sunan Kudus kini menjabat sebagai Penasehat Agung Kesultanan Demak. Sedangkan Sunan Kalijaga tetap bermain di balik layar."
    },
    # SCENE 7 — Cliffhanger: Dua Kubu (Closing)
    {
        "segment_id": "EP1-S007-SEG01",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Raden Getas Pandhawa, guru Pangeran Trenggana, adalah cucu murid Sunan Kalijaga. Praktis, Pangeran Trenggana lebih pro ke Islam Abangan. Dilain pihak, Raden Suryawiyata berguru dan bahkan diangkat sebagai murid emas oleh Sunan Kudus. Oleh karena itu pula, Raden Suryawiyata lebih pro ke Islam Putihan."
    },
    {
        "segment_id": "EP1-S007-SEG02",
        "cue_duration": 30,
        "speaker": "Narrator",
        "text": "Persaingan antara kubu Putihan dan Abangan ini kembali meruncing setelah beberapa waktu lalu sempat mereda saat pemerintahan Raden Patah. Dan persaingan semakin memanas setelah Raden Yunus wafat karena terbunuh. Di Pajang, seorang pemuda bernama Mas Karebet — yang belum kita kenal — sedang menunggu waktunya. Tapi itu, adalah kisah untuk episode berikutnya."
    },
]


async def generate_adaptive(job):
    """Generate 1 TTS dengan adaptive rate supaya fit ke cue_duration."""
    profile = VOICE_PROFILES[job["speaker"]]
    voice = profile["voice"]
    pitch = profile["pitch"]
    cue_dur = job["cue_duration"]
    
    default_rate = profile["rate"]
    max_rate = "+100%"
    max_mult = rate_to_mult(max_rate)
    
    output_path = OUT_DIR / f"{job['segment_id']}.mp3"
    
    print(f"\n[{job['segment_id']}] cue={cue_dur}s | speaker={job['speaker']} | voice={voice}")
    print(f"  text: {job['text'][:70]}{'...' if len(job['text']) > 70 else ''}")
    
    # Step 1: Generate dengan default rate
    print(f"  Step 1: Generate dengan default rate={default_rate}")
    communicate = edge_tts.Communicate(job["text"], voice, rate=default_rate, pitch=pitch)
    await communicate.save(str(output_path))
    actual_dur = get_duration(output_path)
    print(f"  → TTS actual: {actual_dur:.2f}s")
    
    # Step 2: Adaptive
    target_max = cue_dur - 1.0  # buffer 1s
    pad_silence = 0
    
    if actual_dur <= cue_dur:
        if actual_dur < target_max:
            pad_silence = cue_dur - actual_dur
            print(f"  ✅ FIT, pad silence = {pad_silence:.2f}s")
        else:
            print(f"  ✅ FIT (mepet)")
        final_rate = default_rate
        final_dur = actual_dur
    else:
        # Too long → adaptive
        default_mult = rate_to_mult(default_rate)
        new_mult = (actual_dur * default_mult) / target_max
        
        if new_mult > max_mult:
            print(f"  ⚠️ TIDAK MUAT walau rate {max_rate} (need {new_mult:.2f}, max {max_mult:.2f})")
            new_rate = max_rate
            await edge_tts.Communicate(job["text"], voice, rate=new_rate, pitch=pitch).save(str(output_path))
            final_dur = get_duration(output_path)
            final_rate = new_rate
        else:
            new_rate = mult_to_rate(new_mult)
            print(f"  Step 2: Re-generate dengan adaptive rate={new_rate} (mult={new_mult:.2f})")
            await edge_tts.Communicate(job["text"], voice, rate=new_rate, pitch=pitch).save(str(output_path))
            final_dur = get_duration(output_path)
            final_rate = new_rate
            print(f"  ✅ FIT: durasi={final_dur:.2f}s (target ≤ {target_max:.2f}s)")
    
    return {
        "segment_id": job["segment_id"],
        "speaker": job["speaker"],
        "voice": voice,
        "cue_duration": cue_dur,
        "tts_duration": final_dur,
        "actual_rate": final_rate,
        "pad_silence": pad_silence,
        "output_path": str(output_path)
    }


async def main():
    print("=" * 70)
    print("TTS ADAPTIVE BATCH — EP1 JAKA TINGKIR (24 jobs)")
    print("=" * 70)
    print(f"Output dir: {OUT_DIR}")
    print(f"Total jobs: {len(TTS_JOBS)}")
    print(f"Default rate: +25% (1.25x), max +100% (2.0x)")
    print()
    
    results = []
    for i, job in enumerate(TTS_JOBS, 1):
        print(f"\n[{i}/{len(TTS_JOBS)}]")
        result = await generate_adaptive(job)
        results.append(result)
    
    # Summary
    print("\n" + "=" * 70)
    print("TTS BATCH COMPLETE — EP1 JAKA TINGKIR")
    print("=" * 70)
    print(f"{'Seg ID':25s} {'Cue':>5s} {'TTS':>7s} {'Rate':>8s} {'Pad':>6s} {'Status':>10s}")
    print("-" * 70)
    total_tts = 0
    total_pad = 0
    fit_count = 0
    for r in results:
        if r["tts_duration"] <= r["cue_duration"]:
            status = "FIT ✅"
            fit_count += 1
        else:
            status = "OVER ⚠️"
        pad_str = f"{r['pad_silence']:.2f}s" if r["pad_silence"] > 0 else "-"
        print(f"{r['segment_id']:25s} {r['cue_duration']:>4d}s {r['tts_duration']:>6.2f}s {r['actual_rate']:>8s} {pad_str:>6s} {status:>10s}")
        total_tts += r["tts_duration"]
        total_pad += r["pad_silence"]
    print("-" * 70)
    print(f"{'TOTAL':25s} {'':>5s} {total_tts:>6.2f}s {'':>8s} {total_pad:>5.2f}s")
    print(f"\nFIT count: {fit_count}/{len(results)}")
    print(f"Total TTS audio: {total_tts:.2f}s")
    print(f"Total silence pad: {total_pad:.2f}s")
    print(f"Combined: {total_tts + total_pad:.2f}s (target: 720s)")
    
    # Save results
    results_path = OUT_DIR / "_tts_adaptive_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults: {results_path}")


if __name__ == "__main__":
    asyncio.run(main())
