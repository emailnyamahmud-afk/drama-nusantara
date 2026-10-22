#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 4A — VOC Awal (Abad 17-18 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/4A-voc-awal/prompts"

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
    name="Cornelis de Houtman, Dutch expedition leader",
    era_desc="1595-1597 AD, Netherlands/Banten — first Dutch expedition to Nusantara",
    phenotype="Male, 30-35 years old, Dutch European phenotype with pale skin, reddish-brown hair, blue-grey eyes, weathered face from sea voyages. Short hair, trimmed beard. Lean build from months at sea. Sun-burned skin.",
    costume="Wearing late 16th century Dutch merchant-naval attire: dark brown leather jerkin over white linen shirt, dark breeches, leather boots, wide leather belt with rapier sword. A Dutch East Indies merchant's practical clothing — not military, not court, but commercial.",
    props="holding a spyglass (terrestrial telescope) and a rolled sea chart",
    mood="The first Dutchman — Cornelis de Houtman, who led the first Dutch expedition to Nusantara (1595-1597). His voyage proved the Portuguese didn't control the spice route — others could reach the East Indies by sailing around Africa. Arrogant, violent, he insulted the Banten sultan and barely escaped with his life. The beginning of 350 years of Dutch presence in Indonesia.",
    avoid_extra=", modern Dutch clothing, Indonesian costume, 17th century military armor",
)

K002 = k_prompt(
    name="Jan Pieterszoon Coen, VOC Governor-General",
    era_desc="17th century AD (1619-1629), Batavia — founder of Batavia, architect of VOC empire",
    phenotype="Male, 35-40 years old, Dutch European phenotype with pale skin, sharp angular features, cold determined eyes, thin lips. Short brown hair, clean-shaven (Dutch merchant style). Medium build. Stern authoritarian expression.",
    costume="Wearing early 17th century VOC Governor-General attire: black wool coat with gold buttons, white linen collar (ruff), black breeches, leather boots, VOC emblem (VOC monogram) on breast. A rapier at waist. The attire of a man who ruled an empire of trade and was not afraid to use extreme violence.",
    props="holding the VOC charter (oktroi) document",
    mood="The ruthless architect — J.P. Coen founded Batavia (1619) on the ruins of Jayakarta, committed genocide in Banda (1621) for nutmeg monopoly, and established the VOC as a state-within-a-state. His motto: 'Despair not, spare not.' The man who began the Dutch colonial system in the East Indies.",
    avoid_extra=", modern clothing, Indonesian costume, 18th century colonial costume",
)

K003 = k_prompt(
    name="Sultan Hasanuddin, Sultan of Gowa-Tallo (Makassar)",
    era_desc="17th century AD (1653-1669), Makassar, South Sulawesi — 'Rooster of the East'",
    phenotype="Male, 30-40 years old, Bugis-Makassar phenotype with golden brown skin, strong angular features, fierce determined eyes. Short black hair under Makassar-style headcloth. Muscular stocky build from maritime warrior life. Battle scars.",
    costume="Wearing Makassar sultan attire: colorful woven headcloth (destar), dark red silk jacket with gold embroidery, woven Makassar sarong with geometric patterns, keris (Makassar style), gold armlets.",
    props="holding a keris and a Makassar war shield (badjak)",
    mood="The Rooster of the East — Sultan Hasanuddin, who fought the VOC for 14 years (1655-1669). He refused Dutch trade monopoly and became a symbol of Indonesian resistance. The Dutch called him 'De Haantjes van het Oosten.' He surrendered in 1669 but never submitted in spirit.",
    avoid_extra=", Javanese blangkon, turban, European costume, modern clothing",
)

K004 = k_prompt(
    name="Herman Willem Daendels, Governor-General of the Dutch East Indies",
    era_desc="1808-1811 AD, Dutch East Indies — Marshal of Napoleon's empire in Java",
    phenotype="Male, 45-50 years old, Dutch European phenotype with pale skin, stern military features, sharp determined jaw, cold calculating eyes. Short grey-brown hair (military crop). Clean-shaven (Napoleonic military style). Stocky military build. Scowling expression.",
    costume="Wearing Napoleonic-era French/Dutch military uniform: dark blue coat with gold epaulettes (marshal rank), white breeches, black riding boots, bicorne hat (Napoleonic style, NOT tricorn). Sword at waist. Sash in Dutch orange. Daendels was a Marshal of Napoleon's empire — his uniform reflects French military influence, not traditional Dutch colonial dress.",
    props="holding a riding crop and a map of Java's Great Post Road (Jalan Raya Pos)",
    mood="The iron marshal — Daendels, sent by Napoleon's brother (King Louis Bonaparte of Holland) to defend Java against the British. He built the 1,000 km Great Post Road (Jalan Raya Pos) from Anyer to Panarukan in one year, using forced Javanese labor. Thousands died in its construction. A reformer who also exploited — the paradox of 'enlightened' colonialism.",
    avoid_extra=", modern military uniform, 17th century costume, civilian clothing",
)

K005 = k_prompt(
    name="Thomas Stamford Raffles, Lieutenant-Governor of Java",
    era_desc="1811-1816 AD, British Interregnum, Java — founder of Singapore, scholar of Java",
    phenotype="Male, 30-35 years old, British phenotype with pale skin, refined intellectual features, warm curious eyes, light brown hair. Clean-shaven. Lean build. An intellectual, not a military man — his face shows curiosity rather than command.",
    costume="Wearing early 19th century British colonial official attire: dark blue tailcoat with gold buttons, white linen shirt with high collar, white breeches, black shoes. No military insignia — he was a civil administrator, not a soldier. A sash of office. Small spectacles in pocket.",
    props="holding a copy of his book 'The History of Java' (1817) and a Javanese antiquities catalog",
    mood="The scholar-colonizer — Raffles, who governed Java during the British Interregnum (1811-1816). Unlike Daendels, he studied Javanese culture, wrote 'The History of Java' (1817), and discovered Borobudur. He also abolished slave trade and introduced land rent. But his curiosity served empire — knowledge as power. Later founded Singapore (1819).",
    avoid_extra=", modern British costume, military armor, 17th century costume",
)

K006 = k_prompt(
    name="Johannes van den Bosch, Governor-General and Cultuurstelsel architect",
    era_desc="1830-1833 AD, Dutch East Indies — architect of the Cultivation System (Cultuurstelsel)",
    phenotype="Male, 50-60 years old, Dutch European phenotype with pale skin, heavy-set features, stern bureaucratic expression, thinning grey hair. Clean-shaven (early Victorian style). Stocky build. Cold calculating eyes behind small round spectacles.",
    costume="Wearing early 19th century Dutch colonial official attire: black wool tailcoat with high collar, white linen shirt, dark waistcoat, dark trousers. Governor-General's sash. A bureaucrat's uniform — no military gold, just administrative grey. The attire of a man who designed a system of exploitation from behind a desk.",
    props="holding a ledger book and a map of Java's plantation zones",
    mood="The system architect — Van den Bosch, who designed the Cultuurstelsel (Cultivation System, 1830). Javanese farmers were forced to devote 1/5 of their land (or 66 days of labor per year) to export crops (coffee, sugar, indigo) for the Dutch treasury. The system funded Dutch industrialization and railway construction — while millions of Javanese starved. The most efficient colonial exploitation system ever devised.",
    avoid_extra=", modern clothing, military uniform, 17th century costume, Indonesian costume",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Banten (first Dutch landing site, 1596)",
    era_desc="late 16th century AD, Banten, West Java — first contact between Dutch and Nusantara",
    scene_desc="Wide view of Banten harbor in the late 16th century. Pepper-trading port with ships from Arabia, India, China, and Portugal. Wooden warehouses. The Masjid Agung Banten visible (Javanese-style mosque). Sultan's palace nearby. A small Dutch ship (the Mauritius) visible in harbor — the first European ship other than Portuguese to reach Java. The pepper sultanate that controlled the western entrance to the Sunda Strait. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor and mosque), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="First contact — Banten, where Cornelis de Houtman landed in 1596. The sultan of Banten, rich from the pepper trade, saw no reason to give the Dutch special terms. The Portuguese had been here for 80 years; the Dutch were just another set of traders. But this encounter would lead to 350 years of Dutch colonial rule.",
)

L002 = l_prompt(
    name="Batavia (VOC colonial capital, 17th-18th century)",
    era_desc="17th-18th century AD (1619-1800), Jakarta — VOC Asian headquarters",
    scene_desc="Wide cinematic view of Batavia (Jakarta) in the 17th century. Kasteel Batavia (VOC fort) with European-style stone walls and cannons. Dutch-style canal houses (grachtenhuizen) along canals. Drawbridges. Chinese quarter. Harbor with VOC ships (fluyt, galjon). Tropical vegetation contrasting with European architecture. The 'Queen of the East' — the most important Dutch colonial city. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, golden on stone fort and canals), cool 6500K sky fill. Mid contrast 3:1. Tropical haze.",
    mood_desc="The Queen of the East — Batavia, the VOC's capital in Asia. Built on conquered land (Jayakarta, 1619), designed like a Dutch city with canals and gabled houses. From here the VOC governed trade from Japan to Persia. A European island in tropical Asia — beautiful, deadly (malaria), and built on the bones of the conquered.",
)

L003 = l_prompt(
    name="Banda Islands (nutmeg monopoly, site of 1621 genocide)",
    era_desc="17th century AD (1621), Maluku — world's only source of nutmeg",
    scene_desc="Wide aerial view of the Banda Islands — small volcanic islands in deep blue tropical sea. Nutmeg trees (Myristica fragrans) covering the volcanic hillsides. A small Banda village on the coast. Fort Belgica (Dutch VOC fort) visible on hilltop — built to control the nutmeg monopoly. In 1621, J.P. Coen's VOC expedition killed or enslaved nearly the entire Banda population. Beautiful islands with a terrible history. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on nutmeg trees and sea), cool 6500K sky fill. Mid contrast 3:1. Tropical sea mist.",
    mood_desc="Blood for nutmeg — the Banda Islands, the world's only source of nutmeg until the 18th century. J.P. Coen's 1621 genocide killed thousands and enslaved the rest, replacing them with Dutch planters (perkeniers). The most extreme example of colonial violence for commercial monopoly.",
)

L004 = l_prompt(
    name="Ternate and Tidore (Maluku spice sultanates)",
    era_desc="16th-17th century AD, North Maluku — clove-producing sultanates",
    scene_desc="Wide view of the twin volcanic islands of Ternate and Tidore rising from the sea. Clove trees (Syzygium aromaticum) on volcanic slopes. Small fortified settlements. A Portuguese fort (Kastella) on Ternate, a Spanish/Dutch fort on Tidore. The two sultanates that controlled the world's clove trade for centuries. Spanish, Portuguese, Dutch, and English all fought for these tiny islands. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on volcanic slopes and sea), cool 6500K sky fill. Mid contrast 3:1. Sea mist around islands.",
    mood_desc="The clove islands — Ternate and Tidore, two volcanic cones in the sea, whose cloves were worth more than gold in Europe. The sultanates resisted European powers for 100+ years. Sultan Babullah expelled the Portuguese in 1575. These tiny islands shaped world history — the search for their spices drove the Age of Discovery.",
)

L005 = l_prompt(
    name="Jalan Raya Pos (Great Post Road, Daendels' highway, 1808-1811)",
    era_desc="1808-1809 AD, Anyer to Panarukan, Java — 1,000 km military road",
    scene_desc="Wide view of the Great Post Road (Jalan Raya Pos) cutting through the Javanese landscape. A straight dirt road lined with tamarind trees (as per Daendels' order), stretching from the coast at Anyer (west Java) toward the interior. Irrigated rice paddies on both sides. Distant volcanic mountains. The road was built in one year using forced Javanese labor — thousands died in its construction. A military highway designed to move troops quickly across Java. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on road and paddies), cool 6500K sky fill. Mid contrast 3:1. Dust haze from road.",
    mood_desc="The road of bones — Jalan Raya Pos, Daendels' 1,000 km highway from Anyer to Panarukan, built in one year (1808-1809) with forced labor. Tens of thousands of Javanese died. A road that connected Java for the first time — but at a terrible human cost. Still in use today as part of Java's northern coast road.",
)

L006 = l_prompt(
    name="Borobudur (rediscovered by Raffles' expedition, 1814)",
    era_desc="1814 AD, Central Java — British rediscovery of the great Buddhist temple",
    scene_desc="Wide view of Borobudur emerging from tropical vegetation in 1814. The great temple is half-overgrown with jungle — trees and vines covering the upper terraces. A small British survey party camp at base. H.C. Cornelius was sent by Raffles to clear the site. The temple had been abandoned for centuries — volcanic ash and jungle had hidden it. The moment of rediscovery of the greatest Buddhist monument in the southern hemisphere. No people visible at temple.",
    lighting_desc="warm 3500K morning sun from camera left (key light, revealing temple through cleared vegetation), cool 6500K sky fill. High contrast 4:1. Morning mist in Kedu valley.",
    mood_desc="The rediscovery — Borobudur, emerging from 800 years of volcanic ash and jungle when Raffles' expedition cleared it in 1814. The temple that Majapahit had abandoned, that Islam had forgotten, was found again — a reminder of a sophisticated pre-Islamic civilization that had preceded the colonial present.",
)

L007 = l_prompt(
    name="Keraton Yogyakarta under British assault (Geger Sepehi, 1812)",
    era_desc="1812 AD, Yogyakarta — British attack on the Yogyakarta keraton",
    scene_desc="Wide view of the Keraton Yogyakarta under British assault, June 1812. British forces (under Raffles' authority) attacking the keraton walls with cannons. The keraton's defenses breached. Smoke from cannon fire. The sultan's palace, designed as a cosmic mandala of peace, turned into a battlefield. Hamengkubuwana II was deposed and Hamengkubuwana III installed as a British puppet. The event that showed the keraton could be taken by force. No people.",
    lighting_desc="warm 3500K early morning sun from camera left (key light, through cannon smoke), cool 6500K sky fill. High contrast 4:1. Smoke haze obscuring details.",
    mood_desc="The fall of the keraton — Geger Sepehi (1812), when British forces stormed the Yogyakarta keraton with 1,200 troops and 23 cannons. The sultan's palace, the symbolic center of the Javanese universe, was breached in one day. The message was clear: the keraton, like Java itself, could be taken by European force.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="VOC oktroi (charter of 1602, founding the Dutch East India Company)",
    era_desc="1602 AD, Netherlands — the founding document of the VOC",
    scene_desc="A Dutch legal charter document on dark surface. Visible: elaborate Dutch calligraphy, the VOC monogram (Verenigde Oost-Indische Compagnie), the States General seal, and signatures of the Dutch States General. The charter granted the VOC a 21-year monopoly on Dutch trade east of the Cape of Good Hope, including the right to wage war, make treaties, and establish colonies. Approximately 40 cm tall, aged parchment with red wax seal.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing calligraphy and wax seal), low ambient fill. High contrast 4:1.",
    mood_desc="The corporation's charter — the VOC oktroi of 1602, creating the world's first multinational corporation with sovereign powers. The VOC could wage war, negotiate treaties, mint coins, and establish colonies — a corporation that functioned as a state. For 200 years, this piece of parchment governed the lives of millions in Nusantara.",
)

A002 = a_prompt(
    name="Linschoten's Itinerario (1596, the travel guide that opened the East)",
    era_desc="1596 AD, Netherlands — Jan Huygen van Linschoten's travel guide to the East Indies",
    scene_desc="An opened 16th century Dutch book on dark surface. Visible: Dutch text with Portuguese place names, hand-drawn maps of the Indian Ocean and East Indies, and illustrations of Asian ports. The 'Itinerario' by Jan Huygen van Linschoten — a travel guide based on his years in Portuguese Goa. The book revealed Portuguese trade secrets to Northern Europe, enabling the Dutch (and English) to sail directly to the Spice Islands. Approximately 30 cm tall, leather-bound, aged pages with some color illustrations.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing text, maps, and page texture), low ambient fill. High contrast 4:1.",
    mood_desc="The book that changed history — Linschoten's Itinerario (1596), which published Portuguese navigational secrets for all of Northern Europe to read. Without this book, the Dutch might never have reached the Spice Islands. A book that opened the door to 350 years of Dutch colonialism, simply by sharing knowledge that the Portuguese had kept secret.",
)

A003 = a_prompt(
    name="Cultuurstelsel contract (Cultivation System indenture document, 1830+)",
    era_desc="1830-1870 AD, Java — forced cultivation contract under Van den Bosch's system",
    scene_desc="A Dutch colonial administrative document on dark surface. Visible: official Dutch government form with printed headers (Koninklijk Besluit), handwritten entries in both Dutch and Javanese script. The document records a Javanese village's forced cultivation quota: how much land must be devoted to coffee/sugar/indigo, and how much must be delivered to the government warehouse. Stamped with the colonial government seal. Approximately 35 cm tall, yellowed paper.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing text and stamps), low ambient fill. High contrast 4:1.",
    mood_desc="The paper that enslaved Java — a Cultuurstelsel contract, the bureaucratic instrument of Van den Bosch's Cultivation System. This piece of paper determined how many days a Javanese farmer must work for the Dutch, how much of his land must grow export crops, and how little he would be paid. The system funded the Netherlands' industrialization while starving Java.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the VOC court of Batavia — Governor-General and council",
    era_desc="17th century AD, Batavia — VOC colonial administration",
    composition="Group of 4 individuals in a court/administrative scene pose. Position 1 (center, elevated): VOC Governor-General (representing Coen era), seated on a carved chair, wearing black coat with gold buttons and VOC emblem, holding a gavel. Position 2 (left): a Dutch VOC merchant/official, standing with ledger book, wearing dark brown coat with white collar. Position 3 (right): a Javanese regent (bupati), standing in Javanese attire (batik blangkon, silk jacket, sarong, keris) — the local collaborator. Position 4 (far right): a Chinese merchant (kapitan Cina), standing with abacus and silk sample — the middleman in VOC trade. All in 17th century attire representing the colonial power structure.",
    mood="The colonial triangle — Batavia's VOC court: the Dutch Governor-General (power), the Javanese bupati (local intermediary), and the Chinese kapitan (commercial middleman). Three cultures, one colonial system. The VOC ruled Java through this triangle of Dutch authority, Javanese collaboration, and Chinese commerce for 200 years.",
    k_refs=["4A-K002 (J.P. Coen)"],
    avoid_extra=", modern clothing, 18th century military uniform, Indonesian independence-era costume",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "4A-K001-cornelis-de-houtman.txt": K001,
        "4A-K002-jp-coen.txt": K002,
        "4A-K003-sultan-hasanuddin.txt": K003,
        "4A-K004-daendels.txt": K004,
        "4A-K005-raffles.txt": K005,
        "4A-K006-van-den-bosch.txt": K006,
        # L — 7
        "4A-L001-banten.txt": L001,
        "4A-L002-batavia.txt": L002,
        "4A-L003-banda.txt": L003,
        "4A-L004-ternate-tidore.txt": L004,
        "4A-L005-jalan-raya-pos.txt": L005,
        "4A-L006-borobudur-rediscovery.txt": L006,
        "4A-L007-yogyakarta-1812.txt": L007,
        # A — 3
        "4A-A001-voc-oktroi.txt": A001,
        "4A-A002-linschoten-itinerario.txt": A002,
        "4A-A003-cultuurstelsel-contract.txt": A003,
        # S — 1
        "4A-S001-voc-court-batavia.txt": S001,
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
