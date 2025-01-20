import cv2 as cv # OpenCV library
import numpy as np # Numpy library
from matplotlib import pyplot as plt # Matplotlib library
import sys

def crop_image():
    return 1

def vertical_reflection():
    return 1

def horizontal_reflection():
    return 1

def transpose():
    return 1

img = cv.imread(cv.samples.findFile("flower.jpeg")) # Reads an image
og_img = img.copy()

if img is None:
    sys.exit("Could not read the image.")

k = -1

while not k == ord("s"): # Run until user presses 's' button to save image
    cv.imshow("Display window", img) # Displays image
    k == cv.waitKey(0)
    if k == ord("o"): # original image
        img = og_img
    if k == ord("c"): # crop image
        crop_image()
    elif k == ord("v"): # vertically flips image
        vertical_reflection()
    elif k == ord("h"):
        horizontal_reflection() # horizontally flips image
    elif k == ord("t"): # transposes image
        transpose()

cv.imwrite("flower.jpeg", img) # Saves edited img to flower.jpeg