#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 1D — Logam Awal (2.500 SM – abad 5 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/1D-prasejarah-logam-awal/prompts"

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

def f_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc):
    return f"""Cinematic realistic documentary wildlife photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic animal textures, 35mm film grain, deep depth of field f/5.6, 200mm telephoto lens, 8K hyperdetailed, BBC Earth wildlife documentary aesthetic. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: modern animals, domesticated animals, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."""

def s_prompt(name, era_desc, composition, mood, k_refs, avoid_extra=""):
    k_ref_note = " | ".join(k_refs)
    return f"""Cinematic realistic group character reference of {name}, {era_desc}, arranged in a standing group pose on a clean solid light cream studio background. {composition} Clean studio background, no environment, no historical setting, no landscape elements — neutral studio reference only.

IMPORTANT: Upload the following character reference images before generating: {k_ref_note}. Use each uploaded image as the exact face, body, and identity reference. This prompt only defines group composition, pose, and props — NOT physical features.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting, no dramatic lighting.

Mood: neutral studio reference, group turnaround for production consistency. {mood}

Style: photorealistic skin texture, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: environment background, landscape, historical setting, dramatic lighting, inconsistent faces with reference images, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


# ===== K PROMPTS — 5 karakter =====

K001 = k_prompt(
    name="a Primus Inter Pares (community leader of the perundagian era)",
    era_desc="500 BC - 300 AD, Java — late prehistoric metal age community leader",
    phenotype="Male, 40-55 years old, 165 cm tall, medium brown skin, deep-set dark brown eyes, moderate brow ridge, broad nose, full lips, strong jaw with some greying. Short black wavy hair with early greying at temples. Stocky build from settled agrarian lifestyle. Distinguished bearing — authority from achievement not birthright. Skin marked by sun exposure. Tattoo marks on arms (status symbols).",
    costume="Wearing a woven batik-pattern cloth sarong, barkcloth upper wrap, multiple necklaces of imported glass beads (Roman/Indian), gold ear ornaments, bronze arm ring. Woven fiber headband with small gold disc.",
    props="holding a bronze ceremonial axe (nekara mini)",
    mood="First among equals — the Primus Inter Pares, a leader chosen by peers for wisdom and achievement, not born to rule. The bridge between egalitarian foragers and hierarchical kingdoms.",
)

K002 = k_prompt(
    name="a metalworker (Undagi) of the perundagian era",
    era_desc="500 BC - 300 AD, Gilimanuk/Pangkung Paruk, Bali — bronze and gold craftsman",
    phenotype="Male, 30-45 years old, 162 cm tall, medium brown skin with heat-darkened complexion from forge work. Deep-set dark brown eyes, moderate brow ridge, broad nose. Short black hair. Stocky muscular build from metalworking. Burn scars on forearms and hands. Soot-stained skin. Wearing a barkcloth wrap and simple fiber belt.",
    costume="",
    props="holding a clay crucible with bronze pour tongs",
    mood="Master of fire and metal — the Undagi, the first specialist craftspeople who transformed society by mastering bronze and gold. Their skills created the objects of power that would define the coming kingdoms.",
)

K003 = k_prompt(
    name="a barkcloth maker (pengrajin barkcloth)",
    era_desc="500 BC - 300 AD, Sumba/Sumbawa — textile artisan of the prehistoric era",
    phenotype="Female, 30-40 years old, 158 cm tall, medium brown skin, dark brown eyes, moderate brow ridge, broad nose. Long black hair tied back. Lean build from artisanal work. Hands calloused from bark beating.",
    costume="Wearing a barkcloth wrap skirt and simple fiber upper garment. Necklace of shell beads.",
    props="holding a wooden bark-beater mallet",
    mood="Weaver of the first textiles — the barkcloth maker, transforming tree bark into the first wearable fabric, predating woven textiles. A craft tradition that survives in parts of Indonesia to this day.",
)

K004 = k_prompt(
    name="a glass bead craftsman of Gilimanuk",
    era_desc="100 BC - 300 AD, Gilimanuk, Bali — Indo-Pacific bead maker",
    phenotype="Male, 25-35 years old, 160 cm tall, light brown skin, dark brown eyes, moderate nose bridge. Short black hair. Lean build from detailed craftwork. Fingers stained with glass residue. Wearing a barkcloth wrap and simple bead necklace.",
    costume="",
    props="holding a finished glass bead strand",
    mood="Maker of treasures — the bead craftsman of Gilimanuk, producing the Indo-Pacific glass beads that became trade currency across the Indian Ocean for a thousand years.",
)

K005 = k_prompt(
    name="a Dongson-drum bearer (ritual specialist)",
    era_desc="200 BC - 200 AD, Java — ceremonial drummer of the metal age",
    phenotype="Male, 25-35 years old, 164 cm tall, medium brown skin, dark brown eyes, prominent cheekbones, broad nose. Short black hair tied with fiber band. Lean athletic build. Wearing a barkcloth wrap, bronze ear discs, and shell bead necklace. Ritual face paint (red ochre lines on cheeks).",
    costume="",
    props="holding a small bronze Dongson drum (moko)",
    mood="Voice of the ancestors — the ritual specialist who played the bronze Dongson drums. These drums, imported from Vietnam, were the most powerful ritual objects of the metal age, bridging the human and spirit worlds.",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Gunung Padang (megalithic punden berundak)",
    era_desc="500 BC, Cianjur, West Java — largest megalithic site in Indonesia",
    scene_desc="Wide aerial view of Punden Berundak Gunung Padang — massive stepped stone pyramid made of andesite blocks, multiple terraces (5+ visible) rising from base to peak. Uppermost terrace has a menhir (standing stone). Tropical rainforest covering surrounding hills. The site is the largest megalithic monument in Indonesia. Distant volcanic mountains. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, raking across terraces revealing stone texture), cool 6500K sky fill. Mid contrast 3:1. Morning mist in valley.",
    mood_desc="Sacred mountain — Gunung Padang, the monumental expression of ancestor worship. A stepped pyramid built by a community organized enough to move thousands of tons of stone, a precursor to the temple culture of Hindu-Buddhist Java.",
)

L002 = l_prompt(
    name="Pulau Kampai (early metal age port, Sumatra Utara)",
    era_desc="5th-7th century AD, Sumatra Utara coast — early trade port",
    scene_desc="Wide view of a coastal trading settlement at Pulau Kampai. Raised wooden houses on stilts along the shoreline. Simple wooden jetty with small outrigger canoes. Open area with evidence of trade: glass beads, Indian pottery sherds, and bronze fragments scattered. Coconut palms and banana plants. The coast where early metal-age traders connected Nusantara to Indian Ocean commerce. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on village and coast), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="Gateway to the world — Pulau Kampai, one of the earliest trading ports where Indian, Roman, and local goods exchanged hands. The prelude to the great trading empires of Srivijaya and Majapahit.",
)

L003 = l_prompt(
    name="Pangkung Paruk (metal age burial site, Bali)",
    era_desc="122-331 AD, Bali — gold bead burial site",
    scene_desc="Wide view of a tropical riverbank clearing at Pangkung Paruk, Bali. Exposed archaeological layers with visible burial goods: gold beads, bronze objects, and pottery sherds in sediment. River flowing past. Dense tropical vegetation. The site where the most spectacular gold bead burial in Indonesia was found — a woman buried with over 100 gold beads of Roman/Indian origin. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, revealing sediment layers), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="Golden graves — Pangkung Paruk, where a person of high status was buried with treasures from across the known world. The gold beads tell a story of connections reaching from Rome to Bali.",
)

L004 = l_prompt(
    name="Gilimanuk (metal age settlement, Bali)",
    era_desc="1st-4th century AD, Bali northwest coast — bead-making settlement",
    scene_desc="Wide view of the Gilimanuk coastal settlement site. Sandy beach with raised wooden houses on stilts. Workshop areas with clay crucibles, glass fragments, and bead-making debris visible on ground. Outrigger canoes on beach. The site was a major bead production center — Indo-Pacific glass beads made here were traded across the Indian Ocean. Mangrove forest at river mouth. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on beach and village), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="Factory of the ancient world — Gilimanuk, where skilled craftspeople mass-produced glass beads that became the currency of Indian Ocean trade. A pre-industrial manufacturing center.",
)

L005 = l_prompt(
    name="Sembiran-Pacung (early Indian contact, Bali)",
    era_desc="200 BC - 200 AD, Bali northeast coast — earliest Indian contact site",
    scene_desc="Wide view of the Sembiran coastal village site on Bali's northeast coast. Raised wooden houses on stilts near the beach. Pottery fragments (Indian rouletted ware) visible in garden soil. Simple jetty with outrigger canoes. The site where the earliest evidence of Indian contact in Bali was found — Indian pottery dating to 200 BC-200 AD. Coconut palms. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on village and coast), cool 6500K sky fill. Mid contrast 3:1. Sea mist.",
    mood_desc="First contact — Sembiran, where Indian traders first made landfall in Bali, bringing pottery, glass beads, and new ideas. The beginning of cultural exchange that would transform Nusantara.",
)

L006 = l_prompt(
    name="Lebak Cibedug (megalithic site, Banten)",
    era_desc="500 BC - 500 AD, Banten — megalithic stone monument",
    scene_desc="Wide view of the Lebak Cibedug megalithic site in Banten. Stone terraces built on a hillside, with menhirs (standing stones) arranged on the terraces. Large flat stones forming altars. Tropical forest surrounding the site. The megalithic tradition of ancestor worship expressed in stone. Distant hills of Banten. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, raking across stone terraces), cool 6500K sky fill. Mid contrast 3:1. Forest mist.",
    mood_desc="Stone ancestors — Lebak Cibedug, where megalithic traditions of erecting standing stones and building terraced monuments persisted alongside the new metal age. The old ways did not die; they evolved.",
)

L007 = l_prompt(
    name="Tanah Luwu (early iron production, Sulawesi Selatan)",
    era_desc="2,000 years ago, Sulawesi Selatan — earliest iron smelting in Indonesia",
    scene_desc="Wide view of a river valley in Tanah Luwu, Sulawesi Selatan. Exposed iron ore deposits on hillside. Remains of clay iron-smelting furnaces at valley floor. Slag heaps (iron production waste) visible. Dense tropical forest. The site that produced the earliest evidence of iron smelting in Indonesia, around 2,000 years ago. No people.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, revealing ore deposits and furnace remains), cool 6500K sky fill. Mid contrast 3:1. Valley mist.",
    mood_desc="Iron from the earth — Tanah Luwu, where Indonesians first smelted their own iron from local ore. The mastery of iron would transform warfare, agriculture, and ultimately society itself.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Dongson bronze drum (nekara)",
    era_desc="200 BC - 200 AD, found across Nusantara — imported from Vietnam",
    scene_desc="A large bronze Dongson drum (nekara) on dark surface. Visible: ornate decoration with concentric circles, star/sun motif at center, geometric patterns, stylized frogs on rim, and warrior/ritual scenes around the body. The drum is 60 cm tall, 50 cm diameter. Greenish-black patina on bronze. These drums were the most prestigious ritual objects of the metal age in Indonesia, imported from the Dongson culture of Vietnam.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing bronze texture and relief decoration), low ambient fill. High contrast 5:1.",
    mood_desc="The voice of power — the Dongson drum, the most prestigious object of the Indonesian metal age. Beaten during rituals, it connected communities to ancestors and the cosmos. Its presence signaled wealth, status, and connection to the wider Southeast Asian world.",
)

A002 = a_prompt(
    name="gold burial beads from Pangkung Paruk",
    era_desc="122-331 AD, Pangkung Paruk, Bali — Roman/Indian gold beads",
    scene_desc="10-15 gold beads arranged on dark velvet. Various shapes: spherical, barrel, bicone. Gold color with some oxidation. Each bead 5-10 mm. These beads were found in a burial at Pangkung Paruk — part of the most spectacular gold burial in prehistoric Indonesia. The beads show Roman/Indian manufacturing techniques, evidence of long-distance trade connections. A few glass beads visible for comparison.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing gold luster and bead shapes), low ambient fill. High contrast 4:1.",
    mood_desc="Gold from afar — these beads traveled thousands of miles from Roman or Indian workshops to a burial in Bali. They speak of a world already connected by trade, centuries before the first written records in Nusantara.",
)

A003 = a_prompt(
    name="stone sarcophagus (Bali megalithic burial)",
    era_desc="500 BC - 500 AD, Bali — megalithic stone coffin tradition",
    scene_desc="A large stone sarcophagus (2 meters long) carved from a single block of volcanic tuff. Visible: lid with carved human figure or geometric motif, body of sarcophagus with carved decorations. The sarcophagus is weathered and partially covered in moss. Found at various sites in Bali. These were burial containers for high-status individuals of the megalithic tradition.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing carved surface texture), low ambient fill. High contrast 4:1.",
    mood_desc="House of the ancestors — the stone sarcophagus of Bali, where the honored dead were laid to rest in carved stone coffins. A tradition that bridged megalithic ancestor worship and the emerging Hindu-Buddhist culture.",
)


# ===== F PROMPTS — 1 fauna =====

F001 = f_prompt(
    name="domesticated water buffalo in early metal-age Jawa village",
    era_desc="500 BC - 300 AD, Java — early domesticated buffalo in agricultural landscape",
    scene_desc="Wide cinematic wildlife shot of 3-4 domesticated water buffalo (Bubalus bubalis) in a flooded rice paddy near a raised wooden village. Large dark grey animals with curved horns, standing in mud and water. One calf nursing. Background: stilt houses, palm trees, early agricultural landscape. The buffalo was introduced from mainland Southeast Asia and transformed Javanese agriculture. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on buffalo and paddy), cool 6500K sky fill. Mid contrast 3:1. Water reflections.",
    mood_desc="Beasts of burden — the water buffalo, the animal that powered the agricultural revolution in Nusantara. With buffalo to plow, rice production expanded, populations grew, and the foundations of the first kingdoms were laid.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="a perundagian community at a metal-age village",
    era_desc="200 BC - 200 AD, Java/Bali",
    composition="Group of 4 individuals in a natural group pose. Position 1 (left): community leader (primus inter pares), standing with arms crossed, wearing multiple bead necklaces and gold ornaments, holding a bronze ceremonial axe. Position 2 (center-left): metalworker, holding clay crucible, wearing barkcloth with soot stains. Position 3 (center-right): barkcloth maker, holding wooden mallet, wearing barkcloth wrap and shell beads. Position 4 (right): Dongson drum bearer, holding small bronze drum, wearing ritual ochre face paint. All wearing woven cloth or barkcloth garments reflecting different craft specializations.",
    mood="Community of specialists — the perundagian village, where the first craft specialists (metalworker, textile maker, bead maker, ritual drummer) emerged alongside community leaders. A society growing more complex, on the eve of the first kingdoms.",
    k_refs=["1D-K001 (primus inter pares)", "1D-K002 (undagi metalworker)", "1D-K003 (barkcloth maker)", "1D-K005 (Dongson drum bearer)"],
    avoid_extra="",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 5
        "1D-K001-primus-inter-pares.txt": K001,
        "1D-K002-undagi-logam.txt": K002,
        "1D-K003-pengrajin-barkcloth.txt": K003,
        "1D-K004-pengrajin-manik-gilimanuk.txt": K004,
        "1D-K005-dongson-drum-bearer.txt": K005,
        # L — 7
        "1D-L001-gunung-padang.txt": L001,
        "1D-L002-pulau-kampai.txt": L002,
        "1D-L003-pangkung-paruk.txt": L003,
        "1D-L004-gilimanuk.txt": L004,
        "1D-L005-sembiran-pacung.txt": L005,
        "1D-L006-lebak-cibedug.txt": L006,
        "1D-L007-tanah-luwu.txt": L007,
        # A — 3
        "1D-A001-nekara-dongson.txt": A001,
        "1D-A002-manik-emas-pangkung-paruk.txt": A002,
        "1D-A003-sarkofagus-bali.txt": A003,
        # F — 1
        "1D-F001-kerbau.txt": F001,
        # S — 1
        "1D-S001-komunitas-perundagian.txt": S001,
    }

    # Delete old v1 files
    old_files = [
        "1D-A001-nekara-dongson.txt", "1D-A002-manik-emas-mesir-roma.txt",
        "1D-A003-sarkofagus-bali.txt",
        "1D-K001-primus-inter-pares.txt", "1D-K002-undagi-logam.txt",
        "1D-K003-pengrajin-barkcloth.txt", "1D-K004-pengrajin-manik-gilimanuk.txt",
        "1D-L001-gunung-padang.txt", "1D-L002-pulau-kampai.txt",
        "1D-L003-pangkung-paruk.txt", "1D-L004-gilimanuk.txt",
        "1D-L005-dataran-tinggi-lore.txt",
    ]
    for f in old_files:
        path = os.path.join(OUTPUT_DIR, f)
        if os.path.exists(path):
            os.remove(path)
            print(f"  Deleted: {f}")

    for filename, content in prompts.items():
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            f.write(content)
        print(f"  Created: {filename}")

    print(f"\n✅ Total: {len(prompts)} files (v2.1)")
    print(f"   K: 5 | L: 7 | A: 3 | F: 1 | S: 1")

if __name__ == "__main__":
    main()
