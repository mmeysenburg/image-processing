"""
* Python script to load a color image as grayscale.
*
* usage: python LoadGray.py <filename>
"""
import sys
import skimage.io
import skimage.color

# read input image, based on filename parameter
image = skimage.io.imread(fname=sys.argv[1], as_gray=True)

# display grayscale image
skimage.io.imshow(image)
