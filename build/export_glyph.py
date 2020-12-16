#!/usr/bin/env python3
import sys
import fontforge
gn=sys.argv[1]
f = fontforge.open(sys.argv[2])
f.ascent+=300
f.descent+=300
g=f[f.findEncodingSlot(gn)]
if g.width == 0:
    g.width = f["A"].width
g.unlinkRef()
g.export("svgs/{}.svg".format(gn))
