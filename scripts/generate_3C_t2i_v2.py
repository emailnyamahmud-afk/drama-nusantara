#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 3C — Mataram Islam (Abad 17-18 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/3C-mataram-islam/prompts"

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
    name="Sultan Agung, Sultan of Mataram",
    era_desc="17th century AD (1613-1645), Mataram, Central Java — greatest Mataram sultan",
    phenotype="Male, 35-45 years old, Javanese phenotype with golden brown skin, sharp regal features, intense determined eyes, commanding presence. Black hair under batik blangkon, full black beard. Muscular build from military campaigns. Battle scars on arms.",
    costume="Wearing Mataram sultan attire: ornate batik blangkon (headcap, NOT turban), dark indigo silk royal jacket with gold-thread embroidered Suluk/Astabrata motifs, brown batik sarong with parang rusak pattern (symbol of broken enemies), keris pusaka at waist, gold armlets, leather sandals. Lencana: Garudamukha (continuing Majapahit tradition).",
    props="holding a keris pusaka and a Qur'an simultaneously",
    mood="'Majapahit Baru' — Sultan Agung, the greatest king of Mataram. He saw himself as the successor of Majapahit, expanded Mataram to its greatest extent (Surabaya 1625, Giri 1636, Blambangan 1640), attacked Batavia twice (1628, 1629), and created the Islamic-Javanese calendar (1633). A warrior-king who blended Islamic faith with Javanese royal tradition.",
    avoid_extra=", turban (must be blangkon), Hindu makuta, fully Arab costume, European costume, modern clothing",
)

K002 = k_prompt(
    name="Amangkurat I, Sultan of Mataram",
    era_desc="17th century AD (1646-1677), Mataram, Central Java — the tyrant sultan",
    phenotype="Male, 40-50 years old, Javanese phenotype with pale complexion from palace isolation, suspicious paranoid eyes, thin lips, gaunt face. Black hair under batik blangkon. Thin build from stress and indulgence. Dark circles under eyes.",
    costume="Wearing Mataram sultan attire: batik blangkon, dark black silk jacket with minimal gold (mourning/authoritarian style), black batik sarong, keris at waist. Gold armlets but no decorative jewelry — authority through fear, not display.",
    props="holding a keris with a tense, suspicious grip",
    mood="The tyrant — Amangkurat I, who murdered 5,000-6,000 ulama and their families at Gebang Kedaton (1646) to prevent political opposition. His paranoid absolutism destroyed Mataram's religious base and led to the Trunojoyo rebellion. A king who ruled through terror and died in exile.",
    avoid_extra=", turban, Islamic scholar costume, European costume, modern clothing",
)

K003 = k_prompt(
    name="Sultan Hamengkubuwana I / Pangeran Mangkubumi, founder of Yogyakarta",
    era_desc="18th century AD (1755-1792), Yogyakarta — founder of Yogyakarta sultanate",
    phenotype="Male, 40-50 years old, Javanese phenotype with golden brown skin, sharp intelligent features, calm but determined expression combining warrior and scholar. Black hair under batik blangkon, grey-streaked beard. Medium build — warrior turned statesman.",
    costume="Wearing Yogyakarta sultan attire: ornate batik blangkon with gold pin, dark green silk jacket (jubah) with elaborate gold-thread embroidery, brown batik sarong with Grombol motif (Yogyakarta style), keris pusaka at waist, gold armlets. The costume shows Mataram tradition refined — not just conquered, but elevated.",
    props="holding a keris pusaka and the Perjanjian Giyanti scroll",
    mood="The divider-creator — Pangeran Mangkubumi, who rebelled against VOC-backed Pakubuwana II, fought the Dutch to a stalemate, then signed the Treaty of Giyanti (1755) splitting Mataram into Yogyakarta and Surakarta. He built Yogyakarta as a new capital — Keraton Yogyakarta — designed as a cosmic mandala. From rebel to founding sultan.",
    avoid_extra=", turban, European costume, modern clothing, Hindu costume",
)

K004 = k_prompt(
    name="Sultan Iskandar Muda, Sultan of Aceh Darussalam",
    era_desc="17th century AD (1607-1636), Aceh — greatest Aceh sultan",
    phenotype="Male, 30-40 years old, Sumatran Malay phenotype with medium brown skin, commanding features, fierce intelligent eyes, short trimmed beard. Black hair under white turban (Aceh style — different from Javanese blangkon). Muscular build from military and maritime life.",
    costume="Wearing Aceh sultan attire: white turban (Aceh-style wrapping, different from Arab), dark crimson silk robe with gold-thread Ottoman-influenced embroidery, woven songket sarong, keris at waist, gold ring with Arabic inscription. Aceh had diplomatic relations with Ottoman Turkey — costume shows Turkish-Islamic influence.",
    props="holding a ceremonial sword (pedang) and a letter from Ottoman Turkey",
    mood="The northern giant — Sultan Iskandar Muda, under whom Aceh reached its peak. He attacked Portuguese Malacca with 19,000 troops (1629, failed), maintained diplomatic relations with Ottoman Turkey, and patronized Sufi scholars (Hamzah Fansuri, Syamsuddin as-Sumatrani). Aceh under him was 'Serambi Mekkah' — the Veranda of Mecca.",
    avoid_extra=", Javanese blangkon (must be turban), Hindu costume, European costume, modern clothing",
)

K005 = k_prompt(
    name="Sultan Hasanuddin, Sultan of Gowa-Tallo (Makassar)",
    era_desc="17th century AD (1653-1669), Makassar, South Sulawesi — 'Rooster of the East'",
    phenotype="Male, 30-40 years old, Bugis-Makassar phenotype with golden brown skin, strong angular features, fierce determined eyes. Short black hair under simple Makassar-style headcloth (not turban, not blangkon). Muscular stocky build from maritime warrior life. Battle scars.",
    costume="Wearing Makassar sultan attire: colorful woven headcloth (destar/lipaa), dark red silk jacket with gold embroidery, woven Makassar sarong with geometric patterns, keris (Makassar style — different from Javanese), gold armlets. The costume blends Bugis-Makassar tradition with Islamic authority.",
    props="holding a keris and a Badjak (Makassar war shield)",
    mood="The Rooster of the East — Sultan Hasanuddin, who fought the VOC for 14 years (1655-1669) in the Makassar War. He refused to submit to Dutch trade monopoly, built alliances with local powers, and became a symbol of resistance. The Dutch called him 'De Haantjes van het Oosten' — the Rooster of the East. He finally surrendered in 1669, but never submitted in spirit.",
    avoid_extra=", Javanese blangkon, turban, European costume, modern clothing",
)

K006 = k_prompt(
    name="Trunojoyo, Madurese rebel leader",
    era_desc="17th century AD (1674-1679), Madura/Mataram — rebel who destroyed Mataram's capital",
    phenotype="Male, 25-35 years old, Madurese phenotype with medium brown skin, lean sharp features, intense revolutionary eyes. Long black hair tied back (warrior style, not court style). Lean muscular build from guerrilla warfare. Scar across forehead.",
    costume="Wearing Madurese warrior attire: simple dark headcloth, brown cotton shirt, dark batik sarong, keris at waist, leather arm guard. No royal regalia — a rebel's simplicity. Carrying a spear and a captured VOC musket.",
    props="holding a spear and a captured VOC musket",
    mood="The destroyer — Trunojoyo, the Madurese prince who rebelled against Amangkurat I's tyranny. His forces sacked the Mataram capital at Plered (1677), forcing Amangkurat to flee and die in exile. He was supported by Karaeng Galesong of Makassar. A rebel who brought down a sultan, only to be betrayed and executed by the VOC.",
    avoid_extra=", royal costume, turban, European costume, modern clothing",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Karta / Plered (Mataram sultanate capital)",
    era_desc="17th century AD (1613-1677/1680), Central Java — Mataram capital before Kartasura",
    scene_desc="Wide cinematic view of the Mataram capital at Karta/Plered. Keraton (palace) complex on elevated ground near the Opak river. Wooden pendopo structures with tile roofs. Alun-alun (town square) with banyan trees. A grand mosque with Javanese-tiered roof. Royal cemetery (makam) nearby. Irrigated rice paddies surrounding the capital. Distant Mount Merapi. Sultan Agung's capital — the heart of Java's greatest Islamic kingdom. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on keraton and paddies), cool 6500K sky fill. Mid contrast 3:1. Morning mist from Opak river.",
    mood_desc="Sultan Agung's capital — Karta/Plered, where Sultan Agung ruled the greatest Mataram. From here he launched attacks on Batavia, issued the Islamic-Javanese calendar, and governed an empire stretching from East Java to West Java. This was the capital that Trunojoyo sacked in 1677.",
)

L002 = l_prompt(
    name="Batavia (VOC headquarters, 1619-1740)",
    era_desc="17th-18th century AD, Jakarta — VOC colonial headquarters",
    scene_desc="Wide cinematic view of Batavia (Jakarta) in the 17th century. VOC fort (Kasteel Batavia) with European-style stone walls and cannons. Dutch-style houses along canals (grachten). Chinese quarter visible. Harbor with VOC ships (fluyt, galjon). The city J.P. Coen built in 1619 on the ruins of Jayakarta. A European colonial city in tropical Asia. Canals, drawbridges, and Dutch architecture contrasting with tropical vegetation. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, golden on fort and canals), cool 6500K sky fill. Mid contrast 3:1. Tropical haze.",
    mood_desc="The colonial city — Batavia, the VOC's Asian headquarters. Built on conquered land, fortified with European walls, laced with Dutch canals. From here the VOC controlled the spice trade, fought Mataram, and eventually dominated Java. The 'Queen of the East' that would become Jakarta.",
)

L003 = l_prompt(
    name="Aceh Darussalam (Kutaraja, Sumatran sultanate capital)",
    era_desc="17th century AD, Aceh — 'Serambi Mekkah' (Veranda of Mecca)",
    scene_desc="Wide view of Aceh Darussalam capital at Kutaraja. Masjid Raya Baiturrahman visible (mosque with white dome and minaret). Sultan's palace (Dalam) on hill. Harbor with ships from Turkey, India, Arabia, and Portugal. Cannon fortifications along coast. Aceh was the most powerful Islamic state in Sumatra under Iskandar Muda. Tropical forest behind city. Indian Ocean visible. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on mosque and harbor), cool 6500K sky fill. Mid contrast 3:1. Indian Ocean sea mist.",
    mood_desc="Veranda of Mecca — Aceh Darussalam, the most powerful Islamic sultanate in western Nusantara. Under Iskandar Muda, its influence reached Malacca, Turkey, and India. Its Sufi scholars (Hamzah Fansuri, Syamsuddin) created a distinctive intellectual tradition. A fortress of Islam on the Indian Ocean.",
)

L004 = l_prompt(
    name="Gowa-Tallo / Makassar (South Sulawesi sultanate)",
    era_desc="17th century AD (1593-1669), Makassar, South Sulawesi",
    scene_desc="Wide view of the Makassar sultanate capital. Fort Rotterdam (VOC-built after conquest, but originally a Gowa fort). Sultan's palace. Harbor with Makassar perahu (phinisi ships) and VOC warships. Makassar was a free trade port that defied the VOC monopoly — open to all traders regardless of nationality. Tropical coast with limestone hills. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor and fort), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="The free port — Makassar/Gowa-Tallo, where Sultan Hasanuddin defied the VOC for 14 years. Makassar was a truly cosmopolitan port: Bugis, Makassarese, Malay, Chinese, Arab, and European traders all traded freely. The VOC destroyed this freedom in 1669, but the spirit of resistance lived on in the Bugis diaspora.",
)

L005 = l_prompt(
    name="Keraton Yogyakarta (Hamengkubuwana I's capital)",
    era_desc="18th century AD (1755+), Yogyakarta — new Mataram capital after Giyanti",
    scene_desc="Wide cinematic view of the Keraton Yogyakarta (Yogyakarta Palace). Javanese palace architecture: pendopo agung (grand pavilion) with high ceiling, carved wooden pillars (saka guru), open courtyards. Alun-alun (square) with banyan trees in front. Tugu (monument) visible in distance. Mount Merapi on horizon. The palace was designed by Hamengkubuwana I as a cosmic mandala — the center of the Javanese universe. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on pendopo and courtyard), cool 6500K sky fill. Mid contrast 3:1. Morning mist from Mount Merapi.",
    mood_desc="The cosmic palace — Keraton Yogyakarta, built by Hamengkubuwana I after the Treaty of Giyanti (1755). Every element is symbolic: the layout faces Mount Merapi to the north and the South Sea to the south, forming a sacred axis. A palace designed not just for governance but as a physical representation of Javanese cosmology.",
)

L006 = l_prompt(
    name="Kartasura (Mataram capital after Plered, 1680-1742)",
    era_desc="17th-18th century AD (1680-1742), Central Java — Mataram capital after Trunojoyo's destruction",
    scene_desc="Wide view of Kartasura — Mataram's second capital. Keraton on lower ground than Karta. Simpler wooden structures (rebuilt after Trunojoyo's sack of Plered). Mosque. Alun-alun. Irrigated rice paddies. The capital that Amangkurat II built after his father's fall. Kartasura was the seat of Mataram during its VOC-influenced decline, until the Geger Pecinan (1740) and the Third Javanese War of Succession led to the Giyanti Treaty (1755). No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on keraton and paddies), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="The declining capital — Kartasura, where Mataram's power waned under VOC influence. From here, Mataram sultans ruled as puppets while the VOC pulled the strings. The Geger Pecinan massacre (1740) and the war of succession that followed would finally split the kingdom in two.",
)

L007 = l_prompt(
    name="Banda Islands (spice islands, VOC conquest 1621)",
    era_desc="17th century AD (1621), Maluku — site of VOC genocide for nutmeg monopoly",
    scene_desc="Wide view of the Banda Islands — small volcanic islands rising from deep blue tropical sea. Nutmeg trees (Myristica fragrans) covering hillsides. A small Banda village on the coast. The islands were the world's only source of nutmeg until the 18th century. In 1621, J.P. Coen led a VOC expedition that killed or enslaved almost the entire Banda population to establish a nutmeg monopoly. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on nutmeg trees and sea), cool 6500K sky fill. Mid contrast 3:1. Tropical sea mist.",
    mood_desc="Blood for spice — the Banda Islands, where the VOC committed genocide for nutmeg. J.P. Coen's 1621 expedition killed thousands, enslaved survivors, and replaced them with Dutch planters (perkeniers). The most extreme example of colonial violence in the name of commerce. The islands' beauty conceals a terrible history.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Kalender Islam-Jawa (Sultan Agung's calendar reform, 1633)",
    era_desc="1633 AD, Mataram, Central Java — Sultan Agung's synthesis of Islamic and Javanese calendars",
    scene_desc="A traditional Javanese calendar (primbon) on dark surface. Visible: combination of Islamic month names (Muharram, Safar, etc.) with Javanese pasaran days (Legi, Pahing, Pon, Wage, Kliwon) and the 7-day week (Saptawara). The calendar shows the fusion of Islamic lunar months with Javanese cyclical days. Hand-written on brown paper with Javanese numerals. Sultan Agung created this hybrid calendar in 1633 (Saka 1555) as a statement of Islamic-Javanese identity — neither purely Islamic nor purely Javanese, but both.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing handwriting and paper texture), low ambient fill. High contrast 4:1.",
    mood_desc="Two calendars, one identity — Sultan Agung's calendar reform of 1633 created a uniquely Javanese Islamic calendar that combined Islamic lunar months with Javanese pasaran days. This calendar is still used in Java today — a living legacy of Sultan Agung's vision of Islam and Javanese culture as inseparable.",
)

A002 = a_prompt(
    name="Perjanjian Giyanti (Treaty of Giyanti, 1755)",
    era_desc="1755 AD, Giyanti, Central Java — treaty that split Mataram into Yogyakarta and Surakarta",
    scene_desc="A Dutch colonial treaty document on dark surface. Visible: Dutch text with Javanese and Malay translations. The VOC coat of arms at top. Signatures of VOC Governor-General and Javanese princes. The Treaty of Giyanti (13 February 1755) split the Mataram Sultanate into two: Yogyakarta (under Hamengkubuwana I) and Surakarta (under Pakubuwana III). The treaty ended decades of civil war but permanently weakened Mataram by dividing it. Approximately 40 cm tall, yellowed paper, wax seal.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing text and wax seal), low ambient fill. High contrast 4:1.",
    mood_desc="The division — the Treaty of Giyanti, 1755, the document that split Mataram in two. The VOC engineered this division to weaken Java. Yogyakarta and Surakarta became rival courts — sometimes cooperating, sometimes competing, but never again united. The treaty still shapes Javanese cultural geography today.",
)

A003 = a_prompt(
    name="Keris Mataram (ceremonial dagger of Mataram sultans)",
    era_desc="17th-18th century AD, Mataram, Central Java — symbol of Javanese kingship",
    scene_desc="A keris (ceremonial dagger) on dark velvet. Visible: wavy blade (luk 13 — 13 curves, highest number, reserved for royalty), pamor pattern (meteoric iron damascene showing 'Beras Wutah' motif), gold hilt (ukiran) with Javanese floral design, gold sheath (wrangka) with pendok (gold cover). The keris is the ultimate symbol of Javanese kingship — combining Islamic authority (keris as symbol of faith) with pre-Islamic mystical tradition (keris as pusaka/sacred heirloom). Approximately 40 cm long.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing pamor damascene pattern and gold detail), low ambient fill. High contrast 5:1.",
    mood_desc="The soul of kingship — the keris of Mataram, where steel, gold, and mysticism meet. The wavy blade represents the naga (serpent) of pre-Hindu belief; the pamor pattern holds magical power; the gold hilt proclaims royal authority. In Mataram, the keris was both weapon and spiritual object — a symbol that bridged Islamic faith and Javanese mysticism.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the division of Mataram — Yogyakarta and Surakarta",
    era_desc="1755 AD, Giyanti, Central Java — signing of the Treaty of Giyanti",
    composition="Group of 3 individuals in a formal scene pose. Position 1 (left): Sultan Hamengkubuwana I (Mangkubumi), standing with keris at waist, wearing Yogyakarta-style green silk jacket and batik blangkon — the new sultan of Yogyakarta, determined and proud. Position 2 (center, elevated): a VOC representative, seated with the treaty document, wearing Dutch colonial official uniform (dark coat, white collar, tricorn hat) — the power broker who engineered the division. Position 3 (right): Pakubuwana III, standing with keris, wearing Surakarta-style blue silk jacket and batik blangkon — the new sultan of Surakarta, resigned to half a kingdom. The composition shows the triangle of power that split Mataram.",
    mood="The division of Mataram — three figures at Giyanti, 1755: two Javanese sultans and one Dutch governor. The VOC engineered this split to control Java through division. Two brothers, two kingdoms, one broken realm. The consequences of this treaty still echo in Yogyakarta and Surakarta today.",
    k_refs=["3C-K003 (Hamengkubuwana I)"],
    avoid_extra=", Islamic scholar costume, Hindu costume, modern clothing, turban (must be blangkon for Javanese, tricorn for Dutch)",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "3C-K001-sultan-agung.txt": K001,
        "3C-K002-amangkurat-i.txt": K002,
        "3C-K003-hamengkubuwana-i.txt": K003,
        "3C-K004-iskandar-muda.txt": K004,
        "3C-K005-hasanuddin.txt": K005,
        "3C-K006-trunojoyo.txt": K006,
        # L — 7
        "3C-L001-karta-plered.txt": L001,
        "3C-L002-batavia.txt": L002,
        "3C-L003-aceh.txt": L003,
        "3C-L004-makassar.txt": L004,
        "3C-L005-yogyakarta.txt": L005,
        "3C-L006-kartasura.txt": L006,
        "3C-L007-banda.txt": L007,
        # A — 3
        "3C-A001-kalender-islam-jawa.txt": A001,
        "3C-A002-perjanjian-giyanti.txt": A002,
        "3C-A003-keris-mataram.txt": A003,
        # S — 1
        "3C-S001-giyanti.txt": S001,
    }

    for filename, content in prompts.items():
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            f.write(content)
        print(f"  Created: {filename}")

    print(f"\n✅ Total: {len(prompts)} files (v2.1)")
    print(f"   K: 6 | L: 7 | A: 3 | S: 1")

if __name__ == "__main__":
    main()
