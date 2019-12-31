# Generate style D, given PNG of a single glyph image. This style is pretty much verbatim copy of the instructions at https://www.xach.com/gimp/tutorials/rough.html

import gi
gi.require_version('Gegl', '0.4')

import gegl
import sys
import os

i_f = os.environ["GIMPIMAGE"]
seed = os.environ["SEED"] or 11
alt = os.environ["ALT"] or 1
outfile = "styleD/{}.{}.png".format(i_f.replace("pngs/", "").replace(".png", ""), alt)
#print("Opening {} and writing to {}".format(i_f, outfile), file=sys.stderr)

g = gegl.Graph("png-load", "scale-ratio", "noise-spread", "noise-spread", "gaussian-blur")
g[0].path = i_f
g[1].x = 0.1
g[1].y = 0.1
g[2].seed = g[3].seed = int(seed)
g[2]["amount-x"] = g[3]["amount-x"] = g[2]["amount-y"] = g[3]["amount-y"] = 35
g[4]["std-dev-x"] = g[4]["std-dev-y"] = 3.5
g2 = gegl.Graph("color", "over", "crop", "threshold", "png-save")
g2[-1].path = outfile
g2[0].value = (1, 1, 1)
g2[2].width = 500
g2[2].height = 1000
g.plug_as_aux(g2[1])
g2()
