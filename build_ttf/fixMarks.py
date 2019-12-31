import unicodedata as ud
import fontforge
f=fontforge.fonts()[0]
WIDTH=547
f.ascent  -= 300
f.descent -= 300

for g in f.glyphs("encoding"):
  if ud.category( chr(abs(g.unicode)) ) == "Mn": 
    g.width = 0
    for i in range (2,10):
      try: f[g.glyphname+".{}".format(str(i))].width = 0
      except: pass
  else:
    g.width = WIDTH
    for i in range (2,10):
      try: f[g.glyphname+".{}".format(str(i))].width = WIDTH
      except: pass