#!/bin/bash
mkdir -p styleB
GIMP="flatpak run --command=gimp org.gimp.GIMP -idf --batch-interpreter=python-fu-eval -b -"
ALT="$3" SEED=$((100000+$2+($4-1))) GIMPIMAGE="$1" $GIMP < styleB.py
