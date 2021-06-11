"""
 * Python program to create a color histogram on a masked image.
 *
 * Usage: python ColorHistogramMask.py <filename>
"""
import sys
import skimage.draw
import skimage.io
import numpy as np
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname=sys.argv[1])

# display the original image
skimage.io.imshow(image)

# create a circular mask to select the 7th well in the first row
# WRITE YOUR CODE HERE

# just for display:
# make a copy of the image, call it masked_image, and
# use np.logical_not() and indexing to apply the mask to it
# WRITE YOUR CODE HERE

# create a new window and display masked_image, to verify the
# validity of your mask
# WRITE YOUR CODE HERE

# list to select colors of each channel line
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    # change this to use your circular mask to apply the histogram
    # operation to the 7th well of the first row
    # MODIFY CODE HERE
    histogram, bin_edges = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))

    plt.plot(bin_edges[0:-1], histogram, color=c)

plt.xlabel("color value")
plt.ylabel("pixel count")

plt.show()
