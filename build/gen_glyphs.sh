#!/bin/bash
mkdir -p pngs svgs
printf "\033[31mStep 1\e[0m"
python3 list_glyphs.py "$1" | parallel --progress './export_glyph.py {}' "$1"
printf "\033[31mStep 2\e[0m"
ls svgs/ | parallel --progress 'inkscape -z {} --export-png=pngs/{/.}.png -d 600'
