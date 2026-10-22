#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 3B — Demak-Pajang (Abad 15-16 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts"

def k_prompt(name, era_desc, phenotype, costume, props, mood, avoid_extra=""):
    return f"""Cinematic realistic character reference sheet of {name}, {era_desc}, shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view {props}, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. {phenotype} {costume} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""

def l_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, avoid_extra=""):
    return f"""Cinematic realistic documentary landscape of {name}, {era_desc}. {scene_desc} No people, no characters, no humans — empty location reference.

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures, 35mm film grain, deep depth of field f/8-f/11, 24mm wide lens, 8K hyperdetailed, BBC Earth documentary aesthetic. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: people, characters, humans, modern buildings, modern roads, modern tourism, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""

def a_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc):
    return f"""Cinematic realistic macro photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens, 8K hyperdetailed, scientific documentation aesthetic. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: modern tools, metal tools, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."""

def s_prompt(name, era_desc, composition, mood, k_refs, avoid_extra=""):
    k_ref_note = " | ".join(k_refs)
    return f"""Cinematic realistic group character reference of {name}, {era_desc}, arranged in a standing group pose on a clean solid light cream studio background. {composition} Clean studio background, no environment, no historical setting, no landscape elements — neutral studio reference only.

IMPORTANT: Upload the following character reference images before generating: {k_ref_note}. Use each uploaded image as the exact face, body, and identity reference. This prompt only defines group composition, pose, and props — NOT physical features.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting, no dramatic lighting.

Mood: neutral studio reference, group turnaround for production consistency. {mood}

Style: photorealistic skin texture, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: environment background, landscape, historical setting, dramatic lighting, inconsistent faces with reference images, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


# ===== K PROMPTS — 6 karakter =====

K001 = k_prompt(
    name="Sultan Trenggana, greatest Sultan of Demak",
    era_desc="16th century AD (r. 1521-1546), Demak, Central Java — conqueror of Majapahit",
    phenotype="Male, 50-60 years old, Javanese phenotype with medium golden brown skin, weathered regal features from years of military campaigns, sharp aristocratic face with determined strategist eyes. Short black hair greying at temples under dark batik blangkon (NOT turban). Full black-and-grey beard neatly trimmed.",
    costume="Wearing Javanese-Islamic sultan attire: dark batik blangkon (Javanese headcap, NOT Arab turban), dark maroon silk royal jacket (atelaan) with gold-thread embroidered Islamic geometric patterns on collar and cuffs, brown batik sarong with parang motif (continuity of Majapahit textile tradition), keris pusaka at waist (sign of royal authority), gold armlets (keyura), leather sandals.",
    props="holding a keris pusaka upright",
    mood="Conqueror-king — Sultan Trenggana, the greatest sultan of Demak. In 1527 he conquered Majapahit's capital at Kediri, then expanded Demak to Surabaya, Pasuruan, Blambangan, Banten, Cirebon, Palembang, and Banjarmasin. A strategic war-leader who blended Javanese royal tradition with Islamic sultan authority.",
    avoid_extra=", turban (must be blangkon), Hindu makuta, Majapahit noble costume, fully Arab costume, Persian costume",
)

K002 = k_prompt(
    name="Sultan Hadiwijaya / Joko Tingkir, King of Pajang",
    era_desc="16th century AD (r. 1549-1581), Pajang, Central Java — founder of Pajang kingdom",
    phenotype="Male, 40-50 years old, Javanese phenotype with golden brown skin, refined aristocratic features, calm diplomatic expression. Short black hair under batik blangkon. Trimmed beard. Medium build from political rather than military life.",
    costume="Wearing Pajang royal attire: batik blangkon, dark green silk jacket with gold calligraphy, brown batik sarong with kawung motif, keris at waist, gold ring. Blends Demak Islamic tradition with restored Javanese court culture. Less martial than Trenggana — more diplomat than warrior.",
    props="holding a royal charter scroll (piagam)",
    mood="The diplomat-king — Hadiwijaya (Joko Tingkir), who moved the capital from Demak to Pajang (near present Surakarta). He defeated the rebel Arya Penangsang and restored stability after Demak's civil war. Under his rule, Javanese court literature and culture revived. The bridge between Demak's militant Islam and Mataram's syncretic tradition.",
    avoid_extra=", turban, Hindu makuta, fully Arab costume",
)

K003 = k_prompt(
    name="Arya Penangsang, regent of Jipang Panolan",
    era_desc="16th century AD (±1540s-1549), Jipang, East Java — tragic rebel prince",
    phenotype="Male, 30-40 years old, Javanese phenotype with golden brown skin, fierce proud features, intense defiant eyes. Long black hair (warrior style, not court style). Muscular build from constant combat. Battle scars on arms and torso. Tattoo marks (traditional warrior tattoos).",
    costume="Wearing Javanese warrior attire: dark batik headband (not blangkon — warrior style), leather chest armor, dark brown batik sarong, keris at waist, gold ear ornaments. No royal regalia — a warrior-prince who claimed the throne by right of blood, not court favor.",
    props="holding a keris and a spear simultaneously",
    mood="The tragic rebel — Arya Penangsang, regent of Jipang, who claimed the Demak throne after Sultan Trenggana's death. A fierce warrior defeated by coalition forces. His death by keris wound to the stomach is one of the most dramatic scenes in Javanese history — immortalized in wayang and chronicle as the fall of a proud prince.",
    avoid_extra=", turban, Islamic scholar costume, modern military uniform",
)

K004 = k_prompt(
    name="Panembahan Senapati, founder of Mataram Sultanate",
    era_desc="late 16th century AD (r. 1587-1601), Mataram, Central Java — founder of Mataram Islam",
    phenotype="Male, 30-40 years old, Javanese phenotype with golden brown skin, sharp ambitious features, intense penetrating eyes. Short black hair under batik blangkon. Lean athletic build from military campaigns. Scar on left cheek.",
    costume="Wearing Mataram founding-era attire: batik blangkon, dark indigo silk jacket with minimal gold trim (not yet full royal regalia — founding king's modesty), brown batik sarong with parang motif, keris pusaka at waist. Blends Islamic authority with Javanese warrior tradition. Lencana: unfinished — still building the kingdom.",
    props="holding a keris pusaka and wearing a battle-scarred leather arm guard",
    mood="The kingdom-builder — Senapati, who took Pajang's territories by force and founded Mataram Sultanate (1587). He moved the capital to Kotagede and began the dynasty that would rule Java for 250 years. His spiritual connections (legend of Nyai Roro Kidul) and military prowess established Mataram's dual legitimacy — sacred and martial.",
    avoid_extra=", turban, fully Arab costume, modern clothing",
)

K005 = k_prompt(
    name="Sunan Prapen, Islamic leader of Giri Kedaton",
    era_desc="16th century AD, Gresik, East Java — leader of Giri religious center",
    phenotype="Male, 50-60 years old, Javanese phenotype with golden brown skin, dignified spiritual features, calm authoritative expression. Short grey hair under white peci. Grey beard trimmed. Medium build.",
    costume="Wearing Giri religious authority attire: white peci (cap), dark green cotton robe, white sarong, simple leather sandals. A wooden prayer bead (tasbih) in hand. No jewelry — religious authority comes from the Giri lineage, not gold. Carries a kitab (Islamic text).",
    props="holding a kitab (Islamic manuscript)",
    mood="The spiritual networker — Sunan Prapen, who continued Sunan Giri's mission of spreading Islam to eastern Indonesia. He sent missionaries to Bali, Lombok, and Sumbawa. His authority rivaled the sultan's — the 'second kingdom' of Giri was both religious center and political power. Sultan Zainal Abidin of Ternate came to Giri to study Islam (1494 AD).",
    avoid_extra=", turban, Hindu costume, modern Islamic scholar costume",
)

K006 = k_prompt(
    name="Hamzah Fansuri, Sufi poet and mystic",
    era_desc="late 16th century AD, Aceh/Barus, Sumatra — greatest Sufi poet of Nusantara",
    phenotype="Male, 40-50 years old, Sumatran Malay phenotype with medium brown skin, deep contemplative features, spiritual intensity in half-closed eyes. Short black hair under simple white cap (songkok). Short beard. Thin build from Sufi ascetic practices.",
    costume="Wearing simple Sufi mystic attire: white songkok, dark blue cotton jubah, white sarong, simple woven cloth sash. No jewelry except a simple carnelian ring (Sufi tradition). Carries a reed pen and ink pot for writing. Barefoot or simple sandals.",
    props="holding a reed pen and a manuscript of his poetry (rubaiyat)",
    mood="The poet-mystic — Hamzah Fansuri, the greatest Sufi poet in Malay literature. His poems (rubaiyat) expressed the doctrine of wahdat al-wujud (Unity of Being) in beautiful Malay verse. He wrote in Barus (Sumatra) and Aceh, connecting Nusantara to the wider Islamic intellectual world. His words still echo in Malay literature 400 years later.",
    avoid_extra=", Hindu costume, Buddhist monk robe, modern Islamic scholar costume, royal attire",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Demak at its peak (first Islamic sultanate capital in Java)",
    era_desc="early 16th century AD, Central Java — capital of Demak sultanate",
    scene_desc="Wide cinematic view of Demak at its peak. The Masjid Agung Demak visible — with distinctive Javanese multi-tiered roof, wooden columns, and mosque compound. Keraton (palace) nearby with defensive walls. Harbor on the Java Sea coast with trading ships. Residential areas with raised wooden houses. Demak was Java's first Islamic capital — from here, the Wali Songo directed the Islamization of Java. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on mosque and harbor), cool 6500K sky fill. Mid contrast 3:1. Morning mist from the coast.",
    mood_desc="First Islamic Java — Demak, where the first Javanese sultan ruled, where the Wali Songo gathered, and where the Masjid Agung stood as the symbol of Islam's triumph over Hindu-Buddhism in Java.",
)

L002 = l_prompt(
    name="Pajang kingdom (Hadiwijaya's capital)",
    era_desc="mid 16th century AD, near present Surakarta, Central Java — Pajang sultanate",
    scene_desc="Wide view of the Pajang kingdom capital. Keraton on elevated ground near a river. Wooden pendopo structures. Irrigated rice paddies surrounding the capital. Tropical forest on hills. Pajang was the successor to Demak — Hadiwijaya moved the capital inland, away from the coast, marking a shift from maritime trade to agrarian rule. The transition between Demak's militant Islam and Mataram's syncretic tradition. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on keraton and paddies), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="The inland turn — Pajang, where Hadiwijaya moved the Islamic capital from the coast to the interior. This shift from maritime Demak to agrarian Pajang set the pattern for Mataram and all subsequent Javanese kingdoms. Islam in Java became less trade-oriented, more court-oriented.",
)

L003 = l_prompt(
    name="Keraton Kasepuhan (Cirebon sultanate palace)",
    era_desc="16th century AD, Cirebon, West Java — palace of the Cirebon sultans",
    scene_desc="Wide view of the Keraton Kasepuhan in Cirebon. Javanese-Islamic palace architecture: pendopo (pavilion) with tiered roof, brick and wood walls, ornate carved gates (lawang). Palace compound with open courtyards. A small mosque within the compound. Decorative tile work showing Chinese and Islamic influence. The palace founded by Sunan Gunung Jati — blending Islamic authority with Javanese-Sundanese court tradition. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, warm on palace walls and carvings), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="The wali's palace — Keraton Kasepuhan, founded by Sunan Gunung Jati. Cirebon was unique: a sultanate founded by a Wali Songo member, where religious authority and political power were held by the same person. The palace architecture shows the fusion: Javanese forms, Islamic function, Chinese decorative tiles.",
)

L004 = l_prompt(
    name="Banten sultanate (western Java Islamic port)",
    era_desc="16th century AD, Banten, West Java — Pepper sultanate",
    scene_desc="Wide view of Banten sultanate capital. Masjid Agung Banten visible (Javanese-style mosque). Harbor with European, Arab, Chinese, and Javanese ships. Pepper warehouses along the coast. Keraton. Banten was founded by Maulana Hasanuddin (son of Sunan Gunung Jati) as a powerful pepper-trading sultanate. The western gateway to Java for international trade. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor and mosque), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="The pepper sultanate — Banten, founded by Sunan Gunung Jati's son, became one of the most powerful Islamic states in Java. Its pepper trade connected it to Europe, China, and the Islamic world. When the Dutch arrived, Banten was a rival to be reckoned with — a Muslim sultanate built on commerce.",
)

L005 = l_prompt(
    name="Giri Kedaton (Sunan Prapen's religious center)",
    era_desc="16th century AD, Gresik, East Java — Islamic learning center and missionary base",
    scene_desc="Wide view of the Giri Kedaton complex on a hill overlooking Gresik. Wooden pendopo structures, a mosque with Javanese-style roof, student dormitories (pondok). The site was Sunan Giri's and later Sunan Prapen's base — a 'second kingdom' whose religious authority rivaled the sultan. From here, missionaries carried Islam to Bali, Lombok, Sumbawa, and Ternate. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on structures and hill), cool 6500K sky fill. Mid contrast 3:1. Distant sea visible.",
    mood_desc="The missionary hill — Giri Kedaton, where the Giri lineage of Islamic scholars trained missionaries for the eastern archipelago. From this hilltop, Islam reached Bali, Lombok, Sumbawa, and even Ternate. A religious center that shaped the faith of half of Indonesia.",
)

L006 = l_prompt(
    name="Aceh Darussalam (Sumatran Islamic sultanate at its peak)",
    era_desc="16th-17th century AD, Aceh — powerful Islamic sultanate",
    scene_desc="Wide cinematic view of Aceh Darussalam capital. Masjid Raya Baiturrahman visible. Sultan's palace (istana) on hill. Harbor with Arab, Turkish, Indian, and Portuguese ships. Cannon fortifications. Aceh was the most powerful Islamic state in Sumatra — 'Serambi Mekkah' (Veranda of Mecca). Under Iskandar Muda, it attacked Portuguese Malacca (1629). Turkish and Arab connections. No people.",
    lighting_desc="warm 4000K late morning sun from camera left (key light, warm on city and harbor), cool 6500K sky fill. Mid contrast 3:1. Sea haze from Indian Ocean.",
    mood_desc="Veranda of Mecca — Aceh Darussalam, the most powerful Islamic sultanate in Sumatra. Its scholars (Hamzah Fansuri, Syamsuddin as-Sumatrani) created a distinctive Sufi intellectual tradition. Its sultans (Iskandar Muda) challenged European power. A center of Islamic learning and military resistance.",
)

L007 = l_prompt(
    name="Kotagede (early Mataram capital, Senapati's seat)",
    era_desc="late 16th century AD (1587-1601), Yogyakarta, Central Java — first Mataram capital",
    scene_desc="Wide view of Kotagede — the first capital of Mataram Sultanate. Wooden keraton (palace) on elevated ground. A mosque with Javanese-style roof nearby. Defensive walls. Surrounded by rice paddies and forest. Kotagede was founded by Panembahan Senapati — the beginning of the Mataram dynasty that would rule Java for 250 years. Silver workshops visible (Kotagede later became famous for silver). No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on keraton and paddies), cool 6500K sky fill. Mid contrast 3:1. Morning mist.",
    mood_desc="The founding seat — Kotagede, where Senapati established Mataram Sultanate. From this small fortified town, the Mataram dynasty grew to rule all of Java. The mosque, the palace, and the royal cemetery here are the foundation of 250 years of Javanese Islamic kingship.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Lawang Bledeg (Sunan Bonang's door, Demak mosque)",
    era_desc="early 16th century AD, Masjid Agung Demak — carved door with cosmological motifs",
    scene_desc="A detailed carved wooden door (lawang) on dark background. Visible: intricate interlocking wood carving (tattik) with Islamic geometric patterns blended with Javanese cosmological motifs (including stylized lighting bolts — 'bledeg'). The door is from the Masjid Agung Demak, attributed to Sunan Bonang. Approximately 2.5 meters tall, made of teak wood, with deep relief carving showing gold leaf traces. The fusion of Islamic geometry and Javanese cosmology.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing carved relief and wood grain), low ambient fill. High contrast 5:1.",
    mood_desc="The door of fusion — Lawang Bledeg, where Islamic geometric patterns meet Javanese cosmological symbolism. The carved door of Demak mosque shows that Islamization was not erasure but fusion — the old worldview did not disappear, it was absorbed into the new faith.",
)

A002 = a_prompt(
    name="Wayang kulit Punakawan figures (Javanese-Islamic cultural tool)",
    era_desc="16th century AD, Java — wayang puppets used by Sunan Kalijaga for Islamic teaching",
    scene_desc="3-4 wayang kulit (shadow puppet) figures on dark background, displayed flat. Visible: Semar (the fat, wise servant), Gareng (the deformed philosopher), and Bagong (the simple truth-teller). Each puppet is approximately 50 cm tall, made of buffalo hide with buffalo horn handles (gapit), painted in gold, red, blue, and white. These are the Punakawan — the Javanese servants who are not in the Indian Mahabharata but were created by Javanese culture. Sunan Kalijaga used them to teach Islamic values through familiar Javanese characters.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing leather texture and paint), low ambient fill from a backlight screen (simulating wayang screen). High contrast 5:1.",
    mood_desc="Culture as dakwah — the Punakawan puppets, Sunan Kalijaga's method of spreading Islam. He didn't destroy wayang; he transformed it. Semar became the voice of Sufi wisdom. Through familiar characters, Islamic values reached Javanese commoners in their own language.",
)

A003 = a_prompt(
    name="Manuskrip Syarab al-Asyiqin (Hamzah Fansuri's Sufi poetry)",
    era_desc="late 16th century AD, Aceh/Barus — Hamzah Fansuri's Sufi manuscript",
    scene_desc="An opened manuscript on dark surface. Visible: Jawi script (Arabic script for Malay language) in black ink on brown paper. The text is 'Syarab al-Asyiqin' (The Drink of Lovers) — Hamzah Fansuri's Sufi treatise on wahdat al-wujud (Unity of Being). The manuscript shows careful calligraphy with some marginal annotations. Approximately 20 cm tall, bound in leather. 4-5 pages visible.",
    lighting_desc="warm 2700K raking light from camera right (key light, revealing ink texture and paper fibers), low ambient fill. High contrast 4:1.",
    mood_desc="Words of the mystic — the Syarab al-Asyiqin manuscript, where Hamzah Fansuri wrote in beautiful Jawi Malay about the mystical journey of the soul toward Unity. His work connected Nusantara to the great Sufi intellectual tradition spanning from Andalusia to Indonesia.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the court of Demak — sultan, wali, and warrior",
    era_desc="early 16th century AD, Demak, Central Java",
    composition="Group of 4 individuals in a court scene pose. Position 1 (center, elevated): Sultan Trenggana, seated on a raised chair, wearing dark maroon royal jacket with gold embroidery, batik blangkon, keris at waist. Position 2 (left): Sunan Kalijaga, standing with wayang puppet, wearing batik blangkon and green jubah — the cultural advisor. Position 3 (right): a Demak warrior (makasirkasir), standing with spear and leather armor — the military arm. Position 4 (far right): a court scribe, sitting cross-legged with Jawi manuscript — the administrative pillar. All wearing Javanese-Islamic attire blending Islamic and Javanese traditions.",
    mood="The three pillars of Islamic Java — Demak's court combined royal authority (sultan), religious legitimacy (wali), and military power (warrior). Under this triangle, Java was transformed from Hindu-Buddhist to Muslim — not through foreign conquest, but through indigenous leaders who adopted and adapted Islam.",
    k_refs=["3B-K001 (Sultan Trenggana)", "3A-K003 (Sunan Kalijaga)"],
    avoid_extra=", Hindu costume, turban (must be blangkon), fully Arab costume, modern clothing",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "3B-K001-sultan-trenggana.txt": K001,
        "3B-K002-sultan-hadiwijaya.txt": K002,
        "3B-K003-arya-penangsang.txt": K003,
        "3B-K004-panembahan-senapati.txt": K004,
        "3B-K005-sunan-prapen.txt": K005,
        "3B-K006-hamzah-fansuri.txt": K006,
        # L — 7
        "3B-L001-demak.txt": L001,
        "3B-L002-pajang.txt": L002,
        "3B-L003-keraton-kasepuhan.txt": L003,
        "3B-L004-banten.txt": L004,
        "3B-L005-giri-kedaton.txt": L005,
        "3B-L006-aceh.txt": L006,
        "3B-L007-kotagede.txt": L007,
        # A — 3
        "3B-A001-lawang-bledeg.txt": A001,
        "3B-A002-wayang-punakawan.txt": A002,
        "3B-A003-manuskrip-syarab-asyiqin.txt": A003,
        # S — 1
        "3B-S001-pendapa-demak.txt": S001,
    }

    # Delete ALL old v1 files
    old_dir = os.listdir(OUTPUT_DIR)
    for f in old_dir:
        if f.endswith(".txt"):
            os.remove(os.path.join(OUTPUT_DIR, f))
            print(f"  Deleted: {f}")

    for filename, content in prompts.items():
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            f.write(content)
        print(f"  Created: {filename}")

    print(f"\n✅ Total: {len(prompts)} files (v2.1)")
    print(f"   K: 6 | L: 7 | A: 3 | S: 1")

if __name__ == "__main__":
    main()
