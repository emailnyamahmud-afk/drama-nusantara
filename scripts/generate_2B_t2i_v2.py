#!/usr/bin/env python3
"""Generate T2I prompts v2.1 untuk era 2B — Mataram-Sriwijaya (Abad 7-11 M)"""

import os

OUTPUT_DIR = "/home/z/my-project/produksi/master-reff-t2i-prompts/2B-mataram-sriwijaya/prompts"

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
    name="Sanjaya, founder of Mataram Kuno (Wangsa Sanjaya)",
    era_desc="8th century AD (732 AD), Central Java — founder of Hindu Siwa Mataram",
    phenotype="Male, 35-45 years old, Javanese phenotype with golden brown skin, sharp regal features, determined expression. Black hair in topknot (jata) with gold diadem. Muscular build from military campaigns. Skin marked by sun exposure.",
    costume="Wearing Hindu Siwa royal costume: gold makuta with crescent moon motif (Siwa), gold hara necklace with lingga pendant, gold keyura armlets, red-and-gold kemben, batik kain with parang pattern, keris at waist. Lencana: Trisula-mukha.",
    props="holding a trisula (trident of Siwa)",
    mood="Founder of Mataram — Sanjaya established lingga Siwa at Bukit Sthirengga (Gunung Wukir) in 732 AD, beginning the Hindu Siwa tradition of Mataram that would build Prambanan. A king who blended local Austronesian leadership with Hindu Siwa theology.",
)

K002 = k_prompt(
    name="Rakai Panangkaran (Wangsa Syailendra, Buddhist king)",
    era_desc="8th century AD (746 AD), Central Java — builder of Borobudur",
    phenotype="Male, 35-45 years old, Javanese phenotype with golden brown skin, serene expression with spiritual depth. Black hair in topknot. Lean build from religious devotion and royal duties.",
    costume="Wearing Buddhist royal costume: gold makuta with Dharma wheel motif, gold necklace with Buddha pendant, simple gold armlets, white-and-gold silk upper wrap, batik kain. Less martial than Sanjaya — Buddhist patron of arts and temple building.",
    props="holding a Buddhist prayer bead mala",
    mood="Builder of Borobudur — Rakai Panangkaran, 'Mustika Keluarga Sailendra', who converted from Hindu Siwa to Buddha Mahayana. His patronage initiated the greatest Buddhist monument in the southern hemisphere.",
    avoid_extra=", Hindu makuta with Siwa motifs, Islamic costume",
)

K003 = k_prompt(
    name="Balaputradewa, King of Sriwijaya",
    era_desc="9th century AD (860-900 AD), Sumatra — Sriwijaya at its peak",
    phenotype="Male, 40-50 years old, Sumatran Malay phenotype with medium brown skin, dignified features, calm scholarly expression. Black hair in simple topknot. Lean build from maritime and scholarly lifestyle.",
    costume="Wearing Sriwijaya royal attire: simple gold headband (not ornate makuta), gold chain with Buddhist pendant, silk jubah in deep blue, woven songket kain. Modest compared to Javanese kings — thalassocracy values scholarship and trade over display.",
    props="holding a palm-leaf Buddhist manuscript",
    mood="Scholar-king — Balaputradewa built the Monastery I at Nalanda (India) for Sriwijayan students. Under his rule, Sriwijaya became the center of Buddhist learning in Southeast Asia, attracting students from China and India.",
    avoid_extra=", Hindu royal costume, Javanese keraton costume, Islamic costume",
)

K004 = k_prompt(
    name="Rakai Pikatan (Wangsa Sanjaya, builder of Prambanan)",
    era_desc="9th century AD (856 AD), Central Java — unifier of two wangsa",
    phenotype="Male, 30-40 years old, Javanese phenotype with golden brown skin, sharp features, confident expression. Black hair in topknot. Athletic build — warrior-king who defeated the Syailendra.",
    costume="Wearing Hindu Siwa royal costume: gold makuta with Siwa motifs, gold hara necklace, gold armlets, red silk kemben, batik kain. Married to Pramodhawardhani (Syailendra princess) — symbol of two wangsa union.",
    props="holding a ceremonial mace",
    mood="Unifier — Rakai Pikatan married the Syailendra princess Pramodhawardhani, uniting Hindu Siwa and Buddhist Mahayana. He built Prambanan (Siwagrha, 856 AD) as the Hindu counterpart to Borobudur. Tolerance through parallelism, not syncretism.",
)

K005 = k_prompt(
    name="Pu Sindok, founder of Mataram East Java (Wangsa Isana)",
    era_desc="10th century AD (929-944 AD), East Java — mover of Mataram capital",
    phenotype="Male, 45-55 years old, Javanese phenotype with golden brown skin, wise weathered features, strategic expression. Black hair in topknot with some grey. Lean build from active governance.",
    costume="Wearing East Javanese royal attire: gold makuta, gold necklace with Wisnu pendant, gold armlets, dark red silk kemben, batik kain. Lencana: Garudamukha (continuing Airlangga's tradition).",
    props="holding a scroll (administrative decree)",
    mood="Visionary — Pu Sindok moved Mataram from Central to East Java after Merapi eruption, founding the Isana dynasty. His vision: use Bengawan Solo and Brantas rivers as trade arteries. Grandfather of Airlangga.",
)

K006 = k_prompt(
    name="Airlangga, King of Mataram East Java",
    era_desc="11th century AD (1019-1042 AD), East Java — restorer after Pralaya",
    phenotype="Male, 30-40 years old, Javanese phenotype with golden brown skin, regal features with weathered look from exile and war. Black hair in topknot, full beard. Muscular build from military campaigns.",
    costume="Wearing Hindu Wisnu royal costume: gold makuta with Garuda motif, gold hara necklace with Wisnu pendant, gold keyura armlets, red-gold kemben, batik kain with parang pattern, keris at waist. Lencana: Garudamukha — identifies with Wisnu as Cakravartin.",
    props="holding a Garudamukha scepter",
    mood="Restorer — Airlangga survived the Pralaya of 1016 (Wurawari's attack), spent 3 years in forest exile, then rebuilt Mataram. Called himself Wisnu-Cakravartin. Built Kambang Putih port. Patron of Kakawin Arjunawiwaha. Divided his kingdom into Janggala and Pangjalu before retiring as a monk.",
)


# ===== L PROMPTS — 7 latar =====

L001 = l_prompt(
    name="Borobudur (Mahayana Buddhist temple, Wangsa Syailendra)",
    era_desc="±780-825 AD, Kedu valley, Central Java — largest Buddhist monument in the world",
    scene_desc="Wide cinematic aerial view of Borobudur — massive stepped pyramid temple rising from the Kedu valley. Three levels visible: square Kamadhatu base, 5 square Rupadhatu terraces, 3 circular Arupadhatu terraces with stupas, and the central great stupa at peak. Andesite stone, weathered grey-brown. Relief panels visible on lower terraces. Surrounded by green rice paddies and distant volcanic mountains (Merapi, Sumbing, Sindoro). No people.",
    lighting_desc="warm 3500K golden sunrise from camera left (key light, long shadows revealing temple relief texture), cool 6500K sky fill from above. Aerial drone perspective from 200m. Morning mist in Kedu valley.",
    mood_desc="Mahakarya — Borobudur, the greatest Buddhist monument in the southern hemisphere. Built by the Syailendra dynasty over 45 years, it represents the Mandala of Vajrayana Buddhism — a mountain of stone that is also a path to enlightenment.",
)

L002 = l_prompt(
    name="Candi Prambanan / Siwagrha (Hindu Siwa temple)",
    era_desc="856 AD, Central Java — largest Hindu temple in Indonesia",
    scene_desc="Wide cinematic view of the Prambanan temple complex — three towering candi (Brahma, Siwa, Wisnu) rising above the Kedu plain. The central Siwa temple is 47 meters tall. Andesite stone with carved reliefs of Ramayana epic on inner walls. Surrounded by smaller perwara temples. Visible: sharp spires (ratna) against sky. Green rice paddies, distant volcanic mountains. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera right (key light, golden on temple spires), cool 6500K sky fill. Mid contrast 3:1. Temple shadows long.",
    mood_desc="Siwagrha — Prambanan, the Hindu answer to Buddhist Borobudur. Built by Rakai Pikatan in 856 AD as a statement that Hindu Siwa and Buddha Mahayana coexist in Mataram. The reliefs tell the Ramayana — Indian epic localized in Javanese stone.",
)

L003 = l_prompt(
    name="Ratu Boko / Abhayagirivihara (Buddhist hilltop complex)",
    era_desc="8th-9th century AD, Central Java — hilltop Buddhist monastery",
    scene_desc="Wide view of the Ratu Boko hilltop complex — ruins of a palace/monastery on a limestone hill overlooking Prambanan valley. Visible: stone pendopo (pavilion) foundations, bathing pools, gate structures (cremation gate), and Buddhist stupa bases. Limestone, weathered white-grey. The site where Sri Lankan Buddhist monks of Abhayagirivihara tradition resided. Distant view of Merapi and Prambanan temples. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, warm on limestone ruins), cool 6500K sky fill. Mid contrast 3:1. Distant haze over Prambanan plain.",
    mood_desc="Hill of the Dharma — Ratu Boko, where Buddhist monks from Sri Lanka studied and meditated, looking down at the Hindu temples of Prambanan below. A site of religious coexistence and international Buddhist scholarship.",
)

L004 = l_prompt(
    name="Palembang and Bukit Siguntang (Sriwijaya capital)",
    era_desc="7th-11th century AD, Sumatra Selatan — heart of Sriwijaya",
    scene_desc="Wide cinematic view of the Musi-Ogan river confluence at Palembang. Wooden stilt houses along riverbank. Trading boats (jong, kelulus) from India, Persia, and China at dock. Bukit Siguntang visible as sacred hill in background with prasasti siddhayatra. Wihara (Buddhist monastery) with golden stupa. Market stalls with gold, camphor, frankincense, agarwood. Tropical rainforest surrounding. No people.",
    lighting_desc="warm 4000K late morning sun from camera left (key light, golden on river and port), cool 6500K sky fill. Mid contrast 3:1. Sea haze.",
    mood_desc="Thalassocracy — Palembang, where river meets sea. The hub of Indian Ocean–South China Sea trade, where Buddhist learning, Malay language, and international commerce converged. Where Dapunta Hyang began the siddhayatra in 682 AD.",
)

L005 = l_prompt(
    name="Bengawan Solo-Brantas river valley (East Javanese Mataram trade route)",
    era_desc="10th-11th century AD, East Java — Pu Sindok's trade artery",
    scene_desc="Wide aerial view of the river valley between Bengawan Solo and Brantas rivers in East Java. Wide meandering rivers connecting interior to coast. Irrigated rice paddies along riverbanks. Raised wooden houses in scattered villages. Distant volcanic mountains (Penanggungan, Arjuno). The landscape Pu Sindok chose for his new capital at Tamwlang — strategic for both agriculture and trade. No people.",
    lighting_desc="warm 4000K morning sun from camera right (key light, warm on rivers and paddies), cool 6500K sky fill. Aerial drone perspective. Mid contrast 3:1. Morning mist in valley.",
    mood_desc="Visionary geography — the Bengawan Solo–Brantas valley that Pu Sindok chose as the new heart of Mataram. Two great rivers as trade arteries connecting agrarian interior to maritime coast. The foundation of East Java's future greatness.",
)

L006 = l_prompt(
    name="Barus / Lobu Tua (Tamil merchant settlement, West Sumatra)",
    era_desc="9th-11th century AD, Tapanuli Tengah, Sumatra Utara — international trade port",
    scene_desc="Wide view of the Barus coastal port at Lobu Tua. Natural harbor with merchant ships from Tamil Nadu, Persia, and Arabia. Wooden warehouse buildings on stilts. Tamil merchant quarter visible with small Hindu shrine. Camphor (kapur barus) processing area. The port where the Tamil inscription (1088 AD) records the 'Five Hundred of Ayyavole' merchant guild. Dense tropical forest behind. No people.",
    lighting_desc="warm 3500K late afternoon sun from camera left (key light, golden on harbor and forest), cool 6500K sky fill. Mid contrast 3:1. Sea breeze.",
    mood_desc="Cosmopolitan port — Barus, where Tamil, Arab, Persian, and Batak traders met. The source of the world's finest camphor, connecting deep interior Sumatra to the Indian Ocean trade network for over a thousand years.",
)

L007 = l_prompt(
    name="Panai / Padang Lawas (Vajrayana Buddhist temple complex, Sumatra)",
    era_desc="11th-14th century AD, Sumatra Utara — Tantrayana Buddhist site",
    scene_desc="Wide view of the Panai temple complex at Padang Lawas. Brick temples (Candi Bahal I, II, III) rising from tropical forest clearing. Simple brick structures with stupa-like superstructures. The site where Vajrayana Buddhism (Tantra Hevajra) flourished alongside Hindu and indigenous beliefs. River Barumun flowing past. Dense tropical forest surrounding. No people.",
    lighting_desc="warm 4000K afternoon sun from camera right (key light, revealing brick texture), cool 6500K sky fill. Mid contrast 3:1. Forest mist.",
    mood_desc="Tantric Buddhism in the forest — Panai, where Vajrayana Buddhism (Hevajra Tantra) coexisted with Hindu and indigenous beliefs. A unique religious landscape showing the diversity of pre-Islamic Sumatra.",
)


# ===== A PROMPTS — 3 artefak =====

A001 = a_prompt(
    name="Prasasti Kedukan Bukit (Sriwijaya founding inscription)",
    era_desc="682 AD (604 Saka), Palembang — oldest Sriwijaya inscription",
    scene_desc="A stone inscription (prasasti) on a small andesite stone. Visible: Pallawa Akhir script in Old Malay language, recording Dapunta Hyang's siddhayatra journey. The text begins 'Selamat tahun Saka 604...' The inscription is the founding document of Kedatuan Sriwijaya — the first written record of the word 'Sriwijaya'. Stone is weathered, approximately 30 cm tall.",
    lighting_desc="warm 3000K raking light from camera right (key light, revealing script), low ambient fill. High contrast 5:1.",
    mood_desc="Proklamasi — the Kedukan Bukit inscription, Sriwijaya's declaration of existence. The first time the name 'Sriwijaya' appears in history, recording Dapunta Hyang's sacred journey from Minanga to the Musi river mouth.",
)

A002 = a_prompt(
    name="Borobudur stupika and dharani (Vajrayana Buddhist ritual objects)",
    era_desc="8th-9th century AD, Central Java — tantric Buddhist artifacts",
    scene_desc="3-5 small ritual objects on dark surface: clay stupika (miniature stupa, 8 cm tall), gold dharani tablet (2 cm, with microscopic script), bronze vajra (ritual thunderbolt, 10 cm), and a clay relief fragment showing a Buddha image. These objects were deposited in Borobudur's stupas as ritual offerings. The dharani tablets contain protective mantras in Sanskrit. Gold tablet gleams, bronze vajra tarnished green-black.",
    lighting_desc="warm 2700K raking light from camera left (key light, revealing gold luster and bronze patina), low ambient fill. High contrast 4:1.",
    mood_desc="Ritual of enlightenment — the stupika and dharini of Borobudur, deposited in the stupas by Vajrayana Buddhists as acts of merit. Each tiny object is a prayer in material form, connecting the worshipper to the path of the Bodhisattva.",
)

A003 = a_prompt(
    name="Prasasti Nalanda (Sriwijaya-India diplomatic inscription)",
    era_desc="860 AD, Nalanda, India — Sriwijaya's diplomatic gift to India",
    scene_desc="A copper plate inscription (3 plates, joined by copper ring). Visible: Sanskrit script in Nagari letters, recording King Devapala of the Pala dynasty granting 5 villages to support a monastery built by Balaputradewa of Sriwijaya at Nalanda. The inscription proves Sriwijaya's international diplomatic status — a Southeast Asian king building a monastery in India. Approximately 25 cm per plate.",
    lighting_desc="warm 3000K raking light from camera left (key light, revealing copper patina and script), low ambient fill. High contrast 5:1.",
    mood_desc="International diplomacy — the Nalanda inscription, proof that Sriwijaya was a global power. King Balaputradewa built a monastery for his students at Nalanda, India's greatest Buddhist university. A Southeast Asian king endowing an Indian institution — diplomacy through religion.",
)


# ===== S PROMPTS — 1 kelompok =====

S001 = s_prompt(
    name="the two wangsa of Mataram: Sanjaya (Hindu Siwa) and Syailendra (Buddha)",
    era_desc="9th century AD, Central Java — parallel Hindu-Buddha kingdoms",
    composition="Group of 4 individuals in a natural standing group pose representing two traditions. Position 1 (far left): Rakai Pikatan (Hindu Siwa king), standing with trisula, wearing gold Siwa regalia. Position 2 (center-left): Pramodhawardhani (Syailendra Buddhist princess, wife of Pikatan), standing with Buddhist mala beads, wearing white-gold Buddhist attire. Position 3 (center-right): a Hindu Siwa priest (Brahmana), holding a ritual fire vessel, wearing white dhoti. Position 4 (far right): a Buddhist monk (Bhikkhu), holding palm-leaf manuscript, wearing saffron robe. The composition shows two wangsa standing together — parallelism, not conflict.",
    mood="Parallelism — Hindu and Buddha standing side by side in Mataram. Not syncretism, not conflict, but coexistence. Two wangsa, two religions, one kingdom. The foundation of Nusantara's religious tolerance.",
    k_refs=["2B-K004 (Rakai Pikatan)"],
    avoid_extra=", Islamic costume, conflict pose",
)


# ===== MAIN =====

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    prompts = {
        # K — 6
        "2B-K001-sanjaya.txt": K001,
        "2B-K002-rakai-panangkaran.txt": K002,
        "2B-K003-balaputradewa.txt": K003,
        "2B-K004-rakai-pikatan.txt": K004,
        "2B-K005-pu-sindok.txt": K005,
        "2B-K006-airlangga.txt": K006,
        # L — 7
        "2B-L001-borobudur.txt": L001,
        "2B-L002-prambanan.txt": L002,
        "2B-L003-ratu-boko.txt": L003,
        "2B-L004-palembang-sriwijaya.txt": L004,
        "2B-L005-bengawan-solo-brantas.txt": L005,
        "2B-L006-barus-lobu-tua.txt": L006,
        "2B-L007-panai-padang-lawas.txt": L007,
        # A — 3
        "2B-A001-prasasti-kedukan-bukit.txt": A001,
        "2B-A002-borobudur-stupika-dharani.txt": A002,
        "2B-A003-prasasti-nalanda.txt": A003,
        # S — 1
        "2B-S001-dua-wangsa-mataram.txt": S001,
    }

    # Delete ALL old v1 files (37 files)
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
