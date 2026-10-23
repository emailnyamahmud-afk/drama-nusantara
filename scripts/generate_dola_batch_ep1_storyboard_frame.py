#!/usr/bin/env python3
"""
Generate 17 storyboard frame prompts untuk EP1 Jaka Tingkir + batch JSON.

Pola:
- Phase 1: master ref (12 image sudah jadi di Flow/Dola)
- Phase 2: storyboard frame (17 image baru, dengan ref input dari Phase 1)

Setiap frame pakai visual spec dari naskah + reference master ref IDs untuk konsistensi karakter.
"""
import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
NASKAH_PATH = ROOT / "produksi/pra-produksi/jaka-tingkir-series/EP1-NASKAH.md"
MASTER_REF_DIR = ROOT / "produksi/t2i-output/jaka-tingkir-ep1/master-ref"
OUT_JSON = ROOT / "produksi/pra-produksi/jaka-tingkir-series/dola-batch-EP1-storyboard-frame.json"


# ============================================================
# Mapping master ref IDs untuk konsistensi karakter
# ============================================================
MASTER_REF_MAP = {
    # Karakter (dari Phase 1 yang sudah jadi)
    "Raden Patah": "EP1-C001-3B-K007-raden-patah",
    "Raden Yunus": "EP1-C002-3B-K008-raden-yunus",
    "Raden Suryawiyata": "EP1-C003-3B-K009-raden-suryawiyata",
    "Sunan Kudus": "EP1-C004-3B-K010-sunan-kudus",
    "Sunan Giri Dalem": "EP1-C005-3B-K011-sunan-giri-dalem",
    "Hang Tuah": "EP1-C006-3B-K012-hang-tuah",
    "Prajurit Demak": "EP1-C007-3B-K013-prajurit-demak",
    "Prajurit Portugis": "EP1-C008-3B-K014-prajurit-portugis",
    # Artefak
    "Keris Naga Sasra": "EP1-P001-3B-A004-keris-kyai-naga-sasra",
    "Singgasana Demak": "EP1-P002-3B-A005-singgasana-demak",
    "Mahkota Sultan": "EP1-P003-3B-A006-mahkota-sultan-demak",
    "Bendera Surya Majapahit": "EP1-P004-3B-A007-bendera-surya-majapahit",
    # Reuse dari era 3B/3A (sudah ada, lokasi pathnya standar)
    "Pangeran Trenggana": "3B-K001-sultan-trenggana",  # reuse
    "Sunan Kalijaga": "3A-K003-sunan-kalijaga",  # reuse
    "Demak Lokasi": "3B-L001-demak",  # reuse
    "Malaka Lokasi": "3A-L002-malaka",  # reuse
    "Pendapa Demak": "3B-S001-pendapa-demak",  # reuse
}


# ============================================================
# 17 Storyboard Frame Prompts — diambil dari naskah EP1
# ============================================================
storyboard_frames = [
    # SCENE 1 — Pembuka: Demak Berdiri (1478 M)
    {
        "segment_id": "EP1-S001-SEG01",
        "scene_id": "EP1-S001",
        "scene_title": "Pembuka: Demak Berdiri (1478 M)",
        "segment_notes": "Aerial Demak Bintara, masjid agung atap tumpang tiga",
        "duration_seconds": 20,
        "linked_asset_ids": ["Demak Lokasi"],
        "linked_assets_role": ["location_context"],
        "prompt": "Cinematic realistic wide aerial establishing shot of Demak Bintara Sultanate in 1478 AD, pesisir utara Pulau Jawa at sunset. The great Demak Grand Mosque with three-tiered pyramidal roof (atap tumpang tiga) made of dark teak wood, towering above surrounding wooden pendapa pavilions with carved pillars. Islamic green banners with golden crescent fluttering in evening wind. The mosque's silhouette against orange-pink sunset sky. Crowded harbor with jong ships (Javanese trading vessels) moored at the docks. Distant mountain ranges in the background. Warm golden hour lighting, high detail, 24mm wide-angle lens, 16:9 horizontal, 8K, photorealistic.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Demak Bintara berdiri 1478 M, Raden Patah naik tahta"
    },
    {
        "segment_id": "EP1-S001-SEG02",
        "scene_id": "EP1-S001",
        "scene_title": "Pembuka: Demak Berdiri (1478 M)",
        "segment_notes": "Raden Patah di singgasana + 4 putra di belakang",
        "duration_seconds": 35,
        "linked_asset_ids": ["Raden Patah", "Singgasana Demak"],
        "linked_assets_role": ["character_consistency", "prop_detail"],
        "prompt": "Cinematic realistic wide shot inside the great pendapa of Demak Bintara, evening with warm torch lighting. Old Sultan Raden Patah (late 60s, long white beard, yellow silk royal robe with golden embroidery, white turban with golden crescent pin) sitting on the carved teak wood throne (singgasana) with mother-of-pearl inlay. Four young princes standing behind the throne: Raden Yunus (eldest, ambitious, green turban, navy silk kebaya), Raden Suryawiyata (second, white robe, plain turban), Pangeran Trenggana (third, calm, dark green robe), and a young princess. Warm golden torch glow, deep shadows, ceremonial atmosphere, 35mm lens, 16:9 horizontal, 8K, photorealistic, Javanese Islamic royal court 15th century.",
        "ken_burns": "pan_right_slow",
        "audio_summary": "Raden Patah dialog (krama inggil) + narrator 4 putra"
    },
    {
        "segment_id": "EP1-S001-SEG03",
        "scene_id": "EP1-S001",
        "scene_title": "Pembuka: Demak Berdiri (1478 M)",
        "segment_notes": "Sunan Kalijaga vs Sunan Kudus, kontras wali",
        "duration_seconds": 35,
        "linked_asset_ids": ["Sunan Kudus"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic two-shot in the great pendapa, dramatic chiaroscuro lighting. On the left: Sunan Kalijaga (in shadow, wearing flowing dark black robe, turban black, mysterious serene smile, barely visible face in shadow). On the right: Sunan Kudus (clearly lit, wearing pure white robe, white turban, stern face, holding silver prayer beads tasbih). Contrast between shadow and light, mysterious versus orthodox. Deep wooden pendapa background with Islamic geometric carvings. Torch light from left, 50mm lens, shallow depth of field, 16:9 horizontal, 8K, photorealistic.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: dua kekuatan Putihan vs Abangan masih bersatu"
    },
    # SCENE 2 — Empat Putra Raden Patah (1480-an)
    {
        "segment_id": "EP1-S002-SEG01",
        "scene_id": "EP1-S002",
        "scene_title": "Empat Putra Raden Patah (1480-an)",
        "segment_notes": "Raden Yunus latihan pedang + Suryawiyata belajar keris",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Yunus", "Raden Suryawiyata", "Keris Naga Sasra"],
        "linked_assets_role": ["character_consistency", "character_consistency", "prop_detail"],
        "prompt": "Cinematic realistic split-scene composition showing two parallel moments. LEFT HALF: Young Raden Yunus (early 20s, athletic, ambitious, green turban, navy silk kebaya) practicing sword fighting on horseback in the royal courtyard of Demak, looking toward the distant sea. RIGHT HALF: Young Raden Suryawiyata (early 20s, sharp, plain white robe, white turban) studying keris at Pesantren Kudus, examining a wavy-bladed kris (keris Kyai Naga Sasra) in candlelight. Visual contrast: naval ambition versus religious study. Warm afternoon light left, candlelight right, 35mm lens, 16:9 horizontal, 8K, photorealistic.",
        "ken_burns": "pan_right_slow",
        "audio_summary": "Narrator: Yunus ambisius laut, Suryawiyata belajar keris di Kudus"
    },
    {
        "segment_id": "EP1-S002-SEG02",
        "scene_id": "EP1-S002",
        "scene_title": "Empat Putra Raden Patah (1480-an)",
        "segment_notes": "Pangeran Trenggana + Raden Getas Pandhawa",
        "duration_seconds": 30,
        "linked_asset_ids": ["Pangeran Trenggana"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic medium shot inside a Javanese pendapa, afternoon light filtering through wooden lattice. Young Pangeran Trenggana (early 20s, calm and wise, dark green robe, holding an ancient lontar palm-leaf manuscript) discussing with an older guru Raden Getas Pandhawa (50s, grey beard, brown robe). They sit on woven mat reading lontar together. Carved teak pillars, batik cloth hanging, low teak table with tea. Soft warm afternoon light, shallow depth of field, 50mm lens, 16:9 horizontal, 8K, photorealistic, 15th century Javanese noble education scene.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Trenggana berguru Raden Getas Pandhawa, cucu Sunan Kalijaga"
    },
    {
        "segment_id": "EP1-S002-SEG03",
        "scene_id": "EP1-S002",
        "scene_title": "Empat Putra Raden Patah (1480-an)",
        "segment_notes": "Visual simbolik dua lilin + siluet Demak malam",
        "duration_seconds": 30,
        "linked_asset_ids": ["Demak Lokasi"],
        "linked_assets_role": ["location_context"],
        "prompt": "Cinematic symbolic shot of two candles on a dark teak altar — one white candle (representing Putihan), one black candle (representing Abangan). Their flames flicker in opposite directions, symbolic of opposing spiritual forces. Background: silhouette of Demak Bintara at night with the great mosque silhouette against deep blue night sky with crescent moon. Dramatic dark moody atmosphere, single candle light source, 85mm lens, shallow depth of field, 16:9 horizontal, 8K, photorealistic symbolic composition.",
        "ken_burns": "zoom_out_slow",
        "audio_summary": "Narrator: dua aliran Putihan vs Abangan dipendam, akan meledak saat Sultan wafat"
    },
    # SCENE 3 — Malaka Jatuh (1511 M)
    {
        "segment_id": "EP1-S003-SEG01",
        "scene_id": "EP1-S003",
        "scene_title": "Malaka Jatuh (1511 M)",
        "segment_notes": "Aerial Malaka damai + armada Portugis mendekat",
        "duration_seconds": 30,
        "linked_asset_ids": ["Malaka Lokasi"],
        "linked_assets_role": ["location_context"],
        "prompt": "Cinematic realistic aerial establishing shot of Malaka port in 1511 AD, busy trading port with Islamic merchant ships (jong, lanchara) at harbor, bustling market with merchants. Suddenly European galleons with white sails and red-cross flags appear on the horizon, approaching. Plumes of cannon smoke rising. Mix of peaceful Islamic harbor and incoming European threat. Wide panoramic view, golden afternoon light, distant cannons firing, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, 16th century Malacca historical scene.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: 1511 M, Malaka jatuh ke Portugis, Alfonso d'Albuquerque"
    },
    {
        "segment_id": "EP1-S003-SEG02",
        "scene_id": "EP1-S003",
        "scene_title": "Malaka Jatuh (1511 M)",
        "segment_notes": "Hang Tuah gugur di geladak + Malaka terbakar",
        "duration_seconds": 30,
        "linked_asset_ids": ["Hang Tuah"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic close-up of legendary Laksamana Hang Tuah (50s, weather-beaten face, black beard with gray, red silk baju with gold embroidery, keris Taming Sari still gripped in hand) lying mortally wounded on the deck of a Malaccan ship. Blood on his chest, peaceful expression in death, eyes closed. Background: Malaka port in flames, smoke billowing, Portuguese ships approaching. Dramatic backlight from burning city, somber heroic mood, 85mm lens, shallow depth of field, 16:9 horizontal, 8K, photorealistic, tragic death of Malay hero 1511.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Hang Tuah gugur, Malaka jatuh"
    },
    {
        "segment_id": "EP1-S003-SEG03",
        "scene_id": "EP1-S003",
        "scene_title": "Malaka Jatuh (1511 M)",
        "segment_notes": "Map animasi Eropa→Constantinopel→Malaka",
        "duration_seconds": 30,
        "linked_asset_ids": [],
        "linked_assets_role": [],
        "prompt": "Cinematic realistic antique map of the world (16th century style, parchment with ink and gold leaf) showing the trade route from Europe through Constantinople (with Turkish crescent flag), around Cape of Good Hope (South Africa), to Malacca (with red cross flag). Hand-drawn compass rose, sailing ship illustrations, decorative Arabic and Latin text. Soft candlelight illumination from upper left, parchment texture visible, 50mm macro lens, f/8 deep depth of field, 16:9 horizontal, 8K, photorealistic, 16th century cartographic style.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Reconquista, Constantinopel jatuh 1453, Eropa cari jalur baru"
    },
    {
        "segment_id": "EP1-S003-SEG04",
        "scene_id": "EP1-S003",
        "scene_title": "Malaka Jatuh (1511 M)",
        "segment_notes": "Raden Patah murka terima kabar",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Patah"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic close-up of old Sultan Raden Patah (now very old, deep wrinkles, long white beard, yellow royal robe, white turban) receiving a scroll from a courier in the pendapa of Demak. His face transforms from calm to anger as he reads the news of Malaka's fall. Holding the scroll tightly in his weathered hand. Torch light casting dramatic shadows on his face, intense emotion, 85mm lens, shallow depth of field, 16:9 horizontal, 8K, photorealistic, 1511 AD historical moment.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: kabar sampai Demak, Raden Patah murka"
    },
    # SCENE 4 — Raden Yunus Serang Malaka (1512 M)
    {
        "segment_id": "EP1-S004-SEG01",
        "scene_id": "EP1-S004",
        "scene_title": "Raden Yunus Serang Malaka (1512 M)",
        "segment_notes": "Armada besar Demak berlayar",
        "duration_seconds": 30,
        "linked_asset_ids": ["Bendera Surya Majapahit"],
        "linked_assets_role": ["prop_detail"],
        "prompt": "Cinematic realistic wide aerial shot of massive Demak naval armada departing from Demak harbor in 1512 AD. Hundreds of Javanese jong warships with three sails each, decorated with crimson Surya Majapahit sun banners and Islamic green banners with golden crescent. Cannons on decks, soldiers in armor on decks. Sea waves, dramatic cloudy sky. Leading ship at front with Raden Yunus standing at the bow. Epic heroic departure, golden hour, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, 16th century Javanese naval campaign.",
        "ken_burns": "pan_right_slow",
        "audio_summary": "Narrator: Raden Patah utus Yunus, ribuan kapal ke Malaka"
    },
    {
        "segment_id": "EP1-S004-SEG02",
        "scene_id": "EP1-S004",
        "scene_title": "Raden Yunus Serang Malaka (1512 M)",
        "segment_notes": "Raden Yunus heroik di haluan kapal",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Yunus"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic low-angle heroic shot of Raden Yunus (early 30s, athletic, ambitious, green turban, navy silk kebaya with golden wave embroidery, kris at waist) standing at the bow of the lead Demak jong warship, raising his kris high to rally the troops. Behind him, hundreds of Demak soldiers cheering with spears raised. Sea spray, dramatic clouds, Surya Majapahit banner flying. Epic heroic mood, low angle from below, golden hour, 35mm lens, 16:9 horizontal, 8K, photorealistic, 16th century naval battle preparation.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Raden Yunus dialog (krama inggil) panggil prajurit Demak"
    },
    {
        "segment_id": "EP1-S004-SEG03",
        "scene_id": "EP1-S004",
        "scene_title": "Raden Yunus Serang Malaka (1512 M)",
        "segment_notes": "Pertempuran laut sengit",
        "duration_seconds": 40,
        "linked_asset_ids": ["Prajurit Demak", "Prajurit Portugis"],
        "linked_assets_role": ["character_consistency", "character_consistency"],
        "prompt": "Cinematic realistic chaotic naval battle scene between Demak and Portuguese fleets in 1512. Demak soldiers in dark brown leather armor with red headwraps boarding a Portuguese galleon. Portuguese soldiers in steel half-armor fighting back with matchlock muskets and swords. Cannon fire, smoke, splintered wood, screaming soldiers, blood on deck. Flames from burning ships in background. Fast dynamic composition, motion blur, dramatic chaos, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, intense 16th century naval combat.",
        "ken_burns": "zoom_in_fast",
        "audio_summary": "Narrator: pertempuran pecah, Portugis kewalalah, Demak berhasil beberapa wilayah"
    },
    {
        "segment_id": "EP1-S004-SEG04",
        "scene_id": "EP1-S004",
        "scene_title": "Raden Yunus Serang Malaka (1512 M)",
        "segment_notes": "Pasukan Malaka diam tak membantu",
        "duration_seconds": 30,
        "linked_asset_ids": ["Prajurit Demak"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic dramatic split composition showing the betrayal. FOREGROUND: Demak soldiers fighting desperately on a beach, exhausted and wounded, bloodied. BACKGROUND: Malaccan local troops standing idle on a hillside, arms crossed, watching coldly without helping. Visual contrast between Demak's desperate struggle and Malacca's cold inaction. Gloomy overcast sky, blood-stained sand, somber atmosphere, 35mm lens, 16:9 horizontal, 8K, photorealistic, 1512 naval battle betrayal scene.",
        "ken_burns": "zoom_out_slow",
        "audio_summary": "Narrator: Malaka diam, takut Demak jadi Majapahit baru"
    },
    {
        "segment_id": "EP1-S004-SEG05",
        "scene_id": "EP1-S004",
        "scene_title": "Raden Yunus Serang Malaka (1512 M)",
        "segment_notes": "Armada Demak hancur pulang",
        "duration_seconds": 20,
        "linked_asset_ids": ["Raden Yunus"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic melancholic aerial shot of defeated Demak fleet returning to Java. Battered ships with broken masts, torn sails, tattered Surya Majapahit banners hanging limp. Raden Yunus standing alone at the bow of the lead ship, head bowed in shame and anger. Gloomy gray sky, calm sea, somber mood of defeat. Wide establishing shot, slow motion feel, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, aftermath of defeat 1512.",
        "ken_burns": "zoom_out_slow",
        "audio_summary": "Narrator: Demak kalah telak, armada pulang dengan malu + dendam"
    },
    # SCENE 5 — Raden Patah Wafat (1518 M)
    {
        "segment_id": "EP1-S005-SEG01",
        "scene_id": "EP1-S005",
        "scene_title": "Raden Patah Wafat (1518 M)",
        "segment_notes": "Raden Patah terbaring, putra di sekitar",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Patah", "Singgasana Demak"],
        "linked_assets_role": ["character_consistency", "prop_detail"],
        "prompt": "Cinematic realistic somber scene inside a Javanese royal bedchamber at night, 1518 AD. Old Sultan Raden Patah (now very aged, long white beard, pale yellow royal robe) lying on a carved teak bed, eyes closed in death. Four sons standing around the bed mourning: Raden Yunus, Raden Suryawiyata, Pangeran Trenggana, and a princess. Sunan Kudus (white robe, white turban) reading Islamic prayers. Torches flickering, soft warm light, deep shadows, somber mood of mourning, 35mm lens, 16:9 horizontal, 8K, photorealistic, death of a sultan historical scene.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: 1518 M, Raden Patah wafat"
    },
    {
        "segment_id": "EP1-S005-SEG02",
        "scene_id": "EP1-S005",
        "scene_title": "Raden Patah Wafat (1518 M)",
        "segment_notes": "Raden Yunus di singgasana, ekspresi keras",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Yunus", "Singgasana Demak", "Mahkota Sultan"],
        "linked_assets_role": ["character_consistency", "prop_detail", "prop_detail"],
        "prompt": "Cinematic realistic coronation scene — Raden Yunus (early 30s, now Sultan II, green turban with golden pin, navy silk kebaya with golden wave embroidery) sitting on the carved teak throne of Demak, wearing the golden mahkota crown with emerald and rubies. His face shows ambitious power but also hardness and aggression. Beside him, the royal keris Kyai Naga Sasra at his waist. In the background, nobles bowing. Cold ambitious atmosphere, mixed lighting (torch + daylight from window), 50mm lens, 16:9 horizontal, 8K, photorealistic, 1518 coronation of Sultan II.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Yunus Sultan II, politik garis keras"
    },
    {
        "segment_id": "EP1-S005-SEG03",
        "scene_id": "EP1-S005",
        "scene_title": "Raden Patah Wafat (1518 M)",
        "segment_notes": "Siluet pembunuhan Yunus, kilat keris",
        "duration_seconds": 30,
        "linked_asset_ids": ["Raden Yunus", "Keris Naga Sasra"],
        "linked_assets_role": ["character_consistency", "prop_detail"],
        "prompt": "Cinematic realistic dramatic silhouette shot in a dark chamber at night, 1521 AD. Raden Yunus standing in shadow, suddenly a dark assassin figure appears behind him. Flash of keris blade (keris Kyai Naga Sasra with dragon motif) catching moonlight from window. Yunus collapsing forward. Dramatic high contrast lighting, mostly dark with moonlight from window, silhouette composition, 85mm lens, 16:9 horizontal, 8K, photorealistic, 16th century assassination scene.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: 1521 M, Yunus terbunuh, dendam Majapahit"
    },
    # SCENE 6 — Kematian Raden Yunus (Detail)
    {
        "segment_id": "EP1-S006-SEG01",
        "scene_id": "EP1-S006",
        "scene_title": "Kematian Raden Yunus (Detail)",
        "segment_notes": "Split-screen 3 versi kematian",
        "duration_seconds": 30,
        "linked_asset_ids": ["Keris Naga Sasra"],
        "linked_assets_role": ["prop_detail"],
        "prompt": "Cinematic realistic triptych (three-panel split-screen) composition showing three versions of Raden Yunus's death. LEFT PANEL: Keris Kyai Naga Sasra with dragon motif, blade gleaming ominously, with text label 'TRADISI' below. CENTER PANEL: A pair of diseased lungs, anatomical medical illustration style, with text 'KRONIK TIONGHOA' below. RIGHT PANEL: Silhouette of a keris blade piercing through shadow, with text 'BERITA PORTUGIS' below. Each panel with different lighting (red for keris, blue for lungs, gray for silhouette), separated by black dividers, 35mm lens, 16:9 horizontal, 8K, photorealistic mixed media composition.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: 3 versi kematian Yunus (keris Naga Sasra / paru-paru / keris Portugis)"
    },
    {
        "segment_id": "EP1-S006-SEG02",
        "scene_id": "EP1-S006",
        "scene_title": "Kematian Raden Yunus (Detail)",
        "segment_notes": "Tahta kosong + mahkota di bantal",
        "duration_seconds": 30,
        "linked_asset_ids": ["Singgasana Demak", "Mahkota Sultan"],
        "linked_assets_role": ["prop_detail", "prop_detail"],
        "prompt": "Cinematic realistic symbolic shot of an empty throne room in Demak Bintara, 1521 AD. The carved teak throne sits empty, with the golden mahkota crown placed on a red velvet cushion on the seat. Sunrise light streaming through the windows behind the throne, casting long shadows. The room is silent, vacant, no people. Symbolic of the power vacuum. Dramatic morning light, dust motes visible in light beams, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, symbolic scene of succession crisis.",
        "ken_burns": "zoom_out_slow",
        "audio_summary": "Narrator: Yunus wafat tanpa putra, Dewan Wali Sangha harus pilih pengganti"
    },
    {
        "segment_id": "EP1-S006-SEG03",
        "scene_id": "EP1-S006",
        "scene_title": "Kematian Raden Yunus (Detail)",
        "segment_notes": "Rapat Dewan Wali Sangha, dua kubu terpisah",
        "duration_seconds": 30,
        "linked_asset_ids": ["Sunan Giri Dalem"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic wide shot inside the great mosque of Demak, the Dewan Wali Sangha (Council of Saints) convening. Sunan Giri Dalem (late 50s, green silk robe, green turban with golden crescent, white beard) sitting in the center as the presiding leader, his face heavy with burden. The council members are split into two opposing groups: LEFT side wearing white robes (Putihan faction supporting Suryawiyata), RIGHT side wearing colored robes (Abangan faction supporting Trenggana). Tense atmosphere, geometric Islamic patterns on wooden walls, soft light filtering through carved window screens, 35mm lens, 16:9 horizontal, 8K, photorealistic, 1521 succession dispute scene.",
        "ken_burns": "pan_right_slow",
        "audio_summary": "Narrator: Dewan Wali Sangha pecah, Suryawiyata vs Trenggana"
    },
    {
        "segment_id": "EP1-S006-SEG04",
        "scene_id": "EP1-S006",
        "scene_title": "Kematian Raden Yunus (Detail)",
        "segment_notes": "Sunan Kalijaga vs Sunan Kudus berhadap-hadapan",
        "duration_seconds": 30,
        "linked_asset_ids": ["Sunan Kudus"],
        "linked_assets_role": ["character_consistency"],
        "prompt": "Cinematic realistic two-shot of the two most senior living wali sitting face to face in a private chamber. LEFT: Sunan Kalijaga (in shadow, dark black robe, black turban, mysterious serene smile, face partially obscured). RIGHT: Sunan Kudus (clearly lit, pure white robe, white turban, stern face, holding silver prayer beads). Between them on a low table: a copy of the Quran and a keris. Visual contrast of two opposing spiritual forces, dramatic chiaroscuro lighting, 50mm lens, shallow depth of field, 16:9 horizontal, 8K, photorealistic, intense dialogue of spiritual rivals.",
        "ken_burns": "zoom_in_slow",
        "audio_summary": "Narrator: Sunan Kalijaga + Sunan Kudus, dua wali paling disegani"
    },
    # SCENE 7 — Cliffhanger: Dua Kubu (Closing)
    {
        "segment_id": "EP1-S007-SEG01",
        "scene_id": "EP1-S007",
        "scene_title": "Cliffhanger: Dua Kubu (Closing)",
        "segment_notes": "Split-screen Trenggana+Kalijaga vs Suryawiyata+Kudus",
        "duration_seconds": 30,
        "linked_asset_ids": ["Pangeran Trenggana", "Sunan Kudus"],
        "linked_assets_role": ["character_consistency", "character_consistency"],
        "prompt": "Cinematic realistic split-screen composition showing the two rival factions. LEFT HALF: Pangeran Trenggana (early 30s, calm, dark green robe) sitting with Sunan Kalijaga (black robe, in shadow) in a pendapa, discussing strategy, warm afternoon light. RIGHT HALF: Raden Suryawiyata (early 30s, sharp, white robe, plain turban) receiving instruction from Sunan Kudus (white robe, white turban, stern) at Pesantren Kudus, candlelight. Visual contrast: warm vs cold, shadow vs light, Abangan vs Putihan. 35mm lens, 16:9 horizontal, 8K, photorealistic, intense political rivalry setup.",
        "ken_burns": "cross_fade",
        "audio_summary": "Narrator: Trenggana pro Abangan, Suryawiyata pro Putihan"
    },
    {
        "segment_id": "EP1-S007-SEG02",
        "scene_id": "EP1-S007",
        "scene_title": "Cliffhanger: Dua Kubu (Closing)",
        "segment_notes": "Siluet Demak malam + pan ke Pengging misterius",
        "duration_seconds": 30,
        "linked_asset_ids": ["Demak Lokasi"],
        "linked_assets_role": ["location_context"],
        "prompt": "Cinematic realistic wide aerial silhouette shot of Demak Bintara at night, the great mosque silhouette against deep blue night sky with crescent moon and stars. The camera slowly pans south toward distant mountains shrouded in mist — toward Pengging, a mysterious unknown land where a young man named Mas Karebet waits. Dark moody atmosphere, distant mountain silhouettes, mist rolling, ominous drone mood, 24mm wide lens, 16:9 horizontal, 8K, photorealistic, dramatic cliffhanger setup shot.",
        "ken_burns": "pan_right_slow",
        "audio_summary": "Narrator: persaingan meruncing, Mas Karebet di Pajang menunggu (cliffhanger EP2)"
    },
]


# ============================================================
# Build storyboard frame jobs (Phase 2 with ref input)
# ============================================================
jobs = []
for i, frame in enumerate(storyboard_frames, 1):
    # Resolve linked_asset_ids to actual master ref image paths
    ref_inputs = []
    for aid, role in zip(frame["linked_asset_ids"], frame["linked_assets_role"]):
        # Determine master ref file
        if aid in MASTER_REF_MAP:
            ref_id = MASTER_REF_MAP[aid]
            # Check if it's a new EP1 master ref (sudah ada di t2i-output) atau reuse existing
            if ref_id.startswith("EP1-"):
                ref_path = f"produksi/t2i-output/jaka-tingkir-ep1/master-ref/{ref_id}.jpg"
            else:
                # Reuse from existing era (3A/3B) — path asumsi
                ref_path = f"produksi/t2i-output/master-reff/{ref_id}.jpg"
            
            ref_inputs.append({
                "asset_id": aid,
                "asset_name": aid,
                "ref_image_path": ref_path,
                "role": role
            })
    
    job = {
        "job_id": f"frame-{frame['segment_id']}",
        "phase": "storyboard_frame",
        "segment_id": frame["segment_id"],
        "scene_id": frame["scene_id"],
        "scene_title": frame["scene_title"],
        "segment_notes": frame["segment_notes"],
        "duration_seconds": frame["duration_seconds"],
        "prompt": frame["prompt"],
        "motion_prompt": "",  # placeholder — not used in T2I, only for future I2V
        "model": "seedream-4.5",  # or nano-banana-2-lite for Google Flow
        "aspect_ratio": "16:9",
        "include_inspiration": True,
        "ref_image_inputs": ref_inputs,
        "depends_on": [r["asset_id"] for r in ref_inputs],
        "output_path": f"produksi/t2i-output/jaka-tingkir-ep1/storyboard-frame/{frame['segment_id']}.jpg",
        "ken_burns": frame["ken_burns"],
        "audio_summary": frame["audio_summary"],
        "notes": f"Storyboard frame {i}/17 — {frame['segment_notes']}"
    }
    jobs.append(job)


# ============================================================
# Compile batch JSON (Phase 2 with dependency on Phase 1)
# ============================================================
batch = {
    "schema_version": "1.0",
    "project": {
        "id": "JT-S1-EP1-STORYBOARD-FRAME",
        "title": "Jaka Tingkir EP1 — Storyboard Frame Batch (Phase 2)",
        "era": "3B Demak-Pajang (1499-1550 M)",
        "type": "storyboard_frame_batch",
        "episode": "EP1: Demak Berdiri, Malaka Jatuh",
        "duration_target_seconds": 720,
        "resolution": "1920x1080",
        "fps": 24,
        "style": "cinematic realistic, Javanese period drama, dark-fantasy tones",
        "date_created": "2026-10-23"
    },
    "instructions_for_agent": {
        "purpose": "Generate 17 storyboard frame images untuk EP1 Jaka Tingkir Series. Phase 2 — dengan ref input dari Phase 1 master ref yang sudah jadi.",
        "phase_2_storyboard_frame": {
            "description": "Generate 17 storyboard frames. Setiap frame pakai ref image dari Phase 1 master ref untuk konsistensi karakter/lokasi.",
            "count": len(jobs),
            "input": "text prompt + ref images (karakter_consistency + location_context + prop_detail)",
            "output": "save each image to output_path",
            "ref_image_rule": "Karakter utama = upload ref image (character_consistency). Lokasi = upload ref image (location_context). Prop = upload ref image (prop_detail). Boleh multiple ref per frame.",
            "aspect_ratio": "16:9 (1920x1080) untuk semua frame",
            "model_hint": "seedream-4.5 (Dola) atau nano-banana-2-lite (Google Flow)"
        },
        "execution_order": "single_phase_parallel_with_ref",
        "output_organization": {
            "storyboard_frame": "produksi/t2i-output/jaka-tingkir-ep1/storyboard-frame/"
        },
        "depends_on": "phase_1_master_ref (sudah jadi di produksi/t2i-output/jaka-tingkir-ep1/master-ref/)",
        "qc_check": {
            "aspect_ratio_check": "All 17 frame harus 16:9 (1920x1080)",
            "character_consistency": "Karakter di frame harus match dengan master ref (mis. Raden Patah sama di segmen 1.2, 3.4, 5.1, 5.3, 6.1)",
            "visual_continuity": "Story flow dari segmen 1 ke 17 harus koheren"
        }
    },
    "phases": [{
        "phase_id": "phase_2_storyboard_frame",
        "name": "Generate Storyboard Frame Images untuk EP1",
        "parallel": True,
        "depends_on": "phase_1_master_ref",
        "jobs": jobs
    }],
    "total_jobs": len(jobs),
    "summary": {
        "total_frames": len(jobs),
        "total_duration_seconds": sum(j["duration_seconds"] for j in jobs),
        "frames_with_ref": sum(1 for j in jobs if j["ref_image_inputs"]),
        "frames_without_ref": sum(1 for j in jobs if not j["ref_image_inputs"]),
        "estimasi_dola_time": "10-15 menit untuk 17 frame dengan ref input",
        "estimasi_flow_time": "10-15 menit untuk 17 frame (Nano Banana 2 Lite)"
    }
}

# Write
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

size_kb = OUT_JSON.stat().st_size / 1024
print(f"✅ Written: {OUT_JSON}")
print(f"   Size: {size_kb:.1f} KB")
print(f"   Total jobs: {batch['total_jobs']}")
print()
print("=== 17 STORYBOARD FRAME JOBS ===")
print(f"{'Seg ID':20s} {'Dur':>4s} {'Refs':>5s} {'Ken Burns':20s}")
print("-" * 60)
for j in jobs:
    refs_count = len(j["ref_image_inputs"])
    print(f"{j['segment_id']:20s} {j['duration_seconds']:>3}s {refs_count:>4d} {j['ken_burns']:20s}")
print("-" * 60)
total_dur = sum(j["duration_seconds"] for j in jobs)
print(f"{'TOTAL':20s} {total_dur:>3}s    17 frames")
print()
print("=== DEPENDENCY MAP (asset → frames yang butuh) ===")
from collections import defaultdict
deps_map = defaultdict(list)
for j in jobs:
    for r in j["ref_image_inputs"]:
        deps_map[r["asset_id"]].append(j["segment_id"])

for aid, segs in sorted(deps_map.items()):
    print(f"  {aid:30s} → {', '.join(segs)}")
