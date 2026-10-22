#!/usr/bin/env python3
"""
Generate T2I prompts v2 untuk era 1B — Pleistosen Tengah-Akhir (700 rb – 12 rb thn lalu)
Standar v2.1: horizontal 16:9 (K, L, F, S) + 1:1 (A). S pakai K reference.
"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/1B-prasejarah-pleistosen-tengah-akhir/prompts"


def k_prompt(name, era_desc, phenotype, costume, props, mood, avoid_extra=""):
    return f"""Cinematic realistic character reference sheet of {name}, {era_desc}, shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view {props}, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. {phenotype} {costume} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all 5 angles in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters (must be same single character in all 5 angles), inconsistent costume between angles, modern clothing, jewelry, western features, Chinese features, Homo sapiens features on Homo erectus (high forehead, thin brow ridge, chin), Neanderthal features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def l_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, style_extra="", avoid_extra=""):
    return f"""Cinematic realistic documentary landscape of {name}, {era_desc}. {scene_desc} No people, no characters, no humans — empty location reference (landscape only, tiny silhouettes for scale acceptable).

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures, 35mm film grain, deep depth of field f/8-f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic{style_extra}. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: people, characters, humans, modern buildings, modern roads, modern tourism, modern researchers, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def a_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc, avoid_extra=""):
    return f"""Cinematic realistic macro photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic textures with visible mineral grains and surface details, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones, scientific documentation aesthetic. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: modern tools, metal tools, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


def f_prompt(name, era_desc, scene_desc, lighting_desc, mood_desc):
    return f"""Cinematic realistic documentary wildlife photography of {name}, {era_desc}. {scene_desc}

Lighting: {lighting_desc}

Mood: {mood_desc}

Style: photorealistic animal textures (fur, skin, feathers), 35mm film grain, deep depth of field f/5.6, 200mm telephoto lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth wildlife documentary aesthetic. Aspect ratio 16:9 horizontal cinematic. High detail, 4K, sharp focus.

Avoid: modern animals, domesticated animals, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."""


def s_prompt(name, era_desc, composition, mood, k_refs, avoid_extra=""):
    k_ref_note = " | ".join(k_refs)
    return f"""Cinematic realistic group character reference of {name}, {era_desc}, arranged in a standing group pose on a clean solid light cream studio background. {composition} Clean studio background, no environment, no historical setting, no landscape elements — neutral studio reference only.

IMPORTANT: Upload the following character reference images before generating: {k_ref_note}. Use each uploaded image as the exact face, body, and identity reference for the corresponding character in this group pose. Preserve the exact face, identity, body proportions from the reference images. This prompt only defines group composition, pose, and props — NOT physical features (which come from the reference images).

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for group character reference, no dramatic lighting.

Mood: neutral studio reference, group turnaround for production consistency. {mood}

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all characters in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: environment background, landscape, historical setting, trees, mountains, rivers, dramatic lighting, inconsistent faces with reference images, modern clothing, modern tools, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated{avoid_extra}."""


# ============================================================
# K PROMPTS — 5 karakter
# ============================================================

K001 = k_prompt(
    name="an adult Homo erectus soloensis (Manusia Solo) from Ngandong",
    era_desc="117-108 thousand years ago, Ngandong, Bengawan Solo valley, Central Java",
    phenotype="Male, 35-45 years old, 165 cm tall (taller than earlier Homo erectus), golden brown weathered skin, deep-set dark brown eyes under prominent brow ridge (less heavy than earlier Homo erectus, more evolved), slightly higher forehead than Trinil specimens, broad nose, less prognathic jaw than earlier. Long black coarse hair, light beard. Lean muscular build from active hunting. Skin marked by sun exposure and healed scars. More advanced than earlier Homo erectus — transitional toward archaic Homo sapiens. Holding a finely made stone cleaver.",
    costume="Wearing a barkcloth wrap around waist (primitive garment).",
    props="holding a stone cleaver",
    mood="Late Pleistocene hunter — the last surviving Homo erectus lineage in Java, evolved over a million years. Ancient wisdom of a species at the edge of transition.",
    avoid_extra=", fully modern Homo sapiens features",
)

K002 = k_prompt(
    name="an adult Homo floresiensis (Manusia Hobbit Flores)",
    era_desc="100-50 thousand years ago, Liang Bua, Flores, NTT",
    phenotype="Female (based on LB1), 30 years old, 106 cm tall (very short — island dwarfism), golden brown skin, small face with prominent brow ridge (archaic Homo erectus-like), low forehead, broad flat nose, full lips, prognathic face. Long black coarse hair tangled. Very small body build — proportionally short legs, long arms relative to body. Small braincase (400 cc) but organized like modern human brain. Lean but sturdy frame adapted to island environment. Wearing a barkcloth wrap. Holding a small stone flake tool.",
    costume="",
    props="holding a small stone flake tool",
    mood="Island dwarf — the remarkable Hobbit of Flores, a small-brained but intelligent human species that survived in isolation on a small island for tens of thousands of years.",
    avoid_extra=", tall stature, modern human proportions, large braincase, Homo sapiens features",
)

K003 = k_prompt(
    name="an adult Homo wajakensis (Manusia Wajak)",
    era_desc="Late Pleistocene ± 37-28 thousand years ago, Wajak, East Java — early Homo sapiens in Nusantara",
    phenotype="Male, 25-35 years old, 170 cm tall (tall for the period), golden brown skin, deep-set dark brown eyes under moderate brow ridge (much less than Homo erectus), relatively high forehead (approaching modern), moderate nose bridge, less prognathic jaw than Homo erectus. Long black wavy hair (not coarse), light beard trimmed. Lean muscular build. Transitional features — archaic Homo sapiens with some robust traits. Skin marked by sun exposure. Holding a finely crafted bone tool.",
    costume="Wearing a barkcloth wrap and simple fiber necklace with shell beads.",
    props="holding a crafted bone tool",
    mood="Early modern human in Java — the Wajak specimen represents the arrival of Homo sapiens in Nusantara, bridging the gap between archaic and modern humans.",
    avoid_extra=", fully modern European features, very dark African features, Homo erectus features (heavy brow ridge, very low forehead)",
)

K004 = k_prompt(
    name="an early Homo sapiens (MMAA Lida Ajer)",
    era_desc="63-73 thousand years ago, Lida Ajer, Sumatra Barat — oldest modern human in Indonesia",
    phenotype="Male, 25-30 years old, 168 cm tall, medium brown skin, deep-set dark brown eyes under light brow ridge, high rounded forehead, moderate nose bridge, flat face (not prognathic), full lips. Short black wavy hair, trimmed beard. Lean athletic build adapted to tropical rainforest. Wearing a barkcloth wrap. Holding a simple wooden digging stick.",
    costume="",
    props="holding a wooden digging stick",
    mood="First modern humans in Sumatra — the Lida Ajer specimen pushes back the arrival of Homo sapiens in Nusantara to at least 63,000 years ago, during the period of global migration from Africa.",
)

K005 = k_prompt(
    name="a Late Pleistocene Homo sapiens hunter from Song Terus cave",
    era_desc="80-60 thousand years ago, Gunung Sewu karst, East Java",
    phenotype="Male, 20-30 years old, 165 cm tall, medium brown skin, deep-set dark brown eyes, moderate brow ridge, high forehead, prominent cheekbones, broad nose. Short black hair, stubble beard. Lean wiry build from cave-dwelling hunter-gatherer lifestyle. Wearing a barkcloth wrap and a simple fiber cord necklace with animal teeth. Holding a finely crafted stone spear point mounted on a wooden shaft.",
    costume="",
    props="holding a stone-tipped spear",
    mood="Cave hunter of the Gunung Sewu karst — a transitional figure between the world of Homo erectus and the emerging dominance of Homo sapiens in Java.",
)


# ============================================================
# L PROMPTS — 7 latar
# ============================================================

L001 = l_prompt(
    name="Toba supervolcano eruption aftermath",
    era_desc="74 thousand years ago, Sumatra Utara — Young Toba Tuff (YTT) eruption",
    scene_desc="Wide cinematic view of the Toba caldera after the supervolcano eruption. Massive volcanic crater (100 km long) with ash-filled landscape stretching to horizon. Barren volcanic landscape covered in grey ash, no vegetation. Distant volcanic peaks partially collapsed. The eruption was the largest volcanic event of the Quaternary — VEI 8, 2,800 km³ of magma. A few tiny Homo sapiens silhouettes in far distance, struggling in the volcanic winter aftermath.",
    lighting_desc="harsh cold 7500K overcast volcanic sky (ash clouds blocking sun), dim diffuse light from above. Low contrast 2:1. Fine ash particles in air, glowing lava in distant crater rim.",
    mood_desc="Cataclysm — the largest volcanic eruption of the human era. Toba reshaped the landscape of Sumatra and may have caused a global population bottleneck. Survival at the edge of extinction.",
)

L002 = l_prompt(
    name="Liang Bua cave (Hobbit cave)",
    era_desc="100-50 thousand years ago, Flores, NTT — home of Homo floresiensis",
    scene_desc="Wide view of the Liang Bua cave entrance — a large limestone cave in a river valley on Flores. Cave mouth is wide and low, overhung with tropical vegetation. Inside: sediment layers visible in the cave walls (excavation layers). Outside: tropical forest, small river flowing past cave. The cave where Homo floresiensis (LB1) was discovered in 2003, dated 100-50 ka. No people.",
    lighting_desc="warm 4000K afternoon sun from camera left (key light, revealing cave mouth texture and surrounding vegetation), cool 6500K sky fill from above. Mid contrast 3:1. Mist in cave entrance.",
    mood_desc="Island refuge — the cave where a tiny human species survived in isolation, hunting dwarf Stegodon and crafting tools on a remote island for 50,000 years.",
)

L003 = l_prompt(
    name="Karst Payakumbuh (Lida Ajer site)",
    era_desc="63-73 thousand years ago, Sumatra Barat — oldest modern human site in Indonesia",
    scene_desc="Wide view of the karst limestone landscape near Payakumbuh, Sumatra Barat. Towering karst formations with cave entrances at base. Dense tropical rainforest covering karst hills. Small river emerging from a cave (Lida Ajer). The site where the oldest Homo sapiens teeth in Indonesia were found, pushing human arrival to 63-73 ka. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, revealing karst texture and forest), cool 6500K sky fill. Mid contrast 3:1. Morning mist in valley.",
    mood_desc="Gateway to Nusantara — the karst landscape where the first modern humans left their marks in Sumatra, arriving via the Sunda Shelf during the Late Pleistocene.",
)

L004 = l_prompt(
    name="Bengawan Solo valley (Late Pleistocene)",
    era_desc="117-40 thousand years ago, Ngandong, Central Java — Homo soloensis site",
    scene_desc="Wide view of the ancient Bengawan Solo river valley in Late Pleistocene. Wide meandering river cutting through terraced fluvial deposits. Gallery forest along banks, open woodland beyond. Herd of Stegodon and other Late Pleistocene fauna drinking at river. Distant volcanic mountains. The river that yielded Homo soloensis fossils at Ngandong (1922-present). No modern elements.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden amber on river and terraces), cool 6500K sky fill. Mid contrast 3:1. River mist.",
    mood_desc="End of an era — the Bengawan Solo valley where the last Homo erectus lineage evolved into the more advanced Homo soloensis before finally being replaced by Homo sapiens.",
)

L005 = l_prompt(
    name="Karst Campurdarat (Gunung Sewu)",
    era_desc="80-12 thousand years ago, East Java — cave-dwelling landscape",
    scene_desc="Wide view of the Gunung Sewu karst landscape at Campurdarat, East Java. Hundreds of karst hills and conical limestone mounds. Cave entrances visible at various levels. Dry tropical vegetation on karst surfaces. The landscape where Song Terus, Gua Pawon, and other cave sites preserve evidence of human habitation from 80 ka to Holocene. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, revealing karst formations), cool 6500K sky fill. Mid contrast 3:1. Heat haze over landscape.",
    mood_desc="Cave country — the Gunung Sewu karst, a vast landscape of hundreds of caves that sheltered humans through the Late Pleistocene and into the Holocene.",
)

L006 = l_prompt(
    name="Sangkulirang-Mangkalihat karst (ancient cave art site)",
    era_desc="40+ thousand years ago, Kalimantan Timur — oldest figurative cave art",
    scene_desc="Wide view of the Sangkulirang-Mangkalihat karst formation in East Kalimantan. Massive limestone cliffs rising from dense tropical rainforest. Cave entrances high on cliff faces. Inside caves: ancient red ochre paintings of animals (wild cattle, deer) — the oldest known figurative cave art in the world at ≥40 ka, predating European cave art. No people outside cave.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, raking across limestone cliff face), cool 6500K sky fill from above. High contrast 4:1. Mist in rainforest canopy.",
    mood_desc="First art — the caves of Sangkulirang where humans created the world's oldest known figurative paintings, marking the dawn of symbolic thought and artistic expression in Southeast Asia.",
)

L007 = l_prompt(
    name="Paparan Sunda (Late Pleistocene transition)",
    era_desc="25-12 thousand years ago, Last Glacial Maximum — sea level -120m",
    scene_desc="Wide aerial view of the exposed Sunda Shelf during the Last Glacial Maximum. Vast savanna plain connecting Sumatra, Java, Kalimantan with mainland Asia. Wide river systems meandering to the exposed South China Sea coast (sea level -120m). Herd of Late Pleistocene megafauna (Stegodon, banteng, deer) visible as small dots. Distant mountains: Sumatra Barisan, Java volcanic arc. The land bridge that enabled the final human migrations before Holocene sea level rise flooded the shelf. No people.",
    lighting_desc="cold 5500K overcast sky (glacial period climate), dim diffuse light. Low contrast 2:1. Wind-blown dust across the savanna.",
    mood_desc="The last land bridge — during the Last Glacial Maximum, the Sunda Shelf was dry land for the last time. Humans and animals migrated freely between islands and mainland. When the ice melted, the sea rose and separated the islands forever.",
)


# ============================================================
# A PROMPTS — 3 artefak
# ============================================================

A001 = a_prompt(
    name="Homo soloensis stone tools (Ngandong lithik)",
    era_desc="117-40 thousand years ago, Ngandong, Bengawan Solo, Central Java",
    scene_desc="3-5 stone tools visible: finely crafted chopper (gray volcanic stone), large cutting tool (cleaver), retouched flake (reddish-brown chert). Visible bifacial flaking, sharp working edges. More refined than earlier Homo erectus tools. Each tool 8-15 cm long. Made by Homo soloensis — the most advanced Homo erectus technology in Java.",
    lighting_desc="warm 3000K raking side light from camera right (key light, revealing flake scars and edge profiles), low ambient fill. High contrast 5:1.",
    mood_desc="Evolved technology — the stone tools of the last Homo erectus, showing cognitive advancement and refined technique after a million years of development in Java.",
)

A002 = a_prompt(
    name="Homo floresiensis stone tools (Liang Bua)",
    era_desc="100-50 thousand years ago, Liang Bua, Flores, NTT",
    scene_desc="5-7 small stone flake tools arranged on dark cave sediment surface. Very small tools (3-6 cm) — scaled to the body size of Homo floresiensis. Simple but effective: sharp-edged flakes for cutting meat, scraping hide, processing plants. Some show evidence of use-wear. Made by a small-brained but capable human species. A few small Stegodon bone fragments visible nearby (hunted dwarf elephant).",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing tiny flake scars), low ambient fill. High contrast 5:1.",
    mood_desc="Small tools, big intelligence — despite a brain only 400 cc (chimpanzee-sized), Homo floresiensis crafted tools sophisticated enough to hunt Stegodon. Intelligence is not just about brain size.",
)

A003 = a_prompt(
    name="Ancient red ochre cave painting (Sangkulirang style)",
    era_desc="40+ thousand years ago, Sangkulirang-Mangkalihat, Kalimantan Timur",
    scene_desc="Close-up of a cave wall painting: red ochre figure of a wild cattle (banteng) drawn with bold strokes. The painting is faded in places, with mineral deposits and calcite layers partially covering it. Rough limestone cave wall surface with natural cracks. The painting dates to ≥40 ka — the oldest known figurative cave art in the world. Approximately 50 cm wide.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing paint texture and cave wall topography), low ambient fill. High contrast 4:1.",
    mood_desc="The birth of art — this is not just paint on rock. It is the first evidence of symbolic thought, of a mind that could represent the world. The dawn of what makes us human.",
)


# ============================================================
# F PROMPTS — 1 fauna
# ============================================================

F001 = f_prompt(
    name="dwarf Stegodon herd on Flores island",
    era_desc="100-50 thousand years ago, Flores, NTT — island dwarf megafauna",
    scene_desc="Wide cinematic wildlife shot of a herd of 5-7 dwarf Stegodon (extinct elephant reduced to 1.5-2 meters tall at shoulder due to island dwarfism). Adults and juveniles grazing in a tropical forest clearing near Liang Bua cave. One adult male with short curved tusks (1m) in foreground. Smaller than mainland Stegodon — adapted to island limited resources. Background: tropical forest, limestone karst hills. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, golden on elephant skin and forest), cool 6500K sky fill. Mid contrast 3:1. Forest mist.",
    mood_desc="Island giants shrunk — the dwarf Stegodon of Flores evolved from large mainland ancestors, shrinking over thousands of years of island isolation. They were the primary prey of the even smaller Homo floresiensis.",
)


# ============================================================
# S PROMPTS — 1 scene kelompok
# ============================================================

S001 = s_prompt(
    name="a small band of Homo floresiensis at Liang Bua cave entrance",
    era_desc="80 thousand years ago, Flores, NTT",
    composition="Group of 4 individuals arranged in a natural group pose. Position 1 (left): adult male, holding a stone flake tool in right hand, body turned slightly right. Position 2 (center-left): adult female, carrying a woven fiber bag with gathered fruits, facing forward. Position 3 (center-right): juvenile, holding a small stone cobble, crouching slightly. Position 4 (right): older individual, sitting on a stone, examining a stone tool. All wearing barkcloth wraps. Small body proportions (short stature, long arms relative to body). Natural relaxed cave-dweller group composition.",
    mood="Island life — the small community of Hobbit people, working together to survive in their island forest home. Production reference for multi-character consistency using K individual references.",
    k_refs=["1B-K002 (adult Homo floresiensis)"],
    avoid_extra=", tall stature, modern human proportions",
)


# ============================================================
# MAIN
# ============================================================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 5 karakter
        "1B-K001-homo-erectus-soloensis.txt": K001,
        "1B-K002-homo-floresiensis.txt": K002,
        "1B-K003-manusia-wajak.txt": K003,
        "1B-K004-mmaa-lida-ajer.txt": K004,
        "1B-K005-song-terus-hunter.txt": K005,
        # L — 7 latar
        "1B-L001-toba-supervolcano.txt": L001,
        "1B-L002-liang-bua.txt": L002,
        "1B-L003-karst-payakumbuh.txt": L003,
        "1B-L004-bengawan-solo-akhir.txt": L004,
        "1B-L005-karst-campurdarat.txt": L005,
        "1B-L006-sangkulirang-cave-art.txt": L006,
        "1B-L007-paparan-sunda-lgm.txt": L007,
        # A — 3 artefak
        "1B-A001-alat-batu-soloensis.txt": A001,
        "1B-A002-alat-batu-floresiensis.txt": A002,
        "1B-A003-lukisan-gua-sangkulirang.txt": A003,
        # F — 1 fauna
        "1B-F001-dwarf-stegodon.txt": F001,
        # S — 1 kelompok
        "1B-S001-kelompok-hobbit.txt": S001,
    }

    # Delete old v1 files
    old_files = [
        "1B-F001-homo-erectus-stegodon-berburu.txt",
        "1B-K001-homo-erectus-soloensis.txt",
        "1B-K002-homo-floresiensis.txt",
        "1B-K003-manusia-wajak.txt",
        "1B-K004-mmaa-lida-ajer.txt",
        "1B-L001-toba-supervolcano.txt",
        "1B-L002-liang-bua.txt",
        "1B-L003-karst-payakumbuh.txt",
        "1B-L004-bengawan-solo-akhir.txt",
        "1B-L005-karst-campurdarat.txt",
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

    print(f"\n✅ Total: {len(prompts)} files generated (v2.1)")
    print(f"   K (karakter single): 5 files — 16:9")
    print(f"   L (latar): 7 files — 16:9")
    print(f"   A (artefak): 3 files — 1:1")
    print(f"   F (fauna): 1 file — 16:9")
    print(f"   S (kelompok): 1 file — 16:9")


if __name__ == "__main__":
    main()
