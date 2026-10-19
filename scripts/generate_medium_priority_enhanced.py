#!/usr/bin/env python3
"""
Generate metadata-only enhanced YAML for remaining 32 chapters (medium priority).
Output: enhanced-chapters/si-j*-*.yaml for all bab yang belum di-enhance manual.
"""
import yaml, os
from pathlib import Path
from datetime import datetime

ROOT = Path('/home/z/my-project/phase-1/sumber-primer/kemenbud-2025')
ENHANCED = ROOT / 'enhanced-chapters'

# 6 bab yang sudah di-enhance manual (critical priority)
MANUAL_DONE = {
    'si-j2-08-bab-3',  # Dinamika Politik
    'si-j2-10-bab-5',  # Puncak Pencapaian Hindu-Buddha
    'si-j3-12-bab-7',  # Wali Songo
    'si-j4-07-bab-2',  # Sultan Agung vs VOC
    'si-j4-11-bab-6',  # VOC Banda
    'si-j5-11-bab-6',  # Pemberontakan abad 19
}

# Mapping bab (berdasarkan title) ke fase drama
# Dibuat berdasarkan analisis judul + keywords di frontmatter
DRAMA_PHASE_MAPPING = {
    # Jilid 1
    'si-j1-06-bab-1': 1,  # Kondisi Lingkungan Alam - latar Fase 1
    'si-j1-07-bab-2': 1,  # Manusia: Persebaran - pra-Mataram
    'si-j1-08-bab-3': 1,  # Perkembangan Teknologi
    'si-j1-09-bab-4': 1,  # Religi, Seni, Tradisi
    'si-j1-10-bab-5': 1,  # Organisasi Sosial
    'si-j1-11-bab-6': 1,  # Maritim dan Jaringan Budaya
    # Jilid 2
    'si-j2-06-bab-1': 1,  # Masyarakat Nusantara - pengantar
    'si-j2-07-bab-2': 1,  # Persilangan Budaya - pra-Mataram
    'si-j2-09-bab-4': 3,  # Kehidupan Keseharian - konteks Majapahit
    'si-j2-11-bab-6': 3,  # Kemunduran - akhir Majapahit
    # Jilid 3
    'si-j3-06-bab-1': 4,  # Arus Perdagangan Jarak Jauh - konteks Demak
    'si-j3-07-bab-2': 4,  # Komunitas Muslim di Bandar Dagang
    'si-j3-08-bab-3': 4,  # Pembentukan Kerajaan (Demak)
    'si-j3-09-bab-4': 4,  # Intensifikasi Islamisasi
    'si-j3-10-bab-5': 4,  # Perkembangan Perdagangan
    'si-j3-11-bab-6': 6,  # Islam dalam Budaya Politik - Mataram Islam
    'si-j3-13-bab-8': 4,  # Kebudayaan Material Islam
    'si-j3-14-bab-9': 4,  # Teks, Ritual, Aksara
    # Jilid 4
    'si-j4-06-bab-1': 7,  # Jaringan Perdagangan Eropa
    'si-j4-08-bab-3': 6,  # Dinamika Keagamaan Baru
    'si-j4-09-bab-4': 7,  # VOC di Nusantara
    'si-j4-10-bab-5': 7,  # Papua Barat 1500-1800
    'si-j4-12-bab-7': 7,  # Diaspora Nusantara
    'si-j4-13-bab-8': 7,  # Rivalitas dan Resistensi
    'si-j4-14-bab-9': 7,  # Riau-Johor dan Aceh abad 17
    'si-j4-15-bab-10': 7,  # Kemunduran VOC
    # Jilid 5
    'si-j5-06-bab-1': 7,  # Pemerintahan Administrasi
    'si-j5-07-bab-2': 7,  # Sistem Hukum
    'si-j5-08-bab-3': 7,  # Ekonomi Kolonial
    'si-j5-09-bab-4': 7,  # Infrastruktur Publik
    'si-j5-10-bab-5': 7,  # Struktur Sosial
    'si-j5-12-bab-7': 7,  # Produksi Pengetahuan Kolonial
}

generated = 0
skipped = 0

# Iterate semua bab markdown
for md_file in sorted(ROOT.glob('jilid-*/*-bab-*.md')):
    with open(md_file, 'r') as f:
        content = f.read()
    if not content.startswith('---'):
        continue
    end = content.find('---', 3)
    if end < 0:
        continue
    fm_text = content[3:end]
    try:
        meta = yaml.safe_load(fm_text)
    except:
        continue

    doc_id = meta.get('doc_id')
    if not doc_id:
        continue

    # Skip yang sudah manual
    if doc_id in MANUAL_DONE:
        skipped += 1
        continue

    # Cek apakah file enhanced sudah ada
    enhanced_file = ENHANCED / f"{doc_id}.yaml"
    if enhanced_file.exists():
        skipped += 1
        continue

    jilid = meta.get('jilid')
    chapter_number = meta.get('chapter_number')
    title = meta.get('title')
    ont = meta.get('ontology') or {}

    # Get word_count from _meta.yaml
    word_count = None
    meta_yaml_path = md_file.parent / '_meta.yaml'
    if meta_yaml_path.exists():
        with open(meta_yaml_path) as mp:
            jilid_meta = yaml.safe_load(mp)
        for section in jilid_meta.get('sections', []):
            if section.get('file') == md_file.name:
                word_count = section.get('word_count')
                break

    # Determine drama phase
    drama_phase = DRAMA_PHASE_MAPPING.get(doc_id, 1)
    reading_time = (word_count // 200) if word_count else None

    # Generate minimal enhanced YAML (metadata-only)
    enhanced_data = {
        'doc_id': doc_id,
        'source_file': str(md_file.relative_to(ROOT)),
        'jilid': jilid,
        'chapter_number': chapter_number,
        'title': title,
        'summary': f"[PENDING ENHANCEMENT] Bab ini belum di-enhance manual. "
                  f"Konten: {title}. Word count: {word_count or 'unknown'}. "
                  f"Untuk produksi drama, baca isi bab atau enhance manual jika prioritas tinggi.",
        'reading_time_minutes': reading_time,
        'key_figures': [],
        'key_events': [],
        'key_locations': [],
        'drama_phase_mapping': {
            'primary_phase': drama_phase,
            'secondary_phases': [],
            'relevance_score': 'medium',
            'drama_anchors_relevant': [],
            'notes': 'Auto-generated mapping berdasarkan judul bab. Belum diverifikasi via pembacaan isi.',
        },
        'enhanced_ontology': {
            'era_specific': ont.get('era') or [],
            'region_specific': ont.get('region') or [],
            'themes': ont.get('topics') or [],
            'keywords_enhanced': ont.get('keywords') or [],
        },
        'metadata_production': {
            'enhanced_by': 'Z.ai Main Agent (auto-generated)',
            'enhanced_at': datetime.now().isoformat(),
            'enhancement_version': '1.0',
            'source_extraction': 'metadata-only',
            'notes': 'Auto-generated dari frontmatter asli. Untuk produksi drama, enhance manual diperlukan.',
        }
    }

    with open(enhanced_file, 'w', encoding='utf-8') as f:
        yaml.dump(enhanced_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100)

    generated += 1
    print(f"  ✓ Generated: {enhanced_file.name}")

print(f"\nTotal: {generated} enhanced YAML di-generate, {skipped} di-skip (sudah manual)")
