# Generate style C, given PNG of a single glyph image.

import gimpfu
import sys
import os

i_f = os.environ["GIMPIMAGE"]
seed = os.environ["SEED"] or 11
alt = os.environ["ALT"] or 1
if alt <= 1:
    outfile = "styleF/{}.png".format(i_f.replace("pngs/", "").replace(".png", ""))
else:
    outfile = "styleF/{}.{}.png".format(i_f.replace("pngs/", "").replace(".png", ""), alt)
#print("Opening {} and writing to {}".format(i_f, outfile))

im = pdb.file_png_load(i_f, 0)
pdb.gimp_image_scale(im,im.width/5,im.height/5)

pdb.gimp_image_resize(im, im.width+500, im.height, 250, 0)
print(im.layers)
for layer in im.layers:
    pdb.gimp_layer_resize_to_image_size(layer)

new_mask = pdb.gimp_layer_create_mask(im.layers[0], gimpfu.ADD_MASK_WHITE)
pdb.gimp_layer_add_mask(im.layers[0], new_mask)
pdb.plug_in_plasma(im, new_mask, seed, 2.5)
pdb.plug_in_gauss(im, im.layers[0], 40, 40, 0)
pdb.gimp_brightness_contrast(new_mask, 45, 45)
pdb.gimp_layer_remove_mask(im.layers[0], gimpfu.MASK_APPLY)
pdb.gimp_layer_flatten(im.layers[0])
pdb.gimp_brightness_contrast(im.layers[0], -117, 127)
pdb.plug_in_gauss(im, im.layers[0], 40, 40, 0)
pdb.gimp_image_convert_grayscale(im)
# 20 is cell-size, 60 is degrees
pdb.plug_in_newsprint(im, im.layers[0], 20, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 1)
pdb.file_png_save_defaults(im, im.layers[0], outfile, 0)
pdb.gimp_quit(1)
