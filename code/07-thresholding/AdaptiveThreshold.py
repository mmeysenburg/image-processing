"""
 * Python script to demonstrate adaptive thresholding using Otsu's method.
 *
 * usage: python AdaptiveThreshold.py <filename> <sigma>
"""
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.filters

# get filename and sigma value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])

# read and display the original image
image = skimage.io.imread(fname=filename)
skimage.io.imshow(image)

# grayscale and blur before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma=sigma)

# perform adaptive thresholding
t = skimage.filters.thresh_otsu(blur)
mask = blur > t

skimage.io.imshow(mask)

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
skimage.io.imshow(sel)
