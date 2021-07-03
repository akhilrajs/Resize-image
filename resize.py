# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:22:22 2021

@author: khilrajs
"""

from PIL import Image
from os import listdir
from os import path
from os import makedirs
from os import getcwd
from os import startfile

if not path.exists("RESIZED"):
    makedirs("RESIZED")
save_location = getcwd() + "/RESIZED/"
folder = input("# Drag and drop the folder containing the image or images : ")
files = listdir(folder)
for file in files:
    im = Image.open(str(folder) + "/" + str(file))
    width, height = im.size
    print("# " + str(file) + " Size : " + str(width) + "*" + str(height) + " px")
factor = input("# factor : ")
COUNT = 1 
factor = int(factor)
for file in files:
    im = Image.open(str(folder) + "/" + str(file))
    width, height = im.size
    im = im.resize((width//factor, height//factor))
    file_name = str(save_location) + str(file) + ".png"
    im.save(file_name, "PNG")
    width, height = im.size
    print("# Resizing and saving " + str(file) + str(width) + "*" + str(height) + " px")
    COUNT += 1
print("# Total number of images resized : " + str(COUNT))
startfile(save_location)