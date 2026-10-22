#!/usr/bin/env python3
"""
Generate Phase 3 master T2I prompts untuk aset prototype 30s yang belum ada:
- 2C-K007-dang-hyang-lohgawe.txt  (K-type, 5-angle horizontal)
- 2C-L008-hutan-tumapel.txt       (L-type, no-people 16:9)
- 2C-L009-pendopo-akuwu-tumapel.txt (L-type, no-people 16:9)
- 2C-A004-sekantung-beras.txt      (A-type, macro 1:1)
- 2C-A005-tombak-prajurit.txt      (A-type, macro 1:1)

Standar v2.1:
- K = single karakter, 5 angle horizontal grid, clean cream studio background
- L = master lokasi, NO people, cinematic realistic 16:9
- A = macro detail, 1:1 square
- Style keyword wajib di awal: 'Cinematic realistic...'
- Barkcloth wajib untuk juvenile (content filter Dola AI)
"""

from pathlib import Path

OUT_DIR = Path("/home/z/my-project/produksi/master-reff-t2i-prompts/2C-singasari-kediri/prompts")
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# C002 Dang Hyang Lohgawe — K-type (5-angle horizontal grid)
# ============================================================
K007_lohgawe = """Cinematic realistic character reference sheet of Dang Hyang Lohgawe, a South East Asian Brahmin ascetic in his early 60s, Hindu sage from India who traveled to 13th century East Java seeking the destined ruler — shown in 5 different angles arranged in a horizontal grid layout on a clean solid light cream studio background. Layout: left-to-right — frontal face close-up, full body front view, side face profile close-up, side full body view holding a carved wooden staff (danda), back full body view. All 5 angles show the exact same single character, same costume, same physical features, same identity. Male, early 60s, lean sinewy build from decades of ascetic practice. Sun-weathered tan skin, prominent cheekbones, sharp piercing dark brown eyes beneath thick graying eyebrows. Long iron-gray hair tied into a high traditional Brahmin topknot, flowing untrimmed white beard reaching his collarbone. Draped in a tattered off-white unbleached cotton robe wrapped across the left shoulder in traditional Brahmin style, paired with a matching loose dhoti-style wrap reaching his calves. Long rosary of carved dark brown rudraksha beads around his neck. Bare feet with worn leather thong sandals tied at the ankles. Calm, penetrating, spiritual presence. Clean studio background, no environment, no historical setting, no other characters.

Lighting: studio 5500K even key light from above-front, soft fill from left, low ambient. Even neutral lighting for character reference, no dramatic lighting.

Mood: neutral studio reference, character turnaround for production consistency. Revered sage who recognizes Ken Arok as the avatar of Vishnu destined for kingship — calm authority, piercing wisdom.

Style: photorealistic skin texture with visible pores and wrinkles, sun-damage texture, 35mm film grain, deep depth of field f/8, 50mm lens, 8K hyperdetailed, color graded neutral, production reference aesthetic. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: dramatic lighting, environment background, historical setting, multiple different characters, inconsistent costume between angles, modern clothing, anime style, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature, low resolution, blurry, oversaturated, jewelry, royal ornaments, ornate fabrics."""

(OUT_DIR / "2C-K007-dang-hyang-lohgawe.txt").write_text(K007_lohgawe, encoding="utf-8")
print("✅ 2C-K007-dang-hyang-lohgawe.txt")


# ============================================================
# L001 Hutan Tumapel — L-type (no-people 16:9)
# ============================================================
L008_hutan = """Cinematic realistic location reference of Hutan Tumapel, a sprawling tropical teak forest in 13th century East Java — NO people, NO characters, NO humans, empty location reference. Towering teak trees with dry peeling bark, dense canopy filtering harsh midday sun into sharp diagonal god rays cutting through mist. Tangled thorny undergrowth, ferns, vines, moss-covered fallen logs spanning across narrow dirt trails. Ground is dry sun-baked earth mixed with patches of damp mud, scattered with golden-brown teak leaves. Limestone boulders half-buried in undergrowth. A narrow winding footpath worn into the forest floor, suggesting frequent foot traffic. Distant misty forest layers creating depth. Wild, untamed, primal Javanese woodland at the height of dry season.

Lighting: harsh midday sun, ~5500K, strong directional god rays from upper-right at 45 degrees, high contrast with deep shadows in undergrowth, volumetric atmospheric haze. Raking light catching dust motes.

Mood: ancient, primal, foreboding yet sacred. A forest where bandits hide and sages appear. Setting for the legendary encounter between Ken Arok and Dang Hyang Lohgawe.

Style: photorealistic natural texture, 24mm wide-angle lens, deep depth of field f/11, hyperdetailed foliage, 8K, cinematic color grade warm earthy tones with golden god rays. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: people, humans, characters, figures, silhouettes, modern buildings, modern roads, vehicles, plastic-looking foliage, cartoon, anime, 3D render, oversaturated greens, watermark, text, low resolution, blurry."""

(OUT_DIR / "2C-L008-hutan-tumapel.txt").write_text(L008_hutan, encoding="utf-8")
print("✅ 2C-L008-hutan-tumapel.txt")


# ============================================================
# L002 Pendopo Akuwu Tumapel — L-type (no-people 16:9)
# ============================================================
L009_pendopo = """Cinematic realistic location reference of Pendopo Kediaman Akuwu Tumapel, the audience hall of the Akuwu (regent) of Tumapel in 13th century East Java — NO people, NO characters, NO humans, empty location reference. Cavernous open-sided pendopo with massive carved teakwood pillars supporting a steeply pitched ijuk (palm fiber) thatched roof. Polished hard-packed earth floor with intricate geometric stone carvings inset at the center. Raised dais at the far end with an ornate carved wooden throne inlaid with semiprecious stones. Stone steps leading up to the dais. Woven bamboo wall panels between pillars at the back. Bronze oil lamps and torches mounted on iron brackets along pillars. Decorative pendopo fabric banners in deep crimson and gold hanging between pillars. Sunlight streams through open sides creating dramatic shafts of light across the stone floor. Distant view of tropical garden through the open archways. Cavernous, hushed, oppressive atmosphere of a petty tyrant's court.

Lighting: mixed — warm 3200K torchlight from oil lamps on pillars, cool 5500K daylight streaming through open sides, high contrast between shadow and light. Volumetric god rays from side openings. Cinematic chiaroscuro.

Mood: oppressive grandeur, hushed anticipation, tyrant's domain. Setting where Ken Arok first sees Ken Dedes and is struck by the prophecy of her divine radiance.

Style: photorealistic architectural detail, 24mm wide-angle lens, deep depth of field f/11, 8K hyperdetailed wood grain and stone texture, cinematic color grade warm torchlight against cool daylight. Aspect ratio 16:9 horizontal. High detail, 4K, sharp focus.

Avoid: people, humans, characters, figures, silhouettes, modern furniture, electric lights, glass windows, concrete, steel, plastic, cartoon, anime, 3D render, watermark, text, low resolution, blurry."""

(OUT_DIR / "2C-L009-pendopo-akuwu-tumapel.txt").write_text(L009_pendopo, encoding="utf-8")
print("✅ 2C-L009-pendopo-akuwu-tumapel.txt")


# ============================================================
# P001 Sekantung Beras — A-type (macro 1:1)
# ============================================================
A004_beras = """Cinematic realistic macro artifact reference of a Sekantung Beras (small sack of unhusked rice) — a coarse loosely woven brown jute sack bound tightly around the bunched neck with frayed hemp twine, used as a prop in 13th century East Java. The sack is partially filled with raw unhulled rice grains, showing patchy dirt smears and a few loose white rice grains poking through strained seam punctures. The lower half is visibly plump and molded by the shifting bulk of small grain within. Natural wear, frayed threads at the binding, slight moisture stains. The sack rests on a dark slate surface for studio macro shot. Empty, no people.

Lighting: studio macro — 4000K soft key light from upper-left at 30 degrees, gentle fill from right, dark neutral background. Even macro lighting to reveal weave texture and grain detail.

Mood: utilitarian, humble, the loot of a thief. A coarse peasant's rice sack snatched by Ken Arok during his bandit days — symbol of his low origins before destiny elevated him.

Style: photorealistic macro photography, 100mm macro lens, f/8 deep depth of field for product detail, 8K hyperdetailed jute fiber weave, color graded neutral warm tones. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern packaging, plastic, branded sacks, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors."""

(OUT_DIR / "2C-A004-sekantung-beras.txt").write_text(A004_beras, encoding="utf-8")
print("✅ 2C-A004-sekantung-beras.txt")


# ============================================================
# P002 Tombak Prajurit — A-type (macro 1:1)
# ============================================================
A005_tombak = """Cinematic realistic macro artifact reference of a Tombak (traditional Javanese infantry spear) — an eight-foot shaft made from polished dark teak wood, capped with an elongated leaf-shaped bronze spearhead showing sharpened glinting bevels and oxidized green lowlights. A thick collar of braided brass wire and a short tuft of dyed red horsehair bind the socket tightly to the wood beneath the point. The wood shaft shows hand-rubbed patina and wear marks from years of campaign use. Iron ferrule at the base. Displayed diagonally against a dark slate background for studio macro shot. Empty, no people.

Lighting: studio macro — 4500K soft key light from upper-right at 45 degrees highlighting bronze spearhead edge and metal reflections, gentle fill from left, dark neutral background. Even macro lighting to reveal metal texture and wood grain.

Mood: weapon of authority, ceremonial yet functional. Carried by Tumapel palace guards pursuing Ken Arok through the forest — symbol of the oppressive order Ken Arok would one day overthrow.

Style: photorealistic macro photography, 100mm macro lens, f/8 deep depth of field for product detail, 8K hyperdetailed bronze patina and wood grain, color graded neutral with warm bronze highlights. Aspect ratio 1:1 square. High detail, 4K, sharp focus.

Avoid: people, hands, modern weapons, rifles, plastic, cartoon, anime, 3D render, watermark, text, low resolution, blurry, oversaturated colors."""

(OUT_DIR / "2C-A005-tombak-prajurit.txt").write_text(A005_tombak, encoding="utf-8")
print("✅ 2C-A005-tombak-prajurit.txt")


# ============================================================
# Summary
# ============================================================
print("\n=== SUMMARY ===")
print(f"5 new master ref prompts generated in:")
print(f"  {OUT_DIR}")
print(f"")
print(f"Files:")
for f in sorted(OUT_DIR.glob("2C-K007*")) + sorted(OUT_DIR.glob("2C-L008*")) + sorted(OUT_DIR.glob("2C-L009*")) + sorted(OUT_DIR.glob("2C-A004*")) + sorted(OUT_DIR.glob("2C-A005*")):
    print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")

print(f"\nTotal file di era 2C sekarang:")
import os
files = sorted(os.listdir(OUT_DIR))
print(f"  {len(files)} file prompt .txt")
for f in files:
    print(f"    {f}")
