"""Acceptance check 2: prove no original file changed, using the release zip's own CRC32s as the baseline.

The zip stores a CRC32 per entry, recorded when the dataset was published, so it is a stronger baseline
than a checksum list taken just before the run.

Usage: python verify_untouched.py --zip ~/Documents/causalmat/matmech.zip --root ~/Documents/causalmat [--sample 20000]
"""
import argparse
import random
import sys
import zipfile
import zlib
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--zip", required=True)
ap.add_argument("--root", required=True, help="directory that CONTAINS the matmech/ tree")
ap.add_argument("--sample", type=int, default=0, help="check a random sample of entries instead of all")
a = ap.parse_args()

root = Path(a.root).expanduser()
z = zipfile.ZipFile(Path(a.zip).expanduser())
entries = [i for i in z.infolist() if not i.is_dir()]
if a.sample:
    entries = random.Random(0).sample(entries, min(a.sample, len(entries)))

missing = changed = ok = 0
bad = []
for i, info in enumerate(entries, 1):
    p = root / info.filename
    if not p.is_file():
        missing += 1
        bad.append(("missing", info.filename))
        continue
    if p.stat().st_size != info.file_size:
        changed += 1
        bad.append(("size", info.filename))
        continue
    crc = 0
    with open(p, "rb") as fh:
        while chunk := fh.read(1 << 20):
            crc = zlib.crc32(chunk, crc)
    if crc != info.CRC:
        changed += 1
        bad.append(("crc", info.filename))
    else:
        ok += 1
    if i % 50000 == 0:
        print(f"  {i}/{len(entries)} checked, {changed} changed, {missing} missing", flush=True)

print(f"checked {len(entries)} original entries: {ok} identical, {changed} changed, {missing} missing")
for kind, name in bad[:20]:
    print("  !", kind, name)
sys.exit(1 if (changed or missing) else 0)
