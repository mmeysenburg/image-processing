"""
* Python script to load a color image as grayscale.
*
* usage: python LoadGray.py <filename>
"""
import sys
import skimage.io
import skimage.color

# read input image, based on filename parameter
image = skimage.io.imread(fname=sys.argv[1])

# display original image
skimage.io.imshow(image)

# convert to grayscale and display
gray_image = skimage.color.rgb2gray(image)
skimage.io.imshow(gray_image)
