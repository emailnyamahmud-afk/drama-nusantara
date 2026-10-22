#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 2D — Majapahit (Abad 13-16 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/2D-majapahit/prompts"

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
    name="Gajah Mada, Mahapatih of Majapahit",
    era_desc="14th century AD (1336-1364), Majapahit — greatest prime minister in Nusantara history",
    phenotype="Male, 40-50 years old, Javanese phenotype with golden brown skin, sharp fierce features, determined piercing eyes, thick beard. Black hair in topknot. Muscular stocky build from military background. Battle scars on arms and chest. Tattoo marks (traditional Javanese warrior tattoos).",
    costume="Wearing Majapahit mahapatih costume: dark batik blangkon (headcap, NOT turban), dark maroon silk jacket with gold-thread embroidered Sumpah Palapa motif, brown batik sarong with parang pattern, gold armlets, keris pusaka at waist. Military commander's bearing.",
    props="holding a keris pusaka (ceremonial dagger) upright",
    mood="Sumpah Palapa — Gajah Mada, the mahapatih who swore not to taste spice until all of Nusantara was united under Majapahit. His military campaigns brought Bali, Sunda, Palembang, and other regions under Majapahit's control. The architect of the greatest empire in Indonesian history.",
    avoid_extra=", Islamic costume, turban, Hindu makuta, modern military uniform",
)

K002 = k_prompt(
    name="Hayam Wuruk, King of Majapahit",
    era_desc="14th century AD (1350-1389), Majapahit — greatest king of Majapahit's golden age",
    phenotype="Male, 25-35 years old (at peak), Javanese phenotype with golden brown skin, refined regal features, intelligent eyes, calm scholarly expression. Black hair in elaborate topknot with gold ornaments. Slender build — more scholar-king than warrior. Light complexion from palace life.",
    costume="Wearing full Majapahit royal costume: gold makuta with Girindra (Siwa) motif, gold hara necklace, gold keyura armlets, gold kankana bracelets, red-and-gold kemben, elaborate batik kain with ceplok pattern, keris at waist. Lencana: Girindrawardhana (mountain lord).",
    props="holding a royal scepter (tetuwuhan)",
    mood="The golden king — Hayam Wuruk, under whose reign Majapahit reached its greatest extent. Patron of Mpu Prapanca (Nagarakretagama) and Mpu Tantular (Sutasoma). His reign is documented in the Nagarakretagama as the peak of Javanese civilization: art, literature, architecture, and empire all flourished.",
)

K003 = k_prompt(
    name="Tribhuwana Tunggadewi, Queen Regent of Majapahit",
    era_desc="14th century AD (1328-1350), Majapahit — queen who appointed Gajah Mada",
    phenotype="Female, 35-45 years old, Javanese phenotype with golden brown skin, dignified regal features, calm authoritative expression. Black hair in elaborate hairstyle with gold pins. Medium build. Forehead marked with Vaishnava tilaka.",
    costume="Wearing Majapahit queen regent costume: gold makuta with Bhre Kahuripan motif, gold hara necklace with Laksmi pendant, gold keyura armlets, deep green-and-gold kemben, batik kain with parang pattern. Queen's elegance blended with royal authority.",
    props="holding a royal decree scroll",
    mood="The queen who chose the mahapatih — Tribhuwana appointed Gajah Mada as Mahapatih in 1336, setting Majapahit on the path to empire. Daughter of Raden Wijaya, mother of Hayam Wuruk. A ruler who understood that the right general matters more than personal glory.",
    avoid_extra=", Islamic costume, modern dress, Hindu goddess costume",
)

K004 = k_prompt(
    name="Raden Wijaya / Kertarajasa Jayawardhana, founder of Majapahit",
    era_desc="13th-14th century AD (1293-1309), East Java — founder of Majapahit",
    phenotype="Male, 25-35 years old, Javanese phenotype with golden brown skin, sharp regal features with weathered look from exile and war. Black hair in topknot, full beard. Muscular build from military campaigns.",
    costume="Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif (Garudamukha), gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold kemben, batik kain with parang pattern, keris pusaka at waist. Lencana: Garudamukha.",
    props="holding a Garudamukha scepter",
    mood="Survivor and founder — Raden Wijaya escaped Jayakatwang, allied with Madura, used Kubilai Khan's Tartar army to destroy Kadiri, then expelled the Tartars. Crowned as Kertarajasa Jayawardhana, founder of Majapahit (1293). Didharmakan as Harihara (Siwa-Wisnu) at Candi Simping, Blitar.",
)

K005 = k_prompt(
    name="Mpu Prapanca, court poet of Majapahit",
    era_desc="14th century AD (1365), Majapahit — author of Nagarakretagama",
    phenotype="Male, 50-60 years old, Javanese phenotype with golden brown skin, wise gentle features, scholarly expression. Shaved head with small topknot (resi/buddhist scholar style). Thin build from scholarly life. Hands stained with lontar ink.",
    costume="Wearing simple Buddhist scholarly attire: white cotton wrap, upavita (sacred thread), wooden bead mala necklace. No jewelry — a scholar's dignity.",
    props="holding a lontar manuscript (the Nagarakretagama)",
    mood="Chronicler of empire — Mpu Prapanca, who in 1365 AD wrote the Nagarakretagama (Desawarnana), the most important historical text of Majapahit. His poem describes Hayam Wuruk's royal progress through the realm, listing territories, temples, and customs. Without his work, much of Majapahit's history would be lost.",
)

K006 = k_prompt(
    name="Adityawarman, King of Malayu (Majapahit vassal)",
    era_desc="14th century AD (1347-1375), Dharmasraya, Sumatra — Majapahit's man in Sumatra",
    phenotype="Male, 40-50 years old, Sumatran-Javanese mixed phenotype with medium brown skin, strong features with spiritual intensity. Black hair in matted topknot (tantric practitioner). Lean build. Forehead marked with ritual ash. Ritual scars from tantrik practices.",
    costume="Wearing tantrik royal costume blending Majapahit and Sumatran styles: gold makuta with Bhairawa skull motif, gold necklace with human bone beads, gold armlets with naga motif, dark red silk kemben with tantrik symbols, keris at waist. Blends Buddhist Vajrayana with local Malay traditions.",
    props="holding a small bronze Amoghapasa statue",
    mood="Vassal and tantrika — Adityawarman, Majapahit's appointed ruler of Malayu (Sumatra). He received Kertanagara's Amoghapasa statue and re-consecrated it as his own. His inscriptions (in Old Malay and Sanskrit) show a unique blend of Majapahit authority and local Sumatran tantrik tradition.",
    avoid_extra=", Islamic costume, simple Hindu costume without tantrik elements",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Trowulan (Majapahit capital city)",
    era_desc="14th century AD, East Java — capital of the greatest Nusantara empire",
    scene_desc="Wide cinematic aerial view of Trowulan — the sprawling capital of Majapahit. Visible: royal palace complex on elevated ground, with pendopo (pavilion) structures and brick foundations. Canal system connecting to Brantas river. Residential areas with raised wooden houses. Market area (Bazaar). Temple compounds (Candi Brahu, Candi Tikus). Surrounding rice paddies and tropical forest. The largest city in Nusantara at its peak — estimated 100,000+ inhabitants. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on city and paddies), cool 6500K sky fill. Aerial drone perspective from 300m. Mid contrast 3:1. Morning mist.",
    mood_desc="The greatest city — Trowulan, capital of Majapahit at its peak under Hayam Wuruk. A cosmopolitan metropolis where Javanese, Chinese, Indian, and Arab traders mingled. Canals, temples, palaces, and markets — the center of an empire stretching from Sumatra to New Guinea.",
)

L002 = l_prompt(
    name="Candi Brahu (royal temple, Trowulan)",
    era_desc="14th-15th century AD, Trowulan — believed cremation temple of Majapahit kings",
    scene_desc="Wide view of Candi Brahu — a tall red-brick temple standing alone in a clearing near Trowulan. Rectangular base with tall narrow tower. Brick walls showing intricate geometric patterns. The temple is associated with the cremation of King Brawijaya (last king of Majapahit). Surrounded by tropical vegetation. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, golden on red brick), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="The last temple — Candi Brahu, where the last kings of Majapahit were cremated. A red-brick monument that witnessed both the glory and the fall of the greatest Javanese empire.",
)

L003 = l_prompt(
    name="Brantas river port (Majapahit maritime gateway)",
    era_desc="14th century AD, East Java — Majapahit's river port to the Java Sea",
    scene_desc="Wide cinematic view of the Brantas river mouth where it meets the Java Sea. Wooden docks with large trading ships (jong, kelulus, pelang) loading and unloading cargo. Warehouses along the riverbank. Outrigger canoes. Chinese, Indian, and Arab ships visible. The port that connected Majapahit's agrarian interior to the maritime trade network spanning from Malacca to the Moluccas. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on river and ships), cool 6500K sky fill. Mid contrast 3:1. Sea haze, river mist.",
    mood_desc="Maritime gateway — the Brantas river port, where Majapahit's agricultural surplus met international trade. From here, rice, gold, and textiles flowed out; spices, silk, and ceramics flowed in. The economic heart of the empire.",
)

L004 = l_prompt(
    name="Candi Sukuh (punden berundak temple, Gunung Lawu)",
    era_desc="15th century AD, Gunung Lawu, Central Java — late Majapahit revivalist temple",
    scene_desc="Wide view of Candi Sukuh — a unique stepped pyramid temple (punden berundak) on the slopes of Gunung Lawu. Unlike typical Javanese temples, it has a flat stepped design resembling pre-Hindu megalithic forms. Stone reliefs with sexual/purification themes. A return to indigenous architectural forms at the end of the Hindu-Buddhist era. Mountain forest surrounding. No people.",
    lighting_desc="warm 3500K morning sun from camera right (key light, revealing stone terraces), cool 6500K sky fill. High contrast 4:1. Mountain mist.",
    mood_desc="Return to the mountain — Candi Sukuh, built at the end of Majapahit, represents a revival of pre-Hindu megalithic forms. A society looking backward to its roots even as the Hindu-Buddhist order was ending. The punden berundak form would persist in Javanese sacred architecture for centuries.",
)

L005 = l_prompt(
    name="Gunung Penanggungan (sacred mountain, mandala of temples)",
    era_desc="14th-15th century AD, East Java — sacred mountain with 81 temple sites",
    scene_desc="Wide aerial view of Gunung Penanggungan — a perfect cone-shaped volcanic mountain rising from the East Javanese plain. On its slopes: scattered small temple sites (petirtaan, candi pendharmaan) at various elevations — believed to be 81 sites total. The mountain was considered a sacred mandala, a earthly representation of Mount Meru. Tropical forest on slopes. Rice paddies at base. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on mountain and forest), cool 6500K sky fill. Aerial drone perspective. Mid contrast 3:1. Morning mist on lower slopes.",
    mood_desc="Sacred mountain — Gunung Penanggungan, where kings came to build pendarmaan temples and bathe in sacred springs. A mountain as mandala, with 81 temple sites ascending toward the peak. Where the human realm met the divine.",
)

L006 = l_prompt(
    name="Bubat field (Battle of Bubat site)",
    era_desc="1357 AD, north of Trowulan, East Java — site of the Battle of Bubat",
    scene_desc="Wide view of an open grassy field (alun-alun) north of Trowulan. Flat open terrain with distant volcanic mountains. The site of the Battle of Bubat (1357 AD) — where Majapahit forces under Gajah Mada ambushed and killed the Sunda king and his entourage, preventing the royal marriage that would have ceded power. A tragic field where diplomacy turned to massacre. Open sky. No people.",
    lighting_desc="cold 5500K overcast sky (key light, flat and somber), dim diffuse light. Low contrast 2:1. Wind-blown grass.",
    mood_desc="The field of betrayal — Bubat, where Gajah Mada's ambition turned a royal wedding into a massacre. The Sunda king died here with his family and guards, and the relationship between Majapahit and Sunda was forever broken. A field that marks the dark side of empire.",
)

L007 = l_prompt(
    name="Candi Simping / Candi Sumberjati (pendharmaan of Raden Wijaya, Blitar)",
    era_desc="13th-14th century AD, Blitar, East Java — temple where Raden Wijaya was deified",
    scene_desc="Wide view of Candi Simping (Sumberjati) — a stone temple in a clearing near Blitar. The temple houses the Arca Harihara (half Siwa, half Wisnu) — the deified form of Raden Wijaya (Kertarajasa Jayawardhana), founder of Majapahit. Simple andesite temple structure with carved reliefs. Tropical vegetation surrounding. Distant hills. No people.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, warm on temple stone), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="Founder's temple — Candi Simping, where Raden Wijaya was deified as Harihara (Siwa-Wisnu). The founder of Majapahit, who began as a fugitive in Kudadu and ended as a god in stone. A temple that bridges the human and divine origins of the empire.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Nagarakretagama lontar (Mpu Prapanca's chronicle)",
    era_desc="1365 AD, Majapahit — the most important historical text of Majapahit",
    scene_desc="An opened lontar (palm-leaf) manuscript on dark surface. Visible: Old Javanese text in Kawi script. The Nagarakretagama (Desawarnana) by Mpu Prapanca — a kakawin (poem) describing King Hayam Wuruk's royal progress through Majapahit's territories. Lists temples, provinces, customs, and political structure. The primary source for Majapahit history. Aged brown palm leaves, some edge damage. 5-6 leaves visible, each 30 cm long.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing script and palm texture), low ambient fill. High contrast 4:1.",
    mood_desc="The empire's memory — the Nagarakretagama lontar, without which Majapahit would be a shadow. Mpu Prapanca's poem is not just literature; it is a census, a map, a temple register, and a political manifesto. The document that proved Majapahit's extent and sophistication to the world.",
)

A002 = a_prompt(
    name="Arca Harihara (Siwa-Wisnu deified form of Raden Wijaya)",
    era_desc="13th-14th century AD, Candi Simping, Blitar — deified founder of Majapahit",
    scene_desc="A stone andesite statue of Harihara — a composite deity: right half is Siwa (with matted hair, third eye, trisula), left half is Wisnu (with crown, conch). Standing in samabhanga pose on a lotus base. The statue represents the deified form of Raden Wijaya (Kertarajasa Jayawardhana), founder of Majapahit. Stone is grey-brown andesite, weathered. Approximately 1.5 meters tall.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing the dual nature of the figure — Siwa and Wisnu), low ambient fill. High contrast 4:1.",
    mood_desc="Two gods, one king — the Harihara of Simping, where Raden Wijaya was deified as both Siwa and Wisnu. The founder of Majapahit transcended individual deity — he became the synthesis of Hinduism's two great gods. A statement of royal divinity that legitimized the Rajasa dynasty.",
)

A003 = a_prompt(
    name="Sutasoma lontar (Mpu Tantular's Buddhist-Hindu synthesis)",
    era_desc="14th century AD, Majapahit — the text that inspired 'Bhinneka Tunggal Ika'",
    scene_desc="An opened lontar manuscript on dark surface. Visible: Old Javanese text in Kawi script. The Sutasoma kakawin by Mpu Tantular — a Buddhist text that describes the unity of Siwa and Buddha. Contains the famous verse 'Bhinneka Tunggal Ika' — 'They are different, yet one' — which became Indonesia's national motto. The text embodies Majapahit's religious tolerance. Aged brown palm leaves. 4-5 leaves visible.",
    lighting_desc="warm 2700K raking light from camera right (key light, revealing script), low ambient fill. High contrast 4:1.",
    mood_desc="Unity in diversity — the Sutasoma lontar, where Mpu Tantular wrote 'Bhinneka Tunggal Ika, tan hana dharma mangrwa' — a phrase that would become Indonesia's national motto 600 years later. The idea that different paths can lead to the same truth — the spiritual foundation of tolerance in Majapahit and modern Indonesia.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the court of Majapahit at its peak — king, mahapatih, and poet",
    era_desc="14th century AD (1360s), Trowulan, East Java — golden age of Majapahit",
    composition="Group of 4 individuals in a court scene pose. Position 1 (center, elevated): King Hayam Wuruk, seated on a raised chair, wearing full gold royal regalia with Girindra motif, holding royal scepter. Position 2 (left, standing): Mahapatih Gajah Mada, standing with keris upright, wearing dark maroon military commander's attire with blangkon. Position 3 (right, standing): Mpu Prapanca, holding lontar manuscript and stylus, wearing simple white scholarly attire. Position 4 (far right): a royal guard (makasirkasir) standing with spear, wearing warrior costume. The composition shows the three pillars of Majapahit: royal authority, military power, and intellectual legacy.",
    mood="The golden court — Majapahit at its peak under Hayam Wuruk: the king who ruled, the mahapatih who conquered, and the poet who immortalized. Three men whose collaboration created the greatest empire in Nusantara history.",
    k_refs=["2D-K002 (Hayam Wuruk)", "2D-K001 (Gajah Mada)", "2D-K005 (Mpu Prapanca)"],
    avoid_extra=", Islamic costume, modern clothing",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "2D-K001-gajah-mada.txt": K001,
        "2D-K002-hayam-wuruk.txt": K002,
        "2D-K003-tribhuwana.txt": K003,
        "2D-K004-raden-wijaya.txt": K004,
        "2D-K005-mpu-prapanca.txt": K005,
        "2D-K006-adityawarman.txt": K006,
        # L — 7
        "2D-L001-trowulan.txt": L001,
        "2D-L002-candi-brahu.txt": L002,
        "2D-L003-pelabuhan-brantas.txt": L003,
        "2D-L004-candi-sukuh.txt": L004,
        "2D-L005-gunung-penanggungan.txt": L005,
        "2D-L006-bubat.txt": L006,
        "2D-L007-candi-simping.txt": L007,
        # A — 3
        "2D-A001-nagarakretagama-lontar.txt": A001,
        "2D-A002-arca-harihara.txt": A002,
        "2D-A003-sutasoma-lontar.txt": A003,
        # S — 1
        "2D-S001-pendapa-majapahit.txt": S001,
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
