#!/usr/bin/env python3
"""
Update storyboard-pilot.json dengan prompt skala imperial maritime.
Segmen yang diupdate:
- seg01 (opening Brantas): skala imperial river + dua dermaga besar
- seg02 (keraton exterior): kompleks istana imperial, bukan satu bangunan
- seg03 (close-up crown): dengan latar kompleks candi di belakang
- seg10 (royal boat): armada imperial, bukan perahu tunggal
- seg12 (Jenggala boat approaching): dengan armada, bukan satu perahu
- seg13 (Jenggala boat docking): armada Kediri docking
- seg25 (wedding ceremony): kompleks candi besar, bukan candi kecil
- seg29 (fire blazing): kompleks candi dengan banyak obor perunggu
- seg33 (sunrise over kingdom): kota imperial Dahanapura, bukan desa
"""

import json
from pathlib import Path

STORYBOARD_PATH = Path(
    "/home/z/my-project/produksi/panji/pre-produksi/storyboard-pilot.json"
)

# Mapping prompt lama → prompt baru dengan skala imperial
PROMPT_UPDATES = {
    # seg01: Brantas opening → imperial scale
    "Extreme wide shot, Sungai Brantas at dawn, 12th century East Java, misty river surface, mountains in background, golden sunrise light, banyan tree silhouette, cinematic establishing shot, 8K, hyperdetailed":
        "Extreme wide aerial shot, Brantas river at dawn, 12th century East Java, wide imperial river 300m, misty surface, two stone imperial docks facing each other (left blue-gold Jenggala, right red-gold Kediri), fleet of royal boats with gold carvings, mountains in background (Kelud Kawi Arjuno), banyan tree silhouette, Panji relief stones on riverbank, golden sunrise light, cinematic establishing shot, hyperdetailed, 8K",

    # seg02: Keraton exterior → imperial complex
    "Wide shot, Jenggala royal palace (Kahuripan) exterior at dawn, 12th century Javanese Hindu architecture, stone candi-style pillars, palm fiber roof, blue-gold royal banner on rooftop, torches, cinematic, 8K, hyperdetailed":
        "Aerial wide shot, 12th century Javanese Hindu imperial palace complex of Jenggala kingdom at Kahuripan, multi-building royal court with candi bentar split gate 8m tall, two giant dwarapala guardian statues, large stone ceremonial courtyard, main pendopo hall with 16 teak pillars blue-gold, three-tier tumpang sari roof with chandra-kapala finial, gold mesh curtains, 50 bronze torches, blue-gold royal banner on gate tower, background canal system with trading boats and distant small temples, cinematic, hyperdetailed, 8K",

    # seg03: close-up crown → with temple complex background
    "Close-up, golden Javanese royal crown (makuta) on stone pedestal, fire torch light reflection on gold, intricate temple motifs, 12th century, macro shot, 8K, hyperdetailed":
        "Close-up, golden Javanese royal destar (panji-crown) on carved stone pedestal, fire torch light reflection on gold, intricate temple motifs of chandra-kapala and kala-makara, 12th century, background shows palace hall with stone pillars and gold mesh curtains, macro shot, hyperdetailed, 8K",

    # seg10: royal boat → imperial fleet
    "Wide shot, Javanese royal boat on Brantas river at dawn, golden sunrise, mist, soldiers rowing, red-gold banner, 12th century, cinematic, 8K, hyperdetailed":
        "Wide shot, Javanese imperial fleet on Brantas river at dawn, 12th century, lead royal boat 20m long with gold carvings and small pendopo roof, escorted by 4-6 smaller perahu with blue-gold Jenggala banners, soldiers rowing in unison, golden sunrise, mist, mountains in background, cinematic, hyperdetailed, 8K",

    # seg12: Jenggala boat approaching → imperial fleet approaching
    "Wide shot, riverbank at dawn, wooden pier, mist, another royal boat approaching from distance, Jenggala banner blue-gold, 12th century, cinematic, 8K, hyperdetailed":
        "Wide shot, riverbank at dawn, large imperial stone dock with blue-gold Jenggala ornaments, mist, Kediri imperial fleet approaching from distance with 5 royal boats 20m long each, red-gold Kediri banners, escort perahu, mountains in background, 12th century, cinematic, hyperdetailed, 8K",

    # seg13: Jenggala boat docking → Kediri imperial fleet docking
    "Wide shot, Jenggala royal boat docking at wooden pier, blue-gold banner, Javanese soldiers, 12th century, misty dawn, cinematic, 8K, hyperdetailed":
        "Wide shot, Kediri imperial fleet docking at large stone dock with red-gold ornaments, 5 royal boats 20m long with gold carvings, red-gold Kediri banners, Javanese soldiers in formation, dayang with ceremonial parasols, misty dawn, 12th century, cinematic, hyperdetailed, 8K",

    # seg25: wedding ceremony wide → temple complex
    "Wide shot, Javanese Hindu wedding ceremony at temple courtyard, sacred fire altar, Kameswara (C001) and Kirana (C002) in ceremonial attire, priests, torches, stars, 12th century, cinematic, 8K, hyperdetailed":
        "Wide shot, Javanese Hindu wedding ceremony at large temple complex courtyard, 12th century, multi-temple complex with main 3-tier candi 15m tall featuring Panji story reliefs, 6-8 smaller supporting candi around, sacred fire altar 2m tall bronze carved, Panji (C001) and Candra Kirana (C002) in ceremonial attire, priests, 8 large bronze torches at corners, flag poles with two kingdom banners, statues of Kamajaya-Kamaratih at gateway, starry night sky, cinematic, hyperdetailed, 8K",

    # seg29: fire blazing → temple complex fire climax
    "Wide shot, temple fire blazing, sparks rising to stars, Kameswara and Kirana silhouettes against fire, ceremony, 12th century, cinematic, 8K, hyperdetailed":
        "Wide shot, temple complex fire blazing at climax of ceremony, sparks rising to stars, Panji and Candra Kirana silhouettes against massive sacred fire, 8 large bronze torches blazing around courtyard, multi-temple complex with Panji story reliefs, two kingdom banners (blue-gold Jenggala and red-gold Kediri) united above, ceremonial smoke, 12th century, cinematic, hyperdetailed, 8K",

    # seg31: overlooking kingdom → imperial city view
    "Wide shot, Kameswara (C001) and Kirana (C002) on palace balcony overlooking unified kingdom, dawn light, Kediri landscape, mountains, river, 12th century, cinematic, 8K, hyperdetailed":
        "Wide shot, Panji (C001) and Candra Kirana (C002) on palace balcony overlooking unified imperial kingdom at dawn, 12th century, massive Dahanapura imperial city with red brick walls 5m tall, four candi bentar split gates, multi-building palace complex, canal system from Brantas river, large marketplace outside palace walls, trading boats on canals with Chinese junks and Indian dhows, multi-ethnic traders, mountains and river in background, golden sunrise light, cinematic, hyperdetailed, 8K",

    # seg33: sunrise over kingdom → imperial city sunrise
    "Wide shot, sunrise over Kediri kingdom, palace, river, mountains, golden light, birds flying, 12th century, cinematic, 8K, hyperdetailed":
        "Extreme wide aerial shot, sunrise over unified imperial kingdom, 12th century East Java, massive Dahanapura imperial city with red brick walls 5m tall and four candi bentar split gates, multi-building palace complex, Siwa-Buddha main temple at city center, canal system from Brantas river, large marketplace, trading boats on canals including Chinese junks and Indian dhows, distant Hujung Galuh harbor with cosmopolitan ships, mountains (Kelud Kawi Arjuno) in background, golden sunrise light, birds flying, cinematic, hyperdetailed, 8K",
}


def main():
    print(f"Membaca: {STORYBOARD_PATH}")
    with open(STORYBOARD_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Backup
    backup_path = STORYBOARD_PATH.with_suffix(".json.bak2")
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Backup: {backup_path}")

    # Walk through acts → scenes → segments
    update_count = 0
    for act in data.get("acts", []):
        for scene in act.get("scenes", []):
            for seg in scene.get("segments", []):
                visual = seg.get("visual", {})
                old_prompt = visual.get("prompt", "")
                if old_prompt in PROMPT_UPDATES:
                    visual["prompt"] = PROMPT_UPDATES[old_prompt]
                    update_count += 1
                    print(f"  ✅ {seg['id']}: updated")

    # Write updated
    with open(STORYBOARD_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nTotal segmen diupdate: {update_count} / {len(PROMPT_UPDATES)}")
    print(f"Tulis: {STORYBOARD_PATH}")

    # Verify JSON valid
    with open(STORYBOARD_PATH, "r", encoding="utf-8") as f:
        verify = json.load(f)
    print(f"✅ JSON valid — {verify['render_status']['total_segments']} segmen")


if __name__ == "__main__":
    main()
