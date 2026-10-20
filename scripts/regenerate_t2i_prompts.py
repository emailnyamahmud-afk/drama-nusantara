#!/usr/bin/env python3
"""
Generate ulang semua 42 file T2I prompt:
- Semua 9:16
- K (karakter): character reference sheet, clean background, 5 angle
- L (latar): scene historis 9:16, no main character
- A/P/F (artefak/fauna/properti): macro/detail 9:16
"""

from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts")

# ============= TEMPLATE =============

TEMPLATE_K = """Cinematic realistic character reference sheet of {name}, shown in 5 different angles arranged in a grid layout on a clean solid light cream studio background. Layout: top-left frontal face close-up, top-right full body front view, middle-left side face profile close-up, bottom-left side full body view {prop_phrase}, bottom-right back full body view. All 5 angles show the exact same character, same costume, same physical features, same identity. {details} Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency.

Style: photorealistic skin texture with visible pores and imperfections, 35mm film grain, deep depth of field f/8 (all 5 angles in focus), 50mm lens equivalent, 8K hyperdetailed, color graded neutral (no dramatic color grading), production reference aesthetic. Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters (must be same character in all 5 angles), inconsistent costume between angles, {avoid}"""

TEMPLATE_L = """Cinematic realistic documentary landscape of {name}, {period}. {scene_details} No main character in foreground (landscape only, tiny silhouettes for scale acceptable).

Lighting: {lighting}

Mood: {mood}

Style: {style} Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: {avoid}"""

TEMPLATE_A = """Cinematic realistic macro photography of {name}. {object_details}

Lighting: {lighting}

Mood: {mood}

Style: {style} Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: {avoid}"""


# ============= DATA 1A =============

PROMPTS_1A = {
    # --- KARAKTER (character reference sheet) ---
    "1A-K001-homo-erectus-dewasa.txt": ("K", {
        "name": "an adult Homo erectus from Pleistocene Awal Jawa",
        "prop_phrase": "holding a chert flake tool",
        "details": "Male, 30-40 years old, 155 cm tall, golden brown weathered skin, deep-set dark brown eyes under heavy supraorbital brow ridge (thick bone above eyes), low sloping forehead, broad flat nose, full lips, prognathic jaw. Long black coarse hair tangled, no beard grooming. Naked torso (no clothing - Pleistocene Awal), skin marked by natural sun exposure, healed scar on left shoulder.",
        "avoid": "modern clothing, jewelry, western features, Chinese features, Homo sapiens features (high forehead, thin brow ridge, chin), Neanderthal features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1A-K002-anak-mojokerto.txt": ("K", {
        "name": "a Homo erectus child from Perning Mojokerto, Pleistocene Awal Jawa",
        "prop_phrase": "holding a small stone",
        "details": "Child, age 5-7 years, golden brown smooth skin but sun-exposed, deep-set dark brown eyes under developing brow ridge, low sloping forehead, broad flat nose, full lips, prognathic jaw developing. Short black coarse hair tangled. Naked (no clothing - Pleistocene Awal), small frame, thin limbs typical of hunter-gatherer child.",
        "avoid": "modern clothing, modern child, western features, Chinese features, adult features (heavy brow ridge fully developed), anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1A-K003-kelompok-berburu.txt": ("K", {
        "name": "a Homo erectus hunter from Pleistocene Awal Jawa",
        "prop_phrase": "holding a wooden spear and chert flake tool",
        "details": "Male, 25-35 years old, 155 cm tall, golden brown weathered skin, deep-set dark brown eyes under heavy supraorbital brow ridge, low sloping forehead, broad flat nose, full lips, prognathic jaw. Long black coarse hair tangled. Naked torso (no clothing - Pleistocene Awal), carrying chert flake tools. Muscular hunter build, alert expression.",
        "avoid": "modern clothing, loincloths, jewelry, body paint, western faces, Chinese faces, Homo sapiens features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # --- LATAR ---
    "1A-L001-paparan-sunda.txt": ("L", {
        "name": "Paparan Sunda (exposed Sunda Shelf) 1.8 million years ago",
        "period": "Pleistocene Awal, East Java",
        "scene_details": "Extreme wide aerial view showing vast exposed continental shelf connecting Sumatra, Java, Kalimantan with mainland Asia. Wide river systems (Proto-Kapuas, Proto-Lupar, Lembah Anambas) meandering across the plain toward distant South China Sea (sea level -120m below today). Tropical savanna with grassland dominant, scattered acacia and gallery forest along rivers. Herd of Stegodon and other Pleistocene fauna visible as small dots in distance. Mountains on horizon: Sumatra Barisan range, Java volcanic arc.",
        "lighting": "golden hour 3500K warm sunrise from camera left (key light, long shadows, warm amber on savana grass), cool 6500K sky fill from above. Aerial drone perspective from 500m altitude. Mist rising from river systems.",
        "mood": "epic geological scale, the birth of a continent - vast ancient landscape, primal and untouched.",
        "style": "photorealistic grass, water, and rock textures, 35mm film grain, deep depth of field f/11, 16mm ultra-wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool teal shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern coastlines (current sea level), modern islands separated, ships, modern vegetation patterns, agricultural fields, roads, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1A-L002-kubah-sangiran.txt": ("L", {
        "name": "Kubah Sangiran geological dome",
        "period": "Sangiran, Central Java, Pleistocene Awal",
        "scene_details": "Exposed stratigraphic layers visible in eroded hillside. 4 distinct formations in horizontal bands: (1) Formasi Kalibeng at bottom - blue clay with marine fossils, (2) Formasi Pucangan middle-bottom - black volcanic breccia and clay, (3) Formasi Grenzbank-Kabuh middle-top - conglomerate with cross-bedded sandstone, (4) Formasi Notopuro at top - volcanic lahar breccia. Bengawan Solo paleo-river at base of dome, meandering through valley.",
        "lighting": "warm 4000K afternoon sun from camera right (key light, raking across stratigraphic layers revealing textures and colors), cool 6500K sky fill from above. Mid contrast 3:1 for geological detail. Dust haze in valley.",
        "mood": "geological time made visible, layers of earth preserving millions of years of human evolution.",
        "style": "photorealistic rock and soil textures with visible stratification, 35mm film grain, deep depth of field f/11, 24mm wide lens equivalent, 8K hyperdetailed, color graded earth tones (browns, ochres, blacks, blues), National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern excavations, modern vegetation cover hiding strata, modern roads, tourists, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, uniform rock color (must show 4 distinct stratigraphic bands)."
    }),
    "1A-L003-bengawan-solo.txt": ("L", {
        "name": "Lembah Bengawan Solo (paleo-Solo River valley)",
        "period": "Pleistocene Awal, East Java, 1.8-0.9 million years ago",
        "scene_details": "Wide muddy river meandering through open savanna landscape with gallery forest along banks. Stegodon herd (5-7 extinct elephants with downward-curving tusks) drinking at river edge, antelopes grazing on plain, deer in forest edge. Volcanic mountains on distant horizon (proto-Kelud, Kawi, Arjuno).",
        "lighting": "warm 4000K late afternoon sun from camera left low angle (key light, long shadows of animals and trees, golden amber on water surface), cool 6500K sky fill from above. High contrast 4:1. River reflecting sunlight. Mist on river.",
        "mood": "primal ecosystem, predator and prey in balance - the cradle of human evolution in Java.",
        "style": "photorealistic water, grass, and animal textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern river engineering, modern agriculture, modern livestock, modern humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern elephant species (must be Stegodon with downward-curving tusks)."
    }),
    "1A-L004-bumiayu.txt": ("L", {
        "name": "Bumiayu site",
        "period": "western Central Java, 1.8 million years ago",
        "scene_details": "Open volcanic landscape at edge of Paparan Sunda. Foreground shows scattered volcanic cobbles (chert, andesite, basalt) suitable for tool-making. Distant volcanic cones smoking faintly. Pleistocene fauna (Stegodon, deer) visible in far distance.",
        "lighting": "warm 3500K morning sun from camera right (key light, long shadows, fresh morning atmosphere), cool 6500K sky fill from above. Mid contrast 3:1.",
        "mood": "first footsteps, discovery of a new land - the earliest documented presence of Homo erectus in Java.",
        "style": "photorealistic volcanic rock and grass textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones, National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern excavations, modern vegetation, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    # --- ARTEFAK / FAUNA ---
    "1A-F001-stegodon-fauna.txt": ("A", {
        "name": "a herd of Stegodon (extinct elephant with downward-curving tusks) grazing on open savanna of Paparan Sunda",
        "object_details": "5-7 individuals, mixed herd with adults and juveniles, larger body than modern elephant. In middle distance, antelopes grazing, deer at forest edge. Volcanic mountains on horizon. Pleistocene Awal to Tengah, East Java.",
        "lighting": "warm 4000K golden hour sun from camera left low angle (key light, dramatic long shadows of Stegodon, warm amber on grass), cool 6500K sky fill from above. High contrast 4:1.",
        "mood": "prehistoric ecosystem, predator and prey - the wildlife of Pleistocene Java.",
        "style": "photorealistic animal fur and skin textures (wrinkled elephant hide), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern elephant species (must be Stegodon with downward-curving tusks), modern African savanna, modern cattle, modern humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern buildings, modern vehicles."
    }),
    "1A-P001-alat-batu-serpih.txt": ("A", {
        "name": "Pleistocene Awal chert flake tools arranged on dark volcanic stone surface",
        "object_details": "3-5 tools visible: chert flake with sharp edge (reddish-brown), obsidian flake (black glassy), basalt cobble tool (gray rough). Visible flaking scars, bulb of percussion, sharp cutting edges. Some tools show use-wear (silica gloss, micro-flaking). Slight patina indicating great age. Each tool 5-10 cm long. Made by Homo erectus, 1.6-1.2 Ma, Dayu Sangiran.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing texture and color of chert, obsidian reflections), low ambient fill. High contrast 5:1. Dust particles in light beam.",
        "mood": "ancient technology, the dawn of human ingenuity - tools that survived 1.6 million years.",
        "style": "photorealistic rock textures with visible mineral grains and flake scars, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones, scientific documentation aesthetic.",
        "avoid": "modern tools, metal tools, polished modern stone tools, ceramic, plastic, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern scale rulers visible."
    }),
    "1A-P002-tengkorak-trinil.txt": ("A", {
        "name": "Homo erectus skull cap (calotte, Trinil 2 specimen replica) on dark velvet background",
        "object_details": "Three-quarter view showing distinctive features: dolichocephalic (long) skull shape, prominent sagittal keel (ridge along top of skull), thick supraorbital torus (heavy brow ridge), low sloping forehead, thick cranial bones. Aged bone with brown/yellow patina. Visible cranial sutures. Brain volume 700-900 cc. ~18 cm long. Holotype of Pithecanthropus erectus (Dubois 1894), Trinil Ngawi East Java 1891-1892.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing skull topography, sutures, bone texture), low ambient fill. High contrast 5:1. Subtle rim light on brow ridge.",
        "mood": "scientific legacy, the discovery that changed paleoanthropology.",
        "style": "photorealistic bone texture with visible porosity and aging, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm sepia highlights cool shadows, museum specimen documentation aesthetic.",
        "avoid": "Homo sapiens skull (must show sagittal keel, thick brow ridge, low forehead, no chin), Neanderthal skull, modern human skull, modern display case, modern labels visible, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, plastic-looking bone."
    }),
}


# ============= DATA 1B =============

PROMPTS_1B = {
    "1B-K001-homo-erectus-soloensis.txt": ("K", {
        "name": "an adult Homo erectus soloensis (Manusia Solo), the latest and most progressive Homo erectus in Java",
        "prop_phrase": "holding a chert spear point",
        "details": "Male, 35-45 years old, 165 cm tall, golden brown deeply weathered skin, deep-set dark brown eyes under heavy but slightly reduced brow ridge (compared to earlier Homo erectus), low sloping forehead but less pronounced, broad flat nose, full lips, prognathic jaw but slightly reduced. Long black coarse hair partially tied back with vine. Naked torso (no clothing - Pleistosen Akhir), skin marked by years of sun exposure, healed scar on left shoulder.",
        "avoid": "modern clothing, jewelry, body paint, western features, Chinese features, Homo sapiens features (high vertical forehead, chin projection, thin brow ridge), Neanderthal features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1B-K002-homo-floresiensis.txt": ("K", {
        "name": "an adult Homo floresiensis (LB1 specimen, Manusia Hobbit of Flores)",
        "prop_phrase": "holding a small chert flake tool",
        "details": "Female, 30 years old, 106 cm tall (extremely short - insular dwarfism), golden brown skin, deep-set dark brown eyes under heavy brow ridge but smaller face than Homo erectus, low sloping forehead, broad flat nose, full lips, prognathic jaw. Long black coarse hair tangled. Small but muscular frame, short legs and arms (proportional dwarfism). Naked torso (no clothing).",
        "avoid": "Homo sapiens features (high forehead, chin), modern child (must be adult dwarf), modern clothing, jewelry, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, full Homo erectus size (must show insular dwarfism - short stature, 106 cm)."
    }),
    "1B-K003-manusia-wajak.txt": ("K", {
        "name": "an adult Homo wajakensis (Manusia Wajak), early modern human with Australoid features",
        "prop_phrase": "holding a wooden spear with chert point",
        "details": "Male (Wajak II specimen), 25-35 years old, 170 cm tall (tall for the period), dark brown skin, deep-set dark brown eyes under moderate brow ridge, medium forehead (less sloped than Homo erectus), broad flat nose, full lips, prognathic jaw but less than Homo erectus. Long black coarse hair, light beard. Naked torso (no clothing), wearing simple necklace of shell beads.",
        "avoid": "Homo erectus features (heavy brow ridge, low forehead, strong prognathism - Wajak is early Homo sapiens), modern clothing, modern jewelry, western features, Chinese features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1B-K004-mmaa-lida-ajer.txt": ("K", {
        "name": "an adult Homo sapiens (Manusia Modern Anatomis Awal - MMAA), the earliest modern human in Indonesia",
        "prop_phrase": "holding a digging stick",
        "details": "Female, 22-30 years old, 158 cm tall, dark brown skin, deep-set dark brown eyes under modern thin brow ridge, vertical forehead (modern Homo sapiens feature), broad flat nose, full lips, slight prognathism but with developed chin (modern feature). Long black coarse hair, partially tied with vine. Wearing simple necklace of palm fiber and seeds.",
        "avoid": "Homo erectus features (heavy brow ridge, low forehead, no chin), modern clothing, modern jewelry, western features, Chinese features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, modern agricultural clearing."
    }),
    "1B-L001-toba-supervolcano.txt": ("L", {
        "name": "the Toba supervolcano eruption",
        "period": "Mount Toba, North Sumatra, 74 thousand years ago",
        "scene_details": "Extreme wide aerial shot. Massive volcanic eruption column rising 40+ km into stratosphere, mushroom cloud shape, dark grey-black with red-orange lava fountains at base. Lightning visible within eruption cloud (volcanic lightning). Pyroclastic flows rushing down slopes as glowing orange rivers. Surrounding Paparan Sunda landscape - tropical forest being devastated, ash falling like grey snow. 2,800 km³ of material ejected. Small fleeing Homo erectus silhouettes in foreground.",
        "lighting": "dramatic orange-red 2000K volcanic glow from eruption column (key light from above center, intense orange on landscape), ambient dark 200K (ash dimming sunlight). Extreme high contrast 8:1. Falling ash creating grey haze.",
        "mood": "apocalyptic, geological catastrophe - the largest eruption in human history.",
        "style": "photorealistic volcanic eruption physics (mushroom cloud, pyroclastic flows, volcanic lightning), 35mm film grain, deep depth of field f/11, 16mm ultra-wide lens equivalent, 8K hyperdetailed, color graded apocalyptic orange-red highlights dark grey-black shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern eruption, modern buildings, modern Lake Toba (must be erupting volcano, not caldera lake), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, peaceful landscape, modern tourism."
    }),
    "1B-L002-liang-bua.txt": ("L", {
        "name": "Liang Bua cave interior",
        "period": "Flores, Nusa Tenggara Timur, 50-18 thousand years ago",
        "scene_details": "Cave entrance visible in background with soft daylight filtering in, revealing cave interior with limestone formations (stalactites, stalagmites), scattered stone tools and bones on cave floor. Small hearth fire in middle of cave. Cave walls with faint soot marks from long occupation. No main character.",
        "lighting": "warm 2200K hearth fire from center (key light, dancing shadows on cave walls), cool 6500K daylight from cave entrance in background (fill light, atmospheric haze). High contrast 5:1.",
        "mood": "hidden world, an isolated cave - the home of Homo floresiensis. Quiet, ancient, mysterious.",
        "style": "photorealistic cave limestone textures (wet, glistening), 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm fire-orange highlights cool blue-grey shadows, National Geographic cave documentary aesthetic.",
        "avoid": "modern cave tourism, modern lighting, modern furniture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern humans."
    }),
    "1B-L003-karst-payakumbuh.txt": ("L", {
        "name": "Karst Payakumbuh landscape",
        "period": "West Sumatra, 73-63 thousand years ago",
        "scene_details": "Dense tropical rainforest covering karst limestone hills with dramatic cliff faces and cave openings. Small stream flowing through valley foreground, with ferns and tropical vegetation. Distant smoke from a hearth. No modern elements.",
        "lighting": "warm 4500K filtered sunlight through rainforest canopy (key light, dappled pattern on landscape), cool 6500K sky fill from above. Mid contrast 3:1. Mist rising from stream, light beams through canopy.",
        "mood": "rainforest frontier, the dawn of modern humanity in Nusantara - Homo sapiens adapting to dense tropical rainforest.",
        "style": "photorealistic rainforest foliage textures (fern, palm, vine, moss), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm green-golden highlights cool blue shadows, BBC Earth rainforest documentary aesthetic.",
        "avoid": "modern buildings, modern agriculture, modern roads, modern logging, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern researchers, modern equipment."
    }),
    "1B-L004-bengawan-solo-akhir.txt": ("L", {
        "name": "Lembah Bengawan Solo valley in Pleistosen Akhir",
        "period": "East Java, 50 thousand years ago",
        "scene_details": "Wide muddy river meandering through open woodland with gallery forest along banks. Mixed fauna: Stegodon herd drinking at river edge, deer in grassland, predators (large cats) in distant brush. Volcanic mountains on distant horizon.",
        "lighting": "warm 3500K golden hour sun from camera left low angle (key light, long shadows of trees and animals, golden amber on river surface), cool 6500K sky fill from above. High contrast 4:1. Mist on river.",
        "mood": "twilight of Homo erectus, the last days of an ancient lineage - landscape that will soon change forever.",
        "style": "photorealistic water, grass, and animal textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern river engineering, modern agriculture, modern livestock, modern humans, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern elephant species (must be Stegodon)."
    }),
    "1B-L005-karst-campurdarat.txt": ("L", {
        "name": "Karst Campurdarat landscape",
        "period": "East Java, 37-28 thousand years ago (Manusia Wajak period)",
        "scene_details": "Dramatic karst limestone hills with multiple cave openings visible on cliff faces. Open woodland with gallery forest in valley, grassland beyond. Pleistocene fauna in distance: deer, wild cattle (Bos javanicus). Distant volcanic mountains.",
        "lighting": "warm 4000K morning sun from camera right (key light, long shadows on karst cliffs revealing texture), cool 6500K sky fill from above left. Mid contrast 3:1. Light mist in valley.",
        "mood": "new chapter, modern humans spread across Java - the karst caves become home to tall, adaptable Homo sapiens.",
        "style": "photorealistic karst limestone textures (rough, weathered), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (cream limestone, green foliage), National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern vegetation patterns, modern agriculture."
    }),
    "1B-F001-homo-erectus-stegodon-berburu.txt": ("A", {
        "name": "a small band of Homo erectus soloensis hunting a Stegodon in open woodland of Bengawan Solo valley",
        "object_details": "4-5 hunters (tiny silhouettes on left) coordinating with wooden spears and chert flake tools, two flanking from left, two from right, one throwing spear. Stegodon (large extinct elephant with downward-curving tusks, center frame) distressed, trunk raised, charging. Other Stegodon (3-4) fleeing in background. Dust kicked up. East Java, 80 ka.",
        "lighting": "warm 3500K late afternoon sun from camera left low angle (key light, dramatic long shadows, dust particles catching light, golden amber on animal skin and hunter bodies), cool 6500K sky fill from above right. High contrast 5:1.",
        "mood": "cooperative survival, the hunt - Homo erectus coordinating to bring down massive prey.",
        "style": "photorealistic animal and human textures (wrinkled elephant hide, weathered human skin), motion blur on charging Stegodon, 35mm film grain, deep depth of field f/5.6, 35mm lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth wildlife documentary aesthetic.",
        "avoid": "modern elephant species (must be Stegodon), modern humans, modern weapons (guns), modern clothing, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, Homo sapiens features in hunters (must be Homo erectus)."
    }),
}


# ============= DATA 1C =============

PROMPTS_1C = {
    "1C-K001-papuamelanesia.txt": ("K", {
        "name": "an adult Papuamelanesia (Australomelanesid) male from Holosen Awal",
        "prop_phrase": "holding a chert flake tool and a digging stick",
        "details": "Male, 30-40 years old, 167 cm tall, dark brown skin, deep-set dark brown eyes under moderate brow ridge (thicker than modern Asian, thinner than Homo erectus), low sloping forehead with temporal not fully rounded, dolichocephalic (long) skull, slight occipital bun, medium face with thick brow arc, deep jaw, strong chewing apparatus with thick lower jaw. Teeth not yet reduced (large molars). Long black coarse hair, light beard. Naked torso (no clothing - Holosen Awal), wearing necklace of shell beads and animal teeth.",
        "avoid": "Homo erectus features (heavy brow ridge, low forehead, strong prognathism), modern Asian features (Mongoloid, epicanthic fold, light skin), modern clothing, modern jewelry, western features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."
    }),
    "1C-K002-penghuni-gua-pawon.txt": ("K", {
        "name": "an adult female from Gua Pawon (Holosen Awal, Jawa Barat)",
        "prop_phrase": "holding a stone pestle (pipisan) for grinding ochre",
        "details": "Female, 25-35 years old, 152 cm tall, dark brown skin, deep-set dark brown eyes under moderate brow ridge, low sloping forehead with Papuamelanesia characteristics, dolichocephalic skull, prognathic jaw, thick lower jaw, large molars (not reduced). Long black coarse hair partially tied. Naked torso (no clothing), wearing simple necklace of perforated shell beads and shark teeth.",
        "avoid": "Homo erectus features, modern Asian features, modern clothing, modern jewelry, western features, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, modern cave tourism, modern equipment, watermark, text, signature, low resolution, blurry, oversaturated, modern lighting."
    }),
    "1C-K003-hoabinhian-sumatra.txt": ("K", {
        "name": "an adult male Hoabinhian hunter from East Sumatra coast",
        "prop_phrase": "holding a Sumatralith (pebble tool with one side flaked) and a digging stick",
        "details": "Male, 30-40 years old, 153 cm tall, dark brown skin deeply weathered by sun and salt air, deep-set dark brown eyes under moderate brow ridge, Papuamelanesia features (low forehead, dolichocephalic skull, prognathic jaw, large molars). Long black coarse hair tangled, light beard. Naked torso (no clothing), wearing shell bead necklace.",
        "avoid": "Homo erectus features, modern Asian features, modern clothing, modern jewelry, modern fishing equipment, modern buildings, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, modern coastal development."
    }),
    "1C-L001-karst-moros-pangkep.txt": ("L", {
        "name": "Karst Maros-Pangkep landscape",
        "period": "South Sulawesi, 40-12 thousand years ago",
        "scene_details": "Dramatic limestone karst towers rising from tropical forest. Cave entrances visible on cliff faces, some with visible red ochre rock art (hand stencils, animal figures - babi, anoa, babirusa) as small red marks. Bengawan Jene river flowing through valley foreground. Tropical rainforest covering valley floor. 530 cave sites in this karst area.",
        "lighting": "warm 3500K late afternoon sun from camera left (key light, long shadows on karst towers revealing texture, warm amber on forest), cool 6500K sky fill from above right. Mid contrast 3:1. Light mist in valley.",
        "mood": "cradle of cave art, a sacred landscape - the densest concentration of Pleistocene rock art in the world.",
        "style": "photorealistic karst limestone textures (rough, weathered, vertical cliff faces), tropical rainforest foliage, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern roads, modern tourism, modern researchers, modern equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern agricultural clearing, modern cave lighting."
    }),
    "1C-L002-sangkulirang-mangkalihat.txt": ("L", {
        "name": "Karst Sangkulirang-Mangkalihat",
        "period": "East Kalimantan, 40-13.6 thousand years ago",
        "scene_details": "Dramatic karst limestone massif rising from tropical rainforest at eastern edge of Eurasian continental shelf. Multiple cave openings visible on cliff faces, with rock art visible as small red markings (banteng silhouettes, hand stencils with dots, datu shaman figures). Tropical rainforest covering valley.",
        "lighting": "warm 3500K morning sun from camera right (key light, raking across karst revealing texture, warm amber on forest), cool 6500K sky fill from above. Mid contrast 3:1. Mist in valley, light beams through canopy.",
        "mood": "three phases of art, 30 thousand years of creative expression - the longest continuous rock art tradition in the world.",
        "style": "photorealistic karst limestone and rainforest textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (cream limestone, green foliage), BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern agricultural clearing, modern logging."
    }),
    "1C-L003-bukit-kerang-sumatra.txt": ("L", {
        "name": "bukit kerang (shell midden / kitchen midden) site",
        "period": "East Sumatra coast, 8 thousand years ago",
        "scene_details": "Large pile of discarded shells (Gastropoda, Bivalvia) accumulated over centuries of coastal foraging, forming a small hill 3-5 meters tall. Coastal vegetation (pandanus, palm trees). Distant sea horizon. Stone tools and food remains scattered around midden.",
        "lighting": "warm 4000K mid-morning sun from camera right (key light, salt-air haze, golden on shells and sand), cool 6500K sky fill from above left. Mid contrast 3:1.",
        "mood": "coastal abundance, the Hoabinhian foragers - centuries of coastal gathering accumulated into shell mounds.",
        "style": "photorealistic shell textures (varied colors, weathered surfaces), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic coastal documentary aesthetic.",
        "avoid": "modern buildings, modern coastal development, modern fishing equipment, modern boats, modern pollution, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern shellfish farms."
    }),
    "1C-L004-gua-pawon.txt": ("L", {
        "name": "Gua Pawon entrance",
        "period": "Karst Rajamandala, Bandung, West Java, 9 thousand years ago",
        "scene_details": "Limestone cave with arched entrance 4-5 meters tall, oriented east-west with opening facing north. Surrounded by tropical vegetation. Tropical rainforest covering karst hills. Distant river.",
        "lighting": "warm 4500K morning sun from camera right (key light, raking across cave entrance revealing limestone texture, warm amber on vegetation), cool 6500K sky fill from above left. Mid contrast 3:1. Soft light spilling into cave interior.",
        "mood": "Holosen home, a cave as dwelling - domestic life at the cave entrance.",
        "style": "photorealistic limestone and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (cream limestone, green foliage), National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern cave lighting, modern researchers, modern equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern agricultural clearing."
    }),
    "1C-L005-leang-panningge.txt": ("L", {
        "name": "Leang Panningge cave entrance",
        "period": "Mallawa, Maros, South Sulawesi, 5 thousand years ago",
        "scene_details": "Cave at 400 mdpl, distant from coast. Scattered food scraps in courtyard (attracting a wild pig Sus celebensis). Cave interior with smoke from hearth. Tropical forest around cave.",
        "lighting": "warm 3500K afternoon sun from camera right (key light, long shadows, golden amber on courtyard and pig), cool 6500K sky fill from above left. Mid contrast 3:1.",
        "mood": "dawn of domestication, the first taming - food scraps attracting a wild pig that has learned to come to the cave entrance.",
        "style": "photorealistic pig (Sus celebensis - wild Sulawesi pig with bristly hair), skin and stone tool textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern domestic pig (must be wild Sus celebensis with bristly hair and slender build), modern clothing, modern buildings, modern pig farming equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern cave tourism."
    }),
    "1C-A001-lukisan-cadas.txt": ("A", {
        "name": "pre-Austronesian rock art on limestone cave wall",
        "object_details": "Two motifs: (1) negative hand stencil (cap tangan negatif) - red ochre sprayed around an outstretched hand, leaving hand silhouette in natural rock color, fingers spread including thumb; (2) animal figure (babi / pig) painted in red ochre, crude but recognizable with body, four legs, head, and tail. Both motifs on rough grey-beige limestone with natural texture, cracks, and weathering. Pigment aged with reddish-brown patina. 40-20 thousand years old, Karst Maros-Pangkep or Sangkulirang-Mangkalihat.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing rock texture, hand stencil silhouette, pigment layering), low ambient fill. High contrast 5:1.",
        "mood": "hands across time, the earliest signature of human creativity - a hand pressed against stone 40 thousand years ago.",
        "style": "photorealistic limestone texture with visible mineral grains and weathering, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones (red ochre, cream limestone), scientific documentation aesthetic.",
        "avoid": "modern graffiti, modern paint (acrylic, oil), modern wall, modern canvas, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern lighting equipment, modern scale rulers visible."
    }),
    "1C-A002-sumatralith.txt": ("A", {
        "name": "a Sumatralith (Hoabinhian pebble tool) on dark volcanic stone surface",
        "object_details": "Flattened river pebble (cobble) of andesite/basalt, roughly oval shape 12 cm long, with one face flaked to create a working edge (unifacial flaking). Other face left natural (cortex). Visible flake scars, sharp working edge, slight patina. Dark grey-black basalt with weathering. Hoabinhian culture, East Sumatra, 8 thousand years ago.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing flake scars and patina), low ambient fill. High contrast 5:1. Dust particles in light beam.",
        "mood": "ancient technology, the distinctive tool of Hoabinhian coastal foragers.",
        "style": "photorealistic rock texture with visible mineral grains and flake scars, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey-black basalt), scientific documentation aesthetic.",
        "avoid": "modern tools, polished modern stone tools, metal tools, ceramic, plastic, modern background, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, bifacial flaking (Sumatralith is unifacial - only one side flaked)."
    }),
}


# ============= DATA 1D =============

PROMPTS_1D = {
    "1D-K001-primus-inter-pares.txt": ("K", {
        "name": "an adult male leader (primus inter pares - first among equals) of a perundagian community in Nusantara",
        "prop_phrase": "holding a bronze adze (kapak corong) as symbol of authority",
        "details": "Male, 40-50 years old, 165 cm tall, dark brown skin weathered by years, deep-set dark brown eyes under moderate brow ridge, medium forehead with Australomelanesian-Papua features (slight prognathism, broad nose, full lips, dolichocephalic skull). Long black coarse hair, some grey, partially tied with vine. Wearing barkcloth (kain kulit kayu) wrap around waist, chest bare, ornate bronze necklace with spiral motifs, gold disc pendant, bronze armlets (keyura).",
        "avoid": "modern clothing, modern jewelry, modern raja/king costume (must be primus inter pares - simpler, less ornate), Homo erectus features, modern Asian features (Mongoloid, light skin), anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, modern crown."
    }),
    "1D-K002-undagi-logam.txt": ("K", {
        "name": "an adult undagi (metal craftsman) casting bronze",
        "prop_phrase": "holding a bronze pouring ladle",
        "details": "Male, 35-45 years old, dark brown skin weathered by heat and labor, deep-set dark brown eyes under moderate brow ridge, Australomelanesian features. Short black hair (for safety near furnace). Naked torso (barkcloth wrap only at waist), soot and sweat on skin, healed burn scars on forearms. Bronze pouring ladle in right hand.",
        "avoid": "modern welding equipment, modern safety gear, modern foundry, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, modern tools, modern furnace, watermark, text, signature, low resolution, blurry, oversaturated, modern workshop."
    }),
    "1D-K003-pengrajin-barkcloth.txt": ("K", {
        "name": "an adult female pengrajin barkcloth (kain kulit kayu) maker",
        "prop_phrase": "holding a barkcloth beater type IV (pemukul kulit kayu - stone tool with 3 grooved sides)",
        "details": "Female, 30-40 years old, 158 cm tall, dark brown skin, deep-set dark brown eyes under moderate brow ridge, Australomelanesian features (broad nose, full lips, dolichocephalic skull). Long black coarse hair tied back. Wearing barkcloth wrap around waist and chest.",
        "avoid": "modern textile equipment, modern loom, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, modern tools, modern workshop, watermark, text, signature, low resolution, blurry, oversaturated, woven fabric (must be beaten barkcloth, not woven)."
    }),
    "1D-K004-pengrajin-manik-gilimanuk.txt": ("K", {
        "name": "an adult female bead maker at Gilimanuk workshop, Bali",
        "prop_phrase": "holding a small bronze wire (tongkat besi) for winding molten glass beads",
        "details": "Female, 25-35 years old, dark brown skin, deep-set dark brown eyes, Australomelanesian features. Long black coarse hair tied back. Wearing barkcloth wrap and ornate shell bead necklace. 100 AD.",
        "avoid": "modern bead-making equipment, modern safety gear, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, modern workshop, modern lighting, watermark, text, signature, low resolution, blurry, oversaturated, plastic beads (must be glass)."
    }),
    "1D-L001-gunung-padang.txt": ("L", {
        "name": "Punden Berundak Gunung Padang",
        "period": "Cianjur, West Java, 200 BC",
        "scene_details": "Massive stepped stone pyramid made of andesite blocks, multiple terraces rising from base to peak (5+ terraces visible). Uppermost terrace (most sacred) has a menhir (standing stone). Tropical rainforest covering surrounding hills. Distant volcanic mountains. Largest punden berundak site in Indonesia.",
        "lighting": "warm 3500K morning sun from camera right (key light, raking across terraces revealing stone texture, long shadows), cool 6500K sky fill from above. Mid contrast 3:1. Mist in valley.",
        "mood": "sacred mountain, the monumental expression of ancestor worship - punden berundak as architectural form of megalithic belief.",
        "style": "photorealistic andesite stone textures (weathered, lichen-covered), 35mm film grain, deep depth of field f/8, 16mm ultra-wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey andesite, green forest), BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern equipment, modern stairs/handrails, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern agricultural clearing, modern vegetation patterns."
    }),
    "1D-L002-pulau-kampai.txt": ("L", {
        "name": "Pulau Kampai coastal trading settlement",
        "period": "Teluk Aru, North Sumatra, 5-7 CE (abad 5-7 Masehi)",
        "scene_details": "Coastal trading settlement with bamboo and thatch houses, workshop areas with furnaces for glass bead making. Trays of glass beads visible (mixed colors: red, yellow, black, green, blue, white, polychrome). Trade goods: imported glass tubes from India, soda plant ash glass from Middle East. Coastal scene with perahu (boats) at dock, distant sea horizon.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on coastal scene and workshop), cool 6500K sky fill from above right. Mid contrast 3:1. Sea haze.",
        "mood": "cosmopolitan workshop, beads as currency and connection - node in Indian Ocean trade networks.",
        "style": "photorealistic bamboo, thatch, glass bead textures (varied colors), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic coastal documentary aesthetic.",
        "avoid": "modern buildings, modern fishing village, modern boats, modern glass-making equipment, modern clothing, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern tourism, modern pollution."
    }),
    "1D-L003-pangkung-paruk.txt": ("L", {
        "name": "Pangkung Paruk burial site",
        "period": "Buleleng, Bali, 122-331 AD",
        "scene_details": "Excavation context showing primary burial (terlentang / supine position) of an adult with rich grave goods: 778 glass beads scattered around the body, 43 gold beads (pentagonal, heksagonal, biconical, granulated, spiral, kail - composition matching Mesir-Roma production). Body wrapped in decayed barkcloth, wearing shell bead necklace. Tropical forest background. Archaeological context.",
        "lighting": "warm 3500K afternoon sun from camera right (key light, raking across excavation revealing textures and colors of beads), cool 6500K sky fill from above. Mid contrast 3:1. Soft light on beads highlighting their colors.",
        "mood": "wealth in death, beads as grave goods - rich burial with gold and glass beads from Egypt-Roma, evidence of Indian Ocean trade reaching Mediterranean.",
        "style": "photorealistic bone, bead (gold and glass), and soil textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (gold beads, blue glass, brown soil), National Geographic archaeology documentary aesthetic.",
        "avoid": "modern excavation equipment, modern researchers, modern clothing on body (must be ancient barkcloth), modern scale rulers, modern labels, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern grave markers."
    }),
    "1D-L004-gilimanuk.txt": ("L", {
        "name": "Gilimanuk trading port",
        "period": "western tip of Bali, 100 AD",
        "scene_details": "Coastal trading port with bamboo and thatch houses along the beach. Boats (perahu) at dock - Javanese, Sumatran, Indian vessels. Market stalls with pottery, barkcloth, metal tools. Trade goods: Indian glass beads, Roman glass, Chinese bronze mirrors (Han Dynasty), Dongson bronze drums from Vietnam. Tropical coastal scene with palm trees, distant volcanoes (Java's Ijen range across strait).",
        "lighting": "warm 3500K late afternoon sun from camera left (key light, long shadows on beach and boats, golden amber on water), cool 6500K sky fill from above. Mid contrast 3:1. Sea haze.",
        "mood": "cosmopolitan port, beads and bronze - meeting point of Indian Ocean and South China Sea trade networks.",
        "style": "photorealistic bamboo, thatch, boat, and trade goods textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, National Geographic coastal documentary aesthetic.",
        "avoid": "modern buildings, modern port, modern boats, modern fishing equipment, modern clothing, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern tourism, modern pollution."
    }),
    "1D-L005-dataran-tinggi-lore.txt": ("L", {
        "name": "Dataran Tinggi Lore with megalithic kalamba",
        "period": "Central Sulawesi, 500 AD",
        "scene_details": "Mountain valley with megalithic kalamba (stone barrel-shaped burial jars) scattered across grassland. Large stone jar with carved patterns, tuatena (stone lid) lying beside it. Other kalamba in middle distance. Tropical forest on surrounding mountains.",
        "lighting": "warm 3500K morning sun from camera right (key light, long shadows revealing kalamba texture, golden amber on grass), cool 6500K sky fill from above. Mid contrast 3:1. Mist in valley.",
        "mood": "sacred valley, megalithic burial tradition - kalamba as architectural form of ancestor worship in the highlands of Sulawesi.",
        "style": "photorealistic stone kalamba textures (carved patterns, weathered surface), 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey stone, green grass), National Geographic documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern equipment, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern grave markers, modern burial practices."
    }),
    "1D-A001-nekara-dongson.txt": ("A", {
        "name": "a nekara (bronze drum) type Heger IA Dong-Son",
        "object_details": "Large drum (60-80 cm tall, 50-70 cm diameter), bronze with green oxidation patina. Decorated with classic Dong-Son motifs: star pattern on top (tympanum), flying bird figures, frog sculptures on rim, geometric patterns (sawtooth, spiral). Aged bronze green-black with original metallic bronze on raised surfaces. Found at Papanlohea, Selayar, South Sulawesi, 200 AD. Produced in Vietnam (Dong-Son culture).",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing bronze texture, motifs, and patina), low ambient fill. High contrast 5:1. Subtle reflections on metallic surfaces.",
        "mood": "exotic import, evidence of trade - a bronze drum from Vietnam, found in Selayar.",
        "style": "photorealistic bronze texture with green patina, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm bronze highlights cool green shadows, museum specimen documentation aesthetic.",
        "avoid": "modern drum, modern bronze, polished modern bronze, modern display case visible, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, plastic-looking metal."
    }),
    "1D-A002-manik-emas-mesir-roma.txt": ("A", {
        "name": "gold beads from Pangkung Paruk burial",
        "object_details": "Several bead types arranged on dark velvet: (1) pentagonal gold bead (5-sided flat shape), (2) heksagonal gold bead (6-sided), (3) biconical gold bead (two cones joined at base), (4) granulated gold bead (surface covered with tiny gold spheres - granulation technique), (5) spiral gold bead (wire wound in coil), (6) hook-shaped gold bead (kail), (7) comma-shaped gold bead (lengkung). Small (5-15 mm each), brilliant metallic gold with subtle patina. Composition matches Egyptian-Roman production. Bali, 122-331 AD.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing gold texture, granulation detail, forms), low ambient fill. High contrast 5:1. Subtle reflections on gold surfaces.",
        "mood": "Mediterranean gold in Bali, evidence of vast trade networks - gold beads produced in Egypt during Roman rule, found in a Balinese burial.",
        "style": "photorealistic gold texture with granulation detail visible, 35mm film grain, shallow depth of field f/2.8, 100mm macro lens equivalent, 8K hyperdetailed, color graded warm gold highlights cool dark shadows, museum specimen documentation aesthetic.",
        "avoid": "modern jewelry, modern gold (too polished), modern display case visible, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, plastic-looking gold, modern bead shapes (must match ancient forms: pentagonal, heksagonal, biconical, granulated, spiral, kail, lengkung)."
    }),
    "1D-A003-sarkofagus-bali.txt": ("A", {
        "name": "a Balinese stone sarkofagus (kubur batu) with bronze drum kubur (burial drum) visible inside",
        "object_details": "Large stone container (1.5 m long, 60 cm wide) with symmetrical lid, carved from single andesite boulder with hollow interior. Inside: human remains (bone fragments), a large bronze drum (50 cm diameter, used as burial container), gold ornaments (spiral, lempeng), and glass beads. Sarkofagus shows local carving style distinct from imported bronze drum. Grey andesite stone, green-patinized bronze, gold. Bali tradition.",
        "lighting": "warm 3000K raking side light from camera right (key light, revealing stone texture, bronze patina, gold reflections), low ambient fill. High contrast 5:1. Subtle reflections on gold and bronze surfaces.",
        "mood": "local adaptation of foreign materials - Balinese craftsmen recast imported bronze drums into local forms.",
        "style": "photorealistic stone, bronze, and gold textures, 35mm film grain, shallow depth of field f/2.8, 50mm macro lens equivalent, 8K hyperdetailed, color graded warm earth tones (grey stone, green bronze, gold), museum specimen documentation aesthetic.",
        "avoid": "modern coffin, modern burial, modern display case visible, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern stone carving, modern bronze."
    }),
}


# ============= GENERATE =============

ALL_PROMPTS = {
    "1A-prasejarah-pleistosen-awal": PROMPTS_1A,
    "1B-prasejarah-pleistosen-tengah-akhir": PROMPTS_1B,
    "1C-prasejarah-holosen-neolitik": PROMPTS_1C,
    "1D-prasejarah-logam-awal": PROMPTS_1D,
}

def gen_k(data):
    return TEMPLATE_K.format(**data)

def gen_l(data):
    return TEMPLATE_L.format(**data)

def gen_a(data):
    return TEMPLATE_A.format(**data)

GENERATORS = {"K": gen_k, "L": gen_l, "A": gen_a}

def main():
    total = 0
    for era_folder, prompts in ALL_PROMPTS.items():
        out_dir = BASE / era_folder / "prompts"
        out_dir.mkdir(parents=True, exist_ok=True)
        for filename, (ptype, data) in prompts.items():
            content = GENERATORS[ptype](data)
            out_path = out_dir / filename
            out_path.write_text(content, encoding="utf-8")
            total += 1
            print(f"  ✅ {era_folder}/prompts/{filename}")
    print(f"\nTotal: {total} file generated")

if __name__ == "__main__":
    main()
