#!/bin/bash
printf "\033[31mStep 1\e[0m"
python list_glyphs.py | parallel --progress './export_glyph.py {}'
printf "\033[31mStep 2\e[0m"
ls svgs/* | parallel --progress 'inkscape -z {} --export-png=pngs/{/.}.png -d 600 2&>/dev/null'
