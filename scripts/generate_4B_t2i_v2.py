#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 4B — Kolonial 19 (1800-1900)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/4B-kolonial-19/prompts"

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
    name="Pangeran Diponegoro, Javanese resistance leader",
    era_desc="Java War 1825-1830, Yogyakarta, Central Java — leader of the Java War",
    phenotype="Male, 40-50 years old, Javanese phenotype with golden brown skin, sharp ascetic features, intense determined eyes with spiritual depth. Black hair under white cap (peci/piyu), full black-and-grey beard. Lean build from ascetic and guerrilla life. Turban wrap (sorban) over peci — Islamic-Javanese spiritual warrior style.",
    costume="Wearing Javanese Islamic warrior attire: white sorban (turban) over dark peci, dark green cotton jubah (robe) — simple, not royal, a guerrilla leader's modesty, brown batik sarong, keris pusaka at waist, simple leather sandals. No royal regalia — Diponegoro rejected court luxury for the guerrilla life. A prayer bead (tasbih) around wrist.",
    props="holding a keris pusaka and a prayer bead (tasbih)",
    mood="The prince who became a guerrilla — Diponegoro, son of Yogyakarta's sultan, who rejected the court and Dutch interference. The Java War (1825-1830) killed 200,000 Javanese and 8,000 Dutch. He fought with Islamic legitimacy (his father was called 'Kanjeng Panembahan') and Javanese mysticism. Betrayed at Magelang (28 March 1830) during peace talks, exiled to Makassar, died 1855. Indonesia's first national hero.",
    avoid_extra=", Dutch colonial costume, modern military uniform, Hindu makuta, 20th century Islamic costume",
)

K002 = k_prompt(
    name="Tuanku Imam Bonjol, Padri leader and Islamic reformer",
    era_desc="Padri War 1821-1837, West Sumatra — Islamic reformer and resistance leader",
    phenotype="Male, 50-60 years old, Minangkabau Malay phenotype with medium brown skin, dignified scholarly features with determined jaw, deep-set dark brown eyes. Short grey hair under white cap (songkok). Full grey beard trimmed. Medium build — scholar-warrior. Forehead mark from prostration (sujud) — pious Muslim.",
    costume="Wearing Minangkabau Islamic attire: white turban or songkok, dark green cotton robe, woven Minangkabau songket sarong with gold thread patterns. Simple leather sandals. A keris (Minang style) at waist. No military uniform — a religious leader, not a soldier. Carrying a Qur'an.",
    props="holding a Qur'an and a prayer bead (tasbih)",
    mood="The Padri reformer — Tuanku Imam Bonjol, Islamic reformer who led the Padri movement in Minangkabau (1821-1837). The Padris sought to purify Islam from adat (custom) practices. Caught between Dutch colonial forces and traditional Minangkabau adat leaders. He fought for 16 years, was captured by treachery (1837), exiled, and died in 1864. A national hero who fought for both Islam and resistance to colonialism.",
    avoid_extra=", Javanese blangkon, Dutch colonial costume, modern clothing, Hindu costume",
)

K003 = k_prompt(
    name="Pangeran Antasari, Banjar resistance leader",
    era_desc="Banjar War 1859-1862, South Kalimantan — leader of Banjarmasin resistance",
    phenotype="Male, 35-45 years old, Banjar Malay phenotype with golden brown skin, strong determined features, fierce patriotic eyes. Short black hair under simple white cap (songkok). Short black beard. Muscular build from jungle warfare. Battle scars on arms.",
    costume="Wearing Banjar Islamic warrior attire: white songkok, dark blue cotton jubah, woven Banjar sarong with geometric patterns, keris (Banjar style) at waist, leather arm guard. Simple attire — a resistance fighter, not a court prince. A captured Dutch musket slung on shoulder.",
    props="holding a keris and a captured Dutch musket",
    mood="The jungle fighter — Pangeran Antasari, who led the Banjar War (1859-1906, longest colonial war in Indonesia). He fought against Dutch intervention in the Banjar sultanate succession. The war continued for 47 years — the longest resistance in Indonesian colonial history. Antasari died of illness in 1862, but his followers fought on for decades. A national hero of South Kalimantan.",
    avoid_extra=", Javanese blangkon, Dutch colonial costume, modern clothing, turban",
)

K004 = k_prompt(
    name="Sisingamangaraja XII, Batak king and resistance leader",
    era_desc="Batak War 1877-1907, North Sumatra — last king of the Batak",
    phenotype="Male, 40-50 years old, Batak phenotype with medium brown skin, strong proud features, intense defiant eyes, high cheekbones. Short black hair under traditional Batak headcloth (ulos draped). Short beard. Muscular stocky build from mountain warfare. Traditional Batak tattoo marks on arms.",
    costume="Wearing Batak royal warrior attire: traditional ulos (woven cloth) draped over shoulder, dark cotton undershirt, woven Batak sarong, traditional Batak belt with knife (pisau surit) and spear. No Islamic or Hindu elements — Batak traditional religion (Parmalim) combined with Christian influence. Feather headdress for ceremonial occasions.",
    props="holding a Batak spear (tombak) and a traditional shield (perisai)",
    mood="The last Batak king — Sisingamangaraja XII, who led resistance against Dutch colonial expansion into the Batak highlands for 30 years (1877-1907). He was both king and priest (in the Sisingamangaraja dynasty, spiritual and political power were united). He fell in battle at Simsim (1907), shot by Dutch forces. A national hero who defended Batak sovereignty to the death.",
    avoid_extra=", Islamic costume, Hindu costume, Javanese blangkon, Dutch colonial costume, modern clothing",
)

K005 = k_prompt(
    name="Multatuli / Eduard Douwes Dekker, Dutch writer and colonial critic",
    era_desc="1860 AD, Netherlands — author of 'Max Havelaar', the novel that exposed Cultuurstelsel",
    phenotype="Male, 40-45 years old, Dutch European phenotype with pale skin, refined intellectual features, melancholic eyes with moral indignation, short brown hair, full brown beard (Victorian style). Lean build. Wearing small round spectacles. A writer's intensity — anger channeled through words.",
    costume="Wearing mid-19th century Dutch civilian attire: dark grey wool coat, white linen shirt with high collar, dark waistcoat, dark trousers, leather shoes. No colonial uniform — he resigned from the colonial service in protest. A civilian writer, not a bureaucrat.",
    props="holding a manuscript of 'Max Havelaar' and a fountain pen",
    mood="The conscience of the Netherlands — Multatuli (Latin: 'I have suffered much'), pen name of Eduard Douwes Dekker. His novel 'Max Havelaar' (1860) exposed the abuses of the Cultuurstelsel: forced cultivation, starvation, corruption. The book shocked Europe and contributed to the system's abolition (1870). A Dutchman who used his pen to fight for Indonesian justice. 'The voice of the oppressed,' he called himself.",
    avoid_extra=", colonial military uniform, 17th century costume, modern clothing",
)

K006 = k_prompt(
    name="Jenderal Hendrik Merkus de Kock, Dutch military commander",
    era_desc="Java War 1827-1830, Dutch East Indies — commander of Benteng Stelsel",
    phenotype="Male, 45-55 years old, Dutch European phenotype with pale skin, stern military features, cold calculating eyes, short grey hair, clean-shaven (military regulation). Stocky build. Scowling expression of a siege commander.",
    costume="Wearing early 19th century Dutch colonial military uniform: dark blue coat with gold epaulettes (lieutenant-general rank), white breeches, black riding boots, bicorne hat with cockade. Sword at waist. The uniform of the man who built the Benteng Stelsel — 250+ fortresses across Central Java to contain Diponegoro's guerrilla war.",
    props="holding a map of the Benteng Stelsel (fortress system) and a riding crop",
    mood="The fortress builder — General de Kock, who defeated Diponegoro not through battle but through the Benteng Stelsel: a network of 250+ small fortresses that strangled the guerrilla resistance by cutting supply lines and terrorizing the civilian population. He also orchestrated the betrayal at Magelang (28 March 1830), where Diponegoro was arrested during peace talks. A military strategist who understood that counterinsurgency is about controlling populations, not winning battles.",
    avoid_extra=", modern military uniform, 17th century costume, civilian clothing",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Javanese village under Cultuurstelsel (1830-1870)",
    era_desc="1830-1870 AD, Central Java — forced cultivation under Van den Bosch's system",
    scene_desc="Wide view of a Javanese village under the Cultuurstelsel. Rice paddies partially replaced by forced cash crops: sugar cane fields, coffee plantations, indigo plots. A Dutch colonial inspection post (controleur) on a hill. Village houses (simple wooden structures on stilts) appear impoverished. A government warehouse (gudang) where crops must be delivered. Exhausted farmland. The scene shows the 1/5 land quota system that funded Dutch industrialization while starving Java. No people.",
    lighting_desc="warm but harsh 4000K midday sun (key light, unforgiving), cool 6500K sky fill. Low contrast 2:1. Dust haze over exhausted fields.",
    mood_desc="Engineered poverty — the Cultuurstelsel landscape, where Javanese farmers were forced to grow export crops (sugar, coffee, indigo) instead of food. The system extracted 19 million guilders per year for the Dutch treasury (40% of Dutch government revenue in the 1850s) while Java suffered famines. The landscape of colonial exploitation.",
)

L002 = l_prompt(
    name="Selarong Cave (Diponegoro's guerrilla headquarters)",
    era_desc="1825-1830 AD, Yogyakarta, Central Java — Diponegoro's mountain base",
    scene_desc="Wide view of Goa Selarong — a cave in a limestone hill south of Yogyakarta, surrounded by dense tropical forest. The cave entrance is partially hidden by vegetation. A simple camp with bamboo structures visible nearby. This was Diponegoro's headquarters during the Java War — a guerrilla base in the mountains. The cave is a place of both military strategy and spiritual meditation. Distant view of Gunung Kidul hills. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on cave entrance and forest), cool 6500K sky fill. Mid contrast 3:1. Forest mist.",
    mood_desc="The guerrilla base — Selarong Cave, where Diponegoro planned the Java War. From this mountain refuge, he coordinated a 5-year guerrilla campaign that cost 200,000 Javanese and 8,000 Dutch lives. The cave symbolizes the marriage of Islamic faith (meditation) and Javanese resistance (warfare).",
)

L003 = l_prompt(
    name="Bukittinggi / Fort de Kock (Minangkabau highlands, Padri War)",
    era_desc="1821-1837 AD, West Sumatra — site of the Padri War",
    scene_desc="Wide view of the Minangkabau highlands near Bukittinggi. Traditional Minangkabau rumah gadang (longhouses with curved roofs) visible in valley. Dutch Fort de Kock on hilltop. Lush tropical highland vegetation. The dramatic landscape of the Padri War — where Islamic reformers (Padris) fought both the Dutch and traditional adat leaders. The deep valley (Ngarai Sianok) visible. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on highlands and rumah gadang), cool 6500K sky fill. High contrast 4:1. Morning mist in valley.",
    mood_desc="The highland war — Bukittinggi/Fort de Kock, where the Padri War (1821-1837) was fought. Three-way conflict: Padris (Islamic reformers), adat leaders (traditional Minangkabau), and the Dutch. Tuanku Imam Bonjol's resistance ended at Bonjol fort (1837). The landscape of Minangkabau — curved-roof houses and dramatic valleys — was the stage for one of Indonesia's longest wars.",
)

L004 = l_prompt(
    name="Bali battlefield (Jagaraga, 1848-1849)",
    era_desc="1848-1849 AD, North Bali — site of the Bali War puputan",
    scene_desc="Wide view of a Balinese battlefield near Jagaraga. Traditional Balinese temple (pura) on a hilltop. Open field with scattered debris of war. Distant view of Balinese mountains and the sea. The Bali Wars (1846-1849) were fought when the Dutch intervened in Balinese politics. The most dramatic moment: the puputan (fight to the death) where Balinese royal families chose death over surrender. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on temple and battlefield), cool 6500K sky fill. Mid contrast 3:1. Sea visible in distance.",
    mood_desc="The puputan field — Jagaraga, where Balinese warriors and royal families fought to the death against Dutch forces. The puputan (from Balinese 'to finish' or 'to end') was a ritual of mass suicide — walking into Dutch gunfire rather than surrender. The most dramatic and tragic form of Balinese resistance.",
)

L005 = l_prompt(
    name="Aceh War landscape (1873-1904)",
    era_desc="1873-1904 AD, Aceh — longest colonial war in Indonesian history",
    scene_desc="Wide view of the Acehnese landscape during the Aceh War. Dense tropical rainforest with rugged hills. Traditional Acehnese village (geudeung houses) partially hidden in forest. A Dutch military blockhouse (benteng) on a cleared hilltop. The landscape of the longest colonial war: 31 years of guerrilla resistance in the jungles of Aceh. The Acehnese fought with Islamic conviction (jihad) and guerrilla tactics. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, warm on rainforest and hilltop fort), cool 6500K sky fill. High contrast 4:1. Rainforest mist.",
    mood_desc="The 31-year war — Aceh, where the Dutch fought their longest colonial war (1873-1904). The Acehnese resisted with Islamic jihad and guerrilla tactics in the dense jungle. The Dutch used concentration camps (concentratiekampen) and scorched earth — a precursor to 20th century counterinsurgency. The war cost 100,000 Acehnese and 12,000 Dutch lives. Aceh never fully surrendered.",
)

L006 = l_prompt(
    name="Lombok battlefield (1894)",
    era_desc="1891-1894 AD, Lombok — Perang Lombok",
    scene_desc="Wide view of the Lombok landscape during the colonial war. Mount Rinjani towering in background. Traditional Sasak village with simple wooden houses. Balinese royal palace (Cakranegara) in distance. The war began as a conflict between Sasak peasants and Balinese rulers, but the Dutch intervened to control the island. Dutch troops fought both Sasak and Balinese. The landscape of a complex three-way conflict. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on Mount Rinjani and village), cool 6500K sky fill. Mid contrast 3:1. Volcanic haze.",
    mood_desc="The island of three wars — Lombok (1891-1894), where Sasak peasants, Balinese rulers, and Dutch colonizers fought a three-way war. The Dutch used the Sasak-Balinese conflict as a pretext to colonize Lombok. The war showed how the Dutch exploited local divisions to expand their control.",
)

L007 = l_prompt(
    name="Plantation scene (sugar factory, Java, late 19th century)",
    era_desc="late 19th century AD, Java — sugar plantation and factory after Cultuurstelsel",
    scene_desc="Wide view of a Java sugar plantation and factory in the Liberal Era (1870s-1890s). A large sugar mill (fabriek) with chimneys visible. Cane fields stretching to horizon. Worker housing (simple barracks). A railway line connecting the factory to the port. After the Cultuurstelsel was abolished (1870), private companies took over — the Agrarian Law (1870) allowed 75-year leases. The plantation system continued exploitation under private capital instead of state control. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, warm on factory and cane fields), cool 6500K sky fill. Mid contrast 3:1. Smoke from factory chimneys.",
    mood_desc="Private exploitation — the post-Cultuurstelsel plantation. After 1870, the Dutch didn't stop exploiting Java — they privatized it. Private companies (383 by 1890) leased land for 75 years. Sugar, coffee, and indigo still flowed to Europe. The faces changed, the system didn't. The foundation of Dutch industrial wealth.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Max Havelaar (Multatuli's novel, 1860)",
    era_desc="1860 AD, Netherlands — the novel that exposed the Cultuurstelsel",
    scene_desc="A first edition of 'Max Havelaar' (1860) by Multatuli on dark surface. Visible: Dutch text, the title page with author name 'Multatuli', leather binding in dark brown, gold lettering on spine. The novel exposed the abuses of the Cultuurstelsel: forced cultivation, corruption, starvation in Lebak (Banten). It caused a scandal in the Netherlands and contributed to the system's abolition in 1870. Approximately 22 cm tall, 350 pages, aged but well-preserved.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing leather texture and gold lettering), low ambient fill. High contrast 4:1.",
    mood_desc="The book that shamed a nation — Max Havelaar (1860), the novel that made the Netherlands confront its colonial crimes. Multatuli's fictional account of a colonial official who tried to stop abuses in Lebak was based on his own experience. The book was called 'the book that killed the Cultuurstelsel.' Literature as a weapon of justice.",
)

A002 = a_prompt(
    name="Benteng Stelsel fort (Dutch colonial counterinsurgency fort, 1827-1830)",
    era_desc="1827-1830 AD, Central Java — small fortress of the Benteng Stelsel system",
    scene_desc="A model/diorama of a Benteng Stelsel fort on dark surface. Visible: small square fortification with earthen walls, wooden palisade, a watchtower, and a small garrison building. Simple and functional — not a grand castle but a counterinsurgency outpost. General de Kock built 250+ of these forts across Central Java to contain Diponegoro's guerrilla war. Each fort controlled a small area and cut supply lines. Approximately 30 cm model, 1:100 scale.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing model details), low ambient fill. High contrast 4:1.",
    mood_desc="The net of forts — the Benteng Stelsel (Fortress System), de Kock's counterinsurgency strategy. Instead of chasing Diponegoro's guerrillas, de Kock built 250+ small forts to control the population and cut supply lines. The strategy worked: Diponegoro's forces were slowly strangled. The Benteng Stelsel was a 19th-century precursor to modern counterinsurgency.",
)

A003 = a_prompt(
    name="Sisingamangaraja's spear and shield (Batak royal regalia)",
    era_desc="late 19th century AD (1877-1907), North Sumatra — royal weapons of the Batak king",
    scene_desc="A Batak spear (tombak) and wooden shield (perisai) on dark velvet. Visible: iron spearhead with intricate Batak carving on the shaft, wooden shield with traditional Batak geometric and figurative carvings (gorga motifs). The spear is approximately 1.5 meters long, the shield 60 cm. These are the weapons of Sisingamangaraja XII — the last Batak king who fought the Dutch for 30 years. The weapons are both practical tools and royal regalia — the spear carries the spiritual power of the Sisingamangaraja dynasty.",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing iron and wood carving detail), low ambient fill. High contrast 5:1.",
    mood_desc="The last king's weapons — the spear and shield of Sisingamangaraja XII, who fell at Simsim in 1907, shot by Dutch forces. These weapons are more than military tools — they are royal regalia imbued with the spiritual power of the Sisingamangaraja dynasty, which ruled the Batak for 12 generations. When the king fell, a dynasty that had lasted centuries ended.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the colonial encounter — Diponegoro's capture at Magelang (1830)",
    era_desc="28 March 1830 AD, Magelang, Central Java — betrayal during peace talks",
    composition="Group of 3 individuals in a dramatic confrontation pose. Position 1 (left): Pangeran Diponegoro, standing with keris and tasbih, wearing white sorban and green jubah — the guerrilla prince who came to negotiate peace. Position 2 (center, elevated): General de Kock, seated on a chair, wearing dark blue military uniform with gold epaulettes — the Dutch commander who betrayed the peace talks. Position 3 (right): a Dutch colonial soldier, standing with rifle at attention — the instrument of betrayal. The composition shows the moment of betrayal: Diponegoro came to negotiate, de Kock arrested him instead.",
    mood="The betrayal — Magelang, 28 March 1830. Diponegoro came to negotiate peace. De Kock arrested him instead. The Javanese prince who had fought for 5 years was betrayed by Dutch dishonor. He was exiled to Makassar, where he died in 1855. The moment that ended the Java War and began the colonial century.",
    k_refs=["4B-K001 (Diponegoro)", "4B-K006 (De Kock)"],
    avoid_extra=", Islamic scholar costume, Hindu costume, modern clothing, 20th century military uniform",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "4B-K001-diponegoro.txt": K001,
        "4B-K002-imam-bonjol.txt": K002,
        "4B-K003-antasari.txt": K003,
        "4B-K004-sisingamangaraja.txt": K004,
        "4B-K005-multatuli.txt": K005,
        "4B-K006-de-kock.txt": K006,
        # L — 7
        "4B-L001-cultuurstelsel-village.txt": L001,
        "4B-L002-selarong.txt": L002,
        "4B-L003-bukittinggi.txt": L003,
        "4B-L004-bali-jagaraga.txt": L004,
        "4B-L005-aceh-war.txt": L005,
        "4B-L006-lombok.txt": L006,
        "4B-L007-plantation.txt": L007,
        # A — 3
        "4B-A001-max-havelaar.txt": A001,
        "4B-A002-benteng-stelsel.txt": A002,
        "4B-A003-sisingamangaraja-weapons.txt": A003,
        # S — 1
        "4B-S001-magelang-betrayal.txt": S001,
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
