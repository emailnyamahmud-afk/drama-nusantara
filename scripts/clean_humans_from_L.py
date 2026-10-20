#!/usr/bin/env python3
"""
Bersihkan semua file L (latar/lokasi reference) di era 2B:
- Hapus semua mentions manusia (monks, priests, guards, merchants, dll)
- Ganti dengan "empty, no people, architecture and environment only"
- Tambah "No people, no characters, no humans" di prompt dan avoid
- Reference lokasi = murni environment untuk composite dengan karakter ref nanti
"""

import re
from pathlib import Path

BASE = Path("/home/z/my-project/produksi/t2i-prompts/2B-mataram-sriwijaya/prompts")

# Patterns to remove (human presence)
HUMAN_PATTERNS = [
    # People descriptions - remove entire phrases
    (r'Buddhist monks in orange robes?[^\n]*\.?', ''),
    (r'Hindu priests in white-yellow robes?[^\n]*\.?', ''),
    (r'Hindu priests in white robes?[^\n]*\.?', ''),
    (r'royal guards with spears?[^\n]*\.?', ''),
    (r'royal guards?[^\n]*\.?', ''),
    (r'guards with spears?[^\n]*\.?', ''),
    (r'guards lining[^\n]*\.?', ''),
    (r'foreign merchants?\s*\([^)]*\)?[^\n]*\.?', ''),
    (r'foreign merchants?[^\n]*\.?', ''),
    (r'Indian merchants?[^\n]*\.?', ''),
    (r'Chinese merchants?[^\n]*\.?', ''),
    (r'Persian merchants?[^\n]*\.?', ''),
    (r'foreign scholars?\s*\([^)]*\)?[^\n]*\.?', ''),
    (r'foreign scholars?[^\n]*\.?', ''),
    (r'international scholars?[^\n]*\.?', ''),
    (r'royal treasurer[^\n]*\.?', ''),
    (r'treasurer[^\n]*\.?', ''),
    (r'Patih[^\n]*\.?', ''),
    (r'patih[^\n]*\.?', ''),
    (r'Mpu\s*\([^)]*\)?\s*[^\n]*\.?', ''),
    (r'Mpu[^\n]*\.?', ''),
    (r'mpu[^\n]*\.?', ''),
    (r'Datu[^\n]*\.?', ''),
    (r'Datu[^\n]*\.?', ''),
    (r'datu[^\n]*\.?', ''),
    (r'courtiers and dignitaries[^\n]*\.?', ''),
    (r'courtiers[^\n]*\.?', ''),
    (r'dignitaries[^\n]*\.?', ''),
    (r'dayang[^\n]*\.?', ''),
    (r'women servants[^\n]*\.?', ''),
    (r'scribes[^\n]*\.?', ''),
    (r'scribes copying[^\n]*\.?', ''),
    (r'craftsmen[^\n]*\.?', ''),
    (r'gardeners[^\n]*\.?', ''),
    (r'stable hands[^\n]*\.?', ''),
    (r'kusir[^\n]*\.?', ''),
    (r'sailors[^\n]*\.?', ''),
    (r'porters[^\n]*\.?', ''),
    (r'pilgrims[^\n]*\.?', ''),
    (r'monks in[^\n]*\.?', ''),
    (r'monks[^\n]*\.?', ''),
    (r'priests in[^\n]*\.?', ''),
    (r'priests[^\n]*\.?', ''),
    (r'scholars[^\n]*\.?', ''),
    (r'subjects[^\n]*\.?', ''),
    (r'Royal family[^\n]*\.?', ''),
    (r'royal family[^\n]*\.?', ''),
    (r'hundreds of people[^\n]*\.?', ''),
    (r'hundreds of subjects[^\n]*\.?', ''),
    (r'thousands of subjects[^\n]*\.?', ''),
    (r'thousands of people[^\n]*\.?', ''),
    (r'hundreds of[^\n]*people[^\n]*\.?', ''),
    (r'people[^\n]*\.?', ''),
    (r'Royal banner[^\n]*\.?', 'Royal banner (red-gold) flying from main tower.'),
    (r'merchants?[^\n]*\.?', ''),
    (r'women?[^\n]*\.?', ''),
    (r'men?[^\n]*\.?', ''),
    (r'Armed guards[^\n]*\.?', ''),
    (r'armed guards[^\n]*\.?', ''),
    (r'Buddhist monks?[^\n]*\.?', ''),
    (r'buddhist monks?[^\n]*\.?', ''),
    (r'Royal tax collectors?[^\n]*\.?', ''),
    (r'tax collectors?[^\n]*\.?', ''),
    (r'Farmers?[^\n]*\.?', ''),
    (r'farmers?[^\n]*\.?', ''),
    (r'Local farmers?[^\n]*\.?', ''),
    (r'local farmers?[^\n]*\.?', ''),
]

def clean_file(filepath):
    content = filepath.read_text(encoding="utf-8")
    original = content
    
    # Apply all patterns
    for pattern, replacement in HUMAN_PATTERNS:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Clean up: remove double spaces, orphaned phrases
    content = re.sub(r'  +', ' ', content)
    content = re.sub(r'\.\.+', '.', content)
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # Add "No people, no characters, no humans" to the prompt if not already there
    if "no people" not in content.lower() and "no humans" not in content.lower():
        # Add to the main description area (after first period in details)
        content = content.replace(
            "No modern elements.",
            "No modern elements. No people, no characters, no humans — empty location reference for composite with character reference sheet."
        )
    
    # Add to Avoid section
    if "people, no characters, no humans" not in content.lower():
        content = content.replace(
            "Avoid: ",
            "Avoid: people, characters, humans, "
        )
    
    # Remove "empty room" from avoid if present (since we now explicitly say no people)
    content = content.replace("empty room (must be ", "furnished room (must be ")
    
    # Write back
    filepath.write_text(content, encoding="utf-8")
    return content != original

def main():
    count = 0
    for f in sorted(BASE.glob("2B-L*.txt")):
        changed = clean_file(f)
        if changed:
            count += 1
            print(f"  ✅ Cleaned: {f.name}")
        else:
            print(f"  — No change: {f.name}")
    
    print(f"\nTotal files cleaned: {count}")
    
    # Verify
    print("\n=== VERIFICATION ===")
    human_check = [
        'monks', 'priests', 'guards', 'merchants', 'sailors', 'porters',
        'scholars', 'scribes', 'pilgrims', 'gardeners', 'craftsmen',
        'subjects', 'courtiers', 'dayang', 'people', 'patih', 'mpu'
    ]
    remaining = 0
    for f in sorted(BASE.glob("2B-L*.txt")):
        content = f.read_text().lower()
        found = [kw for kw in human_check if kw in content]
        if found:
            remaining += 1
            print(f"  ⚠️  Still has: {f.name}: {', '.join(found)}")
    
    if remaining == 0:
        print("  ✅ All L files are now human-free (location reference only)")
    else:
        print(f"  ⚠️  {remaining} files still have human presence")

if __name__ == "__main__":
    main()
