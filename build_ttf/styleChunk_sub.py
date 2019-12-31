import fontforge
import sys
S=sys.argv[1]
ita=sys.argv[2] if len(sys.argv) >= 2 else ''

f=fontforge.open("TT{}_{}.sfd".format(ita, S))
print("Opened file")
for gO in sys.stdin.readlines():
  g = f.createMappedChar(gO.strip())
  if g.glyphname == ".notdef": continue
  if g.glyphname.endswith(".2"): break # loop-around
  origglyphname = g.glyphname
  for j in range(1,10):
    if j!=1: g=f.createChar(-1,origglyphname+"."+str(j))

    print("Trying {} \u2026".format(g.glyphname))

    g.clear()
    try:
      g.importOutlines("build{}/style{}/{}.{}.png".format("I" if ita == "ita" else ita,S,origglyphname,j))
    except:
      print("Failed to import {}".format(g.glyphname))
    g.autoTrace()
    g.clearBackground()
    g.right_side_bearing=547
f.save()
f.close()
print("Font closed")
