"""
 * Python program to use OpenCV drawing tools to create a mask.
 *
"""
import numpy as np
import skimage.io
import skimage.draw

# Load the original image
image = skimage.io.imread("maize-roots.tif")
skimage.io.imshow(image)

# Create the basic mask
mask = np.ones(shape=image.shape[0:2], dtype="bool")

# Draw a filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
mask[rr, cc] = False

# Apply the mask and display the result
image[mask] = 0
skimage.io.imshow(mask)
