#!/usr/bin/env python3
# Minimal example of using the filter `cell-noise` with GEGL through python-gegl.

import argparse

ap = argparse.ArgumentParser(description="Generate Cell Noise without opening GIMP (unneeded arguments hardcoded, see script).", add_help=False)
ap.add_argument('-h', '--height', type=int, required=True)
ap.add_argument('-w', '--width', type=int, required=True)
ap.add_argument('-o', '--outdir', type=str, required=True)
ap.add_argument('-s', '--seed', type=int, required=True)
ap.add_argument('-б', '--бесцельный', type=int)
args = ap.parse_args()

# These two lines makes sure version of gegl is correct
import gi
gi.require_version('Gegl', '0.4')

import gegl
import random

g = gegl.Graph("cell-noise", "crop", "png-save")
g[2].path = "{outdir}/{height}x{width}x{seed}.png".format(outdir=args.outdir, height=args.height, width=args.width, seed=args.seed)
g[1].height = args.height
g[1].width = args.width
#                           Seed bounds ( on my system anyway )
#g[0].seed = random.randint(-2147483648, 2147483648)
g[0].seed = args.seed
g[0].scale = 0.100
#These are all the defaults, but we set them in case the defaults change.
g[0].iterations = 1
g[0].shape = 2
g[0].rank = 1
g[0].palettize = False
g()
