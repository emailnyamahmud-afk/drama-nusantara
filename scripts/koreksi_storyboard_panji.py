#!/usr/bin/env python3
"""
Koreksi storyboard-pilot.json:
- Ganti semua referensi "Kameswara" → "Panji Asmara Bangun" (atau "Panji")
- Ganti semua referensi "Sri Kirana" / "Kirana" (sebagai tokoh) → "Candra Kirana"
- Ganti "Patih Kediri" → "Patih Jenggala"
- Ganti "Kameswara ref" → "Panji ref" di prompt visual
- Update deskripsi karakter sesuai characters.md baru
- Update dialog sesuai story-bible.md baru
- Update lokasi keraton: "Kediri (Dahanapura)" di scene 1 → "Jenggala (Kahuripan)" 
  (karena scene 1 di pendopo Jenggala, bukan Kediri)
- Tambahkan scene 3 di candi (lokal netral, bukan istana Kediri atau Jenggala)

Logika:
- C001 = Panji Asmara Bangun (Pangeran Jenggala), bukan Kameswara
- C002 = Dewi Candra Kirana (Putri Kediri), bukan "Sri Kirana"
- C003 = Patih Jenggala, bukan "Patih Kediri"
- C004 = Mpu Dharmaja (tetap)
- L001 = Keraton Jenggala (Kahuripan) — diubah dari "Keraton Kediri (Dahanapura)"
- L002 = Tepi Sungai Brantas (tetap)
- L003 = Candi/Altar Upacara (tetap)
"""

import json
import re
from pathlib import Path

STORYBOARD_PATH = Path(
    "/home/z/my-project/produksi/panji/pre-produksi/storyboard-pilot.json"
)

# Mapping nama tokoh
CHAR_RENAME = {
    "Sri Kameswara": "Panji Asmara Bangun",
    "Kameswara": "Panji Asmara Bangun",
    "Sri Kirana": "Candra Kirana",
    "Patih Kediri": "Patih Jenggala",
}

# Mapping warna kerajaan: Jenggala = biru, Kediri = merah
COLOR_REPLACEMENTS = [
    # Kameswara wardrobe: red-gold (Kediri) → blue-gold (Jenggala)
    ("red-gold batik kain, golden chest plate", "blue-gold batik kain, golden tunic"),
    ("red-gold kain, golden crown", "blue-gold kain, golden destar"),
    ("red-gold batik kain, golden crown, keris at waist",
     "blue-gold batik kain, golden destar, keris at waist"),
    # Candra Kirana: blue-gold (Jenggala old) → red-gold (Kediri correct)
    ("blue-gold batik kain, small golden crown",
     "red-gold batik kain, small golden crown"),
    ("blue-gold batik", "red-gold batik"),
    # Keraton palette
    ("red-gold royal banner", "blue-gold royal banner"),
    ("red-gold banner", "blue-gold banner"),
    ("red-gold kain", "blue-gold kain"),
]

# Mapping dialog/narasi (sesuai story-bible baru)
DIALOG_REPLACEMENTS = [
    # Narator opening
    ("Kini, seorang raja baru naik takhta di Kediri — Sri Kameswara.",
     "Kini, seorang pangeran muda bertahta di Jenggala — Panji Asmara Bangun."),
    ("Kediri di selatan, Jenggala di utara. Dua kerajaan yang lahir dari satu ayah, Airlangga.",
     "Jenggala di utara, Kediri di selatan. Dua kerajaan yang lahir dari satu ayah, Airlangga."),
    ("Yang membelah wilayahnya sebelum wafat. Selama 140 tahun, mereka bermusuhan.",
     "Yang membelah wilayahnya sebelum wafat. Selama 140 tahun, mereka bermusuhan."),
    # Dialog patih
    ("Baginda, Jenggala menggerudi pasukan di perbatasan. Mereka siap menyerang.",
     "Baginda Pangeran, Kediri menggerudi pasukan di perbatasan. Mereka siap menyerang."),
    # Dialog Panji (sebelumnya Kameswara)
    ("Bukan perang yang aku inginkan, Patih. Tapi perdamaian.",
     "Bukan perang yang aku inginkan, Patih. Tapi perdamaian."),
    ("Aku akan menikahi putri mereka. Sri Kirana. Dua kerajaan menjadi satu.",
     "Aku akan meminang putri mereka. Dewi Candra Kirana. Dua kerajaan menjadi satu."),
    # Narasi transisi
    ("Dan ia punya rencana yang berani. Bukan peperangan, tapi penyatuan.",
     "Dan ia punya rencana yang berani. Bukan peperangan, tapi penyatuan."),
    ("Kameswara berlayar ke perbatasan. Ke tepi Sungai Brantas. Tempat netral. Tempat pertemuan.",
     "Panji berlayar ke perbatasan. Ke tepi Sungai Brantas. Tempat netral. Tempat pertemuan."),
    # Narasi kedatangan Kirana
    ("Sri Kirana. Putri mahkota Jenggala. Bukan sekadar hadiah politik.",
     "Dewi Candra Kirana. Putri mahkota Kediri. Bukan sekadar hadiah politik."),
    ("Ia adalah wanita yang punya syarat sendiri.",
     "Ia adalah wanita yang punya syarat sendiri."),
    # Dialog Panji-Candra Kirana di sungai
    ("Putri Jenggala, aku bukan datang untuk menaklukkan. Aku datang untuk menyatukan.",
     "Putri Kediri, aku bukan datang untuk menaklukkan. Aku datang untuk menyatukan."),
    ("Penyatuan bukan dengan pernikahan, Baginda. Penyatuan adalah dengan kepercayaan.",
     "Penyatuan bukan dengan pernikahan, Baginda. Penyatuan adalah dengan kepercayaan."),
    ("Maka buktikan, Baginda. Bahwa kau pantas. Bukan sekadar raja, tapi seorang ksatria.",
     "Maka buktikan, Baginda. Bahwa kau pantas. Bukan sekadar pangeran, tapi seorang ksatria."),
    # Dialog janji Panji
    ("Aku berjanji, Putri. Bukan sebagai raja, tapi sebagai pria. Keduanya akan kubuktikan.",
     "Aku berjanji, Putri. Bukan sebagai pangeran, tapi sebagai pria. Keduanya akan kubuktikan."),
    # Smaradahana
    ("Sang hyang Kameswara, inkarnasi Kamajaya, dewa cinta yang bersemayam di Dahanapura.",
     "Sang hyang Panji Asmara Bangun, inkarnasi Kamajaya, dewa cinta yang bersemayam di Jenggala."),
    ("Permaisuri Kirana, inkarnasi Kamaratih, ratu yang bersinar bagaikan rembulan.",
     "Putri Candra Kirana, inkarnasi Kamaratih, ratu yang bersinar bagaikan rembulan."),
    # Closing narration
    ("Dan di tepi Sungai Brantas, dua kerajaan berjanji untuk menyatu. Bukan dengan pedang, tapi dengan kata.",
     "Dan di tepi Sungai Brantas, dua kerajaan berjanji untuk menyatu. Bukan dengan pedang, tapi dengan kata."),
    ("Dari pernikahan inilah lahir Smaradahana — Api Cinta.",
     "Dari pernikahan inilah lahir Smaradahana — Api Cinta."),
    ("Kisah yang akan menyeberang lautan. Ke Siam. Ke Khmer. Ke Birma.",
     "Kisah yang akan menyeberang lautan. Ke Siam. Ke Khmer. Ke Birma."),
    ("Kisah yang dikenal sebagai Panji.",
     "Kisah yang dikenal sebagai Panji."),
    ("Yang akan diukir di dinding candi. Dinyanyikan di istana. Ditari di keraton.",
     "Yang akan diukir di dinding candi. Dinyanyikan di istana. Ditari di keraton."),
    ("Dan diingat sepanjang masa.",
     "Dan diingat sepanjang masa."),
]

# Mapping prompt visual (T2I prompts)
PROMPT_REPLACEMENTS = [
    # Kameswara wardrobe → Panji wardrobe
    ("red-gold batik kain, golden chest plate with temple motifs",
     "blue-gold batik kain, golden tunic with temple motifs"),
    ("red-gold batik kain, golden crown, keris at waist",
     "blue-gold batik kain, golden destar crown, keris at waist"),
    ("wearing golden Javanese crown (makuta), red-gold batik kain, golden chest plate",
     "wearing golden Javanese destar, blue-gold batik kain, golden tunic"),
    # Reference to "Kameswara" in prompts
    ("Kameswara (C001 ref)", "Panji Asmara Bangun (C001 ref)"),
    ("Kameswara (C001)", "Panji (C001)"),
    # Candra Kirana wardrobe (already correct mostly, but ensure blue-gold → red-gold)
    ("golden kemben, blue-gold kain", "golden kemben, red-gold kain"),
    # Banner colors per kerajaan
    ("red-gold banner on rooftop", "blue-gold banner on rooftop"),
    ("Jenggala banner blue-gold", "Kediri banner red-gold"),
    # Royal boat colors
    ("Javanese royal boat on Brantas river at dawn, golden sunrise",
     "Javanese royal boat (blue-gold Jenggala colors) on Brantas river at dawn, golden sunrise"),
    ("Jenggala royal boat docking at wooden pier, blue-gold banner",
     "Kediri royal boat docking at wooden pier, red-gold banner"),
    # Kameswara → Panji in descriptive text
    ("Kameswara listening, Patih (C003) standing before him bowing",
     "Panji Asmara Bangun listening, Patih (C003) standing before him bowing"),
    ("Kameswara on throne", "Panji Asmara Bangun on throne"),
    ("Kameswara face, sharp eyes", "Panji face, sharp eyes"),
    ("Kameswara standing from throne", "Panji standing from throne"),
    ("Kameswara hand gripping keris pusaka", "Panji hand gripping keris pusaka"),
    ("Kameswara on royal boat, standing at bow", "Panji on royal boat, standing at bow"),
    ("Kameswara watching from riverbank", "Panji watching from riverbank"),
    # Kirana → Candra Kirana in descriptive text
    ("Sri Kirana (C002) stepping off boat", "Candra Kirana (C002) stepping off boat"),
    ("Sri Kirana (C002) face emerging from mist", "Candra Kirana (C002) face emerging from mist"),
    ("Kirana (C002) face, calm but firm expression", "Candra Kirana (C002) face, calm but firm expression"),
    ("Kirana (C002) smile, first genuine smile", "Candra Kirana (C002) smile, first genuine smile"),
    ("Sri Kirana (C002) face in firelight", "Candra Kirana (C002) face in firelight"),
    # Two-shot references
    ("Kameswara (C001) and Kirana (C002)", "Panji (C001) and Candra Kirana (C002)"),
    ("Kameswara (C001) and Kirana (C002) hands joining over sacred fire",
     "Panji (C001) and Candra Kirana (C002) hands joining over sacred fire"),
    ("Kameswara (C001) kneeling before Kirana (C002)",
     "Panji (C001) kneeling before Candra Kirana (C002)"),
    ("Kameswara and Kirana walking together along riverbank",
     "Panji and Candra Kirana walking together along riverbank"),
    ("Kameswara (C001) and Kirana (C002) foreheads touching",
     "Panji (C001) and Candra Kirana (C002) foreheads touching"),
    ("Kameswara (C001) and Kirana (C002) on palace balcony",
     "Panji (C001) and Candra Kirana (C002) on palace balcony"),
    ("Kameswara and Kirana silhouettes against fire",
     "Panji and Candra Kirana silhouettes against fire"),
]

# Mapping notes
NOTES_REPLACEMENTS = [
    ("First appearance Kameswara", "First appearance Panji Asmara Bangun"),
    ("Patih reports threat", "Patih reports Kediri threat"),
    ("Kameswara reveals plan", "Panji reveals plan"),
    ("Patih protests", "Patih protests Kediri alliance"),
    ("Decision announced", "Decision to marry Candra Kirana announced"),
    ("Symbol: keris = resolve", "Symbol: keris = resolve"),
    ("Transition to Act 2", "Transition to Act 2 — journey to Brantas"),
    ("Kameswara journey", "Panji journey to Brantas"),
    ("Jenggala boat approaching", "Kediri boat approaching"),
    ("Jenggala arrives", "Kediri arrives"),
    ("First appearance Kirana", "First appearance Candra Kirana"),
    ("POV Kameswara sees Kirana", "POV Panji sees Candra Kirana"),
    ("Reveal Kirana face", "Reveal Candra Kirana face"),
    ("Kameswara opens", "Panji opens"),
    ("Kirana challenges", "Candra Kirana challenges"),
    ("Kameswara impressed", "Panji impressed"),
    ("Kirana's challenge", "Candra Kirana's challenge"),
    ("Kameswara pledges", "Panji pledges"),
    ("Kirana accepts", "Candra Kirana accepts"),
    ("Walking together", "Panji & Candra Kirana walk together"),
    ("Transition to Act 3 — ceremony", "Transition to Act 3 — wedding ceremony"),
    ("Wedding ceremony wide", "Wedding ceremony Panji-Candra Kirana wide"),
    ("Hands over fire", "Panji & Candra Kirana hands over fire"),
    ("Mpu Dharmaja reads Smaradahana part 1", "Mpu Dharmaja reads Smaradahana — Panji as Kamajaya"),
    ("Smaradahana part 2 — Kirana described",
     "Smaradahana part 2 — Candra Kirana as Kamaratih"),
    ("Fire climax", "Smaradahana fire climax"),
    ("Intimate climax", "Panji & Candra Kirana intimate climax"),
    ("Overlooking kingdom", "Panji & Candra Kirana overlooking unified kingdom"),
    ("Mpu writes history", "Mpu Dharmaja writes Smaradahana manuscript"),
    ("Final establishing", "Final establishing shot — unified kingdoms"),
    ("Relief = legacy", "Relief of Panji story on candi wall"),
    ("Manuscript = eternal", "Smaradahana lontar — eternal legacy"),
    ("Title card — end of pilot", "Title card — end of pilot"),
]

# Mapping lokasi
LOKASI_REPLACEMENTS = [
    # Scene 1 was at "Keraton Kediri" - sekarang harus Jenggala karena Panji pangeran Jenggala
    # Tapi keraton Kediri muncul di scene Candra Kirana departure - tidak ada di pilot ini
    # L001 deskripsi: "Interior istana batu, pilar candi, atap ijuk, obor, bendera merah-emas"
    # → harus biru-emas karena Jenggala
    ("bendera merah-emas", "bendera biru-emas"),
]

# Mapping character list
CHARACTER_LIST_UPDATE = [
    # C001
    ("Sri Kameswara", "Panji Asmara Bangun"),
    ("Raja Kediri", "Pangeran Mahkota Jenggala"),
    ("Pria Jawa 28 tahun, kulit cokelat keemasan, mata tajam, rambut hitam panjang, mahkota emas Jawa Kuno, kain batik merah tua-emas, keris pusaka",
     "Pria Jawa 28 tahun, kulit cokelat keemasan, mata tajam, rambut hitam panjang, destar emas Jawa Kuno, kain batik biru tua-emas, keris pusaka"),
    # C002
    ("Sri Kirana", "Candra Kirana"),
    ("Putri Jenggala", "Putri Mahkota Kediri"),
    ("Wanita Jawa 22 tahun, kulit kuning langsat, mata besar ekspresif, rambut panjang dengan melati, kemben emas-brocade, kain biru-emas",
     "Wanita Jawa 22 tahun, kulit kuning langsat, mata besar ekspresif, rambut panjang dengan melati, kemben emas-brocade, kain merah-emas"),
    # C003
    ("Patih Kediri", "Patih Jenggala"),
    ("Penasihat militer", "Penasihat militer pangeran Panji"),
    # Voice tidak berubah, kecuali C001 dan C002 swap voice karena sekarang C001 = Panji (Ardi), C002 = Candra Kirana (Sari)
    # Sebelumnya C001 = Kameswara (Ardi), C002 = Sri Kirana (Sari) — tetap sama mapping
]

# Lokasi L001: ganti "Keraton Kediri (Dahanapura)" → "Keraton Jenggala (Kahuripan)"
LOKASI_LIST_UPDATE = [
    ("Keraton Kediri (Dahanapura)", "Keraton Jenggala (Kahuripan)"),
    ("Interior istana batu, pilar candi, atap ijuk, obor, bendera merah-emas",
     "Interior istana batu, pilar candi, atap ijuk, obor, bendera biru-emas (Jenggala)"),
]


def apply_replacements(data):
    """Rekursif ganti semua string sesuai mapping."""
    if isinstance(data, dict):
        return {k: apply_replacements(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [apply_replacements(item) for item in data]
    elif isinstance(data, str):
        result = data
        # Apply all replacement maps
        for old, new in CHARACTER_LIST_UPDATE:
            result = result.replace(old, new)
        for old, new in LOKASI_LIST_UPDATE:
            result = result.replace(old, new)
        for old, new in PROMPT_REPLACEMENTS:
            result = result.replace(old, new)
        for old, new in DIALOG_REPLACEMENTS:
            result = result.replace(old, new)
        for old, new in NOTES_REPLACEMENTS:
            result = result.replace(old, new)
        return result
    else:
        return data


def main():
    print(f"Membaca: {STORYBOARD_PATH}")
    with open(STORYBOARD_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Apply replacements
    new_data = apply_replacements(data)

    # Backup original
    backup_path = STORYBOARD_PATH.with_suffix(".json.bak")
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Backup: {backup_path}")

    # Write corrected
    with open(STORYBOARD_PATH, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
    print(f"Tulis: {STORYBOARD_PATH}")

    # Verifikasi: hitung sisa referensi lama
    with open(STORYBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    old_terms = ["Kameswara", "Sri Kirana", "Patih Kediri",
                 "Putri Jenggala", "merah tua-emas, keris", "merah-emas, keris"]
    print("\nVerifikasi sisa referensi lama:")
    for term in old_terms:
        count = content.count(term)
        if count > 0:
            print(f"  ⚠️  '{term}': {count} sisa")
        else:
            print(f"  ✅ '{term}': bersih")

    # Verifikasi: pastikan nama baru muncul
    new_terms = ["Panji Asmara Bangun", "Candra Kirana", "Patih Jenggala",
                 "Pangeran Mahkota Jenggala", "Putri Mahkota Kediri",
                 "Keraton Jenggala (Kahuripan)"]
    print("\nVerifikasi nama baru:")
    for term in new_terms:
        count = content.count(term)
        print(f"  → '{term}': {count} kemunculan")


if __name__ == "__main__":
    main()
