#!/usr/bin/env python3
"""
Generate detailed room-by-room T2I prompts for:
1. Istana Mataram Kuno (Sindoro-Sumbing)
2. Istana Kedatuan Sriwijaya (Palembang)

Setiap ruang punya prompt terpisah dengan detail spesifik.
"""

from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts/2B-mataram-sriwijaya/prompts")
BASE.mkdir(parents=True, exist_ok=True)

TEMPLATE = """Cinematic realistic documentary {view_type} of {name}, {location}, {period}. {details}

Setting: {setting}

Lighting: {lighting}

Mood: {mood}

Style: {style} Aspect ratio 9:16 portrait. High detail, 4K, sharp focus.

Avoid: {avoid}"""

# ========================================
# MATARAM KUNO - RUANG-RUANG ISTANA (13 ruang)
# Lokasi: Between Mount Sindoro (3,136m) and Mount Sumbing (3,371m), Jawa Tengah
# Periode: Abad 8-9 Masehi (era Sanjaya-Syailendra)
# Skala: Hundreds of hectares complex
# ========================================

MATARAM_ROOMS = {
    "2B-L011-pendopo-agung.txt": {
        "view_type": "interior wide shot",
        "name": "Pendopo Agung (Great Audience Hall) of Mataram Kuno royal palace",
        "location": "between Mount Sindoro and Mount Sumbing, Jawa Tengah",
        "period": "abad 8-9 Masehi",
        "details": "Vast hall 50m x 30m with 36 carved teak pillars painted red-gold, each 10m tall, rising to peaked ceiling 20m high with palm fiber (ijuk) roof and golden chandra-kapala ornament. At far end, elevated golden throne (singgasana) on 7-step stone platform, royal parasol with 5 tiers. Hall can hold 500 people. Floor of polished hardwood with woven rattan mats. Golden ceremonial vessels, incense burners. Hindu priests in white-yellow (left) and Buddhist monks in orange (right) — coexistence. Royal guards with spears lining walls. Patih presenting scroll. View through 8m tall carved wooden windows to Mount Sindoro.",
        "setting": "Main audience hall of royal palace complex spanning hundreds of hectares between Sindoro and Sumbing. Where the king received foreign envoys, held court, and governed Mataram Kuno. Dual-faith (Hindu Siwa + Buddhist Mahayana).",
        "lighting": "warm 2700K sacred firelight from camera left (key light, dancing on throne and pillars), cool 5500K daylight from windows right (view to Sindoro). High contrast 4:1. Incense smoke.",
        "mood": "vast hall of dual faith — where the king held court for hundreds of subjects, where Hindu and Buddhist priests stood side by side, the political heart of a kingdom spanning hundreds of hectares.",
        "style": "photorealistic wood, gold, stone, and fire textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent for expansive interior, 8K hyperdetailed, color graded warm fire-gold highlights cool blue shadows.",
        "avoid": "modern furniture, modern lighting, stone candi interior (must be vast wooden pendopo), small room (must be 50x30m hall), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room, single-faith only."
    },
    "2B-L012-dalem-agung.txt": {
        "view_type": "interior",
        "name": "Dalem Agung (Royal Private Residence) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Private royal quarters — lavish but intimate. Wooden walls with carved Ramayana reliefs, teak floor with woven rattan mats, golden oil lamps. Royal bed (4m x 3m) with silk and batik textiles, golden headboard with Garuda motif. Dressing area with golden mirror (bronze polished), jewelry boxes with gold ornaments, kris collection on wall rack. Private altar with Shiva lingga and Buddha rupa side by side. Small courtyard with lotus pond visible through carved screen. Women servants (dayang) attending. View to Mount Sumbing through lattice window.",
        "setting": "Private residence of the king and queen within the hundreds-of-hectares palace complex. Where the royal family lived, dressed, slept, and prayed privately.",
        "lighting": "warm 2700K oil lamp light from multiple points (key light, intimate golden glow), cool 5500K daylight from courtyard window. Low contrast 2:1 for intimate atmosphere.",
        "mood": "private royal life — where the king and queen lived away from public eye, surrounded by luxury, faith, and the beauty of twin volcanoes.",
        "style": "photorealistic wood, gold, silk, batik, and bronze textures, 35mm film grain, shallow depth of field f/2.8, 35mm lens equivalent, 8K hyperdetailed, color graded warm golden highlights soft amber shadows.",
        "avoid": "modern furniture, modern bedroom, modern lighting, modern mirror, stone candi interior, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, public hall (must be private residence)."
    },
    "2B-L013-pringgitan.txt": {
        "view_type": "interior",
        "name": "Pringgitan (Ceremonial Performance Platform) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Elevated wooden platform 20m x 15m, open-air with carved teak pillars supporting peaked ijuk roof. Used for wayang (shadow puppet) performances, gamelan concerts, and royal ceremonies. Stage with white screen (kelir) for wayang, bronze gamelan instruments (bonang, saron, gender, kendang) arranged on platform. Royal family seated on elevated platform opposite stage. Courtiers and dignitaries seated on lower level. Torches illuminating stage. View to both Mount Sindoro and Mount Sumbing from open sides.",
        "setting": "Ceremonial platform within the palace complex where performing arts, religious ceremonies, and royal celebrations took place. Where gamelan and wayang flourished under royal patronage.",
        "lighting": "warm 2200K torchlight from multiple points around platform (key light, dramatic for performance), cool 6500K moonlight from open sides. High contrast 5:1 for theatrical atmosphere.",
        "mood": "performing arts court — where gamelan resonated between two volcanoes, where wayang told stories of gods and kings, where ceremonies bonded the kingdom together.",
        "style": "photorealistic wood, bronze (gamelan), textile, and fire textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm fire-orange highlights cool blue-black shadows.",
        "avoid": "modern stage, modern lighting, modern instruments, modern theater, stone candi, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, closed room (must be open-air platform)."
    },
    "2B-L014-gadri.txt": {
        "view_type": "interior",
        "name": "Gadri (Royal Archive and Library) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbling",
        "period": "abad 8-9 Masehi",
        "details": "Room 15m x 10m with floor-to-ceiling wooden shelves containing hundreds of lontar (palm leaf manuscripts) and parcaman (paper manuscripts). Scripts in Sanskrit, Jawa Kuno, Kawi aksara. Wooden reading desks with oil lamps. Mpu (royal poets/scholars) working on kakawin (poems). Scribes copying texts. Gold-leafed book covers. Categories: Weda, Sastra, Prasasti copies, Astronomi, Ayurweda (medicine). Stone tablets with prasasti copies displayed on wall. View to gardens with Mount Sindoro background.",
        "setting": "Royal archive within the palace complex — the intellectual center where knowledge was preserved, copied, and created. Where Mpu Sedah, Mpu Panuluh, and other poets would later create Bharatayuddha, Smaradahana, Hariwangsa.",
        "lighting": "warm 2700K oil lamp light from desks (key light, scholarly golden glow), cool 5500K daylight from window. Mid contrast 3:1. Dust particles in light beams.",
        "mood": "repository of knowledge — where lontar manuscripts preserved the wisdom of the kingdom, where Mpu scholars wrote kakawin that would echo through centuries.",
        "style": "photorealistic wood, palm leaf (lontar), gold, and textile textures, 35mm film grain, deep depth of field f/5.6, 35mm lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows.",
        "avoid": "modern books, modern library, modern lighting, modern shelves, paper books (must be lontar palm leaf), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room."
    },
    "2B-L015-kaputren.txt": {
        "view_type": "interior",
        "name": "Kaputren (Royal Women's Quarters) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Beautifully decorated private quarters for royal women — queen, princesses, concubines. Inner courtyard with bathing pool (kolam pemandian) 10m x 5m, dragon-head water spouts carved from stone. Surrounding rooms with carved wooden screens (gebyok) depicting floral and bird motifs. Women's quarters with looms for weaving batik, dressing tables with gold cosmetics boxes, jewelry. Dayang (female attendants) preparing flowers, making offerings, weaving. Queen's private chamber with silk curtains, golden Buddha and Dewi Tara statues (Buddhist influence). Garden with jasmine, melati, kenanga. View to Mount Sumbing.",
        "setting": "Women's quarters within the palace complex — where the queen and princesses lived, where batik was woven, where offerings were prepared, where women held their own court.",
        "lighting": "soft warm 3500K daylight from courtyard (key light, gentle on water and flowers), cool 6500K sky fill. Low contrast 2:1 for feminine atmosphere. Water reflections.",
        "mood": "inner court of women — where beauty, craft, and devotion met, where the queen held her own power, where batik and offerings were created.",
        "style": "photorealistic wood, water, stone, silk, and flower textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm soft golden highlights cool blue-green shadows.",
        "avoid": "modern buildings, modern bathroom, modern furniture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, male figures (must be women's quarters), modern pool."
    },
    "2B-L016-siti-hinggil.txt": {
        "view_type": "exterior wide shot",
        "name": "Siti Hinggil (Elevated Ceremonial Platform) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Stone platform 30m x 30m, elevated 3 meters above ground, accessed by 7 steps on each side. Used for coronation, royal address to thousands of subjects, and great religious ceremonies. Stone paras (pillars) at corners with carved kala-makara. Golden parasol at center. Royal banner. Open-air, view to entire palace complex (hundreds of hectares) and both Mount Sindoro and Mount Sumbing. Thousands of subjects gathered below during ceremony. Stone prasasti mounted on platform.",
        "setting": "Elevated ceremonial platform — the highest point in the palace complex where the king addressed his people, where coronations took place, where the kingdom's power was displayed.",
        "lighting": "warm 3500K golden hour sun from camera right (key light, dramatic on stone platform and twin volcanoes), cool 6500K sky fill. Mid contrast 3:1. Long shadows.",
        "mood": "elevated power — where the king stood above his people, between two sacred volcanoes, where thousands gathered to hear royal decrees.",
        "style": "photorealistic stone, gold, and tropical landscape textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern platform, modern stairs, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small platform (must be 30x30m elevated), narrow view (must show vast complex and twin volcanoes)."
    },
    "2B-L017-mandalasana.txt": {
        "view_type": "interior",
        "name": "Mandalasana (Royal Meditation Hall) of Mataram Kuno",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Sacred meditation hall 15m x 10m, dimly lit, with stone floor and carved walls depicting mandala cosmology. Central stone altar with Shiva lingga (Hindu) and Buddha rupa (Buddhist) side by side — dual faith. Mpu (priests) in meditation on stone seats around perimeter. Bronze incense burners, oil lamps. Wall paintings of Mount Meru (cosmic mountain). Private entrance from royal quarters. View through small window to Mount Sindoro peak. Sacred fire (Agni) in bronze brazier.",
        "setting": "Royal meditation hall — where the king and royal family meditated, where Hindu and Buddhist priests performed rituals, where spiritual power legitimized political power.",
        "lighting": "warm 1800K firelight from sacred brazier (key light, intense orange on altar and priests), low ambient 300K. Extreme high contrast 6:1 for sacred atmosphere. Incense smoke catching light.",
        "mood": "sacred stillness — where king and priest sought spiritual power, where Hindu Siwa and Buddhist Mahayana met in stone and fire, where the kingdom's soul resided.",
        "style": "photorealistic stone, fire, gold, and textile textures, 35mm film grain, shallow depth of field f/2.0, 35mm lens equivalent, 8K hyperdetailed, color graded warm fire-orange highlights dark blue-black shadows.",
        "avoid": "modern room, modern lighting, modern meditation hall, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, bright room (must be dim sacred hall), single-faith (must show Hindu + Buddhist coexistence)."
    },
    "2B-L018-wihara-istana.txt": {
        "view_type": "exterior wide shot",
        "name": "Wihara Utama (Royal Buddhist Monastery) within Mataram Kuno palace",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi (era Syailendra)",
        "details": "Buddhist monastery complex within the royal palace grounds. Stone and wooden buildings: main wihara (prayer hall) with stupa at peak, monks' cells (8 rooms), library with Sanskrit lontar, meditation garden with bodhi tree. Golden Buddha statue 4m tall in main hall. Buddhist monks in orange robes. Stone pathways connecting buildings. View to Mount Sindoro. Part of the hundreds-of-hectares palace complex. Coexists with Hindu pura (temple).",
        "setting": "Royal Buddhist monastery within the palace complex — where Syailendra patronage supported Buddhist scholarship, where monks from Sri Lanka and India came to study, where the Buddhist counterpart to Hindu Sanjaya flourished.",
        "lighting": "warm 4000K morning sun from camera right (key light, golden on stupa and monastery), cool 6500K sky fill. Mid contrast 3:1. Mist from morning dew.",
        "mood": "Buddhist sanctuary — where monks chanted between two volcanoes, where Sanskrit sutras were studied, where peace complemented power.",
        "style": "photorealistic stone, wood, gold, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "modern buildings, modern monastery, Hindu temple as main structure (must be Buddhist wihara), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single building (must be complex of multiple buildings)."
    },
    "2B-L019-pura-siwa-istana.txt": {
        "view_type": "exterior wide shot",
        "name": "Pura Siwa (Royal Hindu Temple) within Mataram Kuno palace",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi (era Sanjaya)",
        "details": "Hindu Siwa temple complex within the royal palace grounds. Stone and wooden structures: main pura (temple) with lingga-yoni at center, priest quarters (4 rooms), sacred fire hall (Agni), offering kitchen. Golden Nandi (bull) statue guarding entrance. Hindu priests in white-yellow robes preparing offerings. Stone pathways. View to Mount Sumbing. Part of the hundreds-of-hectares palace complex. Coexists with Buddhist wihara.",
        "setting": "Royal Hindu temple within the palace complex — where Sanjaya patronage supported Hindu Siwa worship, where Vedic rituals were performed, where the Hindu counterpart to Buddhist Syailendra flourished.",
        "lighting": "warm 3500K afternoon sun from camera left (key light, golden on stone temple and Nandi statue), cool 6500K sky fill. Mid contrast 3:1. Smoke from sacred fire.",
        "mood": "Hindu sanctuary — where Vedic fire rituals honored Agni between two volcanoes, where Shiva lingga stood as symbol of royal power, where dharma met kingship.",
        "style": "photorealistic stone, wood, gold, and fire textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "modern buildings, modern temple, Buddhist temple as main structure (must be Hindu Siwa pura), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single building (must be complex of multiple buildings)."
    },
    "2B-L020-pasar-kerajaan.txt": {
        "view_type": "exterior wide shot",
        "name": "Pasar Kerajaan (Royal Market) within Mataram Kuno palace complex",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Bustling market within palace grounds, covering 2 hectares. Stalls with bamboo and thatch roofs selling: rice, vegetables, fruits, spices, textiles (batik, kain), gold ornaments, bronze tools, pottery, weapons (kris, swords), cattle, horses. Foreign merchants (Indian, Chinese, Khmer) trading silk, beads, bronze mirrors. Local farmers bringing produce. Royal tax collectors at gate. Hundreds of people. Goods from across Nusantara: Sumatran gold, Maluku spices, Kalimantan timber. View to sawah (rice fields) and Mount Sindoro.",
        "setting": "Royal market within the palace complex — economic heart of the kingdom, where trade from across Nusantara and beyond converged, where the kingdom's wealth was visible in goods and people.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on market stalls and goods), cool 6500K sky fill. Mid contrast 3:1. Dust and smoke from cooking.",
        "mood": "commercial heart — where the wealth of the kingdom flowed, where foreign and local merchants met, where hundreds of hectares of royal domain found its economic expression.",
        "style": "photorealistic bamboo, thatch, textile, food, and metal textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern market, modern buildings, modern shops, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small market (must be 2 hectares with hundreds of people)."
    },
    "2B-L021-bengkel-kerajinan.txt": {
        "view_type": "exterior wide shot",
        "name": "Bengkel Kerajinan (Royal Craft Workshops) within Mataram Kuno palace",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Craft workshops covering 1 hectare within palace grounds. Multiple workshops: bronze casting (undagi making kris, arca, nekara), goldsmithing (jewelry, makuta ornaments), wood carving (candi components, furniture), textile weaving (batik, kain), pottery (gerabah, tempayan). Smoke from bronze furnaces, hammering sounds. Craftsmen working in open-air workshops. Finished goods displayed. Raw materials: copper, gold, timber, cotton. View to Mount Sumbing. Part of hundreds-of-hectares complex.",
        "setting": "Royal craft workshops — where the kingdom's artisans produced the objects of power, faith, and beauty: kris, arca, jewelry, textiles, pottery. Where undagi (master craftsmen) trained apprentices.",
        "lighting": "warm 3500K afternoon sun from camera right (key light, golden on bronze furnaces and craftsmen), cool 6500K sky fill. Mid contrast 3:1. Smoke from furnaces, sparks.",
        "mood": "creative industry — where molten bronze became arca and kris, where batik was born, where the kingdom's material culture was created by skilled hands.",
        "style": "photorealistic bronze, gold, wood, textile, and fire textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "modern factory, modern workshop, modern tools, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single craft (must show multiple workshops)."
    },
    "2B-L022-kandang-kerajaan.txt": {
        "view_type": "exterior wide shot",
        "name": "Kandang Kerajaan (Royal Stables) within Mataram Kuno palace",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Royal stables covering 1 hectare. Horses (imported from India/Persia, for royal use and cavalry), elephants (for ceremonial and war), cattle (for agriculture and sacrifice). Wooden stable buildings with thatch roofs, stone watering troughs. Stable hands (kusir) tending animals. Royal chariots and carts stored. Feed storage (padi, rumput). View to sawah and Mount Sindoro. Part of hundreds-of-hectares complex.",
        "setting": "Royal stables — where the kingdom's animals were kept, where cavalry horses were bred, where ceremonial elephants were housed, where agriculture was supported by cattle.",
        "lighting": "warm 4000K morning sun from camera left (key light, golden on animals and stables), cool 6500K sky fill. Mid contrast 3:1. Dust from animals.",
        "mood": "kingdom's strength — where horses for cavalry, elephants for ceremony, and cattle for agriculture were kept, the living power of the realm.",
        "style": "photorealistic wood, thatch, animal, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "modern stable, modern buildings, modern vehicles, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, modern farm equipment."
    },
    "2B-L023-taman-kerajaan.txt": {
        "view_type": "exterior wide shot",
        "name": "Taman Kerajaan (Royal Gardens) within Mataram Kuno palace",
        "location": "within royal palace complex, between Sindoro and Sumbing",
        "period": "abad 8-9 Masehi",
        "details": "Royal pleasure gardens covering 5 hectares. Lotus ponds (3 large, each 30m x 20m) with blooming lotus, fish, and ducks. Stone pathways winding through gardens with jasmine, melati, kenanga, kamboja, frangipani trees. Pavilion (bangsal) for relaxation with view to both Mount Sindoro and Mount Sumbing. Royal bathing pool with dragon-head spouts. Artificial island with small shrine. Peacocks and deer roaming. Fruit trees (mangga, rambutan, durian). Bridges over ponds. Gardeners tending plants.",
        "setting": "Royal gardens — where the royal family relaxed, where beauty was cultivated, where nature and artifice met between two sacred volcanoes.",
        "lighting": "soft warm 4000K morning sun through tree canopy (key light, dappled on ponds and flowers), cool 6500K sky fill. Low contrast 2:1 for serene atmosphere. Mist on ponds.",
        "mood": "royal paradise — where lotus bloomed between Sindoro and Sumbing, where the king walked in contemplation, where beauty was a form of power.",
        "style": "photorealistic water, stone, flower, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm green-golden highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern park, modern garden, modern buildings, modern pool, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small garden (must be 5 hectares)."
    },
}

# ========================================
# KEDATUAN SRIWIJAYA - RUANG-RUANG ISTANA (8 ruang)
# Lokasi: Palembang, pertemuan Sungai Musi-Ogan, Bukit Siguntang
# Periode: Abad 7-11 Masehi
# ========================================

SRIWIJAYA_ROOMS = {
    "2B-L024-pendopo-kedatuan.txt": {
        "view_type": "interior wide shot",
        "name": "Pendopo Kedatuan (Audience Hall) of Kedatuan Sriwijaya",
        "location": "Palembang, Sumatra Selatan, at the confluence of Musi and Ogan rivers",
        "period": "abad 8-9 Masehi (era Balaputradewa)",
        "details": "Vast hall 40m x 25m with 30 carved wooden pillars, open-air with peaked ijuk roof 18m high, golden stupa ornament at peak. At far end, elevated golden throne (singgasana) with Buddhist motifs, royal parasol with 7 tiers. Hall overlooking Sungai Musi — foreign merchants (Indian, Chinese, Persian) presenting gifts (gold dust, camphor, silk, beads). Royal treasurer weighing gold dust. Buddhist monks in orange robes flanking throne. Datu (subordinate kings) seated on lower level paying tribute. Floor of polished hardwood with woven rattan. View through open sides to river and Bukit Siguntang.",
        "setting": "Main audience hall of Kedatuan Sriwijaya — where the Datu (supreme king) received foreign merchants, taxed the wealth of Asia, and governed the thalassocracy. At Palembang, confluence of Musi and Ogan, near sacred Bukit Siguntang.",
        "lighting": "warm 4000K daylight from open sides (key light, river breeze, golden on throne and merchants), cool 6500K sky fill from above. Mid contrast 3:1. River mist.",
        "mood": "court of commerce and dharma — where a Datu ruled the Indian Ocean trade network, where foreign merchants brought gold and camphor, where Buddhist scholarship and maritime commerce met.",
        "style": "photorealistic wood, gold, silk, water, and textile textures, 35mm film grain, deep depth of field f/5.6, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern furniture, modern lighting, modern buildings, stone candi interior (must be wooden pendopo), small room (must be 40x25m hall), Majapahit architecture, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room."
    },
    "2B-L025-wihara-sriwijaya.txt": {
        "view_type": "exterior wide shot",
        "name": "Wihara Utama Sriwijaya (Main Buddhist Monastery)",
        "location": "Palembang, near Bukit Siguntang",
        "period": "abad 8-9 Masehi",
        "details": "Grand Buddhist monastery complex covering 3 hectares. Main wihara (prayer hall) with golden stupa 15m tall. Library (skriptoria) with hundreds of Sanskrit and Melayu Kuno lontar. Monks' cells (12 rooms). Meditation garden with bodhi tree. University area where international scholars (Yijing from China, Syakyakirti) studied. Bronze Buddha statues, stone stupas, prayer wheels. Buddhist monks from India, China, Srivijaya in orange and yellow robes. View to Bukit Siguntang and Sungai Musi. Part of kedatuan complex.",
        "setting": "Main Buddhist monastery of Sriwijaya — the intellectual center of Southeast Asia, where Yijing studied (671 M), where Atisa learned from Dharmakirti Serlingpa, where Mulasarvastivada tradition flourished.",
        "lighting": "warm 4000K morning sun from camera right (key light, golden on stupa and monastery), cool 6500K sky fill. Mid contrast 3:1. Morning mist.",
        "mood": "university of Buddhism — where monks from India, China, and Nusantara studied together, where Sanskrit and Melayu Kuno were taught, where Sriwijaya's intellectual legacy was forged.",
        "style": "photorealistic stone, wood, gold, and tropical foliage textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm amber highlights cool blue shadows.",
        "avoid": "modern buildings, modern university, modern monastery, Hindu temple as main (must be Buddhist), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, single building (must be complex)."
    },
    "2B-L026-skriptoria-sriwijaya.txt": {
        "view_type": "interior",
        "name": "Skriptoria (Royal Library and Scriptorium) of Sriwijaya",
        "location": "within Wihara complex, Palembang",
        "period": "abad 8-9 Masehi",
        "details": "Room 20m x 12m with wooden shelves containing hundreds of lontar manuscripts in Sanskrit, Melayu Kuno, and Chinese. Categories: Buddhist sutras (Mulasarvastivada), grammar (sabdawidya), medicine, astronomy, trade records. Scribes copying texts at wooden desks with oil lamps. Foreign scholars (Chinese, Indian) studying. Gold-leafed book covers. Stone Buddha statue at entrance. View to monastery garden. Center of Buddhist learning in Southeast Asia — where Yijing studied sabdawidya (671 M).",
        "setting": "Royal library and scriptorium — the intellectual heart of Sriwijaya, where Buddhist texts were preserved, copied, and disseminated, where international scholars came to study.",
        "lighting": "warm 2700K oil lamp light from desks (key light, scholarly golden glow), cool 5500K daylight from window. Mid contrast 3:1. Dust particles in light beams.",
        "mood": "repository of wisdom — where lontar preserved the Dharma, where Yijing studied grammar and sutra, where Sriwijaya's reputation as a center of learning was built.",
        "style": "photorealistic wood, palm leaf (lontar), gold, and textile textures, 35mm film grain, deep depth of field f/5.6, 35mm lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows.",
        "avoid": "modern books, modern library, modern lighting, modern shelves, paper books (must be lontar palm leaf), anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, empty room."
    },
    "2B-L027-dock-kerajaan.txt": {
        "view_type": "exterior wide shot",
        "name": "Dermaga Kerajaan (Royal Dock) of Kedatuan Sriwijaya",
        "location": "Sungai Musi, Palembang",
        "period": "abad 8-9 Masehi",
        "details": "Royal dock extending 200m into Sungai Musi. Stone and wooden quay. Multiple berths for: royal perahu (warships with 50 rowers), merchant ships from India (with Indian traders), Persia (with Persian merchants), China (Tang dynasty ships with silk and porcelain), Sumatran perahu (with gold, camphor, agarwood). Customs house (pabean) with royal tax collectors weighing goods. Warehouses storing: gold dust, camphor, frankincense, agarwood, damar resin, cinnamon, silk, porcelain, glass beads. Hundreds of sailors, merchants, porters. Cranes lifting cargo. View across Musi to Bukit Siguntang.",
        "setting": "Royal dock — the economic gateway of the thalassocracy, where ships from India, Persia, and China unloaded their cargo, where Sumatran commodities were loaded for export, where the wealth of Asia changed hands.",
        "lighting": "warm 4000K late morning sun from camera left (key light, golden on ships, dock, and goods), cool 6500K sky fill. Mid contrast 3:1. Sea haze, river mist.",
        "mood": "gateway of empire — where the Indian Ocean trade met the South China Sea, where a thalassocracy's power was measured in ships and cargo, where Asia's wealth flowed.",
        "style": "photorealistic wood, water, stone, silk, and trade goods textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows, National Geographic documentary aesthetic.",
        "avoid": "modern port, modern ships, modern cranes, modern containers, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small dock (must be 200m with multiple international ships)."
    },
    "2B-L028-gudang-dagang.txt": {
        "view_type": "interior wide shot",
        "name": "Gudang Dagang (Royal Trade Warehouse) of Sriwijaya",
        "location": "near Royal Dock, Palembang",
        "period": "abad 8-9 Masehi",
        "details": "Vast warehouse 50m x 30m with high wooden ceiling. Sections for: Sumatran exports (gold dust in jars, camphor blocks, frankincense, agarwood, damar resin, cinnamon bark), foreign imports (Chinese silk rolls, Tang porcelain, Indian glass beads, Persian silverware, Indian cotton). Royal treasurer with bronze scale weighing gold dust. Scribes recording transactions on lontar. Porters carrying baskets and jars. Armed guards protecting valuable goods. Barrels of spices. Bundles of agarwood. Jars of camphor. Silk rolls in various colors. Beads sorted by color.",
        "setting": "Royal trade warehouse — where the kingdom's exports and imports were stored, where gold was weighed, where the economic pulse of the thalassocracy was felt.",
        "lighting": "warm 3500K daylight from high windows (key light, even illumination on goods), cool 6500K sky fill. Mid contrast 3:1. Dust particles, spice aromas visible in air.",
        "mood": "treasury of empire — where gold, camphor, and silk were stored, where the wealth of Asia was counted, where a thalassocracy's economic power was tangible.",
        "style": "photorealistic wood, gold, spice, silk, porcelain, and bead textures, 35mm film grain, deep depth of field f/8, 24mm wide lens equivalent, 8K hyperdetailed, color graded warm golden highlights cool blue shadows.",
        "avoid": "modern warehouse, modern containers, modern forklifts, modern packaging, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, small room (must be 50x30m vast warehouse)."
    },
    "2B-L029-bukit-siguntang.txt": {
        "view_type": "exterior wide shot",
        "name": "Bukit Siguntang (Sacred Hill) of Sriwijaya",
        "location": "Palembang, Sumatra Selatan",
        "period": "abad 7-11 Masehi",
        "details": "Sacred hill 100m above surrounding plain, considered the arupadhatu (formless realm) in Sriwijaya's Buddhist cosmology. At summit: 11 stone prasasti siddhayatra standing in a circle, sacred banyan tree, small shrine with golden Buddha statue. Buddhist monks in meditation. View from summit: entire Palembang city, Sungai Musi and Ogan confluence, royal palace complex (hundreds of hectares), port with international ships, tropical rainforest to horizon. Pilgrims climbing stone steps. Incense smoke from shrine. Sunset view of the thalassocracy.",
        "setting": "Bukit Siguntang — the sacred hill at the center of Sriwijaya's cosmological tridhatu (arupadhatu = summit, rupadhatu = city, kamadhatu = sea). 11 prasasti siddhayatra found here. The spiritual heart of the thalassocracy.",
        "lighting": "warm 3500K golden hour sunset from camera left (key light, dramatic on hill, prasasti, and panoramic view), cool 6500K sky fill. Mid contrast 3:1. Mist in valley, incense smoke.",
        "mood": "sacred summit — where heaven met earth, where 11 siddhayatra prasasti proclaimed the unity of wanua, where the Datu's spiritual authority was legitimized by Buddhist cosmology.",
        "style": "photorealistic stone, gold, tropical foliage, and panoramic landscape textures, 35mm film grain, deep depth of field f/11, 16mm ultra-wide lens equivalent for epic panorama, 8K hyperdetailed, color graded warm amber highlights cool blue shadows, BBC Earth documentary aesthetic.",
        "avoid": "modern buildings, modern tourism, modern researchers, modern stairs, anime style, cartoon, 3D render, watermark, text, signature, low resolution, blurry, oversaturated, narrow view (must show panoramic vista of city, rivers, port), flat terrain (must be elevated hill 100m)."
    },
}

# ========================================
# GENERATE
# ========================================

ALL_ROOMS = {**MATARAM_ROOMS, **SRIWIJAYA_ROOMS}

def main():
    total = 0
    for filename, data in ALL_ROOMS.items():
        content = TEMPLATE.format(**data)
        out_path = BASE / filename
        out_path.write_text(content, encoding="utf-8")
        total += 1
        print(f"  ✅ {filename}")
    print(f"\nTotal: {total} file generated")
    print(f"  Mataram Kuno rooms: {len(MATARAM_ROOMS)}")
    print(f"  Sriwijaya rooms: {len(SRIWIJAYA_ROOMS)}")

if __name__ == "__main__":
    main()
