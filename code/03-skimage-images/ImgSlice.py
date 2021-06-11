"""
 * Python script demonstrating image modification and creation via
 * NumPy array slicing.
"""
import skimage.io

# load and display original image
image = skimage.io.imread(fname="board.jpg")
skimage.io.imshow(image)

# extract, display, and save sub-image
clip = image[60:151, 135:481, :]
skimage.io.imshow(clip)
skimage.io.imsave(fname="clip.tif", arr=clip)

# replace clipped area with sampled color
color = image[330, 90]
image[60:151, 135:481] = color
skimage.io.imshow(image)
