#!/usr/bin/env python3

import sys
import os
from PIL import Image

# grab first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if ouput_folder exists. If not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(img_folder):
  img = Image.open(f'{img_folder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  # added the / in case user doesn't enter it. You may want to check for this and add or remove it. 
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('all done!')

# loop through pokedex
# convert the images in pokedex to PNG
# save to the new folder created, that is, output_folder
# JPGtoPNGconverter.py Pokedex/ new/
# use the above to test your code
