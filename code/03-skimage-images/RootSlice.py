"""
 * Python script to extract a sub-image containing only the plant and
 * roots in an existing image.
"""
import skimage.io

# load and display original image
image = skimage.io.imread(fname="roots.jpg")
skimage.io.imshow(image)

# extract, display, and save sub-image
# WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:

skimage.io.imshow(clip)


# WRITE YOUR CODE TO SAVE clip HERE
