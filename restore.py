#!/usr/bin/env python3
"""Restore akasha_vectors.json from split parts."""
import gzip, os
parts = sorted([f for f in os.listdir('.') if f.startswith('akasha_soul.part')])
print(f"Reassembling {len(parts)} parts...")
with open('akasha_vectors.json.gz', 'wb') as out:
    for p in parts:
        with open(p, 'rb') as f:
            out.write(f.read())
        print(f"  + {p}")
import shutil
with gzip.open('akasha_vectors.json.gz', 'rb') as gz:
    with open('akasha_vectors.json', 'wb') as out:
        shutil.copyfileobj(gz, out)
os.remove('akasha_vectors.json.gz')
print("Restored!")
