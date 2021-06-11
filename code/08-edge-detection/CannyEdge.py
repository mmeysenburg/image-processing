"""
 * Python script to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename> <sigma> <low_threshold> <high_threshold>
"""
import skimage.io
import skimage.feature
import sys

# read command-line arguments
filename = sys.argv[1]
sigma = float(sys.argv[2])
low_threshold = float(sys.argv[3])
high_threshold = float(sys.argv[4])

# load and display original image as grayscale
image = skimage.io.imread(fname=filename, as_gray=True)
skimage.io.imshow(image)

# perform Canny edge detection
edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)

# display edges
skimage.io.imshow(edges)
