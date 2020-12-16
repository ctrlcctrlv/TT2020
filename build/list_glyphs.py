#!/usr/bin/env python3
import sys, os
if os.getenv('APPENDPYPATH'):
    sys.path.append(os.getenv('APPENDPYPATH'))
assert len(sys.argv) == 2
import fontforge
f = fontforge.open(sys.argv[1])
print('\n'.join(['{}'.format(c.glyphname) for c in f.glyphs("encoding")]))
