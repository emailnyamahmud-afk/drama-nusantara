#!/usr/bin/env python3
"""
Generate T2I prompts v2 untuk era 1A — Pleistosen Awal (1,8 jt – 700 rb thn lalu)
Standar v2: aspect ratio horizontal (16:9) untuk K dan L, 1:1 untuk A.

Cara pakai:
  python /home/z/my-project/scripts/generate_1A_t2i_v2.py

Output: file .txt di /home/z/my-project/produksi/t2i-prompts/1A-prasejarah-pleistosen-awal/prompts/
"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/t2i-prompts/1A-prasejarah-pleistosen-awal/prompts"

# ============================================================
# TEMPLATE HELPERS
# ============================================================

def k_prompt(name, era_desc, phenotype, costume, props, mood, avoid_extra=""):
    """Template untuk K (karakter ref sheet 5-angle SINGLE INDIVIDU, 16:9 horizontal)"""
    return f"""Cinematic realistic character reference sheet of {name}, {era_desc}, shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view {props}, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. {phenotype} {costume} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all 5 angles in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters (must be same single character in all 5 angles), inconsistent costume between angles, modern clothing, jewelry, western features, Chinese features, Homo sapiens features (high forehead, thin brow ridge, chin), Neanderthal features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def l_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, style_extra="", avoid_extra=""):
    """Template untuk L (latar/lokasi cinematic, 16:9 horizontal)"""
    return f"""Cinematic realistic documentary landscape of {name}, {era_desc}. {scene_desc} No people, no characters, no humans — empty location reference (landscape only, tiny silhouettes for scale acceptable).

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures, 35mm film grain, deep depth of field f/8-f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic{style_extra}. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: people, characters, humans, modern buildings, modern roads, modern tourism, modern researchers, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def a_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, avoid_extra=""):
    """Template untuk A (artefak macro detail, 1:1 square)"""
    return f"""Cinematic realistic macro photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures with visible mineral grains and surface details, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones, scientific documentation aesthetic. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: modern tools, metal tools, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def f_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc):
    """Template untuk F (fauna, 16:9 horizontal)"""
    return f"""Cinematic realistic documentary wildlife photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic animal textures (fur, skin, feathers), 35mm film grain, deep depth of field f/5.6, 200mm telephoto lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth wildlife documentary aesthetic. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: modern animals, domesticated animals, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."""


def s_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, avoid_extra=""):
    """Template untuk S (scene multi-karakter cinematic, 16:9 horizontal) — 1 angle, multi-karakter dalam setting"""
    return f"""Cinematic realistic documentary scene of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic skin and environment textures, 35mm film grain, deep depth of field f/5.6, 35mm lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: modern clothing, modern buildings, modern tools, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


# ============================================================
# K PROMPTS — Karakter ref sheet (4 files)
# ============================================================

K001 = k_prompt(
    name="an adult Homo erectus from Pleistocene Awal Jawa",
    era_desc="1.8-1.2 million years ago, East Java",
    phenotype="Male, 30-40 years old, 155 cm tall, golden brown weathered skin, deep-set dark brown eyes under heavy supraorbital brow ridge (thick bone above eyes), low sloping forehead, broad flat nose, full lips, prognathic jaw. Long black coarse hair tangled, no beard grooming. Naked torso (no clothing — Pleistocene Awal), skin marked by natural sun exposure, healed scar on left shoulder.",
    costume="",
    props="holding a chert flake tool",
    mood="Primitive survival, ancient wisdom, first human presence in Nusantara.",
)

K002 = k_prompt(
    name="a juvenile Homo erectus (Anak Mojokerto / Mojokerto child)",
    era_desc="1.8 million years ago, Perning, East Java",
    phenotype="Child, 6-9 years old, 110 cm tall, golden brown skin, developing brow ridge, low forehead, broad flat nose, prognathic face. Short black coarse hair. Lean body with visible ribs, skin marked by natural sun exposure. Curious alert expression. Small body proportions typical of Homo erectus juvenile.",
    costume="Wearing a minimal barkcloth loincloth (simple primitive covering made from tree bark fiber — survival garment of early humans).",
    props="holding a small stone cobble",
    mood="Young explorer, the next generation of early humans in Nusantara — curiosity and resilience in a vast ancient landscape.",
)

K003 = k_prompt(
    name="an adult female Homo erectus from Pleistocene Awal Jawa",
    era_desc="1.5 million years ago, East Java",
    phenotype="Female, 25-35 years old, 145 cm tall, golden brown weathered skin, deep-set dark brown eyes under prominent brow ridge (slightly less heavy than male), low sloping forehead, broad flat nose, full lips, prognathic jaw. Long black coarse hair tied back with vine. Lean muscular build from foraging and gathering. Skin marked by sun exposure and healed scars. Wearing a barkcloth wrap around waist (primitive garment from tree bark fiber). Carrying a woven fiber bag with gathered tubers and fruits. Nursing infant visible at hip.",
    costume="",
    props="holding gathered plant food in fiber bag",
    mood="Gatherer and mother — the backbone of early human survival, combining foraging knowledge with childcare in a challenging Pleistocene landscape.",
)

K004 = k_prompt(
    name="an adult Homo soloensis (Ngandong) from Pleistosen Akhir Jawa",
    era_desc="550-143 thousand years ago, Ngandong, Bengawan Solo valley, East Java",
    phenotype="Male, 35-45 years old, 165 cm tall (taller than earlier Homo erectus), golden brown weathered skin, deep-set dark brown eyes under prominent brow ridge (less heavy than earlier Homo erectus), slightly higher forehead than Trinil, broad nose, less prognathic jaw than earlier specimens. Long black coarse hair, light beard. Naked torso, skin marked by sun exposure and healed scars. More advanced than earlier Homo erectus — transitional toward archaic Homo sapiens. Holding a finely made stone cleaver.",
    costume="",
    props="holding a stone cleaver",
    mood="Late Pleistocene hunter — the last surviving Homo erectus lineage in Java, evolved and adapted over a million years. Ancient wisdom of a species that endured.",
    avoid_extra=", fully modern Homo sapiens features, Neanderthal features",
)


# ============================================================
# L PROMPTS — Latar/lokasi (7 files)
# ============================================================

L001 = l_prompt(
    name="Paparan Sunda (exposed Sunda Shelf)",
    era_desc="1.8 million years ago, Pleistocene Awal, East Java",
    scene_desc="Extreme wide aerial view showing vast exposed continental shelf connecting Sumatra, Java, Kalimantan with mainland Asia. Wide river systems (Proto-Kapuas, Proto-Lupar, Lembah Anambas) meandering across the plain toward distant South China Sea (sea level -120m below today). Tropical savanna with grassland dominant, scattered acacia and gallery forest along rivers. Herd of Stegodon and other Pleistocene fauna visible as small dots in distance. Mountains on horizon: Sumatra Barisan range, Java volcanic arc. No main character in foreground.",
    lighting_desc="warm 3500K golden sunrise from camera left (key light, long shadows, warm amber on savanna grass), cool 6500K sky fill from above. Aerial drone perspective from 500m altitude. Mist rising from river systems.",
    mood_desc="Epic geological scale, the birth of a continent — vast ancient landscape, primal and untouched. The Sunda Shelf exposed as dry land, connecting islands to mainland Asia, enabling the first human migration into Nusantara.",
)

L002 = l_prompt(
    name="Kubah Sangiran (Sangiran Dome)",
    era_desc="1.8-0.7 million years ago, Central Java — UNESCO World Heritage Site",
    scene_desc="Wide aerial view of the Sangiran Dome geological formation, exposing 2-million-year stratigraphy of the Solo Zone (Kubah Sangiran). Visible layers: volcanic tuff (Grenzbank zone), blue clay, black clay (Pucangan), white cross-bedded sandstone (Kabuh), and upper Notopuro volcanic deposits. The Cengklik river cuts through the dome, exposing fossil-bearing layers. Tiny silhouettes of archaeological excavation pits visible at base. Distant volcanic mountains (Lawu, Merapi) on horizon. No modern buildings visible.",
    lighting_desc="warm 4000K morning sun from camera right (key light, raking across stratigraphic layers revealing colors and textures), cool 6500K sky fill from above. Mid contrast 3:1. Morning mist in valley.",
    mood_desc="Sacred ground of paleoanthropology — the richest Homo erectus fossil site in the world. Where Dubois, von Koenigswald, and Indonesian archaeologists uncovered the deep past of human ancestry in Java.",
)

L003 = l_prompt(
    name="Lembah Bengawan Solo (Solo River Valley)",
    era_desc="1.8 million years ago to present, East Java — Trinil, Ngandong, Kedungbrubus",
    scene_desc="Wide cinematic view of the ancient Bengawan Solo river valley in Pleistocene Awal. Wide meandering river cutting through volcanic terrain, with steep banks exposing fossil-bearing layers. Tropical gallery forest along riverbanks, open savanna beyond. Herd of Stegodon drinking at river. Distant volcanic mountains (Lawu, Wilis). The river that would later yield the first Homo erectus fossils (Trinil 1891, Ngandong 1931-1933). No modern elements.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden amber on river and forest), cool 6500K sky fill from above right. Mid contrast 3:1. River mist, dust haze.",
    mood_desc="Timeless river of human origins — the Bengawan Solo that has carried the story of human evolution in Java for over a million years, from Homo erectus to the present day.",
)

L004 = l_prompt(
    name="Bumiayu (Pleistocene fauna site)",
    era_desc="700 thousand years ago, Central Java — western part",
    scene_desc="Wide view of the Bumiayu paleontological site. Rolling volcanic hills with exposed fossil beds. Tropical savanna with scattered trees. Small herd of Stegodon and Hexaprotodon (extinct hippo) near a shallow lake. Distant volcanic mountains. The site that yielded important Middle Pleistocene fauna fossils. No modern elements.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on savanna and lake), cool 6500K sky fill from above. Mid contrast 3:1. Heat shimmer over savanna.",
    mood_desc="Middle Pleistocene ecosystem — the fauna world of Java 700,000 years ago, when Homo erectus shared the landscape with extinct elephants and hippos.",
)

L005 = l_prompt(
    name="Semedo (Tegal, Central Java)",
    era_desc="1.5-0.7 million years ago, Pleistocene Awal-Tengah",
    scene_desc="Wide view of the Semedo paleontological site near Tegal, Central Java. Open grassland with exposed volcanic ash layers containing fossils. Scattered acacia trees. Small lake in distance. Distant volcanic peaks. The site that yielded earliest stone tools and Stegodon fossils in Central Java north coast. No modern elements.",
    lighting_desc="warm 4000K morning sun from camera left (key light, raking across fossil beds), cool 6500K sky fill. Mid contrast 3:1. Morning dew on grass.",
    mood_desc="Ancient toolkit — where early humans left their stone tools among the bones of extinct giants, preserving evidence of habitation for over a million years.",
)

L006 = l_prompt(
    name="Patiayam (Central Java)",
    era_desc="1.0-0.5 million years ago, Pleistocene Tengah",
    scene_desc="Wide view of the Patiayam fossil site near Kudus, Central Java. Hillside with exposed fossil-bearing layers. Tropical vegetation on upper slopes. Open savanna at base. Small river cutting through the formation. Distant view of Mount Muria. The site that yielded Homo erectus fossils and Palaeolithic stone tools. No modern elements.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, revealing stratigraphy), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="Hillside of human ancestors — Patiayam, another window into the Middle Pleistocene of Java, where Homo erectus continued to evolve and adapt.",
)

L007 = l_prompt(
    name="Wallacea (biogeographical transition zone)",
    era_desc="1.8 million years ago to present, between Sunda and Sahul shelves",
    scene_desc="Wide aerial view of the Wallacea biogeographical zone — the deep-water gap between the Sunda Shelf (west) and Sahul Shelf (east). Visible: Sulawesi island chain, Flores, Timor, Maluku. Deep ocean trenches separating shallow continental shelves. Tropical islands with unique endemic fauna visible as silhouettes. The zone where Asian fauna (from west) meets Australasian fauna (from east). No modern elements.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, warm on islands and ocean), cool 6500K sky fill from above. Aerial perspective from 2000m altitude. Sea mist around islands.",
    mood_desc="The great biogeographical divide — Wallacea, where two worlds of life meet. The deep-water barrier that Homo erectus could not cross, but that Homo sapiens would later navigate to reach Sahul (Australia + New Guinea).",
)


# ============================================================
# A PROMPTS — Artefak macro (3 files)
# ============================================================

A001 = a_prompt(
    name="Pleistocene Awal chert flake tools",
    era_desc="1.6-1.2 million years ago, Dayu, Sangiran, Central Java",
    scene_desc="3-5 tools visible: chert flake with sharp edge (reddish-brown), obsidian flake (black glassy), basalt cobble tool (gray rough). Visible flaking scars, bulb of percussion, sharp cutting edges. Some tools show use-wear (silica gloss, micro-flaking). Slight patina indicating great age. Each tool 5-10 cm long. Made by Homo erectus.",
    lighting_desc="warm 3000K raking side light from camera right (key light, revealing texture and color of chert, obsidian reflections), low ambient fill. High contrast 5:1. Dust particles in light beam.",
    mood_desc="Ancient technology, the dawn of human ingenuity — tools that survived 1.6 million years, the earliest evidence of human craft in Nusantara.",
)

A002 = a_prompt(
    name="Tengkorak Trinil 2 (Trinil skull calotte)",
    era_desc="discovered 1891 by Eugéne Dubois, Trinil, Bengawan Solo, East Java — ~1.0 million years old",
    scene_desc="Skull cap (calotte) of Homo erectus on dark velvet background. Visible: thick cranial bone (10mm), low sloping forehead, prominent supraorbital torus (brow ridge), broad temporal fossae. Bone color: aged ivory with slight mineral staining (manganese dendrites). Post-mortem cracks filled with sediment. The specimen that Dubois named Pithecanthropus erectus in 1894 — the type specimen of Homo erectus. ~15 cm wide.",
    lighting_desc="warm 3200K raking light from camera left (key light, revealing bone texture and topography), cool 5500K fill from right. High contrast 4:1.",
    mood_desc="The skull that changed human history — Trinil 2, the first fossil evidence of human evolution outside Europe/Africa. The type specimen that proved Asia was a cradle of humanity.",
)

A003 = a_prompt(
    name="Stegodon fossil remains (tusk and molar)",
    era_desc="1.8-0.7 million years ago, Pleistocene Awal, Sangiran and Trinil",
    scene_desc="Stegodon tusk fragment (spiral, 1.5m length visible, ivory color with mineral staining) and large molar tooth (15 cm, ridged surface, dark brown enamel). Both on dark volcanic stone surface. The extinct elephant that was the dominant megafauna of Pleistocene Java, hunted by Homo erectus. Visible growth lines in tusk cross-section.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing ivory texture and enamel ridges), low ambient fill. High contrast 5:1.",
    mood_desc="Giants of the Pleistocene — Stegodon, the largest mammal of ancient Java, coexisted with and was hunted by Homo erectus. Their bones tell the story of a vanished ecosystem.",
)


# ============================================================
# F PROMPTS — Fauna (1 file)
# ============================================================

F001 = f_prompt(
    name="Stegodon herd in Pleistocene Jawa savanna",
    era_desc="1.5 million years ago, Pleistocene Awal, East Java — Paparan Sunda savanna",
    scene_desc="Wide cinematic wildlife shot of a herd of 8-10 Stegodon (extinct elephant with long straight tusks, larger than modern elephant, 4 meters tall at shoulder). Adults and juveniles grazing on tropical savanna grassland near a riverbank. One large male with massive tusks (3m long) in foreground. Background: open savanna with scattered acacia trees, distant volcanic mountains. Late afternoon golden light. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden amber on elephant skin and savanna grass), cool 6500K sky fill from above right. Mid contrast 3:1. Dust kicked up by herd.",
    mood_desc="Majestic giants of a lost world — Stegodon, the dominant megafauna of Pleistocene Java, sharing the landscape with the first humans. A glimpse of an ecosystem that vanished 500,000 years ago.",
)


# ============================================================
# S PROMPTS — Scene multi-karakter cinematic (1 file)
# ============================================================

S001 = s_prompt(
    name="a cooperative hunting party of Homo erectus in Pleistocene Java savanna",
    era_desc="1.5 million years ago, Pleistocene Awal, East Java — Paparan Sunda",
    scene_desc="Wide cinematic scene of a group of 5 Homo erectus individuals working together on a hunt in tropical savanna. Composition: 1 adult male (30-40, 155 cm, muscular, crouching with raised wooden spear, leading the hunt) in left foreground; 1 adult female (25-30, 145 cm, wearing barkcloth wrap, carrying infant on hip, watching from mid-right) gathering plant food; 1 juvenile (8-10, 120 cm, crouching behind adult male with small cobble) learning; 1 older male (45-50, 150 cm, standing in background holding large chopper tool, watching herd); 1 young adult male (18-22, 152 cm, flanking right with chert flake, ready to drive prey). All with Homo erectus features: heavy brow ridge, low forehead, broad nose, prognathic jaw. Black coarse hair, barkcloth wraps around waist, weathered skin. Target: a small Stegodon juvenile grazing 20 meters ahead in the savanna. Scattered acacia trees, distant volcanic mountains on horizon. Stone tools and wooden spears visible.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden amber on skin, grass, and dust), cool 6500K sky fill from above right. Mid contrast 3:1. Dust haze from movement, smoke from distant grass fire.",
    mood_desc="Cooperative survival — the social fabric of early human groups, collective hunting and tool-making. The moment before the strike, tension and teamwork across generations and genders.",
    avoid_extra=", modern human features on any individual, modern weapons, metal tools, bows and arrows (must be wooden spears and stone tools only), fully modern clothing",
)


# ============================================================
# MAIN — Write all files
# ============================================================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — Karakter ref (4 files, single individu each)
        "1A-K001-homo-erectus-dewasa.txt": K001,
        "1A-K002-anak-mojokerto.txt": K002,
        "1A-K003-homo-erectus-betina.txt": K003,  # CHANGED: was "kelompok-berburu", now single female
        "1A-K004-homo-soloensis-ngandong.txt": K004,
        # L — Latar (7 files)
        "1A-L001-paparan-sunda.txt": L001,
        "1A-L002-kubah-sangiran.txt": L002,
        "1A-L003-bengawan-solo.txt": L003,
        "1A-L004-bumiayu.txt": L004,
        "1A-L005-semedo.txt": L005,
        "1A-L006-patiayam.txt": L006,
        "1A-L007-wallacea.txt": L007,
        # A — Artefak (3 files)
        "1A-A001-alat-batu-serpih.txt": A001,
        "1A-A002-tengkorak-trinil.txt": A002,
        "1A-A003-fosil-stegodon.txt": A003,
        # F — Fauna (1 file)
        "1A-F001-stegodon-fauna.txt": F001,
        # S — Scene multi-karakter (1 file) — NEW TYPE
        "1A-S001-kelompok-berburu.txt": S001,
    }

    # Delete old files (including old K003-kelompok-berburu which is now S001)
    old_files = [
        "1A-F001-stegodon-fauna.txt",
        "1A-K001-homo-erectus-dewasa.txt",
        "1A-K002-anak-mojokerto.txt",
        "1A-K003-kelompok-berburu.txt",  # OLD — will be replaced by S001 + K003-betina
        "1A-L001-paparan-sunda.txt",
        "1A-L002-kubah-sangiran.txt",
        "1A-L003-bengawan-solo.txt",
        "1A-L004-bumiayu.txt",
        "1A-P001-alat-batu-serpih.txt",
        "1A-P002-tengkorak-trinil.txt",
    ]
    for f in old_files:
        path = os.path.join(OUTPUT_DIR, f)
        if os.path.exists(path):
            os.remove(path)
            print(f"  Deleted: {f}")

    # Write new files
    for filename, content in prompts.items():
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            f.write(content)
        print(f"  Created: {filename}")

    print(f"\n✅ Total: {len(prompts)} files generated (v2.1 horizontal + S type)")
    print(f"   K (karakter single): 4 files — 16:9 horizontal")
    print(f"   L (latar): 7 files — 16:9 horizontal")
    print(f"   A (artefak): 3 files — 1:1 square")
    print(f"   F (fauna): 1 file — 16:9 horizontal")
    print(f"   S (scene multi-karakter): 1 file — 16:9 horizontal [NEW TYPE]")


if __name__ == "__main__":
    main()
