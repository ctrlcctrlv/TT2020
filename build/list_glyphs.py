#!/usr/bin/env python3
import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import fontforge
f = fontforge.open("../TT_ita.sfd")
print('\n'.join(['{}'.format(c.glyphname) for c in f.glyphs("encoding")]))
