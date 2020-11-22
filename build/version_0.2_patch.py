#!/usr/bin/env python3
# I was in the middle of moving when this release was made and some vital build files were on another computer.
# Therefore, let's patch the binaries and call it a release. Users will never know as long as I don't fuck up.
# (Famous last words.)

import fontTools.ttLib
import sys

assert len(sys.argv) == 2, "No filename given"

ttf=fontTools.ttLib.TTFont(file=sys.argv[1])

# SFNT revision
ttf["head"].fontRevision = 0.2

# `name` font version
padZeroes = lambda bs: b'\x00'.join([b.encode('ascii') for b in bs])
names=ttf["name"].names
for n in names:
    if n.nameID != 5: continue
    n.string = n.string.replace(b'001', b'0.2').replace(padZeroes('001'), padZeroes('0.2')) \
                       .replace(b'0.1', b'0.2').replace(padZeroes('0.1'), padZeroes('0.2'))
ttf["name"].names=names

# `liga` ⇒ `dlig` (Closes #8)
if "GSUB" in ttf:
    for fr in ttf["GSUB"].table.FeatureList.FeatureRecord:
        fr.FeatureTag = 'dlig' if fr.FeatureTag == 'liga' else fr.FeatureTag

ttf.save(sys.argv[1])
print("Patched {}".format(sys.argv[1]), file=sys.stderr)
