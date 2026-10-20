#!/usr/bin/env python3
"""Generate T2I prompts untuk era 2C Singasari & Kediri."""

from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts/2C-singasari-kediri/prompts")
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
    "2C-K01-KEDIRI-jayabhaya.txt": ("K", {
        "name": "Sri Maharaja Sang Mapanji Jayabhaya, King of Kadiri (Jawa Timur, abad 12 Masehi)",
        "prop_phrase": "holding a golden royal scepter",
        "details": "Male, 40-55 years old, Javanese phenotype with golden brown skin, regal dignified bearing, long black hair with grey streaks tied in topknot with gold diadem, full beard trimmed. Wearing Hindu Javanese royal costume: gold makuta with trident motif, gold hara necklace with Shiva lingga pendant, gold keyura armlets, deep red-gold batik kain with parang pattern, kris pusaka at waist. Hindu Siwa — patron of Bharatayuddha (1157 M), unifier of Janggala and Pangjalu.",
        "mood": "Jayabhaya is the king who unified Janggala-Pangjalu into Kadiri, patron of Bharatayuddha (1157 M) that commemorated the peace.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-K02-KEDIRI-kameswara.txt": ("K", {
        "name": "Sri Maharaja Sri Kameswara, King of Kadiri (Jawa Timur, abad 12 Masehi, era 1185 M)",
        "prop_phrase": "holding a golden lotus flower (symbol of Kama Jaya)",
        "details": "Male, 30-40 years old, Javanese phenotype with golden brown skin, handsome regal features, long black hair tied in topknot with gold diadem, clean-shaven. Wearing Hindu Javanese royal costume: ornate gold makuta with lotus and bow motifs (Kama Jaya symbols), gold hara necklace with lotus pendant, gold keyura armlets, blue-gold batik kain. Hindu Siwa but celebrated as incarnation of Kama Jaya (god of love) in Smaradahana by Mpu Dharmaja. Romantic king.",
        "mood": "Kameswara is the romantic king celebrated in Smaradahana as incarnation of Kama Jaya, whose love story with Sri Kirana became the basis of the Panji cycle.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-K03-SINGASARI-ken-arok.txt": ("K", {
        "name": "Ranggah Rajasa (Ken Arok), founder of Singasari kingdom (Tumapel/Malang, 1222 Masehi)",
        "prop_phrase": "holding a kris pusaka (keris Mpu Gandring)",
        "details": "Male, 30-40 years old, Javanese phenotype with weathered golden brown skin, sharp fierce features, short black hair, stubble beard. Muscular warrior build, scar on cheek. Wearing warrior-king costume: simple leather armor vest over cotton tunic, cloth headband (destar), dark brown kain, kris at waist. NOT ornate royal costume — this is a self-made king from common origins. Fierce, ambitious, dangerous.",
        "mood": "Ken Arok is the commoner who became king — killed Tunggul Ametung, married Ken Dedes, defeated Kadiri at Ganter, founded Wangsa Rajasa.",
        "avoid": "modern clothing, ornate royal costume (must be warrior-king, simpler), modern jewelry, Chinese emperor costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-K04-SINGASARI-kertanagara.txt": ("K", {
        "name": "Sri Maharaja Kertanagara, last king of Singasari (Tumapel/Malang, 1268-1292 Masehi)",
        "prop_phrase": "holding a golden vajra (Buddhist ritual object)",
        "details": "Male, 35-45 years old, Javanese phenotype with golden brown skin, sharp intelligent features, long black hair tied in topknot with gold diadem, beard. Wearing syncretic Hindu-Buddhist royal costume: gold makuta with both Shiva trident and Buddhist stupa motifs, gold hara necklace with Harihara pendant (Wisnu+Siwa combined), gold keyura armlets, red-gold batik kain, kris at waist. Visionary king — cakrawala mandala, expansion to dwipantara (all of Nusantara). Buddhist Tantric practitioner.",
        "mood": "Kertanagara is the visionary king who dreamed of uniting all of Nusantara (cakrawala mandala), sent expeditions to Sumatra, defied Kubilai Khan, killed by Jayakatwang's treachery.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-K05-MAJAPAHIT-raden-wijaya.txt": ("K", {
        "name": "Raden Wijaya (Sri Kertarajasa Jayawardhana), founder of Majapahit (Jawa Timur, 1293 Masehi)",
        "prop_phrase": "holding a golden Garuda scepter",
        "details": "Male, 25-35 years old, Javanese phenotype with golden brown skin, sharp regal features, weathered from forest exile, long black hair tied back with gold band, clean-shaven. Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif, gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold batik kain, kris pusaka at waist. Garudamukha emblem. Son-in-law of Kertanagara (married 4 princesses). Strategic genius who used Tartar invasion to destroy Jayakatwang then expelled Tartars.",
        "mood": "Raden Wijaya is the strategic genius who founded Majapahit — escaped Jayakatwang, built alliance with Madura, used Kubilai Khan's army as tool, then expelled them.",
        "avoid": "modern clothing, modern jewelry, Chinese emperor costume, Indian Mughal costume, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # LATAR (8)
    "2C-L01-KEDIRI-daha-ibukota.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Daha, capital of Kadiri kingdom",
        "period": "Jawa Timur, abad 12 Masehi (era Jayabhaya-Kameswara)",
        "details": "Grand royal complex spanning hundreds of hectares in the fertile Brantas river valley. Wooden palace complex with tumpang sari roofs, candi bentar gateways, stone dwarapala guardians. Multiple buildings: pendopo agung, dalem, pringgitan, gadri, kaputren. Wihara (Buddhist), pura (Hindu Siwa). Market (pasar), workshops (bengkel), royal gardens (taman) with lotus ponds. Sawah extending to horizon. Mount Kelud and Mount Kawi visible. JAVANESE architecture — NOT Chinese, NOT Indian, NOT Thai.",
        "setting": "Capital of Kadiri kingdom at Daha (modern Kediri), abad 12 M. Center of politics, sastra (Bharatayuddha, Smaradahana), administrasi 3 tingkat (thani-wisaya-bhumi), militer (makasirkasir).",
        "lighting": "warm 4000K morning sun from camera right (key light, golden on palace and sawah), cool 6500K sky fill. Mid contrast 3:1. Mist from Brantas river.",
        "mood": "golden age of Kadiri — where Bharatayuddha was composed, where Janggala-Pangjalu were united, where Javanese literature flourished.",
        "style": "photorealistic JAVANESE wood, stone, gold, palm fiber (ijuk) roof, and tropical foliage textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture (no pagoda, no curved roofs, no upturned eaves, no dragon ridge, no paifang, no Chinese lions), INDIAN architecture (no shikhara, no gopuram), THAI architecture (no prang, no chofa), modern buildings, modern Kediri, stone candi as main structures, single small house, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L02-SINGASARI-tumapel-ibukota.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Tumapel, capital of Singasari kingdom",
        "period": "Malang, Jawa Timur, abad 13 Masehi (1222-1292 M)",
        "details": "Royal complex at foot of Gunung Kawi. Wooden palace with tumpang sari roofs, candi bentar gateways, square teak pillars. Multiple buildings: pendopo, dalem, pringgitan, gadri, kaputren, wihara, pura. Military training grounds. Horse stables. View to Gunung Kawi (sacred mountain). Sawah and tropical forest surrounding. JAVANESE architecture — NOT Chinese.",
        "setting": "Capital of Singasari at Tumapel (Malang), abad 13 M. Founded by Ken Arok (Ranggah Rajasa) 1222 M. Seat of Kertanagara's cakrawala mandala vision.",
        "lighting": "warm 3500K afternoon sun from camera left (key light, golden on palace and Gunung Kawi), cool 6500K sky fill. Mid contrast 3:1. Mist from mountain.",
        "mood": "new power in the east — where Ken Arok built a kingdom from nothing, where Kertanagara dreamed of uniting Nusantara, where the Rajasa dynasty began.",
        "style": "photorealistic JAVANESE wood, stone, gold, and tropical foliage textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture, INDIAN architecture, THAI architecture, modern buildings, modern Malang, stone candi as main structures, single small house, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L03-SINGASARI-candi-singosari.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Candi Singosari",
        "period": "Malang, Jawa Timur, abad 13 Masehi",
        "details": "Stone Hindu-Buddhist temple complex. Main candi with tall towering spire (10m), andesite stone with intricate carvings: kala-makara at doorway, panteon astadikpalaka (guardian deities) in niches. Smaller perwara temples in courtyard. Tropical vegetation surrounding. View to Gunung Kawi. JAVANESE Hindu-Buddhist architecture — NOT Chinese.",
        "setting": "Candi Singosari, Malang — religious complex of Singasari kingdom, abad 13 M. Built during era Kertanagara. Hindu-Buddhist syncretic.",
        "lighting": "warm 3500K golden hour sun from camera right (key light, long shadows on stone temple), cool 6500K sky fill. Mid contrast 3:1. Mist from Gunung Kawi.",
        "mood": "sacred temple of the Rajasa dynasty — where Hindu Siwa and Buddhist Mahayana met in stone, where Kertanagara's syncretic vision was immortalized.",
        "style": "photorealistic andesite stone textures (carved reliefs, guardian statues, towering spire), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey-brown stone, green foliage), BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture, INDIAN architecture, THAI architecture, modern buildings, modern tourism, modern stairs/handrails, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L04-SINGASARI-gunung-kawi.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Gunung Kawi, sacred mountain of Singasari",
        "period": "Malang, Jawa Timur, abad 13 Masehi",
        "details": "Sacred volcanic mountain towering 2,551m above the Singasari plain. Lush tropical forest on slopes. Stone meditation caves and hermitages carved into cliff faces. Candi tebing (cliff temples) visible. Waterfalls. Mist on peak. Royal meditation site. View to valley below where Tumapel palace complex visible.",
        "setting": "Gunung Kawi — sacred mountain east of Tumapel. Where Ken Arok/Ranggah Rajasa established power base. Meditation site for Singasari kings.",
        "lighting": "warm 3500K morning sun from camera right (key light, golden on mountain peak and forest), cool 6500K sky fill. Mid contrast 3:1. Mist and clouds on peak.",
        "mood": "sacred mountain of power — where kings meditated, where Ken Arok began his rise, where the spiritual authority of Singasari was rooted.",
        "style": "photorealistic volcanic rock, tropical forest, waterfall, and cliff temple textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm green-golden highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern stairs, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L05-KEDIRI-istana-eksterior.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Grand royal palace complex (keraton) of Kadiri",
        "period": "Daha/Kediri, Jawa Timur, abad 12 Masehi (era Jayabhaya-Kameswara)",
        "details": "Massive complex spanning 300 hectares in Brantas valley. Dozens of grand JAVANESE wooden buildings with tumpang sari roofs (NOT Chinese). Main pendopo agung (50m x 30m, 36 square teak pillars), dalem, pringgitan, gadri (archive with lontar), kaputren, wihara, pura. Candi bentar gateways. Stone dwarapala. Market (2 hectares), workshops, gardens (5 hectares). Sawah to horizon. Mount Kelud and Kawi visible. High stone wall enclosing complex. JAVANESE Hindu-Buddhist architecture.",
        "setting": "Royal palace of Kadiri at Daha, abad 12 M. Political, sastra, and economic center. Where Bharatayuddha was composed, where Jayabhaya ruled.",
        "lighting": "warm 3500K golden hour sun from camera right, cool 6500K sky fill. Mid contrast 3:1. Mist from Brantas.",
        "mood": "golden age kingdom — 300 hectares of Javanese royal city where literature, governance, and military innovation flourished.",
        "style": "photorealistic JAVANESE wood, stone, gold, palm fiber roof textures, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent (buildings prominent), 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "CHINESE architecture (no pagoda, curved roofs, upturned eaves, dragon, paifang, Chinese lions), INDIAN architecture, THAI architecture, modern buildings, stone candi as main, single small house, tiny buildings, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, 16mm ultra-wide."
    }),
    "2C-L06-KEDIRI-istana-interior-pendopo.txt": ("L", {
        "view_type": "interior wide shot",
        "name": "Pendopo Agung (Great Audience Hall) of Kadiri royal palace",
        "period": "Daha/Kediri, abad 12 Masehi",
        "details": "Vast hall 50m x 30m with 36 square carved teak pillars painted red-gold, each 10m tall, rising to peaked ceiling 20m with tumpang sari roof and golden chandra-kapala. At far end, elevated golden throne (singgasana) on 7-step stone platform with Shiva lingga, royal parasol 5 tiers. Floor polished hardwood with woven rattan mats. Golden ceremonial vessels, incense burners. Stone prasasti mounted on wall. View through carved windows to Mount Kawi. JAVANESE architecture. No people.",
        "setting": "Main audience hall of Kadiri palace. Where Jayabhaya received Mpu Panuluh presenting Bharatayuddha. Where Smaradahana was first recited.",
        "lighting": "warm 2700K firelight from camera left (key light, dancing on throne and pillars), cool 5500K daylight from windows. High contrast 4:1. Incense smoke.",
        "mood": "hall of literature and power — where kings heard kakawin recited, where Bharatayuddha commemorated peace, where Smaradahana celebrated love.",
        "style": "photorealistic JAVANESE wood, gold, stone, and fire textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm fire-gold highlights cool blue shadows.",
        "avoid": "CHINESE architecture, modern furniture, modern lighting, stone candi interior, small room, people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L07-MAJAPAHIT-hutan-terik.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Majapahit — hutan Térik being cleared for new kingdom",
        "period": "Jawa Timur, 1292-1293 Masehi",
        "details": "Tropical forest being cleared — felled trees, smoke from land clearing, early wooden structures being built. A new settlement emerging from wilderness. Simple wooden palace on stilts under construction. Brantas river visible nearby. View to distant mountains. Raw, unfinished, full of potential. This is the beginning of what will become Majapahit empire.",
        "setting": "Hutan Térik — forest given by Jayakatwang to Raden Wijaya as residence. Being cleared 1292-1293 M to become Majapahit. Site where Raden Wijaya built his base, allied with Arya Wiraraja from Madura, and prepared to strike back.",
        "lighting": "warm 3500K afternoon sun through smoke (key light, hazy golden on clearing), cool 6500K sky fill. Mid contrast 3:1. Smoke from land clearing.",
        "mood": "birth of an empire — from forest clearing to kingdom, the humble beginning of what will become the greatest empire in Nusantara history.",
        "style": "photorealistic wood, smoke, tropical foliage, and river textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm smoky-amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture, modern buildings, modern construction, completed grand palace (must be under construction, raw), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-L08-BLITAR-simping.txt": ("L", {
        "view_type": "wide establishing shot",
        "name": "Simping (Sumberjati), Blitar — dharma site of Kertarajasa",
        "period": "Blitar, Jawa Timur, abad 14 Masehi",
        "details": "Sacred stone temple (candi dharma) in peaceful forest clearing at Sumberjati, south of Blitar. Small stone candi housing arca Harihara (combined Wisnu-Siwa deity, representing Kertarajasa/Raden Wijaya). Stone pathway through tropical garden. Lotuses in small pond. Peaceful, meditative. Surrounding forest. No people.",
        "setting": "Simping (Sumberjati, Blitar) — where Raden Wijaya/Kertarajasa was didharmakan (deified) as arca Harihara (Wisnu+Siwa combined). Memorial site for founder of Majapahit.",
        "lighting": "soft warm 4000K morning sun through forest canopy (key light, dappled on candi), cool 6500K sky fill. Low contrast 2:1 for peaceful atmosphere.",
        "mood": "eternal rest of the founder — where Raden Wijaya was immortalized as Harihara, where Hindu and Buddhist traditions merged in stone.",
        "style": "photorealistic stone (andesite), gold, tropical foliage, and water textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones, BBC Earth documentary aesthetic.",
        "avoid": "CHINESE architecture, modern buildings, modern tourism, large temple complex (must be small dharma site), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # ARTEFAK (4)
    "2C-A01-prasasti-mula-malurung.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Prasasti Mula Malurung (1255 M)",
        "period": "Singasari, abad 13 Masehi",
        "details": "Copper plate inscription (lempeng tembaga) with Jawa Kuno script. Records genealogy of Singasari kings and the concept of Nusantara unification. Issued by King Wisnuwardhana (Nararyya Smi nin Rat). Green patina on copper. Multiple lempeng visible.",
        "setting": "Prasasti Mula Malurung (1177 Saka/1255 M) — most important Singasari inscription, recording royal genealogy and early concept of Nusantara.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing script depth and patina), low ambient fill. High contrast 5:1.",
        "mood": "birth certificate of Nusantara — where the concept of a unified archipelago was first written in copper.",
        "style": "photorealistic copper texture with green patina and carved script, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm copper-green tones, museum specimen aesthetic.",
        "avoid": "modern display case, modern labels, modern lighting, stone inscription (must be copper plate), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-A02-arca-harihara.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Arca Harihara (statue of Raden Wijaya/Kertarajasa)",
        "period": "Simping/Sumberjati, Blitar, abad 14 Masehi",
        "details": "Stone statue (andesite) of Harihara — combined deity with right half as Wisnu (with cakra/discus and shankha/conch) and left half as Siwa (with trident and drum). Represents King Kertarajasa (Raden Wijaya) deified after death. 1.5m tall. Grey andesite with weathering, lichen. Serene expression combining both deities. Four arms. Crown with both Wisnu and Siwa motifs.",
        "setting": "Arca Harihara from Simping (Sumberjati, Blitar). Dharma statue of Raden Wijaya, founder of Majapahit. Symbol of Hindu-Buddhist syncretism — Wisnu and Siwa in one body.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing stone texture, carving detail, patina), low ambient fill. High contrast 5:1.",
        "mood": "immortal founder — where the first king of Majapahit became a god, where Hindu traditions merged Wisnu and Siwa into one.",
        "style": "photorealistic andesite stone texture with weathering, lichen, and intricate carving, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm grey-green tones, museum specimen aesthetic.",
        "avoid": "modern statue, modern display case, modern lighting, metal statue (must be stone), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single deity (must show combined Wisnu-Siwa)."
    }),
    "2C-A03-bharatayuddha-lontar.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Lontar manuscript of Bharatayuddha kakawin",
        "period": "Kadiri, abad 12 Masehi (1157 M / 1079 Saka)",
        "details": "Palm leaf manuscript (lontar) with Jawa Kuno/Kawi script in ink. Text of Bharatayuddha — Javanese version of Mahabharata war, composed by Mpu Sedah and Mpu Panuluh under patronage of King Jayabhaya (1157 M). Dried palm leaves with string binding, wooden covers with gold leaf. Script清晰 visible. Aged brown palm leaf.",
        "setting": "Bharatayuddha kakawin (1079 Saka/1157 M) — masterpiece of Kadiri literature, composed by Mpu Sedah and Mpu Panuluh. Commemorated unification of Janggala-Pangjalu.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing palm leaf texture and script), low ambient fill. High contrast 5:1.",
        "mood": "literary masterpiece — where the Mahabharata war was retold in Javanese, where peace between Janggala and Pangjalu was commemorated in verse.",
        "style": "photorealistic palm leaf (lontar), ink, wood, and gold leaf textures, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm brown-gold tones, museum specimen aesthetic.",
        "avoid": "modern paper, modern book, modern display case, modern lighting, stone inscription (must be palm leaf), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "2C-A04-smaradahana-lontar.txt": ("L", {
        "view_type": "extreme close-up macro",
        "name": "Lontar manuscript of Smaradahana kakawin",
        "period": "Kadiri, abad 12 Masehi (era Kameswara)",
        "details": "Palm leaf manuscript (lontar) with Jawa Kuno/Kawi script in ink. Text of Smaradahana — 'Api Cinta' — composed by Mpu Dharmaja under patronage of King Kameswara (1185 M). Tells story of Kama Jaya (god of love) and Kamaratih, celebrating Kameswara and Sri Kirana as incarnations. Dried palm leaves with string binding, wooden covers. Aged brown.",
        "setting": "Smaradahana kakawin — masterpiece by Mpu Dharmaja, era Kameswara (1185 M). Celebrated the king as incarnation of Kama Jaya. Basis of the Panji cycle that spread across Southeast Asia.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing palm leaf texture and script), low ambient fill. High contrast 5:1.",
        "mood": "poem of love — where a king became the god of love, where Sri Kirana became Kamaratih, where the Panji cycle was born.",
        "style": "photorealistic palm leaf (lontar), ink, and wood textures, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm brown-gold tones, museum specimen aesthetic.",
        "avoid": "modern paper, modern book, modern display case, modern lighting, stone inscription (must be palm leaf), people, characters, humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
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
