#!/usr/bin/env python3
import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import fontforge
gn=sys.argv[1]
f = fontforge.open("../TT_ita.sfd")
f.ascent+=300
f.descent+=300
g=f[gn]
if g.width == 0:
    g.width = f["A"].width
g.export("svgs/{}.svg".format(gn))
