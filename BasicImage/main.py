import cv2 as cv # OpenCV library
import numpy as np # Numpy library
import math
import sys

def crop_image(img, rows, cols):
    return img[rows[0]:rows[1],cols[0]:cols[1]]

def vertical_reflection(img):
    height, width = img.shape[:2]
    
    # Create the vertical reflection matrix
    reflection_matrix = np.array([
        [1, 0, 0],
        [0, -1, height - 1]  # Must translate down by height, as img reflection will be outside the canvas
    ], dtype=np.float32)
    
    # Apply the transformation
    return cv.warpAffine(img, reflection_matrix, (width, height))

def horizontal_reflection(img):
    height, width = img.shape[:2]
    
    # Create the horizontal reflection matrix
    reflection_matrix = np.array([
        [-1, 0, width - 1], # Must translate left by width, as img reflection will be outside the canvas
        [0, 1, 0]  
    ], dtype=np.float32)
    
    # Apply the transformation
    return cv.warpAffine(img, reflection_matrix, (width, height))

def rotate(img, theta):
    height, width = img.shape[:2]

    a = math.cos(theta)
    b = math.sin(theta)
    
    # Create the rotation matrix
    rotation_matrix = np.array([
        [a, b, (1 - a) * width / 2 - b * height / 2], # Must translate to image's origin to make it rotate about the center of the image
        [-b, a, b * width / 2 + (1 -a) * height / 2]
    ], dtype=np.float32)
    
    # Apply the rotation around the center
    return cv.warpAffine(img, rotation_matrix, (width, height))

def transpose(img):
    m, n, p = img.shape[:3]

    # new_img with dimensions n x m x p
    new_img = np.empty((n, m, p), dtype=img.dtype)

    for row in range(m):
        for col in range(n):
            # swapping row entries to column entries
            new_img[col, row] = img[row, col]

    return new_img

def lighten(img):
    return 1

def contrast(img):
    return 1

img = cv.imread(cv.samples.findFile("img.jpg")) # Reads an image
og_img = img.copy()

if img is None:
    sys.exit("Could not read the image.")

k = -1

while not k == ord("s"): # Run until user presses 's' button to save image
    cv.imshow("Display window", img) # Displays image
    k = cv.waitKey(0)
    if k == ord("o"): # original image
        img = og_img
    if k == ord("c"): # crop image
        print(img.shape)
        rows = []
        cols = []
        print("Input row 1: ")
        rows.append(int(input()))
        print("Input row 2: ")
        rows.append(int(input()))
        print("Input column 1: ")
        cols.append(int(input()))
        print("Input column 2: ")
        cols.append(int(input()))
        img = crop_image(img, rows, cols)
    elif k == ord("v"): # vertically flips image
        img = vertical_reflection(img)
    elif k == ord("h"):
        img = horizontal_reflection(img) # horizontally flips image
    elif k == ord("t"): # transposes image
        img = transpose(img)
    elif k == ord("r"):
        img = rotate(img, math.radians(45))
    elif k == ord("l"):
        img = lighten(img)
    elif k == ord("n"):
        img = contrast(img)

cv.imwrite("edited_img.jpg", img) # Saves edited img to edited_img.jpeg