import fontforge
f=fontforge.fonts()[0]

f.ascent+=300
f.descent+=300


for g in f.glyphs("encoding"):
  if g.glyphname == ".notdef": continue
  if g.glyphname.endswith(".2"): break # loop-around
  if g.glyphname.startswith("NameMe"): break # ignore junkies
  origglyphname = g.glyphname
  for j in range(1,10):
    if j!=1: g=f.createChar(-1,origglyphname+"."+str(j))

    print("Trying {} \u2026".format(g.glyphname))

    g.clear()
    try:
      # Change this line as needed, depending on where the glyph bitmaps are
      g.importOutlines("buildI/styleB/"+origglyphname+".{}.png".format(j))
    except:
      print("Failed to import {}".format(g.glyphname))
    g.autoTrace()
    g.clearBackground()
    g.right_side_bearing=547
