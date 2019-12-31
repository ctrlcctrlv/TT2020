# Generate style B, given PNG of a single glyph image.

import sys
import os
import subprocess

i_f = os.environ["GIMPIMAGE"]
seed = os.environ["SEED"] or 11
alt = os.environ["ALT"] or 1
if alt <= 1:
    outfile = "styleB/{}.png".format(i_f.replace("pngs/", "").replace(".png", ""))
else:
    outfile = "styleB/{}.{}.png".format(i_f.replace("pngs/", "").replace(".png", ""), alt)
print("Opening {} and writing to {}".format(i_f, outfile))

im = pdb.file_png_load(i_f, 0)
print("===SIZE IS: {}===".format(str(im.height)+"X"+str(im.width)))
pdb.gimp_image_scale(im,im.width/3,im.height/3)
print("===SIZE IS: {}===".format(str(im.height)+"X"+str(im.width)))

pdb.gimp_image_resize(im, im.width+1000, im.height, 500, 0)
print(im.layers)
for layer in im.layers:
    pdb.gimp_layer_resize_to_image_size(layer)

pdb.plug_in_gauss(im, im.active_drawable, 80, 80, 0)
cell_noise_file = "gegl:cell-noise/{}x{}x{}.png".format(im.height, im.width, seed)
if not os.path.isfile(cell_noise_file):
    command = "/usr/bin/python3.8 gen_cell_noise.py -h {} -w {} -o 'gegl:cell-noise' -s {}".format(im.height, im.width, seed)
    os.system(command)
la = pdb.gimp_file_load_layer(im, cell_noise_file)
new_mask = pdb.gimp_layer_create_mask(la, 5)
pdb.gimp_layer_add_mask(im.layers[0], new_mask)
pdb.gimp_drawable_invert(new_mask, False)
pdb.gimp_brightness_contrast(new_mask, 57, 94)
pdb.gimp_layer_remove_mask(im.layers[0], 0)
pdb.gimp_layer_flatten(im.layers[0])
pdb.gimp_brightness_contrast(im.active_drawable, -127, 127)
pdb.gimp_image_convert_indexed(im, 0, 3, 0, False, True, '')
pdb.gimp_image_convert_grayscale(im)
pdb.gimp_layer_add_alpha(im.layers[0])
pdb.gimp_image_select_color(im, 2, im.active_drawable, (1.0,1.0,1.0))
pdb.gimp_drawable_edit_clear(im.active_drawable)
pdb.script_fu_distress_selection(im, im.active_drawable, 127, 2, 2, 10, 1, 1)
pdb.gimp_selection_invert(im)
nl = pdb.gimp_layer_new(im, im.width, im.height, 3, "QQ", 100, 0)
pdb.gimp_image_insert_layer(im, nl, None, -1)
pdb.gimp_image_remove_layer(im, im.layers[0])
#Below is problem command
pdb.gimp_edit_bucket_fill(im.active_drawable, 0, 0, 100, 255, True, 1.0, 1.0)
pdb.file_png_save_defaults(im, im.active_drawable, outfile, 0)
pdb.gimp_quit(1)
