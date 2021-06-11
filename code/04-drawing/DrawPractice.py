"""
 * Program to practice with OpenCV drawing methods.
"""
import skimage.io
import numpy as np
import random

# create the black canvas
image = np.zeros(shape=(600, 800, 3), dtype="uint8")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE

# display the results
skimage.io.imshow(image)
