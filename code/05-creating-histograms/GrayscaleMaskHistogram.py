"""
 * Generate a grayscale histogram for an image.
 * Usage: python GrayscaleMaskHistogram.py <filename>
"""
import sys
import skimage.draw
import skimage.io
import numpy as np
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = skimage.io.imread(fname=sys.argv[1], as_gray=True)

# display the image
skimage.io.imshow(image)

# create mask here, using np.zeros() and skimage.draw.rectangle()
# WRITE YOUR CODE HERE

# apply the mask to the input image, create the histogram
# MODIFY CODE HERE
histogram, bin_edges = np.histogram(image, bins=256, range=(0.0, 1.0))

# configure and draw the histogram figure
plt.figure()

plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0, 1])

plt.plot(bin_edges[0:-1], histogram)

plt.show()
