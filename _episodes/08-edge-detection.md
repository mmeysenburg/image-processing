---
title: "Edge Detection"
teaching: 20
exercises: 45
questions:
- "How can we automatically detect the edges of the objects in an image?"
objectives:
- "Apply Canny edge detection to an image."
- "Explain how we can use sliders to expedite finding appropriate parameter
values for our skimage function calls."
- "Create skimage windows with sliders and associated callback functions."
keypoints:
- "The `skimage.viewer.ImageViewer` is extended using a `skimage.viewer.plugins.Plugin`."
- "We supply a filter function callback when creating a Plugin."
- "Parameters of the callback function are manipulated interactively by creating sliders with the `skimage.viewer.widgets.slider()` function and adding them to the plugin."
---

In this episode, we will learn how to use skimage functions to apply *edge
detection* to an image. In edge detection, we find the boundaries or edges of
objects in an image, by determining where the brightness of the image changes
dramatically. Edge detection can be used to extract the structure of objects in
an image. If we are interested in the number, size, shape, or relative location
of objects in an image, edge detection allows us to focus on the parts of the
image most helpful, while ignoring parts of the image that will not help us.

For example, once we have found the edges of the objects in the image (or once
we have converted the image to binary using thresholding), we can
use that information to find the image *contours*, which we will learn about in
the following [connected components]({{ page.root }}/09-connected-components) episode. With the
contours, we can do things like counting the number of objects in the image,
measure the size of the objects, classify the shapes of the objects, and so on.

As was the case for blurring and thresholding, there are several different
methods in skimage that can be used for edge detection, so we will examine only
one in detail.

## Introduction to edge detection

To begin our introduction to edge detection, let us look at an image with a
very simple edge -- this grayscale image of two overlapped pieces of paper, one
black and and one white:

![Black and white image](../fig/07-bw.jpg)

The obvious edge in the image is the vertical line between the black paper and
the white paper. To our eyes, there is a quite sudden change between the black
pixels and the white pixels. But, at a pixel-by-pixel level, is the transition
really that sudden?

If we zoom in on the edge more closely, as in this image, we can see that the
edge between the black and white areas of the image is not a clear-cut line.

![Black and white edge pixels](../fig/07-bw-edge-pixels.jpg)

We can learn more about the edge by examining the color values of some of the
pixels. Imagine a short line segment, halfway down the image and straddling the
edge between the black and white paper. This plot shows the pixel values
(between 0 and 255, since this is a grayscale image) for forty pixels spanning
the transition from black to white.

![Gradient near transition](../fig/07-bw-gradient.png)

It is obvious that the "edge" here is not so sudden! So, any skimage method to
detect edges in an image must be able to decide where the edge is, and place
appropriately-colored pixels in that location.

## Canny edge detection

Our edge detection method in this workshop is *Canny edge detection*, created
by John Canny in 1986. This method uses a series of steps, some incorporating
other types of edge detection. The skimage `skimage.feature.canny()` function performs
the following steps:

1. A Gaussian blur (that is characterized by the `sigma` parameter, see [introduction]({{ page.root }}/06-blurring/)) is applied to remove noise
from the image. (So if we are doing edge detection via this function, we should
not perform our own blurring step.)
2. Sobel edge detection is performed on both the x and y dimensions, to find
the intensity gradients of the edges in the image. Sobel edge detection
computes the derivative of a curve fitting the gradient between light and
dark areas in an image, and then finds the peak of the derivative, which is
interpreted as the location of an edge pixel.
3. Pixels that would be highlighted, but seem too far from any edge, are
removed. This is called *non-maximum suppression*, and the result is edge lines
that are thinner than those produced by other methods.
4. A double threshold is applied to determine potential edges. Here extraneous
pixels caused by noise or milder color variation than desired are eliminated.
If a pixel's gradient value -- based on the Sobel differential -- is above the
high threshold value, it is considered a strong candidate for an edge. If the
gradient is below the low threshold value, it is turned off. If the gradient is
in between, the pixel is considered a weak candidate for an edge pixel.
5. Final detection of edges is performed using *hysteresis*. Here, weak
candidate pixels are examined, and if they are connected to strong candidate
pixels, they are considered to be edge pixels; the remaining, non-connected
weak candidates are turned off.

For a user of the `skimage.feature.canny()` edge detection function, there are three important
parameters to pass in: `sigma` for the Gaussian filter in step one and the low and high threshold values used in step four
of the process. These values generally are determined empirically, based on the
contents of the image(s) to be processed.

The following program illustrates how the `skimage.feature.canny()` method can be used to
detect the edges in an image.
We will execute the program on this image, which we used before in the [Thresholding]({{ page.root }}/07-thresholding/) episode:

![Colored shapes](../fig/07-junk.jpg)

We are interested in finding the edges of the shapes in the image, and so the
colors are not important. Our strategy will be to read the image as grayscale,
and then apply Canny edge detection.
Note that when reading the image with `skimage.io.imread(..., as_gray=True)` the image is converted to a float64 grayscale with the original dtype range being mapped to values ranging from 0.0 to 1.0.

This program takes three command-line arguments: the filename of the image to
process, and then two arguments related to the double thresholding in step four
of the Canny edge detection process. These are the low and high threshold
values for that step. After the required libraries are imported, the
program reads the command-line arguments and saves them in their respective
variables.

~~~
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
~~~
{: .python}

Next, the original images is read, in grayscale, and displayed.

~~~
# load and display original image as grayscale
image = skimage.io.imread(fname=filename, as_gray=True)
skimage.io.imshow(image)
~~~
{: .python}

Then, we apply Canny edge detection with this function call:

~~~
edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)
~~~
{: .python}

As we are using it here, the `skimage.feature.canny()` function takes four parameters.
The first parameter is the input image. The `sigma` parameter determines the
amount of Gaussian smoothing that is applied to the image. The next two
parameters are the low and high threshold values for the fourth step of the
process.

The result of this call is a binary image. In the image, the edges detected by
the process are white, while everything else is black.

Finally, the program displays the `edges` image, showing the edges that were
found in the original.

~~~
# display edges
skimage.io.imshow(edges)
~~~
{: .python}

Here is the result, for the colored shape image above,
with sigma value 2.0, low threshold value 0.1 and high threshold value 0.3:

![Output file of Canny edge detection](../fig/07-canny-edges.png)

Note that the edge output shown in an skimage window may look significantly
worse than the image would look if it were saved to a file due to resampling artefacts in the interactive image viewer.
The image above is the edges of the junk image, saved in a PNG file.
Here is how the same image looks when displayed in an skimage output window:

![Output window of Canny edge detection](../fig/07-canny-edge-output.png)


## Interacting with the image viewer using viewer plugins

As we have seen, for a user of the `skimage.feature.canny()` edge detection function,
three important parameters to pass in are sigma, and the low and high threshold values used
in step four of the process. These values generally are determined empirically,
based on the contents of the image(s) to be processed.

Here is an image of some glass beads that we can use as input into a Canny edge
detection program:

![Beads image](../fig/07-beads.jpg)

We could use the **CannyEdge.py** program above to find edges in this image. To
find acceptable values for the thresholds, we would have to run the program
over and over again, trying different threshold values and examining the
resulting image, until we find a combination of parameters that works best for
the image.

*Or*, we can write a Python program and create a viewer plugin that uses skimage *sliders*, that allow us
to vary the function parameters while the program is running. In
other words, we can write a program that presents us with a window like this:

![Canny UI](../fig/07-canny-ui.png)

Then, when we run the program, we can use the sliders to vary the
values of the sigma and threshold parameters until we are satisfied with the results.
After we have determined suitable values, we can
use the simpler program to utilize the parameters without bothering with the
user interface and sliders.

Here is a Python program that shows how to apply Canny edge detection, and how
to add sliders to the user interface. There are four parts to this program,
making it a bit (but only a *bit*) more complicated than the programs we have
looked at so far.
The added complexity comes from setting up the sliders for the parameters that were previously read from the command line:
In particular, we have added

* The `canny()` filter function that returns an edge image,
* The `cannyPlugin` plugin object, to which we add
* The sliders for *sigma*, and *low* and *high threshold* values, and
* The main program, i.e., the code that is executed when the program runs.

We will look at the main program part first, and then return to writing the plugin.
The first several lines of the main program are easily recognizable
at this point: saving the command-line argument, reading the image in
grayscale, and creating a window.

~~~
"""
 * Python script to demonstrate Canny edge detection
 * with sliders to adjust the thresholds.
 *
 * usage: python CannyTrack.py <filename>
"""
import skimage.io
import skimage.feature
import skimage.viewer
import sys


filename = sys.argv[1]
image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.io.imshow(image)
~~~
{: .python}

The `skimage.viewer.plugins.Plugin` class is designed to manipulate images.
It takes an `image_filter` argument in the constructor that should be a function.
This function should produce a new image as an output, given an image as the first argument, which then will be automatically displayed in the image viewer.

~~~
# Create the plugin and give it a name
canny_plugin = skimage.viewer.plugins.Plugin(image_filter=skimage.feature.canny)
canny_plugin.name = "Canny Filter Plugin"
~~~

We want to interactively modify the parameters of the filter function interactively.
Skimage allows us to further enrich the plugin by adding widgets, like `skimage.viewer.widgets.Slider`, `skimage.viewer.widgets.CheckBox`, `skimage.viewer.widgets.ComboBox`.
Whenever a widget belonging to the plugin is updated, the filter function is called with the updated parameters.
This function is also called a callback function.
The following code adds sliders for `sigma`, `low_threshold` and `high_thresholds`.

~~~
# Add sliders for the parameters
canny_plugin += skimage.viewer.widgets.Slider(
    name="sigma", low=0.0, high=7.0, value=2.0
)
canny_plugin += skimage.viewer.widgets.Slider(
    name="low_threshold", low=0.0, high=1.0, value=0.1
)
canny_plugin += skimage.viewer.widgets.Slider(
    name="high_threshold", low=0.0, high=1.0, value=0.2
)
~~~
{: .python}

A slider is a widget that lets you choose a number by dragging a handle along a line.
On the left side of the line, we have the lowest value, on the right side the highest value that can be chosen.
The range of values in between is distributed equally along this line.
All three sliders are constructed in the same way:
The first argument is the name of the parameter that is tweaked by the slider.
With the arguments `low`, and `high`, we supply the limits for the range of numbers that is represented by the slider.
The `value` argument specifies the initial value of that parameter, so where the handle is located when the plugin is started.
Adding the slider to the plugin makes the values available as parameters to the `filter_function`.

> ## How does the plugin know how to call the filter function with the parameters?
>
> The filter function will be called with the slider parameters according to their *names* as *keyword* arguments.
> So it is very important to name the sliders appropriately.
{: .callout}

Finally, we add the plugin the viewer and display the resulting user interface:

~~~
# add the plugin to the viewer and show the window
viewer += canny_plugin
viewer.show()
~~~
{: .python}

Here is the result of running the preceding program on the beads image, with a sigma value 1.0,
low threshold value 0.1 and high threshold value 0.3. The image
shows the edges in an output file.

![Beads edges (file)](../fig/07-beads-out.png)

> ## Applying Canny edge detection to another image (5 min)
>
> Now, navigate to the **Desktop/workshops/image-processing/08-edge-detection**
> directory, and run the **CannyTrack.py** program on the image of colored
> shapes, **junk.jpg**. Use a sigma of 1.0 and adjust low and high threshold sliders
> to produce an edge image that looks like this:
>
> ![Colored shape edges](../fig/07-canny-junk-edges.png)
>
> What values for the low and high threshold values did you use to
> produce an image similar to the one above?
>
> > ## Solution
> >
> > The colored shape edge image above was produced with a low threshold
> > value of 0.05 and a high threshold value of 0.07. You may be able to
> > achieve similar results with other threshold values.
> {: .solution}
{: .challenge}

> ## Using sliders for thresholding (30 min)
>
> Now, let us apply what we know about creating sliders to another, similar
> situation. Consider this image of a collection of maize seedlings, and
> suppose we wish to use simple fixed-level thresholding to mask out everything
> that is not part of one of the plants.
>
> ![Maize roots image](../fig/07-maize-roots.jpg)
>
> To perform the thresholding, we could first create a histogram, then examine
> it, and select an appropriate threshold value. Here, however, let us create
> an application with a slider to set the threshold value. Create a program
> that reads in the image, displays it in a window with a slider, and allows
> the slider value to vary the threshold value used. You will find the image
> in the **Desktop/workshops/image-processing/08-edge-detection** directory,
> under the name **maize-roots.jpg**.
>
> > ## Solution
> >
> > Here is a program that uses a slider to vary the threshold value used in
> > a simple, fixed-level thresholding process.
> >
> > ~~~
> > """
> >  * Python program to use a slider to control fixed-level
> >  * thresholding value.
> >  *
> >  * usage: python interactive_thresholding.py <filename>
> > """
> >
> > import skimage
> > import skimage.viewer
> > import sys
> >
> > filename = sys.argv[1]
> >
> >
> > def filter_function(image, sigma, threshold):
> >     masked = image.copy()
> >     masked[skimage.filters.gaussian(image, sigma=sigma) <= threshold] = 0
> >     return masked
> >
> >
> > smooth_threshold_plugin = skimage.viewer.plugins.Plugin(
> >     image_filter=filter_function
> > )
> >
> > smooth_threshold_plugin.name = "Smooth and Threshold Plugin"
> >
> > smooth_threshold_plugin += skimage.viewer.widgets.Slider(
> >     "sigma", low=0.0, high=7.0, value=1.0
> > )
> > smooth_threshold_plugin += skimage.viewer.widgets.Slider(
> >     "threshold", low=0.0, high=1.0, value=0.5
> > )
> >
> > image = skimage.io.imread(fname=filename, as_gray=True)
> >
> > viewer = skimage.viewer.ImageViewer(image=image)
> > viewer += smooth_threshold_plugin
> > viewer.show()
> > ~~~
> > {: .python}
> >
> > Here is the output of the program, blurring with a sigma of 1.5 and a
> > threshold value of 0.45:
> >
> > ![Thresholded maize roots](../fig/07-maize-roots-threshold.png)
> {: .solution}
{: .challenge}

Keep this plugin technique in your image processing "toolbox." You can use
sliders (or other interactive elements, see the [skimage documentation](https://scikit-image.org/docs/dev/api/skimage.viewer.widgets.html)) to vary other kinds of parameters, such as sigma for blurring, binary
thresholding values, and so on. A few minutes developing a program to tweak
parameters like this can save you the hassle of repeatedly running a program
from the command line with different parameter values.
Furthermore, skimage already comes with a few viewer plugins that you can check out in the [documentation](https://scikit-image.org/docs/dev/api/skimage.viewer.plugins.html).

## Other edge detection functions

As with blurring, there are other options for finding edges in skimage. These
include `skimage.filters.sobel()`, which you will recognize as part of the Canny
method. Another choice is `skimage.filters.laplace()`.
