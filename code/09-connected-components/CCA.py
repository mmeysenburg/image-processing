"""
 * Python script count objects in an image
 *
 * usage: python CCA.py <filename> <sigma> <threshold>
"""
import sys

import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.measure

# get filename, sigma, and threshold value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])
t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread(fname=filename, as_gray=True)
skimage.io.imshow(image)

# blur and grayscale before thresholding
blur = skimage.filters.gaussian(image, sigma=sigma)

# perform inverse binary thresholding
mask = blur < t

# display the result
skimage.io.imshow(mask)

# Perform CCA on the mask
labeled_image = skimage.measure.label(mask, connectivity=2)

skimage.io.imshow(skimage.color.label2rbg(labeled_image, bg_label=0))

