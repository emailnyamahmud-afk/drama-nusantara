#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 2A — Hindu-Buddha Awal (Abad 4-7 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/2A-hindu-buddha-awal/prompts"

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
    name="Mulawarman, King of Kutai",
    era_desc="4th-5th century AD, Kutai, Kalimantan Timur — earliest Hindu kingdom in Nusantara",
    phenotype="Male, 35-45 years old, Javanese-Indonesian phenotype with golden brown skin, sharp facial features, regal bearing. Black hair tied in topknot. Muscular build from royal lifestyle.",
    costume="Wearing early Hindu royal costume: gold makuta (crown) with leaf motifs, gold hara necklace with Shiva linga pendant, gold keyura armlets, gold kankana bracelets, red-and-gold kemben (brocade), batik kain with parang pattern, kris pusaka at waist.",
    props="holding a ceremonial golden staff",
    mood="Raja yang berkeadaban baik, kuat dan kuasa — the first Hindu king of Nusantara, who gave 20,000 cows to Brahmana at Waprakeswara. Vedic Hindu, pre-Trimurti.",
    avoid_extra=", Chinese emperor costume, Indian Mughal costume, Islamic costume",
)

K002 = k_prompt(
    name="Purnawarman, King of Tarumanagara",
    era_desc="5th century AD, West Java — king who built the Gomati canal",
    phenotype="Male, 35-45 years old, Sundanese-Javanese phenotype with golden brown skin, sharp regal features, determined expression. Black hair in topknot with gold diadem. Athletic build from military campaigns.",
    costume="Wearing Hindu Waisnawa royal costume: gold makuta with Vishnu Garuda motif, gold necklace with Vishnu Trivikrama pendant, gold armlets, red silk upper wrap, batik kain, kris at waist. Lencana: Garudamukha (Garuda emblem).",
    props="holding a ceremonial sword",
    mood="Vikkranta — the king who identified himself with Vishnu's three steps. Builder of the 11 km Gomati canal in 21 days, conqueror who called himself cakravartin. Early Waisnawa Hindu.",
    avoid_extra=", Islamic costume, Buddhist costume, Chinese emperor costume",
)

K003 = k_prompt(
    name="Dapunta Hyang Srijayanasa, founder of Kedatuan Sriwijaya",
    era_desc="682 AD, Palembang, Sumatra Selatan — founder of Sriwijaya maritime empire",
    phenotype="Male, 40-50 years old, Sumatran Malay phenotype with medium brown skin, dignified features, calm authoritative expression. Black hair in simple topknot (not ornate crown — Datu title is local, not Indian). Lean build from maritime lifestyle.",
    costume="Wearing Melayu Kuno royal attire: simple gold headband (not makuta), gold chain necklace with Buddhist pendant, gold armlets, dark blue silk jubah, woven songket kain. Modest compared to Javanese kings — thalassocracy values function over display.",
    props="holding a ceremonial kendi (water vessel — siddhayatra symbol)",
    mood="Siddhayatra — the visioner who united the maritime states of Swarnadwipa. Local Datu title (not Indian raja), Buddhist patron, builder of thalassocracy. The foundation of Nusantara's first great empire.",
    avoid_extra=", Hindu makuta crown, Javanese keraton costume, Islamic costume",
)

K004 = k_prompt(
    name="a South Indian Brahmana priest",
    era_desc="4th-5th century AD, Kutai/Tarumanagara — Vedic Hindu priest from India",
    phenotype="Male, 50-60 years old, South Indian Dravidian phenotype with dark brown skin, sharp features, deep-set dark brown eyes. Shaved head with small topknot (shikha). Lean build from ascetic lifestyle. Forehead marked with Vaishnava tilaka (U-shaped white mark).",
    costume="Wearing simple white dhoti, upavita (sacred thread across chest), rudraksha bead necklace. No jewelry except simple copper bangle. Carrying a wooden staff and a copper ritual vessel.",
    props="holding a ritual fire vessel (Agni offering)",
    mood="Bearer of civilization — the Brahmana who brought Sanskrit, Pallawa script, and Vedic ritual to Nusantara. Not a conqueror, but a teacher whose knowledge transformed indigenous kingdoms.",
    avoid_extra=", modern Hindu priest costume, Islamic costume, Buddhist monk robe",
)

K005 = k_prompt(
    name="a Buddhist monk (Bhikkhu) of early Sriwijaya",
    era_desc="7th century AD, Palembang — Mulasarvastivada Buddhist monk",
    phenotype="Male, 30-40 years old, Sumatran/Malay phenotype with medium brown skin, serene expression, shaved head. Lean build from monastic lifestyle. Wearing simple saffron/orange robe (sanghati) draped over one shoulder. Carrying a palm-leaf manuscript and wooden alms bowl.",
    costume="",
    props="holding a palm-leaf manuscript",
    mood="Keeper of the Dharma — the Buddhist monk of Sriwijaya, where Yijing reported Mulasarvastivada tradition flourishing. These monks made Palembang a center of Buddhist learning that attracted students from China and India.",
    avoid_extra=", Hindu Brahmana costume, Islamic costume, Tibetan Buddhist costume",
)

K006 = k_prompt(
    name="an indigenous datu (local chieftain) of Swarnadwipa",
    era_desc="5th-6th century AD, Sumatra — pre-Sriwijaya local leader",
    phenotype="Male, 40-50 years old, Sumatran Malay phenotype with medium brown skin, strong features, weathered skin from maritime life. Black hair in simple topknot. Muscular build from seafaring. Tattoo marks on arms (traditional Malay tattooing).",
    costume="Wearing local attire: woven songket cloth, barkcloth upper wrap, simple gold ear discs, shell bead necklace. No crown — local datu title. Carrying a keris and a woven bag.",
    props="holding a keris (dagger)",
    mood="Local power — the indigenous datu who controlled river ports and trade routes before Sriwijaya consolidated them. The foundation upon which Dapunta Hyang built the thalassocracy.",
    avoid_extra=", Hindu royal costume, Buddhist monk robe, Islamic costume",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Muara Kaman, Kutai (Waprakeswara sacred ground)",
    era_desc="4th-5th century AD, Kalimantan Timur — earliest Hindu kingdom in Nusantara",
    scene_desc="Wide cinematic view of the Mahakam riverbank at Muara Kaman. A sacred ceremonial ground (Waprakeswara) on the riverbank — open clearing with 7 yupa (stone pillars with Pallawa script) standing in a row. Tropical rainforest behind. Herd of cattle grazing in clearing. Distant longhouses of local Kutai people. River Mahakam flowing past. No people.",
    lighting_desc="warm 4000K late afternoon sun from camera left (key light, golden on river and forest), cool 6500K sky fill. Mid contrast 3:1. Mist on river.",
    mood_desc="Birth of a kingdom — Muara Kaman, where the first Hindu state in Nusantara was born. The 7 yupa pillars mark the Vedic sacrifice of 20,000 cows by Mulawarman, recorded in the oldest Sanskrit inscription in Southeast Asia.",
)

L002 = l_prompt(
    name="Tarumanagara (West Java kingdom landscape)",
    era_desc="5th century AD, West Java — Purnawarman's kingdom",
    scene_desc="Wide view of the Tarumanagara landscape — tropical lowland with the Gomati canal (11 km long, hand-dug in 21 days) cutting through rice paddies. Distant volcanic mountains (Halimun). River Citarum flowing through valley. Scattered village settlements with raised wooden houses. The canal that Purnawarman built — engineering marvel of early Java. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, revealing canal and paddies), cool 6500K sky fill. Mid contrast 3:1. Morning mist.",
    mood_desc="Engineering kingdom — Tarumanagara, where King Purnawarman built the Gomati canal in just 21 days. A demonstration of organized labor and royal power that preceded the monumental temple culture of central Java.",
)

L003 = l_prompt(
    name="Batujaya temple complex (early Buddhist site, West Java)",
    era_desc="5th-7th century AD, West Java — earliest Buddhist temple in Nusantara",
    scene_desc="Wide view of the Batujaya temple complex — low brick stupas and temple foundations emerging from rice paddies. Simple rectangular brick structures (not yet the tall stone towers of later Mataram). Tropical vegetation around perimeter. The site shows Mahayana Buddhism arrived in Tarumanagara alongside Hindu Waisnawa. Distant flat coastal plain. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, revealing brick textures), cool 6500K sky fill. Mid contrast 3:1.",
    mood_desc="First Buddhist temple — Batujaya, where simple brick stupas mark the arrival of Mahayana Buddhism from Nalanda (India). The coexistence of Hindu and Buddhist sites in 5th century West Java shows the tolerance of early Nusantara kingdoms.",
)

L004 = l_prompt(
    name="Palembang / Bukit Siguntang (Sriwijaya capital)",
    era_desc="7th century AD, Sumatra Selatan — heart of Kedatuan Sriwijaya",
    scene_desc="Wide cinematic view of the Musi-Ogan river confluence at Palembang. Wooden stilt houses along riverbank. Trading boats from India, Persia, and China at dock. Bukit Siguntang visible as sacred hill in background with stone prasasti (siddhayatra). Wihara (Buddhist monastery) with golden stupa. Market stalls with gold, camphor, frankincense, agarwood. Tropical rainforest surrounding. No people.",
    lighting_desc="warm 4000K late morning sun from camera left (key light, golden on river and port), cool 6500K sky fill from above right. Mid contrast 3:1. Sea haze, smoke from cooking fires.",
    mood_desc="Thalassocracy — Sriwijaya, maritime empire where river meets sea. The hub of Indian Ocean–South China Sea trade, where Buddhist learning, Malay language, and international commerce converged. The first great Nusantara empire.",
)

L005 = l_prompt(
    name="Barus (kapur barus port, West Sumatra coast)",
    era_desc="4th-10th century AD, Tapanuli Tengah, Sumatra Utara — camphor trade port",
    scene_desc="Wide view of the Barus coastal port. Natural harbor with merchant ships from Persia and India. Wooden warehouse buildings on stilts near shore. Camphor trees (Dryobalanops aromatica) visible on hills behind. The port that gave its name to 'kapur barus' (camphor) — the most valuable commodity of ancient Nusantara trade. Bongal site (4th century artifacts) in foreground. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor and forest), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="Source of the world's finest camphor — Barus, the port that connected Nusantara to Persia, India, and the Middle East for over a thousand years. Where Tamil, Arab, and Batak traders met to exchange gold, camphor, and ideas.",
)

L006 = l_prompt(
    name="Kan-to-li / Jambi (Batanghari river port)",
    era_desc="5th-6th century AD, Jambi, Sumatra — pre-Sriwijaya trade polity",
    scene_desc="Wide view of the Batanghari river mouth at Jambi. Wide river with trading canoes. Raised wooden houses on riverbanks. Dense tropical forest. Site of ancient Kan-to-li polity (5th-6th century AD) that sent envoys to China. River connects interior gold and forest products to coast. Site of Muarajambi temple complex (later period). No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on river and forest), cool 6500K sky fill. Mid contrast 3:1. River mist.",
    mood_desc="River of gold — Kan-to-li on the Batanghari, where gold from the interior met traders from China and India. The polity that would evolve into the Sriwijaya-Malayu succession.",
)

L007 = l_prompt(
    name="Teluk Jakarta (ancent Tarumanagara port)",
    era_desc="5th century AD, Jakarta — Tarumanagara's maritime gateway",
    scene_desc="Wide view of ancient Teluk Jakarta (Jakarta Bay) in the 5th century. Natural harbor with simple wooden jetties. Outrigger trading canoes on calm water. Raised wooden houses along shore. Dense tropical forest behind settlement. The bay where Faxian (Chinese monk) landed in 414 AD and noted 'Brahmana religion flourishes, Buddhists few.' Distant flat coastal plain. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on bay and forest), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="Gateway — Teluk Jakarta, where Indian culture first entered Java through Tarumanagara's port. Where Faxian the Chinese pilgrim landed and observed the early Hindu kingdom, recording the first foreign account of an Indonesian state.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Prasasti Yupa (Yupa stone pillar of Kutai)",
    era_desc="4th-5th century AD, Muara Kaman, Kutai, Kalimantan Timur",
    scene_desc="A single yupa (stone pillar) made of andesite, 1.5 meters tall, standing on a stone base. Visible: Pallawa script (Brahmi Akhir) carved in Sanskrit language, metrum Anusthubh poetry. Weathered surface with lichen. The 7 yupa at Muara Kaman are the oldest written inscriptions in Indonesia — recording Mulawarman's genealogy and 20,000 cow sacrifice.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing carved script), low ambient fill. High contrast 5:1.",
    mood_desc="First words — the Yupa of Kutai, the oldest written record in Indonesia. These stone pillars mark the moment Nusantara entered history: Sanskrit, Pallawa script, Vedic ritual, and royal genealogy, all carved in stone.",
)

A002 = a_prompt(
    name="Prasasti Tugu (Purnawarman's canal inscription)",
    era_desc="5th century AD, Jakarta — longest early Javanese inscription",
    scene_desc="A large round stone pillar (prasasti) with Pallawa script in Sanskrit, detailing King Purnawarman's construction of the Gomati canal. The inscription mentions: canal length 11 km (6,122 bows), 21 days construction, year 22 of Purnawarman's reign, 1,000 cows given to Brahmana. Stone is weathered with some erosion. ~1 meter tall, cylindrical.",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing carved text), low ambient fill. High contrast 5:1.",
    mood_desc="Royal engineering — the Tugu inscription, recording the greatest public works project of early Java. An 11 km canal dug in 21 days, demonstrating the organizational power of Tarumanagara.",
)

A003 = a_prompt(
    name="Arca Buddha Sambas (gold and silver Buddha)",
    era_desc="7th-8th century AD, Sambas, Kalimantan Barat — early Mahayana Buddhist art",
    scene_desc="3-4 small Buddhist statues on dark velvet: 2 standing Buddha figures and 2 seated Bodhisattva figures, made of gold and silver. Each 10-15 cm tall. Post-Gupta style (Indian influence). Found at Sambas, Kalimantan Barat — evidence of early Buddhist presence. The 'Sambas Treasure' includes the finest early Buddhist metalwork in Indonesia. Gold figures gleam, silver figures tarnished.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing gold luster and silver patina), low ambient fill. High contrast 4:1.",
    mood_desc="Treasure of the forest — the Sambas hoard, golden Buddhas found deep in Kalimantan's interior. They speak of Buddhist missionary activity reaching even the most remote parts of Nusantara, carried by trade routes up the Kapuas river.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="a Vedic ritual at Waprakeswara, Kutai",
    era_desc="4th-5th century AD, Muara Kaman, Kalimantan Timur",
    composition="Group of 4 individuals in a ritual scene pose. Position 1 (left): King Mulawarman, standing with arms raised in blessing, holding golden staff. Position 2 (center): South Indian Brahmana priest, sitting cross-legged near ritual fire (Agni), holding ritual vessel. Position 3 (right): a local Kutai dignitary, standing with hands clasped in respect. Position 4 (far right): a servant holding a tray of offerings (gold, oil, flowers). All wearing appropriate costumes: king in gold regalia, Brahmana in white dhoti, dignitary in local attire, servant in simple barkcloth. Studio background.",
    mood="The first Vedic sacrifice — Mulawarman's gift of 20,000 cows to Brahmana at Waprakeswara. The ritual that marked the arrival of Hindu civilization in Nusantara, recorded on the 7 Yupa pillars.",
    k_refs=["2A-K001 (Mulawarman)", "2A-K004 (Brahmana priest)"],
    avoid_extra=", Islamic costume, Buddhist monk robe",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "2A-K001-mulawarman.txt": K001,
        "2A-K002-purnawarman.txt": K002,
        "2A-K003-dapunta-hyang.txt": K003,
        "2A-K004-brahmana-india.txt": K004,
        "2A-K005-bhikkhu-sriwijaya.txt": K005,
        "2A-K006-datu-swarnadwipa.txt": K006,
        # L — 7
        "2A-L001-muara-kaman-kutai.txt": L001,
        "2A-L002-tarumanagara.txt": L002,
        "2A-L003-batujaya.txt": L003,
        "2A-L004-palembang-sriwijaya.txt": L004,
        "2A-L005-barus.txt": L005,
        "2A-L006-jambi-kantoli.txt": L006,
        "2A-L007-teluk-jakarta.txt": L007,
        # A — 3
        "2A-A001-yupa-kutai.txt": A001,
        "2A-A002-prasasti-tugu.txt": A002,
        "2A-A003-arca-buddha-sambas.txt": A003,
        # S — 1
        "2A-S001-ritual-waprakeswara.txt": S001,
    }

    # Delete old v1 files
    old_files = [
        "2A-A001-yupa-kutai.txt", "2A-A002-prasasti-tugu.txt", "2A-A003-arca-buddha-sambas.txt",
        "2A-K001-mulawarman.txt", "2A-K002-purnawarman.txt", "2A-K003-brahmana-india.txt",
        "2A-K004-aswawarman.txt",
        "2A-L001-muara-kaman-kutai.txt", "2A-L002-batu-tumbuh-tarumanagara.txt",
        "2A-L003-batujaya.txt", "2A-L004-batanghari-kantoli.txt", "2A-L005-kampung-pahat-sanggau.txt",
        "2A-L006-istana-kutai.txt", "2A-L007-istana-tarumanagara.txt",
        "2A-L008-istana-kantoli.txt", "2A-L009-interior-istana-kutai.txt",
        "2A-L010-interior-istana-tarumanagara.txt", "2A-L011-interior-istana-kantoli.txt",
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
    print(f"   K: 6 | L: 7 | A: 3 | S: 1")

if __name__ == "__main__":
    main()
