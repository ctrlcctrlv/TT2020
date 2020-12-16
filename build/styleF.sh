#!/bin/bash
mkdir -p styleF
GIMP="flatpak run --command=gimp org.gimp.GIMP -idf --batch-interpreter=python-fu-eval -b -"
ALT="$3" SEED=$((100000+($2*1000)+($4-1))) GIMPIMAGE="$1" $GIMP < styleF.py
