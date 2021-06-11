"""
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
"""
import sys
import skimage.io

# read input image, based on filename parameter
image = skimage.io.imread(fname=sys.argv[1])

# display original image
skimage.io.imshow(image)

# keep only high-intensity pixels
image[image < 128] = 0

# display modified image
skimage.io.imshow(image)
