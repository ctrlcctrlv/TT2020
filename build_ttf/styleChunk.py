import fontforge
import subprocess
import sys
S=sys.argv[1]
ita=sys.argv[2] if len(sys.argv) >= 2 else ''
f=fontforge.open("TT{}.sfd".format("_"+ita if len(ita) > 0 else ""))

from itertools import zip_longest # for Python 3.x
def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

f.ascent+=300
f.descent+=300
G = list()

for g in f.glyphs("encoding"):
  if g.glyphname == ".notdef": continue
  if g.glyphname.endswith(".2"): break # loop-around
  G.append(g.glyphname)

f.save("TT{}_{}.sfd".format(ita,S))
f.close()

for gL in grouper(100, G):
  glyphs = "\n".join([e for e in gL if e is not None])
  pr = subprocess.Popen(["fontforge", "-lang=py", "-script", "styleChunk_sub.py", S, ita], stdin=subprocess.PIPE, bufsize=0)
  pr.communicate(glyphs.encode("ascii"))
