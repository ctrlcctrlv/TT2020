#!/bin/bash
ALT="$3" SEED=$((100000+$2+($4-1))) GIMPIMAGE="$1" /home/fred/Downloads/GIMP_AppImage-release-2.10.8-withplugins-x86_64.AppImage -idf --batch-interpreter=python-fu-eval -b - < styleB.py
