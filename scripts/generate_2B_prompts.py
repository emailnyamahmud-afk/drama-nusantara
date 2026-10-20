#!/usr/bin/env python3
"""
Generate T2I prompts untuk era 2B Mataram Kuno & Sriwijaya.
Pola hibrida: karakter ref sheet (5 angle, clean background) + latar scene + istana eksterior + interior + artefak macro.
Semua 9:16.
"""

from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts/2B-mataram-sriwijaya/prompts")
BASE.mkdir(parents=True, exist_ok=True)

TEMPLATE_K = """Cinematic realistic character reference sheet of {name}, shown in 5 different angles arranged in a grid layout on a clean solid light cream studio background. Layout: top-left frontal face close-up, top-right full body front view, middle-left side face profile close-up, bottom-left side full body view {prop_phrase}, bottom-right back full body view. All 5 angles show the exact same character, same costume, same physical features, same identity. {details} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all 5 angles in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters (must be same character in all 5 angles), inconsistent costume between angles, {avoid}"""

TEMPLATE_L = """Cinematic realistic documentary landscape of {name}, {period}. {scene_details} No main character in foreground (landscape only, tiny silhouettes for scale acceptable).

Lighting: {lighting}

Mood: {mood}

Style: {style} Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: {avoid}"""

PROMPTS = {
    # KARAKTER (5 file)
    "2B-K001-dapunta-hyang.txt": ("K", {
        "name": "Dapunta Hyang Srijayanasa, King of Kedatuan Sriwijaya (Sumatra Selatan, abad 7 Masehi)",
        "prop_phrase": "holding a ceremonial golden scepter",
        "details": "Male, 35-50 years old, Sumatran phenotype with golden brown skin, sharp facial features, regal bearing, long black hair tied back with gold band, full beard. Wearing early Buddhist-Malay royal costume: gold makuta (crown) with lotus motifs, gold hara necklace with Buddha pendant, gold keyura armlets, rich red-gold songket kain, kris at waist. Gold sandals. Buddhist Mahayana influence mixed with local Sumatran tradition.",
        "mood": "Dapunta Hyang is the maritime king who unified wanua (port states) via siddhayatra (sacred journey), creating the thalassocracy of Sriwijaya.",
        "avoid": "modern clothing, modern jewelry, Indian Mughal costume, Chinese emperor costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2B-K002-balaputradewa.txt": ("K", {
        "name": "Balaputradewa, King of Kedatuan Sriwijaya at its peak (Sumatra Selatan, abad 9 Masehi)",
        "prop_phrase": "holding a palm leaf manuscript (lontar) with Sanskrit Buddhist text",
        "details": "Male, 40-55 years old, Sumatran phenotype with golden brown skin, wise regal bearing, long black hair with early greying tied in topknot with gold diadem, trimmed beard. Wearing Buddhist Mahayana royal costume: ornate gold makuta with stupa motif, gold hara necklace with Buddha amulet, gold keyura armlets, deep red-gold songket kain, kris at waist. Buddhist scholarly influence — patron of Nalanda monastery.",
        "mood": "Balaputradewa is the king at the peak of Sriwijaya power, who built Monastery I at Nalanda (India) for Sriwijayan students, diplomat who allied with Pala dynasty.",
        "avoid": "modern clothing, modern jewelry, Indian Mughal costume, Chinese emperor costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2B-K003-sanjaya.txt": ("K", {
        "name": "Sang Ratu Sanjaya, King of Mataram Kuno, founder of Wangsa Sanjaya (Jawa Tengah, 732 Masehi)",
        "prop_phrase": "holding a ceremonial golden lingga (Shiva symbol)",
        "details": "Male, 35-50 years old, Javanese phenotype with golden brown skin, sharp facial features, regal bearing, long black hair tied in topknot with gold diadem. Wearing early Hindu Siwa royal costume: gold makuta with trident motif, gold hara necklace with Shiva lingga pendant, gold keyura armlets, red-gold batik kain with parang pattern, kris pusaka at waist. Hindu Saiva — founder of Candi Gunung Wukir, establisher of lingga worship at Bukit Sthirengga.",
        "mood": "Sanjaya is the founder of Wangsa Sanjaya (Hindu Siwa), who established lingga at Gunung Wukir (732 M, Prasasti Canggal), marking the beginning of Mataram Kuno.",
        "avoid": "modern clothing, modern jewelry, Indian Mughal costume, Chinese emperor costume, Buddhist costume (must be Hindu Siwa), anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2B-K004-rakai-panangkaran.txt": ("K", {
        "name": "Rakai Panangkaran (Maharaja Dyah Pancapana Kariyana Panamkarana), King of Mataram Kuno from Wangsa Syailendra (Jawa Tengah, 746-784 Masehi)",
        "prop_phrase": "holding a golden stupa model",
        "details": "Male, 35-50 years old, Javanese phenotype with golden brown skin, regal bearing, long black hair tied in topknot with gold diadem. Wearing hybrid Hindu-Buddhist royal costume: gold makuta with lotus and stupa motifs, gold hara necklace with Tara pendant, gold keyura armlets, blue-gold batik kain. 'Mustika Keluarga Sailendra' — built Candi Kalasan (778 M) for Dewi Tara, 52 stupa. Buddhist Mahayana patron though from Sanjaya lineage.",
        "mood": "Rakai Panangkaran is the transitional king — from Sanjaya (Hindu) to Syailendra (Buddhist), who built Candi Kalasan for Dewi Tara and brought Buddhist scholars from Sri Lanka.",
        "avoid": "modern clothing, modern jewelry, Indian Mughal costume, Chinese emperor costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2B-K005-airlangga.txt": ("K", {
        "name": "Raja Airlangga, King of Mataram (Jawa Timur, 1019-1042 Masehi)",
        "prop_phrase": "holding a golden Garuda scepter (Garudamukha emblem)",
        "details": "Male, 30-45 years old, Balinese-Javanese phenotype with golden brown skin, weathered face from years of forest exile, sharp regal features, long black hair tied back with gold band, full beard. Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif, gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold batik kain, kris pusaka at waist. Garudamukha (Garuda = vehicle of Wisnu) as royal emblem. Cakravartin (ideal universal ruler).",
        "mood": "Airlangga is the king who rose from forest exile after Pralaya 1016 M (Wurawari attacked palace), rebuilt Mataram, built canals and ports, then divided the kingdom into Janggala and Pangjalu in 1042 M.",
        "avoid": "modern clothing, modern jewelry, Indian Mughal costume, Chinese emperor costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # LATAR — CANDI & SITUS (6 file)
    "2B-L001-palembang-sriwijaya.txt": ("L", {
        "name": "Palembang, capital of Kedatuan Sriwijaya",
        "period": "Sumatra Selatan, abad 7-11 Masehi",
        "scene_details": "Wide river Musi meeting Ogan, with bustling maritime port. Wooden stilt houses along riverbank, trading boats from India, Persia, and China at dock. Bukit Siguntang visible as sacred hill in background with stone prasasti (siddhayatra). Wihara (Buddhist monastery) with golden stupa. Market stalls with gold, camphor, frankincense, agarwood. Tropical rainforest surrounding. No modern elements.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on river and port), cool 6500K sky fill from above right. Mid contrast 3:1. Sea haze, smoke from cooking fires.",
        "mood": "thalassocracy — maritime empire where river meets sea, the hub of Indian Ocean-South China Sea trade network, where Buddhist scholarship and Malay language flourished.",
        "style": "photorealistic water, wood, gold, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic coastal documentary aesthetic.",
        "avoid": "modern buildings, modern Palembang, modern port, modern boats, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern tourism, modern pollution."
    }),
    "2B-L002-borobudur.txt": ("L", {
        "name": "Candi Borobudur, the great Buddhist Mahayana monument",
        "period": "Kedu valley, Jawa Tengah, abad 8-9 Masehi (780-825 M)",
        "scene_details": "Massive stepped pyramid with 3 levels: Kamadhatu (base), Rupadhatu (5 square terraces with 504 Buddha statues and 2672 relief panels), Arupadhatu (3 circular terraces with 72 stupas). Central main stupa at peak. Volcanic andesite stone. Surrounded by tropical forest, Gunung Menoreh in background, Gunung Merapi distant. No modern elements.",
        "lighting": "warm 3500K morning sun from camera right (key light, raking across stone terraces revealing relief detail, long shadows), cool 6500K sky fill from above left. Mid contrast 3:1. Mist in valley.",
        "mood": "bhumisambhara — earth of accumulated virtues and knowledge, the largest Buddhist monument in the world, built by Wangsa Syailendra over 60-80 years, where sutras are carved in stone.",
        "style": "photorealistic andesite stone textures (weathered, carved reliefs, stupas), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey stone, green forest), BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern stairs/handrails, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern vegetation cover hiding structure, Hindu temple (must be Buddhist)."
    }),
    "2B-L003-prambanan.txt": ("L", {
        "name": "Candi Prambanan (Siwagrha), the great Hindu Siwa temple complex",
        "period": "Prambanan valley, Jawa Tengah, 856 Masehi",
        "scene_details": "Three towering stone temples: Candi Siwa (47m tall, center), Candi Brahma (south), Candi Wisnu (north). Volcanic andesite stone with intricate carvings: Ramayana relief on boundary walls, panteon astadikpalaka (guardian deities) in niches. 240 perwara (smaller) temples in courtyard. Tropical forest surrounding, Gunung Merapi in background. No modern elements.",
        "lighting": "warm 3500K golden hour sun from camera left (key light, long shadows of towers, golden amber on stone), cool 6500K sky fill from above. Mid contrast 3:1. Mist from Merapi.",
        "mood": "Siwagrha — abode of Shiva, the grandest Hindu temple in Nusantara, built by Rakai Pikatan (Wangsa Sanjaya) in 856 M, standing alongside Buddhist Borobudur as proof of religious coexistence.",
        "style": "photorealistic andesite stone textures (carved reliefs, towering spires, guardian statues), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey-brown stone, green forest), BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern stairs/handrails, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, Buddhist temple (must be Hindu Siwa)."
    }),
    "2B-L004-ratu-boko.txt": ("L", {
        "name": "Keraton Ratu Boko (Abhayagirivihara)",
        "period": "Bukit Boko, Jawa Tengah, 792 Masehi",
        "scene_details": "Royal palace complex on hilltop with panoramic view of Prambanan valley. Pendopo (audience hall) with stone pillars, keputren (royal quarters), bathing pools with dragon spouts, cremation temple, wihara (Buddhist monastery). Stone gates with kala-makara ornaments. View to Candi Prambanan and Gunung Merapi. Mixed Hindu-Buddhist elements. No modern elements.",
        "lighting": "warm 3500K late afternoon sun from camera right (key light, golden on stone ruins and valley view), cool 6500K sky fill from above. Mid contrast 3:1. Mist in valley.",
        "mood": "royal hilltop — the palace-monastery where Sri Lankan Buddhist monks (Abhayagiri) served the Mataram kings, where Hindu and Buddhist traditions merged in stone.",
        "style": "photorealistic andesite stone ruins and tropical landscape textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, fully restored (must show partially ruined ancient state)."
    }),
    "2B-L005-tamwlang.txt": ("L", {
        "name": "Tamwlang, capital of Mataram Kuno in Jawa Timur",
        "period": "Between Bengawan Solo and Brantas rivers, Jawa Timur, 929-1016 Masehi",
        "scene_details": "Royal palace complex on elevated ground between two great rivers. Wooden palace on stilts with early Hindu-Javanese architecture, pendopo agung with 16 carved teak pillars, peaked ijuk roof. Bendungan (dams) and irigasi (irrigation canals) visible. Bengawan Solo flowing in background with trading boats. Tropical forest, paddy fields. No modern elements.",
        "lighting": "warm 4000K morning sun from camera right (key light, golden on palace, paddy fields, river), cool 6500K sky fill from above left. Mid contrast 3:1. Mist over rivers.",
        "mood": "new capital in the east — Pu Sindok's vision of an economically powerful kingdom built on two great rivers (Solo and Brantas), with irrigation for agriculture and trade routes to the sea.",
        "style": "photorealistic wood, water, and paddy field textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern irrigation, modern agriculture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, stone candi (must be wooden palace complex)."
    }),
    # ISTANA EKSTERIOR (2 file)
    "2B-L006-istana-sriwijaya.txt": ("L", {
        "name": "Royal palace complex (kedatuan) of Kedatuan Sriwijaya",
        "period": "Palembang, Sumatra Selatan, abad 8-9 Masehi",
        "scene_details": "Grand royal complex on riverbank of Musi. Main pendopo agung with 16 carved wooden pillars, peaked ijuk roof rising 15 meters, golden stupa ornament at peak. Flanked by dalem (royal residence) and wihara (Buddhist monastery). Front courtyard opening to river with royal dock — trading boats from India, Persia, China. Bukit Siguntang visible in background. High wooden palisade. Royal banner (red-gold) flying. Buddhist golden stupa at courtyard. No modern elements.",
        "lighting": "warm 4000K morning sun from camera right (key light, golden on wooden palace, river, and stupa), cool 6500K sky fill from above left. Mid contrast 3:1. River mist.",
        "mood": "maritime kedatuan — the palace of the thalassocrat, where a Datu ruled the federasi of port states, where Buddhist scholars from India and China came to study.",
        "style": "photorealistic wood, gold, stone, and water textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern Palembang, modern port, stone candi (must be wooden palace complex), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, rumah adat individual (must be royal palace complex)."
    }),
    "2B-L007-istana-mataram.txt": ("L", {
        "name": "Royal palace complex (keraton) of Mataram Kuno",
        "period": "Jawa Tengah, abad 8-9 Masehi (era Sanjaya-Syailendra)",
        "scene_details": "Grand royal complex in Jawa Tengah valley. Main pendopo agung with 16 carved teak pillars painted red-gold, peaked ijuk roof rising 15 meters, golden chandra-kapala (skull-crescent) ornament at peak. Flanked by dalem and pringgitan. Front gateway with stone dwarapala guardians. Ceremonial courtyard with stone prasasti. View to Gunung Merapi and Gunung Menoreh. High wooden palisade. Royal banner (red-gold) flying. Hindu Siwa + Buddhist Mahayana elements coexisting. No modern elements.",
        "lighting": "warm 3500K late afternoon sun from camera right (key light, golden on pendopo, stone guardians, and mountains), cool 6500K sky fill from above left. Mid contrast 3:1. Mist from Merapi.",
        "mood": "dual faith palace — where Hindu Sanjaya and Buddhist Syailendra coexisted, where Borobudur and Prambanan were commissioned, the political and religious center of Mataram Kuno.",
        "style": "photorealistic wood, stone, gold, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern Yogyakarta, stone candi (must be wooden palace complex), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, rumah adat individual (must be royal palace complex)."
    }),
    # ISTANA INTERIOR (2 file)
    "2B-L008-interior-istana-sriwijaya.txt": ("L", {
        "name": "Interior of the royal throne room (ruang tahta) of Kedatuan Sriwijaya",
        "period": "Palembang, abad 8-9 Masehi",
        "scene_details": "Grand interior of pendopo agung with 16 carved wooden pillars. At center, elevated golden throne (singgasana) with Buddhist stupa motifs, golden footstool, royal parasol with 3 tiers. Throne flanked by Buddhist monks in orange robes holding palm leaf manuscripts. Wall behind throne decorated with golden Buddha relief and red-gold royal banner. Floor of polished hardwood with woven rattan mats. Golden ceremonial vessels, offering plates with lotus flowers and incense. Foreign merchants (Indian, Chinese, Persian) waiting at front with gifts (gold dust, camphor, silk). Trade route map painted on wooden panel. No modern elements.",
        "lighting": "warm 4000K daylight from camera right (key light, through carved window screens, dappled on throne), cool 6500K sky fill from above. Mid contrast 3:1. Incense smoke.",
        "mood": "court of commerce and dharma — where a Datu received foreign traders, taxed the wealth of Asia, and patronized Buddhist scholarship, the hub of the Indian Ocean trade network.",
        "style": "photorealistic wood, gold, silk, and textile textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern furniture, modern lighting, modern buildings visible, stone candi interior (must be wooden pendopo interior), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room (must be furnished with throne, monks, merchants, trade goods)."
    }),
    "2B-L009-interior-istana-mataram.txt": ("L", {
        "name": "Interior of the royal throne room (ruang tahta) of Mataram Kuno",
        "period": "Jawa Tengah, abad 8-9 Masehi",
        "scene_details": "Grand interior of pendopo agung with 16 carved teak pillars painted red-gold. At center, elevated golden throne (singgasana) with Shiva lingga and Garuda motifs, golden footstool, royal parasol with 3 tiers. Throne flanked by Hindu priests in white-yellow robes and Buddhist monks in orange robes (coexistence). Wall behind throne decorated with golden Shiva relief and red-gold royal banner. Floor of polished hardwood with woven rattan mats. Golden ceremonial vessels, offering plates with flowers. Stone prasasti on display. Royal adviser (patih) kneeling with scroll. View to Mount Merapi through carved window. No modern elements.",
        "lighting": "warm 2700K sacred firelight from camera left (key light, dancing on golden throne and pillars), cool 5500K daylight from window right (fill light). High contrast 4:1. Smoke from ritual fire.",
        "mood": "dual faith throne room — where Hindu Siwa and Buddhist Mahayana coexisted, where Sanjaya and Syailendra traditions met, the center of Mataram Kuno power.",
        "style": "photorealistic wood, gold, stone, and fire textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm fire-gold highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern furniture, modern lighting, modern buildings visible, stone candi interior (must be wooden pendopo interior), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room (must be furnished with throne, priests, monks, adviser)."
    }),
    # ARTEFAK (3 file)
    "2B-A001-prasasti-kedukan-bukit.txt": ("L", {
        "name": "Prasasti Kedukan Bukit, the proclamation of Sriwijaya",
        "period": "Palembang, 682 Masehi (604 Saka)",
        "scene_details": "Extreme close-up macro of ancient stone inscription on andesite. Pallawa/Malay Kuno script carved in stone, recording Dapunta Hyang's siddhayatra (sacred journey) to unify wanua maritim. Stone is grey with reddish-brown patina, moss in crevices. Background blurred showing river Musi. The earliest evidence of Sriwijaya as a political entity.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing script depth and patina), low ambient fill. High contrast 5:1. Dust particles in light beam.",
        "mood": "the proclamation — the earliest written evidence of Sriwijaya, recording the siddhayatra vision that created the thalassocracy.",
        "style": "photorealistic stone texture with visible mineral grains and carved script, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones, museum specimen documentation aesthetic.",
        "avoid": "modern display case, modern labels, modern lighting, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern stone, polished surface (must show ancient weathering)."
    }),
    "2B-A002-borobudur-stupa.txt": ("L", {
        "name": "Bell-shaped stupa at the Arupadhatu level of Borobudur",
        "period": "Jawa Tengah, abad 9 Masehi",
        "scene_details": "Extreme close-up macro of a bell-shaped perforated stupa at the upper circular terrace of Borobudur. Andesite stone with intricate lattice perforations revealing a Buddha statue inside. Weathered grey stone with lichen. Other stupas visible in background, slightly blurred. Morning mist on the Arupadhatu level.",
        "lighting": "warm 3500K morning sun from camera right (key light, raking across stone stupa revealing texture and perforations), cool 6500K sky fill from above. High contrast 4:1. Mist particles.",
        "mood": "the realm of formlessness — Arupadhatu, the highest level of Borobudur where 72 stupas enclose Buddha statues, the pinnacle of Buddhist spiritual journey.",
        "style": "photorealistic andesite stone texture with weathering, lichen, and perforation detail, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm grey-green tones, museum specimen documentation aesthetic.",
        "avoid": "modern display case, modern labels, modern lighting, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern stone, Hindu temple (must be Buddhist stupa)."
    }),
    "2B-A003-arca-tara.txt": ("L", {
        "name": "Bronze statue of Dewi Tara from Candi Kalasan",
        "period": "Jawa Tengah, 778 Masehi",
        "scene_details": "Extreme close-up macro of a bronze statue of Dewi Tara (Buddhist goddess), originally housed in Candi Kalasan. Statue is 6 meters tall (show upper torso and face). Green patina on bronze surface, with original metallic bronze visible on raised surfaces (face, hands, ornaments). Serene expression, half-closed eyes, elaborate crown, lotus motif. Post-Gupta Indian style influence. Background dark velvet.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing bronze texture, patina, and carving detail), low ambient fill. High contrast 5:1. Subtle reflections on metallic surfaces.",
        "mood": "the first Buddhist goddess — Tara, the female Buddha, enshrined at Candi Kalasan by Rakai Panangkaran (778 M), representing the transition from Hindu to Buddhist patronage in Mataram.",
        "style": "photorealistic bronze texture with green patina and metallic highlights, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm bronze highlights cool green shadows, museum specimen documentation aesthetic.",
        "avoid": "modern statue, modern bronze, polished modern bronze, modern display case visible, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, plastic-looking metal, Hindu deity (must be Buddhist Tara)."
    }),
}

def gen_k(data):
    return TEMPLATE_K.format(**data)

def gen_l(data):
    return TEMPLATE_L.format(**data)

GENERATORS = {"K": gen_k, "L": gen_l}

def main():
    total = 0
    for filename, (ptype, data) in PROMPTS.items():
        content = GENERATORS[ptype](data)
        out_path = BASE / filename
        out_path.write_text(content, encoding="utf-8")
        total += 1
        print(f"  ✅ {filename}")
    print(f"\nTotal: {total} file generated")

if __name__ == "__main__":
    main()
