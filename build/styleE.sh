#!/bin/bash
mkdir -p styleE
mkdir -p gegl:cell-noise
GIMP="flatpak run --command=gimp org.gimp.GIMP -idf --batch-interpreter=python-fu-eval -b -"
ALT="$3" SEED=$((100000+$2+($4-1))) GIMPIMAGE="$1" $GIMP < styleE.py
