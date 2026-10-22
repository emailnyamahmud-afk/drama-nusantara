#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 2C — Singasari-Kediri (Abad 11-13 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/2C-singasari-kediri/prompts"

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
    name="Sri Jayabhaya, King of Kadiri",
    era_desc="12th century AD (1135-1157), Kadiri, East Java — golden age of Kadiri",
    phenotype="Male, 40-50 years old, Javanese phenotype with golden brown skin, regal dignified features, calm authoritative expression. Black hair in topknot with some grey. Medium build from royal lifestyle. Forehead marked with Vaishnava tilaka.",
    costume="Wearing Kadiri royal costume: gold makuta with Vishnu Madhusudhana motif, gold hara necklace with Vishnu pendant, gold keyura armlets, deep red silk kemben with gold thread, batik kain with parang pattern, keris at waist. Lencana: Srenggalancana (buffalo horn emblem).",
    props="holding a ceremonial mace",
    mood="Paduka Bhatara Jayabhaya — the golden age king of Kadiri. Patron of Bharatayuddha (1157 AD). Under his rule, Kadiri introduced 3-tier administrative system, military reforms (makasirkasir), and the first Senapati Sarwwajala (admiral). His reign also saw the emergence of Bhairawa tantrik tradition.",
)

K002 = k_prompt(
    name="Ken Arok / Ranggah Rajasa, founder of Singhasari",
    era_desc="13th century AD (1222), Tumapel, East Java — founder of Singhasari kingdom",
    phenotype="Male, 25-35 years old, Javanese phenotype with golden brown skin, sharp ambitious features, intense determined eyes. Black hair in simple topknot (not yet royal — commoner origin). Lean muscular build from military life. Scar on left cheek from combat. Tattoo marks on arms (commoner tradition).",
    costume="Wearing simple warrior attire: leather chest armor, woven cloth kain, simple iron keris at waist. After becoming king: gold makuta, gold necklace, red silk kemben. The character bridges commoner-to-king transformation.",
    props="holding the Keris Mpu Gandring (cursed keris of legend)",
    mood="Rags to raja — Ken Arok, the commoner who killed Tunggul Ametung, became king of Tumapel, and defeated Kadiri in 1222. Sri Ranggah Rajasa Bhatara Sang Amurwabhumi — founder of the Rajasa dynasty that would produce both Singhasari and Majapahit kings.",
)

K003 = k_prompt(
    name="Wisnuwardhana, King of Singhasari",
    era_desc="13th century AD (1248-1270), Singhasari, East Java — visionary of Nusantara concept",
    phenotype="Male, 35-45 years old, Javanese phenotype with golden brown skin, wise calm features, scholarly expression. Black hair in topknot with gold diadem. Lean build from balanced royal and scholarly life.",
    costume="Wearing Singhasari royal costume: gold makuta with Wisnu motif, gold hara necklace, gold armlets, blue-and-gold silk kemben, batik kain. Lencana: Sri jayawisnuwarddhana.",
    props="holding a prasasti (copper plate inscription — the Mula Malurung)",
    mood="Visionary of Nusantara — Wisnuwardhana, who in 1255 AD issued the Prasasti Mula Malurung containing the first written mention of 'Nusantara' — 'the land beneath his feet shall become the umbrella of the world, all Jawadwipamandala, then Nusantara.' A concept that would echo through centuries.",
)

K004 = k_prompt(
    name="Kertanagara, last King of Singhasari",
    era_desc="13th century AD (1270-1292), Singhasari — tantrik king, cakrawala mandala visionary",
    phenotype="Male, 30-40 years old, Javanese phenotype with golden brown skin, intense spiritual eyes with slightly wild expression. Black hair in matted jata (ascetic style). Lean build from tantrik practices. Forehead marked with ritual ash (vibhuti). Ritual scars on arms from tantrik practices.",
    costume="Wearing tantrik royal costume: ornate gold makuta with skull motif (Bhairawa), gold necklace with human skull beads (mala), gold armlets with serpent (naga) motif, dark red-and-black silk kemben with tantrik symbols, keris at waist. The costume blends royal authority with tantrik esoteric power.",
    props="holding a vajra (ritual thunderbolt) and a kapala (skull cup)",
    mood="Tantrik king — Kertanagara, the last and most controversial king of Singhasari. Buddhist Tantra (Jnanabajreswara, Aksobhya) and Hindu Bhairawa in one. Built Candi Jawi with Siwa below and Buddha above. Sent Amoghapasa to Dharmasraya. His vision: cakrawala mandala — uniting all islands. Died in Jayakatwang's attack, 1292.",
    avoid_extra=", Islamic costume, simple Hindu costume without tantrik elements",
)

K005 = k_prompt(
    name="Raden Wijaya / Kertarajasa Jayawardhana, founder of Majapahit",
    era_desc="13th-14th century AD (1293-1309), East Java — founder of Majapahit",
    phenotype="Male, 25-35 years old, Javanese phenotype with golden brown skin, sharp regal features with weathered look from exile and war. Black hair in topknot, light beard. Muscular build from military campaigns. Scar on forearm from combat during escape.",
    costume="Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif (Garudamukha), gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold kemben, batik kain with parang pattern, keris pusaka at waist. Lencana: Garudamukha — identifying with Wisnu as Cakravartin.",
    props="holding a Garudamukha scepter",
    mood="Survivor and founder — Raden Wijaya escaped Jayakatwang's attack (1292), hid in Kudadu village, fled to Madura, allied with Arya Wiraraja, used Kubilai Khan's Tartar army to destroy Kadiri, then expelled the Tartars. Crowned as Kertarajasa Jayawardhana, founder of Majapahit (1293). The kingdom that would become the greatest in Nusantara history.",
)

K006 = k_prompt(
    name="Mpu Panuluh, Kadiri court poet",
    era_desc="12th century AD, Kadiri — author of Bharatayuddha, Hariwangsa, Gatotkacasraya",
    phenotype="Male, 50-60 years old, Javanese phenotype with golden brown skin, wise gentle features, scholarly expression. Shaved head with small topknot (resi style). Thin build from scholarly life. Hands stained with ink from writing on lontar.",
    costume="Wearing simple scholarly attire: white cotton wrap, upavita (sacred thread), simple wooden bead necklace. No jewelry — a poet's dignity comes from words, not gold.",
    props="holding a lontar manuscript and a writing stylus",
    mood="Voice of the golden age — Mpu Panuluh, the greatest poet of Kadiri. His Bharatayuddha (1157 AD) is a literary masterpiece that also served as military manual. His works preserved the cultural sophistication of Kadiri for posterity. A commoner who achieved immortality through words.",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Daha / Kadiri (Kadiri kingdom capital)",
    era_desc="12th-13th century AD, Kediri, East Java — capital of Kadiri kingdom",
    scene_desc="Wide cinematic view of the Kadiri capital at Daha. Royal palace complex on elevated ground overlooking the Brantas river valley. Wooden pendopo (pavilion) structures with tiled roofs visible. Irrigated rice paddies along the river. Dense tropical forest on hillsides. The kingdom that produced Bharatayuddha, introduced 3-tier administration, and built the first Indonesian navy (Senapati Sarwwajala). No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on palace and river valley), cool 6500K sky fill. Mid contrast 3:1. Morning mist over Brantas.",
    mood_desc="Golden age capital — Daha/Kadiri, the kingdom of poets and administrators. Where Jayabhaya ruled, Mpu Panuluh wrote, and the foundations of Javanese statecraft were laid. A sophisticated agrarian kingdom that preceded Singhasari and Majapahit.",
)

L002 = l_prompt(
    name="Tumapel / Singhasari (early Singhasari capital)",
    era_desc="13th century AD (1222-1292), Malang, East Java — Singhasari kingdom",
    scene_desc="Wide view of Tumapel — the Singhasari capital at the foot of Mount Kawi. Royal compound with wooden structures on raised stone platforms. Mount Kawi towering behind. Tropical forest on mountain slopes. Open agricultural land in foreground. The place where Ken Arok established his kingdom after defeating Kadiri in 1222. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on compound and Mount Kawi), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="Rise of a new power — Tumapel/Singhasari, where a commoner's ambition became a kingdom. From here, five kings would rule, culminating in Kertanagara's grand vision of cakrawala mandala — a united Nusantara.",
)

L003 = l_prompt(
    name="Candi Singhasari (Singosari temple complex)",
    era_desc="13th century AD, Malang, East Java — Singhasari temple complex",
    scene_desc="Wide view of the Candi Singhasari temple complex — a stone andesite temple with tall spire, standing on a terrace. Visible: carved reliefs on temple walls (Durga, Ganesa, Agastya, Mahakala, Nandiswara in niches). Two massive Dwarapala guardian statues (3.7 meters tall) flanking the entrance to the complex. Alun-alun (square) in front. Mount Kawi in background. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, golden on andesite temple), cool 6500K sky fill. High contrast 4:1. Long shadows.",
    mood_desc="Stone legacy — Candi Singhasari, the temple that outlived its kingdom. Its reliefs and statues (including the famous Prajnaparamita) represent the highest artistic achievement of the Singhasari period. The Dwarapala guardians still stand, silent witnesses to a fallen dynasty.",
)

L004 = l_prompt(
    name="Candi Jawi (Kertanagara's tantrik temple)",
    era_desc="13th century AD (1270-1292), Pasuruan, East Java — Siwa-Buddha temple",
    scene_desc="Wide view of Candi Jawi — a unique temple combining Hindu Siwa (lower level) and Buddhist (upper level with stupa). Brick and andesite structure with tall cylindrical tower topped by a stupa. Located at the foot of Mount Kumukus. The temple embodies Kertanagara's vision of uniting Siwa and Buddha in one structure. Tropical vegetation surrounding. No people.",
    lighting_desc="warm 3500K golden sunrise from camera left (key light, raking across temple revealing both Hindu and Buddhist elements), cool 6500K sky fill. Mid contrast 3:1. Morning mist from Mount Kumukus.",
    mood_desc="Two faiths, one tower — Candi Jawi, Kertanagara's architectural statement of religious unity. Siwa below, Buddha above. Not syncretism, but parallelism — two paths to the same peak, embodied in stone.",
)

L005 = l_prompt(
    name="Bengawan Solo river (Janggala-Pangjalu border)",
    era_desc="11th-12th century AD, East Java — border river between Janggala and Pangjalu",
    scene_desc="Wide view of a small river (Sungai Ndempol) winding through agricultural land near Mojokerto. On one bank: remnants of a prasasti stone (Pandan inscription, 1042 AD). On the other bank: another prasasti (Turunhyang, 1036/1044 AD). The river that served as the natural border between Janggala (west) and Pangjalu (east) after Mpu Bharada divided Airlangga's kingdom. Rice paddies, scattered villages. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on river and paddies), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="The divided land — Sungai Ndempol, the river that split Java in two. After Mpu Bharada poured water from his kendi in 1042 AD, this small stream became the border between rival kingdoms. For 60 years, brothers fought across this water.",
)

L006 = l_prompt(
    name="Kudadu village (Raden Wijaya's hiding place)",
    era_desc="1292 AD, East Java — village where Raden Wijaya hid from Jayakatwang",
    scene_desc="Wide view of a small village clearing at dawn. Simple wooden houses on stilts. Tropical forest surrounding. A village well and a small rice field. This is where Raden Wijaya arrived at dawn, exhausted, hungry, and hopeless, after fleeing Jayakatwang's attack on Singhasari. The village headman sheltered him, gave food and water. The place where the future founder of Majapahit was saved by commoners. No people.",
    lighting_desc="cold 5500K pre-dawn light (key light, dim and blue-grey), warm 2700K firelight from village houses (fill). Low contrast 2:1. Morning mist.",
    mood_desc="The lowest point — Kudadu, where a prince became a fugitive. At dawn, hungry and broken, Raden Wijaya was saved by a village headman's kindness. From this humble refuge, the greatest kingdom in Nusantara history would be born. The Prasasti Kudadu (1294 AD) commemorates this act of compassion.",
)

L007 = l_prompt(
    name="Dharmasraya / Padangroco (Sumatra, Kertanagara's diplomatic reach)",
    era_desc="13th century AD (1286), Sumatra Barat — where Kertanagara sent the Amoghapasa statue",
    scene_desc="Wide view of the Batanghari river upper reaches at Dharmasraya, Sumatra Barat. Dense tropical rainforest. Stone foundation of a shrine (where the Amoghapasa Lokeswara statue was placed in 1286 AD). The Prasasti Dharmasraya on the statue's base records Kertanagara's gift. The site proves Singhasari's influence reached Sumatra — the cakrawala mandala was not just a dream. No people.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, revealing rainforest and stone foundation), cool 6500K sky fill. Mid contrast 3:1. Rainforest mist.",
    mood_desc="Diplomatic reach — Dharmasraya, where Kertanagara's statue of Amoghapasa Lokeswara was sent in 1286 AD, received with joy by the local king. The cakrawala mandala vision made real: Singhasari's influence extended from Java to Sumatra. A diplomatic act that preceded the military conquests of Majapahit.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Prasasti Mula Malurung (first mention of 'Nusantara')",
    era_desc="1255 AD (1177 Saka), Singhasari — copper plate inscription with the word 'Nusantara'",
    scene_desc="A copper plate inscription (prasasti) — multiple plates joined by copper ring. Visible: Old Javanese script (Kawi/aksara Jawa Kuno) in Javanese Kuno language. The text contains the first written mention of 'Nusantara' — 'anuluyani nusantara' (then becoming Nusantara). Issued by King Wisnuwardhana. The plates show green patina, approximately 20 cm per plate. 5 plates visible.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing patina and script), low ambient fill. High contrast 5:1.",
    mood_desc="The first 'Nusantara' — the Mula Malurung inscription, where the word 'Nusantara' appears for the first time in history. Wisnuwardhana declared that the land beneath his feet would become the umbrella of the world, all Jawadwipamandala, then Nusantara. A concept born in 1255 AD that still defines Indonesia today.",
)

A002 = a_prompt(
    name="Arca Prajnaparamita (Singhasari masterpiece)",
    era_desc="13th century AD, Singhasari — finest Buddhist sculpture from Java",
    scene_desc="A stone andesite statue of Prajnaparamita (Goddess of Transcendent Wisdom) on dark background. The figure sits in lotus position (dhyana asana) with hands in dharmachakra mudra (turning the wheel of Dharma). Serene face with half-closed eyes, elaborate jewelry (makuta, necklace, armlets). Andesite stone, grey-brown color with some weathering. Approximately 1.5 meters tall. One of the finest sculptures ever produced in Southeast Asia.",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing stone texture and carving detail), low ambient fill. High contrast 4:1.",
    mood_desc="Perfection in stone — the Prajnaparamita of Singhasari, embodying the highest artistic achievement of East Javanese sculpture. This goddess of wisdom represents the intellectual sophistication of the Singhasari court, where Buddhist philosophy and artistic craft reached their pinnacle.",
)

A003 = a_prompt(
    name="Kakawin Bharatayuddha manuscript (lontar)",
    era_desc="1157 AD, Kadiri — Mpu Sedah and Mpu Panuluh's epic poem",
    scene_desc="An opened lontar (palm-leaf) manuscript on dark surface. Visible: Old Javanese text in Kawi script, written with stylus on dried palm leaves. The text is the Bharatayuddha — the Javanese retelling of the Mahabharata's great war, composed by Mpu Sedah (started) and Mpu Panuluh (completed) in 1157 AD under King Jayabhaya. The lontar is aged brown, with some edge damage. Approximately 30 cm long per leaf, 4-5 leaves visible.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing script and palm-leaf texture), low ambient fill. High contrast 4:1.",
    mood_desc="Words that outlived kingdoms — the Bharatayuddha lontar, the greatest literary work of Kadiri. Written 1157 AD, it served as both epic literature and military manual. Its themes of dharma, duty, and righteous war resonated through Singhasari, Majapahit, and into modern Indonesian culture.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the court of Kadiri under Jayabhaya — king, poet, and warriors",
    era_desc="12th century AD (1157 AD), Daha/Kadiri, East Java",
    composition="Group of 4 individuals in a court scene pose. Position 1 (center): King Jayabhaya, seated on a raised chair, wearing full royal regalia with Vishnu motifs, holding ceremonial mace. Position 2 (left): Mpu Panuluh, standing with lontar manuscript and stylus, wearing simple white scholarly attire. Position 3 (right): a Kadiri warrior (makasirkasir), standing with spear and leather armor, wearing warrior costume with animal-name (Kbo = buffalo) motif. Position 4 (far right): a royal advisor (Rakai Kanuruhan), standing with administrative scroll. All in appropriate Kadiri-era costumes.",
    mood="The golden court — Jayabhaya's Kadiri at its peak: the king who patronized literature, the poet who immortalized it, the warrior who protected it, and the administrator who organized it. A model of the sophisticated Javanese state that would inspire Singhasari and Majapahit.",
    k_refs=["2C-K001 (Jayabhaya)", "2C-K006 (Mpu Panuluh)"],
    avoid_extra=", Islamic costume, Buddhist monk robe, modern clothing",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "2C-K001-jayabhaya.txt": K001,
        "2C-K002-ken-arok.txt": K002,
        "2C-K003-wisnuwardhana.txt": K003,
        "2C-K004-kertanagara.txt": K004,
        "2C-K005-raden-wijaya.txt": K005,
        "2C-K006-mpu-panuluh.txt": K006,
        # L — 7
        "2C-L001-daha-kadiri.txt": L001,
        "2C-L002-tumapel-singhasari.txt": L002,
        "2C-L003-candi-singhasari.txt": L003,
        "2C-L004-candi-jawi.txt": L004,
        "2C-L005-sungai-ndempol.txt": L005,
        "2C-L006-kudadu.txt": L006,
        "2C-L007-dharmasraya.txt": L007,
        # A — 3
        "2C-A001-prasasti-mula-malurung.txt": A001,
        "2C-A002-arca-prajnaparamita.txt": A002,
        "2C-A003-bharatayuddha-lontar.txt": A003,
        # S — 1
        "2C-S001-pendapa-kadiri.txt": S001,
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
