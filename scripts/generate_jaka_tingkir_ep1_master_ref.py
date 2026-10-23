#!/usr/bin/env python3
"""
Generate 12 master ref T2I prompt .txt baru untuk EP1 Jaka Tingkir.

Asset baru:
- 8 K (karakter): Raden Patah, Raden Yunus, Suryawiyata, Sunan Kudus, Sunan Giri Dalem, Hang Tuah, Prajurit Demak, Prajurit Portugis
- 4 A (artefak): Keris Kyai Naga Sasra, singgasana kayu Demak, mahkota sultan, bendera Surya Majapahit

Pola: era 3B Demak-Pajang (sesuai dengan master-era Jaka Tingkir).
Standar v2.1 (sama dengan yang sudah ada):
- K = 5-angle horizontal grid, clean cream studio
- A = macro 1:1 square
- Style keyword di awal: 'Cinematic realistic...'
"""

from pathlib import Path

OUT_DIR = Path("/home/z/my-project/produksi/master-reff-t2i-prompts/3B-demak-pajang/prompts")
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 8 KARAKTER (K-type, 5-angle horizontal grid)
# ============================================================

# 1. Raden Patah — Sultan Demak I, tua, jenggot putih
prompts = {}

prompts["3B-K007-raden-patah"] = """Cinematic realistic character reference sheet of Raden Patah (Panembahan Jiem-Boen / Sultan Syah Alam Akbar Jiem-Boen-ningrat I), founder of Demak Bintara Sultanate, late 15th-early 16th century (1478-1518 AD), East Java — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding the royal keris, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 60s to early 70s, weathered wise face with deep wrinkles around eyes and forehead, long flowing white beard reaching mid-chest, kind but authoritative dark brown eyes beneath thick white eyebrows. Bald crown with long white hair at sides flowing to shoulders. Wearing royal yellow silk robe with golden thread embroidery of Islamic calligraphy patterns, dark green sash across chest, white turban with golden crescent pin, dark sarung with batik parang pattern. Heavy gold necklace with Arabic inscriptions, gold ring on right index finger, holding a wooden staff with ivory handle. Bare feet in leather sandals. Calm, wise, kingly presence. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Founder of Demak Bintara — descendant of Brawijaya V (Majapahit) and Putri Cempa (Chinese Muslim), established first Islamic sultanate in Java 1478, ruled until death 1518.

Style: photorealistic skin texture with visible pores and age spots, white hair with individual strand detail, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, jewelry excessive beyond royal, military armor (he is sultan not warrior)."""


# 2. Raden Yunus — Sultan Demak II, muda, ambisius, gagah
prompts["3B-K008-raden-yunus"] = """Cinematic realistic character reference sheet of Raden Yunus (Adipati Yunus / Dipati Unus / Pangeran Sabrang Lor / Sultan Syah Alam Akbar Jiem-Boen-ningrat II), Sultan Demak II, early 16th century (ruled 1518-1521 AD), East Java — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a kris and wearing battle armor, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 30s to early 40s, athletic warrior build, sharp ambitious features, intense dark brown eyes that pierce forward, thick black beard trimmed short following Islamic fashion, mustache curled upward. Black hair cropped medium, hidden under dark green turban with silver pin. Olive-bronze skin tanned from sea campaigns. Wearing royal navy blue silk kebaya with golden embroidery of wave patterns (signifying naval ambition), dark green sash, dark batik sarung with megamendung pattern, leather arm bracers with brass studs. Gold necklace with single large emerald, gold earring in left ear. Kris Kyai Naga Sasra (dragon-shaped kris) tucked at waist. Bare feet in leather sandals. Confident, ambitious, slightly aggressive stance. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Prince who led failed naval attack on Malaka 1512 against Portuguese, got title Pangeran Sabrang Lor (Prince who crossed to the North). Sultan II 1518-1521, applied radical Islamic politics. Killed 1521 by remaining Majapahit loyalists (or by Keris Kyai Naga Sasra biting his back, per traditional tale).

Style: photorealistic skin texture with visible pores, individual beard hairs, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated."""


# 3. Raden Suryawiyata — Adipati Jipang, pro Putihan
prompts["3B-K009-raden-suryawiyata"] = """Cinematic realistic character reference sheet of Raden Suryawiyata (Pangeran Sekar Seda Lepen), Adipati Jipang Panolan, second son of Raden Patah, early 16th century (died 1521 AD), Central Java (Blora region) — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a kris, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 30s, lean ascetic build from religious practice, sharp angular face with high cheekbones, narrow suspicious dark eyes beneath thin arched eyebrows, thin black beard following orthodox Islamic style (neatly trimmed, no mustache curl), short black hair under white turban with subtle pattern. Pale olive skin from indoor study. Wearing white cotton robe (signifying Putihan orthodox Islam), dark gray sash, plain dark sarung without batik (anti-ornamentation), simple leather belt. Single silver ring, no other jewelry. Kris tucked at waist but hidden under robe. Bare feet in plain leather sandals. Stern, orthodox, judgmental expression. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Adipati of Jipang Panolan (Blora), orthodox pro-Putihan leader, rival to brother Pangeran Trenggana. Led failed rebellion after Trenggana became Sultan III. Murdered while praying Dzuhur at riverbank, became Pangeran Sekar Seda Lepen (Flower that Fell by the River).

Style: photorealistic skin texture with visible pores, individual beard hairs, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, ornate royal clothing, military armor."""


# 4. Sunan Kudus — Penasehat Agung, dendam
prompts["3B-K010-sunan-kudus"] = """Cinematic realistic character reference sheet of Sunan Kudus (Sunan Kudus / Ngingsun Kudus), Wali Songo member, Penasehat Agung Kesultanan Demak, early 16th century, Kudus, Central Java — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding prayer beads (tasbih), back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 60s, slightly stooped but dignified build, sharp angular face with deep-set eyes, piercing dark brown eyes beneath thick white eyebrows, full white beard trimmed short, white hair cropped short under white turban with black band. Dark olive skin weathered from years of religious study. Wearing pure white cotton robe (signifying Putihan orthodox Islam and his role as religious advisor), dark green sash with Arabic calligraphy, plain dark sarung, leather belt with silver buckle. Long silver prayer beads (tasbih) in right hand, going around neck multiple times. Silver ring with carved Arabic inscription. Bare feet in plain leather sandals. Stern, judgmental, calculating expression — but with underlying depth of wisdom. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. One of two most senior living Wali (with Sunan Kalijaga) in 1521. Penasehat Agung Demak (relinquished Senopati role to Fatahillah). Pro-Putihan, mentor of Raden Suryawiyata. Held grudge after Pangeran Prawata stole Keris Kyai Brongot Setan Kober from his wife. Adopted orphaned son of Suryawiyata — trained him as Arya Penangsang.

Style: photorealistic skin texture with visible pores and wrinkles, individual white beard hairs, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, ornate royal jewelry, military armor."""


# 5. Sunan Giri Dalem — Pimpinan Dewan Wali Sangha
prompts["3B-K011-sunan-giri-dalem"] = """Cinematic realistic character reference sheet of Sunan Giri Dalem, leader of Dewan Wali Sangha (Council of Saints) and Sultan of Giri, early 16th century (succeeded 1506 AD), Giri, East Java — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a book (kitab), back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 50s, medium dignified build, broad face with kind but authoritative features, warm dark brown eyes beneath medium white eyebrows, neatly trimmed white beard, white hair cropped short under green turban with golden crescent. Medium olive skin. Wearing green silk robe (color of Giri sultanate) with golden Arabic calligraphy embroidery, dark green sash, dark batik sarung with Giri-specific pattern, leather belt with brass buckle. Gold ring with carnelian stone, holding leather-bound kitab (Islamic book) in left hand. Bare feet in leather sandals. Calm, mediating, regal presence. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Son of Sunan Giri Kedhaton (died 1506), succeeded as Sultan of Giri. Head of Dewan Wali Sangha — presided over succession dispute between Raden Suryawiyata and Pangeran Trenggana after Raden Yunus died 1521. Eventually chose Trenggana after Sunan Kalijaga's lobbying.

Style: photorealistic skin texture with visible pores, individual white beard hairs, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, military armor (he is religious leader not warrior)."""


# 6. Hang Tuah — Laksamana Malaka, gugur 1511
prompts["3B-K012-hang-tuah"] = """Cinematic realistic character reference sheet of Hang Tuah, legendary Laksamana (Admiral) of Malaka Sultanate, late 15th-early 16th century (died 1511 AD), Malaka — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding the keris Taming Sari, back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 50s, athletic warrior build from decades of naval combat, broad weather-beaten face, calm determined dark brown eyes beneath thick black eyebrows, full black beard with hints of gray, long black hair tied back in warrior topknot. Dark bronze skin tanned from sea life. Wearing traditional Malay warrior attire — red silk baju with golden thread embroidery of waves, dark blue sarung with songket pattern, red sash across chest, leather arm bracers with brass studs. Gold ring on right hand. Keris Taming Sari (legendary invincible keris) tucked at waist. Bare feet in leather sandals. Calm, noble, dignified — warrior-poet presence. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Legendary admiral of Malaka, said to never lose a duel. Loyal to Sultan Mahmud Syah. Gugur (killed) in 1511 during Portuguese attack on Malaka led by Alfonso d'Albuquerque. Symbol of Malay heroism and Islamic resistance to European colonialism.

Style: photorealistic skin texture with visible pores and sea-weather, individual black beard hairs with gray strands, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, Javanese clothing (he is Malay not Javanese), excessive jewelry beyond warrior minimum."""


# 7. Prajurit Demak — Pasukan abad 16
prompts["3B-K013-prajurit-demak"] = """Cinematic realistic character reference sheet of a Prajurit Demak (Demak Bintara soldier), early 16th century (circa 1512 AD), Demak Bintara Sultanate, East Java — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a spear (tombak), back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 20s, athletic muscular build from military training, broad jawline, intense focused dark brown eyes, short black stubble beard (or clean-shaven following Islamic military fashion), short black hair hidden under dark red headwrap (destar). Medium olive-bronze skin. Wearing dark brown leather cuirass over white cotton tunic, dark green sash, dark batik sarung hitched up for combat mobility, leather belt with brass buckle. Arm guards of hardened leather. Kris tucked at waist, holding tombak (spear) with leaf-shaped bronze head and teak wood shaft. Bare feet in leather field sandals. Ready, alert, disciplined stance. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Common Demak soldier of early 16th century — combination of Javanese martial tradition and Islamic military fashion. Fought in Malaka 1512 and various campaigns.

Style: photorealistic skin texture with visible pores, individual stubble hairs, leather texture with wear, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, European armor, ornate royal costume (he is common soldier not noble)."""


# 8. Prajurit Portugis — Pasukan abad 16
prompts["3B-K014-prajurit-portugis"] = """Cinematic realistic character reference sheet of a Portuguese soldier (Soldado Português), early 16th century (circa 1511 AD), Age of Discovery, Malaka campaign — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a matchlock musket (espingarda), back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, late 20s, medium muscular build, weathered European face with strong jaw, determined gray-blue eyes, short brown beard trimmed European style, medium-length brown hair. Pale skin tanned and weathered from sea voyages. Wearing steel half-armor (cuirass with breastplate and backplate) over white cotton shirt with red cross of Order of Christ stitched on chest, dark red velvet trousers, leather belt with brass buckle. Steel morion helmet (cabasset style) on head. Matchlock musket (espingarda) in right hand, sword (espada) at left waist. Leather boots with spurs. Ready, disciplined European military stance. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Portuguese soldier of early 16th century Age of Discovery, served under Alfonso d'Albuquerque. Conquered Malaka 1511. Symbol of European Reconquista spirit reaching Southeast Asia.

Style: photorealistic skin texture with visible pores, individual beard hairs, steel armor with patina and reflection, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, Javanese/Asian clothing, ornate noble armor (he is common soldier not knight)."""


# ============================================================
# 4 ARTEFAK (A-type, macro 1:1 square)
# ============================================================

# 9. Keris Kyai Naga Sasra
prompts["3B-A004-keris-kyai-naga-sasra"] = """Cinematic realistic macro artifact reference of Keris Kyai Naga Sasra, a legendary pusaka (heirloom) kris of Demak Bintara sultanate, early 16th century, East Java — a wavy-bladed (luk 13) dagger forged from pamor iron with intricate dragon (naga) motifs along the blade. The blade shows damascene pamor patterns in silvery-gray against darker iron, with the head of a dragon (naga) carved in relief near the base (ganja). The hilt (dhuwung) is carved from dark buffalo horn in the form of a coiled naga with open mouth, eyes originally inlaid with rubies. The mendhak (hilt ring) is of beaten gold. The warangka (sheath) is carved from pelet wood with natural grain patterns, bound with gold. Displayed diagonally against a dark slate background for studio macro shot. Empty, no people.

Lighting: studio macro — 4200K soft key light from upper-left at 30 degrees highlighting the pamor pattern, gentle fill from right, dark neutral background. Even macro lighting to reveal blade texture and carving detail.

Mood: mystical, dangerous, royal heirloom. Legendary keris said to have "bitten" the back of Sultan Raden Yunus II causing his death in 1521 (per traditional tale). Symbol of supernatural power and fate.

Style: photorealistic macro photography, 100mm macro lens, f/8 deep depth of field for product detail, 8K hyperdetailed pamor pattern, color graded neutral with cool iron tones. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern packaging, plastic, branded items, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors, plain keris without dragon motifs."""

# 10. Singgasana kayu Demak
prompts["3B-A005-singgasana-demak"] = """Cinematic realistic macro artifact reference of the Singgasana Demak (royal wooden throne of Demak Bintara Sultanate), late 15th century (circa 1478 AD), Demak, East Java — a carved teak wood throne with high backrest featuring Islamic geometric patterns combined with Javanese floral motifs. The throne has a stepped base with three levels symbolizing the three pillars of Islam (Iman, Islam, Ihsan). Armrests carved as naga (dragon) heads. The seat cushion is of deep crimson velvet with gold thread embroidery of Arabic calligraphy reading "Allahu Akbar". The backrest is inlaid with mother-of-pearl (ratu mutiara) forming a sun pattern with rays. The wood is dark teak with deep patina from years of use. Displayed in studio against a dark neutral background. Empty, no people.

Lighting: studio macro — 4500K soft key light from upper-right at 45 degrees highlighting wood grain and carving detail, gentle fill from left, dark neutral background. Even macro lighting to reveal wood texture and mother-of-pearl inlay.

Mood: royal, sacred, ceremonial. Throne of Sultan Demak Bintara (Raden Patah and successors). Symbol of legitimate Islamic rule in Java.

Style: photorealistic macro photography, 100mm macro lens, f/11 deep depth of field for product detail, 8K hyperdetailed wood grain and carving, color graded neutral with warm wood tones. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern furniture, plastic, electric lights, glass, concrete, steel, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors."""

# 11. Mahkota sultan Demak
prompts["3B-A006-mahkota-sultan-demak"] = """Cinematic realistic macro artifact reference of the Mahkota Sultan Demak (royal crown of Demak Bintara Sultanate), late 15th-early 16th century, Demak, East Java — a crown (mahkota) of beaten gold with arabesque openwork pattern, set with precious stones. The crown has a curved dome shape with pointed top, decorated with seven points (representing the seven wali). Front center features a large emerald (zamrud) set in gold flower motif. Around the band, alternating rubies (merah delima) and pearls (mutiara). At the very top, a crescent moon (bulan sabit) of gold with small diamond (intan). The interior is lined with red velvet. Displayed on a dark wooden stand against a dark slate background for studio macro shot. Empty, no people.

Lighting: studio macro — 4500K soft key light from upper-right at 45 degrees highlighting gold and gem reflections, gentle fill from left, dark neutral background. Even macro lighting to reveal metalwork detail and gem brilliance.

Mood: royal, sacred, ceremonial. Crown of Sultan Demak Bintara, worn during coronation and major religious festivals. Symbol of legitimate Islamic rule.

Style: photorealistic macro photography, 100mm macro lens, f/8 deep depth of field for product detail, 8K hyperdetailed gold texture and gem facets, color graded neutral with warm gold tones. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern packaging, plastic, branded items, European crown, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors."""

# 12. Bendera Surya Majapahit
prompts["3B-A007-bendera-surya-majapahit"] = """Cinematic realistic macro artifact reference of the Bendera Surya Majapahit (Sun of Majapahit flag), a royal banner combining Majapahit Hindu-Buddhist sun symbol with Islamic additions, early 16th century, Demak Bintara — a rectangular flag of deep crimson silk with golden sun (Surya) motif in center, eight rays radiating outward with human, god, and animal figures at each ray tip (Surya Majapahit pattern). Around the sun, Arabic calligraphy in gold thread reads "Bismillahirrahmanirrahim" — symbolizing Demak's claim as legitimate successor to Majapahit. The flag has a fringe of golden tassels along the bottom edge. Mounted on a bamboo pole with a bronze crescent finial. Displayed draped against a dark slate background for studio macro shot. Empty, no people.

Lighting: studio macro — 4500K soft key light from upper-right at 45 degrees highlighting silk texture and golden embroidery, gentle fill from left, dark neutral background. Even macro lighting to reveal silk weave and thread detail.

Mood: royal, ancestral, syncretic. Banner of Demak Bintara combining Majapahit legacy with Islamic identity. Symbol of religious and political continuity. Used during naval campaign against Malaka 1512.

Style: photorealistic macro photography, 100mm macro lens, f/11 deep depth of field for product detail, 8K hyperdetailed silk weave and golden thread, color graded neutral with warm crimson tones. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern packaging, plastic, plain flag without sun motif, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors, modern national flag."""


# ============================================================
# WRITE ALL FILES
# ============================================================
for name, content in prompts.items():
    path = OUT_DIR / f"{name}.txt"
    path.write_text(content.strip() + "\n", encoding="utf-8")
    size_kb = path.stat().st_size / 1024
    print(f"✅ {path.name} ({size_kb:.1f} KB)")

print()
print("=" * 70)
print(f"Total prompts generated: {len(prompts)}")
print(f"  - 8 K karakter (5-angle horizontal): Raden Patah, Raden Yunus, Suryawiyata, Sunan Kudus, Sunan Giri Dalem, Hang Tuah, Prajurit Demak, Prajurit Portugis")
print(f"  - 4 A artefak (macro 1:1): Keris Kyai Naga Sasra, singgasana Demak, mahkota sultan, bendera Surya Majapahit")
print()
print(f"Location: {OUT_DIR}")
print()
print("Total file di era 3B sekarang:")
import os
files = sorted(os.listdir(OUT_DIR))
for f in files:
    print(f"  {f}")
print(f"Total: {len(files)} file")
