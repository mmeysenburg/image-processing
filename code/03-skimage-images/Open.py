"""
 * Python program to open, display, and save an image.
 *
"""
import skimage.io

# read image
image = skimage.io.imread(fname="chair.jpg")

# display image and wait for keypress, using a resizable window
skimage.io.imshow(image)

# save a new version in .tif format
skimage.io.imsave(fname="chair.tif", arr=image)
