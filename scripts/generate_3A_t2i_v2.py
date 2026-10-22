#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 3A — Islamisasi Awal (Abad 7-1511 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/3A-islamisasi-awal/prompts"

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
    name="Sultan Malik al-Saleh (formerly Merah Silu), founder of Samudra Pasai",
    era_desc="late 13th century AD (died ±1297), North Sumatra — first Muslim sultan in Southeast Asia",
    phenotype="Male, 50-60 years old, Sumatran Malay phenotype with medium brown skin, dignified regal features with serene convert's expression. Short-cropped black hair turning grey at temples. Full but neatly trimmed grey-black beard.",
    costume="Wearing early Malay-Islamic royal attire: white turban (sorban) wrapped around head, dark green silk robe with gold-thread embroidery of Arabic calligraphy border, gold sash (pending) at waist, keris pusaka at left waist, simple gold ring with Arabic inscription on right index finger. Recently converted — modest Islamic dignity blended with Malay royal tradition.",
    props="holding a Qur'an on a wooden stand (rehal)",
    mood="First sultan — Merah Silu converted to Islam via dream of Prophet Muhammad, took the name Malik al-Saleh, and founded Samudra Pasai — the first Islamic kingdom in Southeast Asia. His conversion began the long process of Islamization that would transform Nusantara over the next 300 years.",
    avoid_extra=", Hindu-Buddhist costume, Hindu makuta, Javanese keraton costume, Arab Bedouin costume, Persian costume",
)

K002 = k_prompt(
    name="Sunan Ampel (Raden Rahmat), Wali Songo member",
    era_desc="15th century AD (1400-1481), Ampel Denta, Surabaya — early Islamic teacher",
    phenotype="Male, 50-60 years old, mixed Arab-Javanese phenotype with light brown skin, wise gentle features, scholarly expression. Short grey beard trimmed. Wearing simple white turban. Lean build from scholarly and teaching life.",
    costume="Wearing simple Islamic scholar attire: white turban, dark blue cotton robe (gamis/jubah), white cotton sarong, simple leather sandals. No jewelry — a teacher's authority comes from knowledge, not gold. Carrying a prayer bead (tasbih).",
    props="holding a tasbih (prayer beads)",
    mood="The teacher — Sunan Ampel, descendant of Arab traders, established the pesantren (Islamic boarding school) at Ampel Denta. His students included future kings and other Wali Songo. He represents the scholarly, peaceful approach to Islamization — conversion through education, not conquest.",
    avoid_extra=", Hindu costume, Buddhist monk robe, modern Islamic scholar costume",
)

K003 = k_prompt(
    name="Sunan Kalijaga, Wali Songo member (cultural Islamizer)",
    era_desc="15th-16th century AD (±1450-1586), Central Java — Sufi mystic and cultural adapter",
    phenotype="Male, 50-60 years old, Javanese phenotype with golden brown skin, warm charismatic features, serene Sufi expression with hint of mischief. Long grey-black hair (not cropped — Kalijaga was a mystic, not a conventional scholar). Thin build from ascetic wandering. Wearing simple batik.",
    costume="Wearing Javanese-Islamic attire: simple batik blangkon (headcap, NOT turban), plain green cotton jubah over batik sarong, wooden prayer beads. No shoes — barefoot mystic. Simple iron ring. Kalijaga blended Javanese culture (wayang, gamelan) with Islamic teachings.",
    props="holding a wayang kulit puppet (puppet used for Islamic teaching)",
    mood="The cultural bridge — Sunan Kalijaga used wayang (shadow puppet theater) and gamelan to spread Islam among Javanese commoners. He understood that faith must speak the people's language, wear their clothes, play their music. The most beloved of the Wali Songo — a Sufi who found God in Javanese culture.",
    avoid_extra=", Arab costume, turban (must be blangkon), Hindu costume, modern clothing",
)

K004 = k_prompt(
    name="Sunan Giri (Raden Paku), Wali Songo member",
    era_desc="15th-16th century AD (1443-1505), Gresik, East Java — Islamic educator and political advisor",
    phenotype="Male, 40-50 years old, Javanese-Bugis mixed phenotype with golden brown skin, sharp intelligent features, determined expression. Short black hair under white cap (peci). Trimmed beard. Medium build.",
    costume="Wearing Islamic educator attire: white peci (cap), dark green cotton robe, white sarong, simple leather belt. Giri was both religious teacher and political leader — his pesantren at Giri was a center of Islamic learning that trained missionaries for eastern Indonesia.",
    props="holding a kitab (Islamic text) bound in leather",
    mood="The educator-king — Sunan Giri built a pesantren that became so powerful it was called a 'second kingdom.' From Giri, missionaries were sent to Bali, Lombok, Sumbawa, and even Ternate. His network of students spread Islam across the eastern archipelago.",
    avoid_extra=", Hindu costume, turban, modern clothing",
)

K005 = k_prompt(
    name="Sunan Gunung Jati (Syarif Hidayatullah), Wali Songo member",
    era_desc="15th-16th century AD (1448-1568), Cirebon, West Java — founder of Cirebon sultanate",
    phenotype="Male, 50-60 years old, mixed Arab-Sundanese phenotype with light brown skin, commanding features, authoritative expression blending spiritual and military bearing. Short grey beard. Short black hair under white turban. Stocky build.",
    costume="Wearing Cirebon sultan attire: white turban, dark blue silk robe with gold calligraphy, batik parang sarong, keris at waist, gold ring. Blends Islamic authority with Sundanese-Javanese royal tradition. Military-spiritual leader who conquered Sunda Kelapa (renamed Jayakarta, later Jakarta).",
    props="holding a keris pusaka and a prayer bead simultaneously",
    mood="The conqueror-saint — Sunan Gunung Jati combined Sufi spirituality with military conquest. He founded the Cirebon sultanate, conquered Sunda Kelapa (1527), and expanded Islamic influence in West Java. A wali who was both prayer leader and military commander.",
    avoid_extra=", Hindu costume, modern military uniform, Arab Bedouin costume",
)

K006 = k_prompt(
    name="Parameswara, founder of Malacca Sultanate",
    era_desc="15th century AD (1400-1424), Malacca — founder of the Malacca Sultanate",
    phenotype="Male, 40-50 years old, Sumatran Malay phenotype with medium brown skin, shrewd diplomatic features, ambitious expression. Short black hair under simple songkok. Trimmed beard. Medium build from trading and political life.",
    costume="Wearing early Malacca sultan attire: simple songkok (cap, not turban), dark red silk robe, woven songket sarong, gold chain, keris at waist. Parameswara was a Hindu prince from Palembang/Singapura who converted to Islam after marrying a Pasai princess. Took the name Iskandar Shah.",
    props="holding a diplomatic letter (surat)",
    mood="The opportunist-founder — Parameswara, a refugee prince from Singapura, founded Malacca around 1400. After converting to Islam (taking name Iskandar Shah), he built Malacca into the greatest trading port in Southeast Asia. His sultanate controlled the strait that bore his city's name, making Islam the dominant maritime culture.",
    avoid_extra=", Hindu makuta, Javanese keraton costume, Arab costume, modern clothing",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Samudra Pasai (first Islamic sultanate in Southeast Asia)",
    era_desc="13th-16th century AD, North Sumatra — first Muslim kingdom in Nusantara",
    scene_desc="Wide cinematic view of the Samudra Pasai coastal settlement. Wooden houses on stilts along a calm bay. Small harbor with Arab dhow and Malay perahu. A simple wooden mosque visible. Muslim cemetery with carved stone nisans (grave markers). Coconut palms and tropical forest. The first place where Islam took political root in Southeast Asia — Malik al-Saleh's kingdom. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on bay and settlement), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="First Islam — Samudra Pasai, where the first Muslim sultanate in Southeast Asia was established. From this small North Sumatran port, Islam would spread to Malacca, then to Java, and eventually across the entire archipelago.",
)

L002 = l_prompt(
    name="Malacca (greatest trading port of Southeast Asia)",
    era_desc="15th-16th century AD, Malacca — cosmopolitan Islamic trade hub",
    scene_desc="Wide cinematic view of Malacca harbor at its peak. Massive harbor with ships from Arabia, India, China, and Nusantara. Wooden godowns (warehouses) along shore. Sultan's palace on hill. Mosque with minaret visible. Market stalls with spices, silk, ceramics, and gold. The busiest port in Southeast Asia — where the Indian Ocean and South China Sea trade networks met under Islamic rule. No people.",
    lighting_desc="warm 4000K late morning sun from camera left (key light, golden on harbor and city), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="The emporium — Malacca, the greatest port in Southeast Asian history. Under the sultanate, it controlled the strait, taxed the trade, and spread Islam through commerce. When the Portuguese took it in 1511, it was the end of Muslim Malay maritime supremacy.",
)

L003 = l_prompt(
    name="Lobu Tua / Barus (Tamil merchant settlement, West Sumatra)",
    era_desc="9th-15th century AD, Tapanuli Tengah, Sumatra — international camphor trade port",
    scene_desc="Wide view of the Barus coastal port at Lobu Tua. Natural harbor. Tamil merchant quarter with small Hindu shrine and stone inscription (1088 AD, the 'Five Hundred of Ayyavole' guild). Arab merchant quarter with small mosque. Camphor processing area. The port where Tamil, Arab, and Batak traders met. Source of kapur barus (camphor) — the most valuable commodity of ancient Nusantara. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="Cosmopolitan port — Barus/Lobu Tua, where Tamil Hindus and Arab Muslims traded side by side. The Tamil inscription (1088 AD) records the merchant guild that made this port their home. Where Islam first touched Sumatra's west coast through Arab traders.",
)

L004 = l_prompt(
    name="Gresik (early Islamic trade port, East Java)",
    era_desc="14th-16th century AD, East Java — earliest Islamic settlement in Java",
    scene_desc="Wide view of the Gresik coastal port. Harbor with merchant ships from Malacca, India, and Arabia. Wooden houses and warehouses on stilts. A simple early mosque (masjid agung). Muslim cemetery with carved stone nisans. Gresik was one of the first places where Islam took root in Java — through trade, not conquest. Chinese, Arab, and Javanese Muslim communities coexisted. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, golden on port and mosque), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="Java's Islamic doorway — Gresik, where the first Muslims in Java settled among Chinese and Arab traders. Sunan Gresik (Maulana Malik Ibrahim) arrived here in the early 1400s, beginning the Wali Songo era. Trade and faith walked hand in hand on this beach.",
)

L005 = l_prompt(
    name="Ampel Denta (Sunan Ampel's pesantren, Surabaya)",
    era_desc="15th century AD, Surabaya, East Java — first Islamic school in Java",
    scene_desc="Wide view of the Ampel Denta pesantren complex. Simple wooden structures on raised platforms. A small mosque with minimal architecture (Javanese-style roof, not Arab dome). Student dormitories (pondok). The site where Sunan Ampel taught Islam to future Wali Songo and Javanese nobility. Tropical setting near Surabaya coast. The first center of Islamic education in Java. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on wooden structures), cool 6500K sky fill. Mid contrast 3:1. Morning mist.",
    mood_desc="The first school — Ampel Denta, where Sunan Ampel established Java's first pesantren. From here, the Wali Songo movement radiated outward. Education, not conquest, was the method. Students carried Islam from this modest compound to every corner of Java.",
)

L006 = l_prompt(
    name="Giri Kedaton (Sunan Giri's religious center, Gresik)",
    era_desc="15th-16th century AD, Gresik, East Java — Islamic learning center and 'second kingdom'",
    scene_desc="Wide view of the Giri Kedaton complex on a hill overlooking Gresik. Wooden pendopo (pavilion) structures. A mosque with Javanese-style multi-tiered roof (not Arab dome). Student quarters. The site was so powerful it was called a 'second kingdom' — Sunan Giri's religious authority rivaled the sultan of Demak. Missionaries trained here were sent to Bali, Lombok, Sumbawa, and Ternate. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on structures and hill), cool 6500K sky fill. Mid contrast 3:1. Sea visible in distance.",
    mood_desc="The second kingdom — Giri Kedaton, where Sunan Giri built a center of Islamic learning so powerful that it rivaled the sultan of Demak. From this hill, missionaries carried Islam to the eastern archipelago — Bali, Lombok, Sumbawa, even Ternate.",
)

L007 = l_prompt(
    name="Demak (first Islamic sultanate in Java)",
    era_desc="15th-16th century AD, Central Java — first Muslim kingdom in Java",
    scene_desc="Wide view of the Demak sultanate capital. The Demak Great Mosque (Masjid Agung Demak) visible — with its distinctive Javanese multi-tiered roof (not Arab dome), wooden columns, and mosque compound. Royal palace (keraton) nearby. Defensive walls. Demak was the first Islamic kingdom in Java, founded by Raden Patah in the late 1400s. From Demak, the Wali Songo launched the Islamization of Java. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on mosque and palace), cool 6500K sky fill. Mid contrast 3:1. Morning mist.",
    mood_desc="Java's first Islamic state — Demak, where the Wali Songo gathered, where the first Javanese sultan ruled, and where the Masjid Agung stood as a symbol of the new faith. From this small Central Javanese town, Islam replaced Hindu-Buddhism as the religion of Java's rulers.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Nisan Malik al-Saleh (oldest Islamic grave marker in Southeast Asia)",
    era_desc="1297 AD, Samudra Pasai, North Sumatra — earliest Islamic tomb in Nusantara",
    scene_desc="A carved stone nisan (grave marker) made of Acehneses stone. Visible: Arabic calligraphy in relief, with ornate floral and geometric border patterns. The stone is approximately 1.5 meters tall, weathered grey-white. This is the tombstone of Sultan Malik al-Saleh, the first Muslim sultan in Southeast Asia, dated 1297 AD (696 AH). The stone shows a blend of Indian, Arabic, and local artistic traditions.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing carved calligraphy and stone texture), low ambient fill. High contrast 5:1.",
    mood_desc="The first Muslim grave — the nisan of Malik al-Saleh, dated 1297 AD. The oldest physical evidence of Islam in Southeast Asia. A stone that marks the beginning of a religious transformation that would remake the entire archipelago.",
)

A002 = a_prompt(
    name="Masjid Agung Demak (Javanese-style mosque architecture)",
    era_desc="15th-16th century AD, Demak, Central Java — prototype of Javanese mosque",
    scene_desc="A detailed architectural model/fragment of the Masjid Agung Demak. Visible: the distinctive Javanese multi-tiered roof (tumpang tiga — three stacked roofs, NOT Arab dome), wooden pillars (saka guru — four main pillars), carved wooden mihrab (prayer niche), and decorative mustaka (finial) on roof peak. The mosque blends Islamic function with Javanese architectural tradition. 1:50 scale model. Wood and tile materials visible.",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing wood grain and architectural detail), low ambient fill. High contrast 4:1.",
    mood_desc="Javanese Islam in wood and tile — the Masjid Agung Demak, prototype of the Javanese mosque. Not an Arab dome, but a Javanese tiered roof. Not a desert minaret, but Javanese mustaka. The Wali Songo understood that Islam in Java must speak Javanese — even in architecture.",
)

A003 = a_prompt(
    name="Koin emas dinasti Umayyah dan Abbasiyah (early Islamic coins in Nusantara)",
    era_desc="7th-10th century AD, found at Bongal, North Sumatra — earliest Islamic artifacts",
    scene_desc="5-7 gold and silver coins on dark velvet. Visible: Arabic calligraphy (Quranic verses) stamped on coins. Dinasti Umayyah (7th-8th century) and Abbasiyah (8th-10th century) coins. These coins were found at the Bongal site in North Sumatra, proving that Arab Muslim traders reached Nusantara as early as the 7th century — contemporaneous with the rise of Islam itself. Coins show wear from circulation. Each 1.5-2.5 cm.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing gold luster and Arabic calligraphy), low ambient fill. High contrast 4:1.",
    mood_desc="First contact — these Islamic coins from the Umayyah and Abbasiyah caliphates, found in North Sumatra, prove that Arab Muslim traders reached Nusantara in the 7th century. Within a hundred years of Prophet Muhammad's death, Islam had reached the edge of Southeast Asia through trade.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the Wali Songo — nine saints of Islam in Java",
    era_desc="15th-16th century AD, Java — the nine Islamic missionaries who converted Java",
    composition="Group of 5 individuals (representing the most prominent Wali Songo) in a natural standing group pose. Position 1 (left): Sunan Ampel, holding tasbih prayer beads, wearing white turban and dark blue robe. Position 2 (center-left): Sunan Kalijaga, holding wayang puppet, wearing batik blangkon and green jubah. Position 3 (center): Sunan Giri, holding kitab, wearing white peci and green robe. Position 4 (center-right): Sunan Gunung Jati, holding keris and prayer beads, wearing white turban and dark blue robe. Position 5 (right): Sunan Gresik (Maulana Malik Ibrahim), holding a Qur'an, wearing white turban and beige robe. All wearing distinctive Javanese-Islamic attire blending Islamic and local traditions.",
    mood="The nine saints — Wali Songo, the religious teachers who brought Islam to Java not by conquest but by culture, education, and adaptation. Each wali had a different approach: scholarship (Ampel), culture (Kalijaga), education (Giri), military (Gunung Jati), trade (Gresik). Together they transformed Java from Hindu-Buddhist to Muslim.",
    k_refs=["3A-K002 (Sunan Ampel)", "3A-K003 (Sunan Kalijaga)", "3A-K004 (Sunan Giri)", "3A-K005 (Sunan Gunung Jati)"],
    avoid_extra=", Hindu costume, Buddhist monk robe, Arab Bedouin costume, modern Islamic clothing",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "3A-K001-malik-al-saleh.txt": K001,
        "3A-K002-sunan-ampel.txt": K002,
        "3A-K003-sunan-kalijaga.txt": K003,
        "3A-K004-sunan-giri.txt": K004,
        "3A-K005-sunan-gunung-jati.txt": K005,
        "3A-K006-parameswara.txt": K006,
        # L — 7
        "3A-L001-samudra-pasai.txt": L001,
        "3A-L002-malaka.txt": L002,
        "3A-L003-lobu-tua-barus.txt": L003,
        "3A-L004-gresik.txt": L004,
        "3A-L005-ampel-denta.txt": L005,
        "3A-L006-giri-kedaton.txt": L006,
        "3A-L007-demak.txt": L007,
        # A — 3
        "3A-A001-nisan-malik-al-saleh.txt": A001,
        "3A-A002-masjid-demak.txt": A002,
        "3A-A003-koin-islam-bongal.txt": A003,
        # S — 1
        "3A-S001-wali-songo.txt": S001,
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
