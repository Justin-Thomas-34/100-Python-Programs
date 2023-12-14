# Program 43: Python Program to Find the Size(Resolution) of a Image

import PIL

from PIL import Image

img = PIL.Image.open("C:/Users/UserName/Desktop/banner-img.png")
width , height = img.size

print(width,"x",height)