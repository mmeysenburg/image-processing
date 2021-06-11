"""
 * Python script to demonstrate simple thresholding.
 *
 * usage: python Threshold.py <filename> <sigma> <threshold>
"""
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.filters
import skimage.util.dtype

# get filename, kernel size, and threshold value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])
t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread(fname=filename)
skimage.io.imshow(image)

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma=sigma)

# perform inverse binary thresholding
t = skimage.filters.thresh_otsu(blur)
mask = blur < t

# display the mask image
skimage.io.imshow(mask)

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
skimage.io.imshow(sel)
