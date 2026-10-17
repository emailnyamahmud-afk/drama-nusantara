#!/usr/bin/env python3
"""
Build quality report for all Kemenbud 2025 chapters.
Output: _quality-report.yaml
"""
import os, yaml
from pathlib import Path
from datetime import datetime

ROOT = Path('/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025')

# Collect all chapter files
all_files = sorted(ROOT.glob('jilid-*/*.md'))

chapters_data = []
stats = {
    'total_files': 0,
    'total_bab': 0,
    'total_front_matter': 0,
    'total_back_matter': 0,
    'review_status': {},
    'reviewer_distribution': {},
    'era_distribution': {},
    'region_distribution': {},
    'keywords_filled': 0,
    'keywords_empty': 0,
    'total_keywords_unique': set(),
    'chapter_type_distribution': {},
    'bab_with_word_count': 0,
    'bab_without_word_count': 0,
    'total_words_all_bab': 0,
}

for f in all_files:
    stats['total_files'] += 1
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if not content.startswith('---'):
        continue
    end = content.find('---', 3)
    if end < 0:
        continue
    fm_text = content[3:end]
    try:
        meta = yaml.safe_load(fm_text)
    except Exception:
        continue

    rel_path = str(f.relative_to(ROOT))
    jilid = int(rel_path.split('/')[0].replace('jilid-', ''))
    filename = rel_path.split('/')[1]

    chapter_type = meta.get('chapter_type', 'unknown')
    stats['chapter_type_distribution'][chapter_type] = stats['chapter_type_distribution'].get(chapter_type, 0) + 1

    if chapter_type == 'bab':
        stats['total_bab'] += 1
    elif chapter_type in ('front-matter', 'sambutan', 'persembahan', 'pendahuluan', 'daftar-isi', 'pendahuluan-jilid'):
        stats['total_front_matter'] += 1
    elif chapter_type in ('back-matter', 'epilog', 'penutup-jilid'):
        stats['total_back_matter'] += 1

    rs = meta.get('review_status', 'unknown')
    stats['review_status'][rs] = stats['review_status'].get(rs, 0) + 1

    rv = meta.get('reviewer', 'unknown')
    stats['reviewer_distribution'][rv] = stats['reviewer_distribution'].get(rv, 0) + 1

    ont = meta.get('ontology') or {}
    for era in (ont.get('era') or []):
        stats['era_distribution'][era] = stats['era_distribution'].get(era, 0) + 1
    for region in (ont.get('region') or []):
        stats['region_distribution'][region] = stats['region_distribution'].get(region, 0) + 1

    kws = ont.get('keywords') or []
    if kws:
        stats['keywords_filled'] += 1
        for k in kws:
            stats['total_keywords_unique'].add(k)
    else:
        stats['keywords_empty'] += 1

    chapter_info = {
        'doc_id': meta.get('doc_id'),
        'jilid': jilid,
        'filename': filename,
        'title': meta.get('title'),
        'chapter_type': chapter_type,
        'chapter_number': meta.get('chapter_number'),
        'source_pages': meta.get('source_pages'),
        'cetak_pages': meta.get('cetak_pages'),
        'review_status': rs,
        'reviewer': rv if rv != 'unknown' else None,
        'ontology_era': ont.get('era') or [],
        'ontology_region': ont.get('region') or [],
        'ontology_topics': ont.get('topics') or [],
        'ontology_keywords': kws,
        'has_word_count': False,
        'word_count': None,
    }

    meta_yaml_path = f.parent / '_meta.yaml'
    if meta_yaml_path.exists():
        with open(meta_yaml_path, 'r') as mp:
            jilid_meta = yaml.safe_load(mp)
        for section in jilid_meta.get('sections', []):
            if section.get('file') == filename:
                chapter_info['word_count'] = section.get('word_count')
                chapter_info['size_bytes'] = section.get('size_bytes')
                chapter_info['has_word_count'] = True
                if chapter_type == 'bab':
                    stats['bab_with_word_count'] += 1
                    stats['total_words_all_bab'] += section.get('word_count', 0)
                break

    if chapter_type == 'bab' and not chapter_info['has_word_count']:
        stats['bab_without_word_count'] += 1

    chapters_data.append(chapter_info)

# Compose quality report
report = {
    'generated_at': datetime.now().isoformat(),
    'generator': 'build_quality_report.py',
    'scope': 'Kemenbud 2025 - 5 jilid Sejarah Indonesia',
    'statistics': {
        'total_files': stats['total_files'],
        'total_bab': stats['total_bab'],
        'total_front_matter': stats['total_front_matter'],
        'total_back_matter': stats['total_back_matter'],
        'bab_with_word_count': stats['bab_with_word_count'],
        'bab_without_word_count': stats['bab_without_word_count'],
        'total_words_all_bab': stats['total_words_all_bab'],
        'keywords_filled_bab': stats['keywords_filled'],
        'keywords_empty_bab': stats['keywords_empty'],
        'unique_keywords_count': len(stats['total_keywords_unique']),
        'review_status_distribution': stats['review_status'],
        'reviewer_distribution': stats['reviewer_distribution'],
        'chapter_type_distribution': stats['chapter_type_distribution'],
        'era_distribution': stats['era_distribution'],
        'region_distribution': stats['region_distribution'],
    },
    'issues_found': [
        {
            'issue': 'review_status tidak konsisten',
            'severity': 'medium',
            'description': f"3 nilai berbeda: {list(stats['review_status'].keys())}",
            'affected_files': sum(1 for c in chapters_data if c.get('review_status') != 'reviewed'),
            'fix': 'Standardisasi semua jadi "reviewed" atau gunakan status baru "needs-enhancement"',
        },
        {
            'issue': 'ontology.era terlalu generik',
            'severity': 'high',
            'description': 'Banyak bab di-tag multiple era padahal isinya spesifik satu era',
            'affected_files': sum(1 for c in chapters_data if len(c.get('ontology_era') or []) > 2),
            'fix': 'Audit per-bab, kurangi era tags ke yang paling spesifik',
        },
        {
            'issue': 'ontology.region tidak spesifik',
            'severity': 'high',
            'description': 'Region tags tidak spesifik per bab - 38 dari 38 bab tagged dengan 4-5 region yang sama',
            'affected_files': stats['total_bab'],
            'fix': 'Audit per-bab, isi region tags sesuai konten bab',
        },
        {
            'issue': 'reviewer tidak tercatat untuk sebagian besar bab',
            'severity': 'low',
            'description': '23 bab tidak punya field reviewer',
            'affected_files': sum(1 for c in chapters_data if c.get('reviewer') is None),
            'fix': 'Tambah field reviewer atau hapus field ini',
        },
        {
            'issue': 'tidak ada field summary/abstract per bab',
            'severity': 'high',
            'description': 'Untuk navigasi cepat, perlu ringkasan 2-3 kalimat per bab',
            'affected_files': stats['total_bab'],
            'fix': 'Tambah field "summary" di enhanced metadata (file paralel)',
        },
        {
            'issue': 'tidak ada field key_figures/key_events/key_locations per bab',
            'severity': 'high',
            'description': 'Untuk riset drama, perlu daftar tokoh, peristiwa, dan lokasi penting per bab',
            'affected_files': stats['total_bab'],
            'fix': 'Tambah field "key_figures", "key_events", "key_locations" di enhanced metadata (file paralel)',
        },
        {
            'issue': 'tidak ada field drama_phase_mapping per bab',
            'severity': 'high',
            'description': 'Tidak ada mapping eksplisit antara bab buku dan 10 fase drama',
            'affected_files': stats['total_bab'],
            'fix': 'Tambah field "drama_phase_mapping" di enhanced metadata (file paralel)',
        },
    ],
    'chapters': chapters_data,
}

output = ROOT / '_quality-report.yaml'
with open(output, 'w', encoding='utf-8') as f:
    yaml.dump(report, f, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100)

print(f"✓ Quality report generated: {output}")
print(f"  Total chapters audited: {stats['total_files']}")
print(f"  Total bab: {stats['total_bab']}")
print(f"  Issues found: {len(report['issues_found'])}")
print(f"  Total words in bab: {stats['total_words_all_bab']:,}")
