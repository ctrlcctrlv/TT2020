# TT2020 build files

Required:
* Python 3+
* GEGL
* `python-gegl`
* GIMP
* Inkscape

Here lie the TT2020 build files; they are typically called in this order:

* gen_glyphs.sh (list_glyphs.py, export_glyph.py): `./gen_glyphs.sh ../TT.sfd`
* gen_style.sh (style[A-G].sh): `TT=../TT.sfd ./gen_style.sh D`

Most styles are generated via GIMP scripts; all styles so far generate bitmaps which are expected to be autotraced by FontForge.

Possible future work would be, using Inkscape to generate a style, and using OpenGL shaders to much more quickly generate a style than GIMP can do.

## Version 0.3 warning

We now use the Flatpak GIMP. This is because GIMP on my distribution, Arch Linux, dropped Python support. Even if it's added back, we'll keep using Flatpak GIMP. It's more up to date and supports OpenCL.

You must install GIMP:
```bash
flatpak install https://flathub.org/repo/appstream/org.gimp.GIMP.flatpakref
```

You then need to chew a hole in Flatpak's sandbox (this allows us to use the system GEGL from GIMP's Python interpreter):

```bash
sudo flatpak override org.gimp.GIMP --talk-name=org.freedesktop.Flatpak
```

## Ubuntu tip!

GEGL won't work without the very opaquely named package `gir1.2-gegl-0.4`.
