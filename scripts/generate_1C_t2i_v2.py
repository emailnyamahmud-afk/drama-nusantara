#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 1C — Holosen/Neolitik (12 rb – 2.500 SM)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/1C-prasejarah-holosen-neolitik/prompts"

def k_prompt(name, era_desc, phenotype, costume, props, mood, avoid_extra=""):
    return f"""Cinematic realistic character reference sheet of {name}, {era_desc}, shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view {props}, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. {phenotype} {costume} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8, 50mm lens equivalent, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

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
    name="an adult Papuamelanesia (early Holocene modern human)",
    era_desc="10,000-5,000 years ago, Papua and eastern Indonesia — Australomelanesian phenotype",
    phenotype="Male, 25-35 years old, 168 cm tall, dark brown skin, deep-set dark brown eyes, prominent brow ridge, broad flat nose, full lips, strong jaw. Short black curly hair (tightly coiled, not wavy). Lean muscular build from hunter-gatherer lifestyle. Skin marked by sun exposure and ritual scars on arms and chest.",
    costume="Wearing a barkcloth wrap at waist, simple fiber armbands, and a necklace of small shells and animal teeth.",
    props="holding a stone adze",
    mood="First modern humans of the Holocene — the Papuamelanesia people, descendants of the earliest Homo sapiens to cross Wallacea and reach Sahul. Their ancestry still lives in modern Papuan and eastern Indonesian populations.",
    avoid_extra=", light skin, European features, wavy hair",
)

K002 = k_prompt(
    name="an adult Hoabinhian forager from Sumatra",
    era_desc="10,000-5,000 years ago, Gua Harimau, South Sumatra — Hoabinhian stone tool tradition",
    phenotype="Male, 25-30 years old, 165 cm tall, medium brown skin, deep-set dark brown eyes, moderate brow ridge, broad nose, full lips. Short black straight hair. Lean wiry build adapted to rainforest foraging. Skin marked by sun exposure and tropical environment.",
    costume="Wearing a barkcloth wrap, fiber cord necklace with river shells.",
    props="holding a large unifacial Hoabinhian pebble tool (sumatralith)",
    mood="Rainforest survivor — the Hoabinhian people of Sumatra, masters of the tropical forest, crafting distinctive pebble tools and painting their caves with red ochre hand stencils.",
)

K003 = k_prompt(
    name="an early Austronesian settler (Neolithic farmer-explorer)",
    era_desc="4,000-2,500 years ago, Kalumpang, Sulawesi Barat — Austronesian expansion",
    phenotype="Female, 20-30 years old, 158 cm tall, light brown skin, almond-shaped dark brown eyes, moderate brow ridge, moderate nose bridge, high cheekbones. Long black straight hair tied back. Compact muscular build from farming and pottery-making. Skin marked by minor sun exposure.",
    costume="Wearing a woven fiber sarong (early textile), barkcloth upper wrap, shell bead necklace, woven fiber armbands.",
    props="holding a decorated pottery vessel",
    mood="Newcomers from the north — the Austronesian expansion brought farming, pottery, and a new language family that would eventually cover half the globe from Madagascar to Easter Island.",
    avoid_extra=", dark Papuamelanesia features, light European features",
)

K004 = k_prompt(
    name="an early Neolithic cave dweller from Gunung Sewu",
    era_desc="8,000-5,000 years ago, Song Keplek, Gunung Sewu karst, East Java",
    phenotype="Male, 30-40 years old, 162 cm tall, medium brown skin, deep-set dark brown eyes, moderate brow ridge, broad nose, prognathic face. Short black wavy hair, light beard. Lean build from cave-dwelling forager lifestyle. Distinguished from Papuamelanesia by mixed features — possible early admixture. Skin marked by cave soot and sun exposure.",
    costume="Wearing a barkcloth wrap and a necklace of drilled shell beads.",
    props="holding a bone awl tool",
    mood="Cave to village — the people of Gunung Sewu karst transitioning from mobile cave-dwelling foragers to settled communities. A bridge between the hunter-gatherer past and the Neolithic future.",
)

K005 = k_prompt(
    name="an early metal-age metalworker from Bali",
    era_desc="2,500-1,500 years ago, Gilimanuk/Sembiran, Bali — early metal age transition",
    phenotype="Male, 30-40 years old, 165 cm tall, light brown skin, dark brown eyes, moderate nose bridge, high cheekbones. Short black hair, trimmed beard. Stocky build from metalworking. Skin marked by heat exposure from forge work.",
    costume="Wearing a woven sarong with simple geometric patterns, fiber belt, copper arm ring.",
    props="holding a bronze axe casting mold",
    mood="Dawn of metal — the first metalworkers in Nusantara, bringing bronze and iron technology that would transform society from the Neolithic into the early historical period.",
    avoid_extra=", dark Papuamelanesia features, European features",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Karst Maros-Pangkep (cave art landscape)",
    era_desc="40,000+ years ago to present, Sulawesi Selatan — UNESCO World Heritage",
    scene_desc="Wide view of the towering karst limestone towers of Maros-Pangkep rising from flat rice paddies. Sheer cliff faces with visible cave entrances at various heights. Tropical vegetation clinging to karst surfaces. The karst contains the oldest known cave hand stencils and figurative animal paintings (≥44 ka for hand stencils, ≥40 ka for animal art). Distant mountains. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera right (key light, raking across karst towers revealing texture), cool 6500K sky fill. High contrast 4:1.",
    mood_desc="Gallery of human origins — the Maros-Pangkep karst, where humans created some of the oldest art in the world, tens of thousands of years before Lascaux.",
)

L002 = l_prompt(
    name="Sangkulirang-Mangkalihat karst (prehistoric art complex)",
    era_desc="40,000+ years ago, Kalimantan Timur — largest cave art complex in Indonesia",
    scene_desc="Wide view of the massive Sangkulirang-Mangkalihat limestone massif rising from dense tropical rainforest. Kilometers of cliff faces with hundreds of cave art sites. Three phases of art visible: red ochre hand stencils, purple hand stencils, and charcoal drawings. Distant rainforest canopy. No people.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, raking across limestone cliff), cool 6500K sky fill. High contrast 4:1. Mist in rainforest.",
    mood_desc="Borneo's prehistoric gallery — the Sangkulirang karst preserves over 40,000 years of continuous artistic tradition, from the oldest hand stencils to late charcoal drawings.",
)

L003 = l_prompt(
    name="Gunung Sewu karst (cave dwelling landscape)",
    era_desc="8,000-3,000 years ago, East Java — cave dwelling to early settlement",
    scene_desc="Wide view of the Gunung Sewu karst landscape — hundreds of conical limestone hills spread across the horizon. Cave entrances visible at various levels on hill slopes. Dry tropical vegetation on karst surface. Small valley with patches of early garden cultivation between hills. The landscape where Song Keplek, Song Terus, and other caves preserve the transition from cave-dwelling to village life. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, revealing karst formations), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="From caves to villages — the Gunung Sewu karst, where the last cave-dwellers gradually settled down, began farming, and built the first permanent communities.",
)

L004 = l_prompt(
    name="Bukit Kerang (shell midden coast, Sumatra Timur)",
    era_desc="8,000-3,000 years ago, Sumatra Timur coast — coastal shell midden sites",
    scene_desc="Wide view of a tropical coastal landscape with large shell mounds (middens) along the shoreline. Middens composed of thousands of discarded shells (mollusks, oysters) accumulated over generations of coastal foraging. Mangrove forest along coast, open grassland behind middens. Small river estuary. The coast where Hoabinhian foragers exploited marine resources intensively. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on shell mounds and mangrove), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="Coastal abundance — the shell midden sites of Sumatra, where generations of foragers built their livelihood on the rich marine resources of the Sunda Shelf coast.",
)

L005 = l_prompt(
    name="Gua Harimau (tiger cave, OKU Sumatra Selatan)",
    era_desc="10,000-2,000 years ago, Ogan Komering Ulu, Sumatra Selatan — Hoabinhian cave art",
    scene_desc="Wide view of Gua Harimau — a large cave entrance in a limestone hill in the tropical rainforest of South Sumatra. Cave mouth is wide and dark, with tropical vegetation framing the entrance. Inside: Hoabinhian stone tool layers, red ochre cave paintings (hand stencils and animal figures). The cave served as habitation for Hoabinhian foragers for thousands of years. Dense rainforest surrounding. No people outside cave.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, revealing cave mouth and rainforest), cool 6500K sky fill. Mid contrast 3:1. Cave interior in shadow.",
    mood_desc="Forest refuge — Gua Harimau, a cave that sheltered Hoabinhian hunter-gatherers for millennia, preserving their tools, burials, and art in its deep sediment layers.",
)

L006 = l_prompt(
    name="Kalumpang (early Neolithic village, Sulawesi Barat)",
    era_desc="4,000-2,500 years ago, Sulawesi Barat — early Austronesian settlement",
    scene_desc="Wide view of an early Neolithic village site in the Kalumpang valley, Sulawesi Barat. Open river valley with patches of early swidden gardens (taro, yam). Raised wooden house platforms on stilts near river. Pottery fragments visible in garden soil. Stone adze working area. The site represents the earliest Austronesian farming settlements in central Indonesia. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on valley and gardens), cool 6500K sky fill. Mid contrast 3:1. Morning mist in valley.",
    mood_desc="First farmers — Kalumpang, where Austronesian settlers established one of the earliest farming villages in Sulawesi, bringing pottery, agriculture, and a new way of life to the region.",
)

L007 = l_prompt(
    name="Pulau Kampai (early metal age coastal site, Sumatra)",
    era_desc="2,500-1,500 years ago, Sumatra Timur coast — early metal age port",
    scene_desc="Wide view of a tropical coastal settlement at Pulau Kampai. Raised wooden houses on stilts along the shoreline. Simple wooden jetty with small outrigger canoes. Open area with evidence of metalworking (clay crucibles, bronze fragments). Coconut palms and banana plants around settlement. The coast where early metal-age traders and fishermen established a small port community. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on coastal village and palms), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="Edge of the historical era — the early metal-age coastal settlements like Pulau Kampai represent the final stage of prehistory, just before the first written records and Hindu-Buddhist kingdoms emerge.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Hoabinhian sumatralith (pebble tool)",
    era_desc="10,000-5,000 years ago, Gua Harimau, Sumatra Selatan",
    scene_desc="3-5 unifacial pebble tools (sumatraliths) on dark cave sediment surface. Large river cobbles (8-15 cm) flaked on one side only to create a working edge. Distinctive Hoabinhian tradition: thick, robust, versatile tools used for chopping, scraping, and cutting. Varied stone types: andesite, limestone, quartzite. Some show heavy use-wear and polished edges from prolonged use.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing flake scars and cobble texture), low ambient fill. High contrast 5:1.",
    mood_desc="The versatile tool — the Hoabinhian sumatralith, a single tool type that served multiple purposes. A testament to adaptability: one tool, many uses, in the diverse environments of Southeast Asian rainforests.",
)

A002 = a_prompt(
    name="Red ochre hand stencil (cave painting)",
    era_desc="40,000+ years ago, Maros-Pangkep, Sulawesi Selatan",
    scene_desc="Close-up of a red ochre hand stencil on rough limestone cave wall. Hand placed flat against wall, ochre pigment blown around it leaving negative impression. Faded and mineral-coated with age. Multiple hand stencils visible in layers — different sizes (adults and children). The oldest known hand stencils in the world at ≥44,000 years. Cave wall texture rough, with natural cracks and calcite deposits.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing paint texture and cave wall topography), low ambient fill. High contrast 4:1.",
    mood_desc="I was here — the hand stencil is humanity's oldest signature. A person placed their hand on this rock 44,000 years ago and left their mark. The beginning of identity, of self-awareness, of saying 'I exist'.",
)

A003 = a_prompt(
    name="Early Neolithic red-slipped pottery (Kalumpang style)",
    era_desc="4,000-2,500 years ago, Kalumpang, Sulawesi Barat",
    scene_desc="3-5 pottery sherds and one reconstructed vessel on dark surface. Red-slipped surface (distinctive Austronesian pottery tradition). Simple globular pot with everted rim, 15 cm tall. Decorated with incised geometric patterns (triangles, parallel lines). Burnished surface. The pottery tradition that marks the Austronesian expansion across Island Southeast Asia. Made by coiling and paddle-and-anvil technique.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing slip texture and incised decoration), low ambient fill. High contrast 5:1.",
    mood_desc="Clay and fire — the red-slipped pottery of the Austronesian expansion. Each sherd is a fingerprint of migration: from Taiwan to the Philippines to Sulawesi, these pots trace the path of the greatest maritime migration in human history.",
)


# ===== F PROMPTS — 1 fauna =====

F001 = f_prompt(
    name="wild banteng (Bos javanicus) in Holocene Jawa forest",
    era_desc="8,000 years ago, Holocene, Java — wild cattle of the forest edge",
    scene_desc="Wide cinematic wildlife shot of a small herd of 4-5 wild banteng (Bos javanicus — endangered wild cattle native to Southeast Asia). Adult male with dark brown-black coat, white stockings on legs, large curved horns, standing in forest clearing. Females and juveniles with lighter brown coats grazing behind. Background: edge of tropical forest with open grassland. The banteng would later be domesticated in the Neolithic. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on banteng coat and forest), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="Wild ancestors — the banteng, native wild cattle of Java, later domesticated as the Balinese cow. One of the key species that defined the Holocene transition from hunting to herding.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="a Hoabinhian forager band at Gua Harimau cave entrance",
    era_desc="8,000 years ago, Sumatra Selatan",
    composition="Group of 4 individuals arranged in a natural group pose. Position 1 (left): adult male, holding a sumatralith pebble tool in right hand, body turned slightly right. Position 2 (center-left): adult female, carrying a woven fiber bag with gathered forest fruits, facing forward. Position 3 (center-right): juvenile, holding a small unworked cobble, crouching slightly. Position 4 (right): older individual, sitting cross-legged, examining a stone tool. All wearing barkcloth wraps and simple fiber ornaments. Natural relaxed cave-dweller group composition.",
    mood="Forest foragers — a Hoabinhian band at their cave home, working together to process food and tools from the rainforest. Production reference for multi-character consistency.",
    k_refs=["1C-K002 (Hoabinhian forager)"],
    avoid_extra="",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 5
        "1C-K001-papuamelanesia.txt": K001,
        "1C-K002-hoabinhian-sumatra.txt": K002,
        "1C-K003-austronesian-settler.txt": K003,
        "1C-K004-song-keplek-cave-dweller.txt": K004,
        "1C-K005-metalworker-bali.txt": K005,
        # L — 7
        "1C-L001-karst-moros-pangkep.txt": L001,
        "1C-L002-sangkulirang-mangkalihat.txt": L002,
        "1C-L003-gunung-sewu-karst.txt": L003,
        "1C-L004-bukit-kerang-sumatra.txt": L004,
        "1C-L005-gua-harimau.txt": L005,
        "1C-L006-kalumpang.txt": L006,
        "1C-L007-pulau-kampai.txt": L007,
        # A — 3
        "1C-A001-sumatralith.txt": A001,
        "1C-A002-lukisan-cadas.txt": A002,
        "1C-A003-keramik-merah.txt": A003,
        # F — 1
        "1C-F001-banteng.txt": F001,
        # S — 1
        "1C-S001-kelompok-hoabinhian.txt": S001,
    }

    # Delete old v1 files
    old_files = [
        "1C-A001-lukisan-cadas.txt", "1C-A002-sumatralith.txt",
        "1C-K001-papuamelanesia.txt", "1C-K002-penghuni-gua-pawon.txt",
        "1C-K003-hoabinhian-sumatra.txt",
        "1C-L001-karst-moros-pangkep.txt", "1C-L002-sangkulirang-mangkalihat.txt",
        "1C-L003-bukit-kerang-sumatra.txt", "1C-L004-gua-pawon.txt",
        "1C-L005-leang-panningge.txt",
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
