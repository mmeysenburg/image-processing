"""
 * Python program to create a color histogram.
 *
 * Usage: python ColorHistogram.py <filename>
"""
import sys
import skimage.io
import numpy as np
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname=sys.argv[1])

# display the image
skimage.io.imshow(image)

# tuple to select colors of each channel line
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()
