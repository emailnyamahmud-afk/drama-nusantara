#!/usr/bin/env python3
"""Generate T2I prompts untuk era 2D Majapahit."""

from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts/2D-majapahit/prompts")
BASE.mkdir(parents=True, exist_ok=True)

TEMPLATE_K = """Cinematic realistic character reference sheet of {name}, shown in 5 different angles arranged in a grid layout on a clean solid light cream studio background. Layout: top-left frontal face close-up, top-right full body front view, middle-left side face profile close-up, bottom-left side full body view {prop_phrase}, bottom-right back full body view. All 5 angles show the exact same character, same costume, same physical features, same identity. {details} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all 5 angles in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters (must be same character in all 5 angles), inconsistent costume between angles, {avoid}"""

TEMPLATE_L = """Cinematic realistic documentary {view_type} of {name}, {period}. {details} No people, no characters, no humans — empty location reference.

Setting: {setting}

Lighting: {lighting}

Mood: {mood}

Style: {style} Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: people, characters, humans, {avoid}"""

PROMPTS = {
    # KARAKTER (5)
    "2D-K01-MAJAPAHIT-raden-wijaya.txt": ("K", {
        "name": "Sri Kertarajasa Jayawardhana (Raden Wijaya), founder of Majapahit (Jawa Timur, 1293-1309 Masehi)",
        "prop_phrase": "holding a golden Garuda scepter (Garudamukha emblem)",
        "details": "Male, 30-40 years old, Javanese phenotype with golden brown skin, sharp regal features with weathered look from years of exile and war, long black hair tied back with gold band, full beard. Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif, gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold batik kain with parang pattern, kris pusaka at waist. Garudamukha (Garuda = vehicle of Wisnu) as royal emblem. Strategic genius who used Tartar invasion to destroy Jayakatwang then expelled Tartars.",
        "mood": "Raden Wijaya is the founder of Majapahit — escaped Jayakatwang, built alliance with Madura, used Kubilai Khan's army as tool, then expelled them. Married 4 princesses of Kertanagara.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-K02-MAJAPAHIT-gajah-mada.txt": ("K", {
        "name": "Mahapatih Gajah Mada, prime minister of Majapahit (Jawa Timur, abad 14 Masehi, era Hayam Wuruk)",
        "prop_phrase": "holding a golden keris (symbol of Mahapatih authority)",
        "details": "Male, 45-55 years old, Javanese phenotype with dark brown weathered skin, fierce determined face, sharp eyes, short black hair with grey, trimmed beard. Muscular military build. Wearing Mahapatih costume: dark red and gold military tunic with gold embroidery, leather armor vest, gold makuta (simpler than king's), gold keyura armlets, dark red kain, keris at waist. NOT ornate royal costume — this is a warrior-statesman. Fierce, loyal, visionary. Took Sumpah Palapa — swore not to rest until all Nusantara united under Majapahit.",
        "mood": "Gajah Mada is the legendary Mahapatih who swore the Sumpah Palapa — to unite all of Nusantara. His vision encompassed Sumatra, Malaya, Kalimantan, Bali, Nusa Tenggara, and Maluku.",
        "avoid": "modern clothing, modern military uniform, Chinese costume, Indian costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, ornate royal costume (must be warrior-statesman)."
    }),
    "2D-K03-MAJAPAHIT-hayam-wuruk.txt": ("K", {
        "name": "Sri Maharaja Hayam Wuruk (Sri Rajasanagara), King of Majapahit at its peak (Jawa Timur, 1350-1389 Masehi)",
        "prop_phrase": "holding a golden royal charter scroll",
        "details": "Male, 20-30 years old (ascended throne 1350 M), Javanese phenotype with golden brown skin, refined intelligent features, calm regal bearing, long black hair tied in topknot with ornate gold diadem, clean-shaven. Wearing Hindu-Buddhist syncretic royal costume: ornate gold makuta with both Siwa trident and Buddhist stupa motifs, gold hara necklace with Harihara pendant, gold keyura armlets, deep blue-gold batik kain, kris pusaka at waist. Scholarly king — patron of Nagarakretagama (Mpu Prapanca) and Sutasoma (Mpu Tantular). Ruled at peak of Majapahit's power.",
        "mood": "Hayam Wuruk is the king at Majapahit's zenith — ruled over all of Nusantara from Sumatra to Maluku, patron of literature and arts, traveled extensively across his kingdom.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-K04-MAJAPAHIT-tribhuwana.txt": ("K", {
        "name": "Ratu Tribhuwanatunggadewi Jayawisnuwardhani, Queen Regent of Majapahit (Jawa Timur, 1328-1350 Masehi)",
        "prop_phrase": "holding a golden royal scepter",
        "details": "Female, 35-45 years old, Javanese phenotype with golden brown skin, dignified regal features, long black hair tied in elaborate updo with gold ornaments. Wearing Hindu Javanese queen costume: gold makuta with lotus motifs, gold hara necklace with large pendant, gold kundala earrings, gold keyura armlets, red-gold kemben (brocade), batik kain with parang pattern. Mother of Hayam Wuruk. Appointed Gajah Mada as Mahapatih during her reign.",
        "mood": "Tribhuwanatunggadewi is the queen who appointed Gajah Mada, under whom Sumpah Palapa was sworn — the beginning of Majapahit's expansion across Nusantara.",
        "avoid": "modern clothing, modern jewelry, Chinese empress costume, Indian costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-K05-MAJAPAHIT-mpu-prapanca.txt": ("K", {
        "name": "Mpu Prapanca, royal poet of Majapahit (Jawa Timur, abad 14 Masehi, era Hayam Wuruk)",
        "prop_phrase": "holding a palm leaf manuscript (lontar) with Jawa Kuno script",
        "details": "Male, 40-55 years old, Javanese phenotype with golden brown skin, contemplative scholarly features, deep-set eyes, short grey-streaked black hair, short beard. Wearing Buddhist scholar attire: simple white-yellow robe (jubah) with gold-thread border, rudraksha bead necklace, cloth headband. Holding lontar manuscript of Nagarakretagama (1365 M). Buddhist monk-scholar who documented Majapahit's empire.",
        "mood": "Mpu Prapanca is the poet who wrote Nagarakretagama (1365 M) — the most important text about Majapahit, documenting its territories, government, royal travels, and cosmology.",
        "avoid": "modern clothing, modern glasses, modern books, Chinese costume, Indian costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # LATAR (8)
    "2D-L01-MAJAPAHIT-trowulan-ibukota.txt": ("L", {
        "view_type": "wide aerial establishing shot",
        "name": "Trowulan (Wilwatikta), capital of Majapahit empire",
        "period": "Mojokerto, Jawa Timur, abad 14 Masehi (era Hayam Wuruk)",
        "details": "Massive royal city spanning 500+ hectares in the Brantas valley — NOT a single building but an entire imperial capital. Dozens of grand JAVANESE buildings with tumpang sari roofs visible: main keraton (palace), pendopo agung (50m x 30m audience hall), dalem, pringgitan, gadri, kaputren, wihara (Buddhist), pura (Hindu). Candi bentar gateways. Stone dwarapala guardians. Market (pasar, 2 hectares), workshops (bengkel), royal gardens (taman, 5 hectares with lotus ponds). Brick temples visible (Candi Brahu, Candi Tikus, Candi Bajang Ratu). Wide ceremonial plaza. High brick wall enclosing complex. Sawah extending to horizon with irrigation canals. Gunung Penanggungan and Gunung Arjuno visible in distance. JAVANESE architecture — tumpang sari, candi bentar, square pillars, kala-makara — NOT Chinese.",
        "setting": "Trowulan/Wilwatikta — capital of Majapahit empire at its peak. Kosmologi: keraton = Indraan (tempat tinggal para dewa), raja = dewa di puncak Mahameru. 500+ hectares of imperial city.",
        "lighting": "warm 3500K golden hour sun from camera right (key light, long shadows, golden on dozens of rooftops and sawah), cool 6500K sky fill. Mid contrast 3:1. Mist from Brantas river.",
        "mood": "imperial capital at its zenith — 500 hectares of Javanese imperial city, the heart of an empire spanning from Sumatra to Maluku, the greatest kingdom in Nusantara history.",
        "style": "photorealistic JAVANESE wood, brick, stone, gold, palm fiber roof, sawah, and tropical foliage textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent (buildings prominent, NOT tiny), 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture (no pagoda, curved roofs, upturned eaves, dragon, paifang, Chinese lions), INDIAN architecture, THAI architecture, modern buildings, modern Trowulan, stone candi as main structures (must be wooden palace + brick temples), single small house, tiny buildings, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, 16mm ultra-wide, distant shot."
    }),
    "2D-L02-MAJAPAHIT-istana-eksterior.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Grand royal palace complex (keraton) of Majapahit",
        "period": "Trowulan, Jawa Timur, abad 14 Masehi (era Hayam Wuruk)",
        "details": "Grand keraton complex spanning 300 hectares. Main pendopo agung (great audience hall, 50m x 30m, 36 square teak pillars, tumpang sari roof 20m tall, golden chandra-kapala at peak). Dozens of secondary buildings: dalem, pringgitan, gadri (archive with lontar), kaputren, wihara (with golden stupa), pura (with lingga-yoni). Candi bentar gateways. Stone dwarapala (3m tall, Javanese kneeling giant with club). Market (2 hectares), workshops, gardens (5 hectares, lotus ponds, bathing pools). High brick wall enclosing complex. Sawah to horizon. Gunung Penanggungan visible. JAVANESE architecture.",
        "setting": "Royal palace of Majapahit at Trowulan, abad 14 M. Where Hayam Wuruk held court, where Gajah Mada administered the empire, where Nagarakretagama was composed.",
        "lighting": "warm 3500K golden hour, cool 6500K sky fill. Mid contrast 3:1. Mist from Brantas.",
        "mood": "imperial palace — 300 hectares of Javanese royal city, the seat of power from which all of Nusantara was governed.",
        "style": "photorealistic JAVANESE wood, brick, stone, gold textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent (buildings prominent), 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "CHINESE architecture, INDIAN architecture, THAI architecture, modern buildings, single small house, tiny buildings, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, 16mm ultra-wide."
    }),
    "2D-L03-MAJAPAHIT-istana-interior-pendopo.txt": ("L", {
        "view_type": "interior wide shot",
        "name": "Pendopo Agung (Great Audience Hall) of Majapahit royal palace",
        "period": "Trowulan, abad 14 Masehi (era Hayam Wuruk)",
        "details": "Vast hall 50m x 30m with 36 square carved teak pillars painted red-gold, each 10m tall, rising to peaked ceiling 20m with tumpang sari roof and golden chandra-kapala. At far end, elevated golden throne (singgasana) on 7-step stone platform, royal parasol 7 tiers. Floor polished hardwood with woven rattan mats. Golden ceremonial vessels, incense burners. Stone prasasti mounted on wall. View through 8m tall carved windows to Gunung Penanggungan. JAVANESE architecture. No people.",
        "setting": "Main audience hall of Majapahit palace. Where Hayam Wuruk received foreign envoys, where Gajah Mada reported conquests, where Mpu Prapanca recited Nagarakretagama.",
        "lighting": "warm 2700K firelight from camera left, cool 5500K daylight from windows. High contrast 4:1. Incense smoke.",
        "mood": "hall of empire — where the king of all Nusantara held court, where the greatest decisions of the archipelago were made.",
        "style": "photorealistic JAVANESE wood, gold, stone, and fire textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm fire-gold highlights cool blue shadows.",
        "avoid": "CHINESE architecture, modern furniture, modern lighting, stone candi interior, small room, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-L04-MAJAPAHIT-candi-brahu.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Candi Brahu, red brick temple of Majapahit",
        "period": "Trowulan, Jawa Timur, abad 14-15 Masehi",
        "details": "Red brick temple (candi) with tall rectangular structure, distinctive Majapahit brick architecture. Ornate brick carvings, geometric patterns. Smaller than Prambanan but unique red brick construction. Surrounding garden with stone pathways. Tropical vegetation. Part of Trowulan temple complex. Other brick structures visible in distance (Candi Tikus, Candi Bajang Ratu). No people.",
        "setting": "Candi Brahu at Trowulan — red brick temple of Majapahit era. Part of the religious landscape of the imperial capital.",
        "lighting": "warm 3500K golden hour sun from camera right (key light, golden on red brick), cool 6500K sky fill. Mid contrast 3:1.",
        "mood": "red brick temple of empire — distinctive Majapahit architecture, where Hindu and Buddhist traditions met in fired clay.",
        "style": "photorealistic red brick, stone, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm red-brown highlights cool blue shadows.",
        "avoid": "CHINESE architecture, INDIAN architecture, THAI architecture, modern buildings, modern tourism, modern stairs, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, stone temple (must be red brick)."
    }),
    "2D-L05-MAJAPAHIT-pasar-trowulan.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Grand market (pasar) of Majapahit at Trowulan",
        "period": "Jawa Timur, abad 14 Masehi (era Hayam Wuruk)",
        "details": "Vast market complex covering 3 hectares within the imperial capital. Hundreds of bamboo and thatch stalls. Goods from across Nusantara: Sumatran gold and camphor, Malukan spices (cengkih, pala, fuli), Javanese rice and textiles (batik), Indian silk and beads, Chinese porcelain and silk, Khmer bronze. Warehouses storing spices, gold dust. Harbor area with perahu at dock on Brantas river. Trading boats from across Asia. No people.",
        "setting": "Grand market of Majapahit — the economic hub where goods from all of Nusantara and Asia converged. Spices from Maluku, gold from Sumatra, porcelain from China, silk from India.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on market stalls and goods), cool 6500K sky fill. Mid contrast 3:1. Spice dust in air.",
        "mood": "emporium of the archipelago — where the wealth of an empire spanning from Sumatra to Maluku was traded, the commercial heart of Majapahit.",
        "style": "photorealistic bamboo, thatch, spice, textile, porcelain, and gold textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows.",
        "avoid": "CHINESE architecture, modern market, modern buildings, modern shops, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small market (must be 3 hectares)."
    }),
    "2D-L06-MAJAPAHIT-pelabuhan-brantas.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Royal harbor (pelabuhan) of Majapahit on Brantas river",
        "period": "Trowulan, Jawa Timur, abad 14 Masehi",
        "details": "Massive river harbor on Brantas. Stone quay extending 300m. Multiple berths for: Majapahit warships (jong, perahu with 100 rowers), merchant ships from China (Ming dynasty junks), India, Arabia, Khmer. Warehouses storing: spices, gold, porcelain, silk, beads. Customs house (pabean). Cranes lifting cargo. View to Trowulan palace complex in background. Tropical vegetation. No people.",
        "setting": "Royal harbor of Majapahit — the maritime gateway of the agro-maritim empire, where ships from across Asia docked, where the wealth of Nusantara was exported and foreign luxury goods imported.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on ships and harbor), cool 6500K sky fill. Mid contrast 3:1. River mist.",
        "mood": "maritime gateway of empire — where the thalassocratic power of Majapahit met the trade routes of Asia, where ships from China, India, and Arabia converged.",
        "style": "photorealistic wood, water, stone, silk, and porcelain textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern port, modern ships, modern cranes, modern containers, CHINESE architecture, modern buildings, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small dock (must be 300m with international ships)."
    }),
    "2D-L07-MAJAPAHIT-hutan-terik.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Hutan Térik — forest being cleared to become Majapahit",
        "period": "Jawa Timur, 1292-1293 Masehi",
        "details": "Tropical forest being cleared — felled trees, smoke from land clearing, early wooden structures under construction. Simple wooden palace on stilts. Brantas river nearby. View to distant mountains. Raw, unfinished, full of potential. The beginning of what will become the greatest empire in Nusantara history.",
        "setting": "Hutan Térik — forest given by Jayakatwang to Raden Wijaya. Being cleared 1292-1293 M to become Majapahit.",
        "lighting": "warm 3500K afternoon sun through smoke (key light, hazy golden on clearing), cool 6500K sky fill. Mid contrast 3:1. Smoke from land clearing.",
        "mood": "birth of an empire — from forest clearing to kingdom, the humble beginning of Majapahit.",
        "style": "photorealistic wood, smoke, tropical foliage, and river textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm smoky-amber highlights cool blue shadows.",
        "avoid": "CHINESE architecture, modern buildings, modern construction, completed grand palace, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-L08-BLITAR-simping-candi.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Candi Simping (Sumberjati), dharma temple of Kertarajasa",
        "period": "Blitar, Jawa Timur, abad 14 Masehi",
        "details": "Stone temple (candi dharma) in peaceful forest clearing at Sumberjati, south of Blitar. Small stone candi housing Arca Harihara (combined Wisnu-Siwa). Stone pathway through tropical garden. Lotuses in small pond. Peaceful, meditative. Surrounding forest. No people.",
        "setting": "Simping (Sumberjati, Blitar) — where Raden Wijaya/Kertarajasa was didharmakan as Arca Harihara. Visited by Hayam Wuruk 1363 M.",
        "lighting": "soft warm 4000K morning sun through forest canopy (key light, dappled on candi), cool 6500K sky fill. Low contrast 2:1 for peaceful atmosphere.",
        "mood": "eternal rest of the founder — where Raden Wijaya was immortalized as Harihara, where Hindu and Buddhist traditions merged in stone.",
        "style": "photorealistic andesite stone, gold, tropical foliage, water textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture, modern buildings, modern tourism, large temple complex, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # ARTEFAK (4)
    "2D-A01-MAJAPAHIT-nagarakretagama-lontar.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Lontar manuscript of Nagarakretagama kakawin",
        "period": "Majapahit, 1365 Masehi (Mpu Prapanca)",
        "details": "Palm leaf manuscript (lontar) with Jawa Kuno/Kawi script in ink. Text of Nagarakretagama — most important document about Majapahit empire, listing all territories of Nusantara (pupuh 13-14), royal genealogy, government structure, royal travels of Hayam Wuruk. Dried palm leaves with string binding, wooden covers with gold leaf. Aged brown. Written by Mpu Prapanca 1365 M.",
        "setting": "Nagarakretagama (1365 M) by Mpu Prapanca — the most comprehensive source on Majapahit, documenting its territories from Sumatra to Maluku.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing palm leaf texture and script), low ambient fill. High contrast 5:1.",
        "mood": "encyclopedia of empire — where the territories of Nusantara were first listed in writing, where Majapahit's cosmology was documented.",
        "style": "photorealistic palm leaf (lontar), ink, wood, gold leaf textures, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm brown-gold tones, museum specimen aesthetic.",
        "avoid": "modern paper, modern book, modern display case, modern lighting, stone inscription, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-A02-MAJAPAHIT-sutasoma-lontar.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Lontar manuscript of Sutasoma kakawin",
        "period": "Majapahit, abad 14 Masehi (Mpu Tantular)",
        "details": "Palm leaf manuscript (lontar) with Jawa Kuno/Kawi script. Text of Sutasoma by Mpu Tantular — containing the famous phrase 'Bhinneka Tunggal Ika' (although diverse, still one) which became the motto of Republic of Indonesia. Aged brown palm leaves with ink script, wooden covers.",
        "setting": "Sutasoma by Mpu Tantular — the kakawin that gave Indonesia its national motto 'Bhinneka Tunggal Ika', symbolizing unity in diversity.",
        "lighting": "warm 3000K raking side light from camera right (key light), low ambient fill. High contrast 5:1.",
        "mood": "motto of a nation — where 'Bhinneka Tunggal Ika' was first written, a phrase that would echo 600 years later as the motto of modern Indonesia.",
        "style": "photorealistic palm leaf, ink, wood textures, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm brown-gold tones, museum specimen aesthetic.",
        "avoid": "modern paper, modern book, modern display case, modern lighting, stone inscription, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2D-A03-MAJAPAHIT-arca-harihara.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Arca Harihara (statue of Raden Wijaya/Kertarajasa)",
        "period": "Simping/Sumberjati, Blitar, abad 14 Masehi",
        "details": "Stone statue (andesite) of Harihara — combined deity: right half Wisnu (cakra, shankha), left half Siwa (trident, drum). Represents King Kertarajasa (Raden Wijaya) deified. 1.5m tall. Grey andesite with weathering, lichen. Four arms. Crown with both Wisnu and Siwa motifs. Serene expression. Background dark velvet.",
        "setting": "Arca Harihara from Simping (Sumberjati, Blitar). Dharma statue of Raden Wijaya, founder of Majapahit. Symbol of Hindu-Buddhist syncretism.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing stone texture, carving detail), low ambient fill. High contrast 5:1.",
        "mood": "immortal founder — where the first king of Majapahit became a god, where Wisnu and Siwa merged into one.",
        "style": "photorealistic andesite stone texture with weathering, lichen, carving, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm grey-green tones, museum specimen aesthetic.",
        "avoid": "modern statue, modern display case, modern lighting, metal statue, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single deity (must show combined Wisnu-Siwa)."
    }),
    "2D-A04-MAJAPAHIT-prasasti-kudadu.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Prasasti Kudadu (1294 M)",
        "period": "Majapahit, 1216 Saka/1294 Masehi",
        "details": "Copper plate inscription (lempeng tembaga) with Jawa Kuno script. Records Raden Wijaya's gratitude to pejabat desa Kudadu who hid him from enemies. First prasasti of Majapahit kingdom. Green patina on copper. Multiple lempeng visible.",
        "setting": "Prasasti Kudadu (1216 Saka/1294 M) — first inscription of Majapahit, recording the king's gratitude to those who helped him during his darkest hour.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing script and patina), low ambient fill. High contrast 5:1.",
        "mood": "first document of a new kingdom — where Raden Wijaya's gratitude was immortalized in copper, the birth certificate of Majapahit.",
        "style": "photorealistic copper texture with green patina, carved script, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm copper-green tones, museum specimen aesthetic.",
        "avoid": "modern display case, modern labels, modern lighting, stone inscription, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
}

GENERATORS = {
    "K": lambda d: TEMPLATE_K.format(**d),
    "L": lambda d: TEMPLATE_L.format(**d),
}

def main():
    total = 0
    for filename, (ptype, data) in PROMPTS.items():
        content = GENERATORS[ptype](data)
        (BASE / filename).write_text(content, encoding="utf-8")
        total += 1
        print(f"  ✅ {filename}")
    print(f"\nTotal: {total} file generated")

if __name__ == "__main__":
    main()
