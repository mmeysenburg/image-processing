---
title: "Drawing and Bitwise Operations"
teaching: 45
exercises: 45
questions:
- "How can we draw on skimage images and use bitwise operations and masks to
select certain parts of an image?"
objectives:
- "Create a blank, black skimage image."
- "Draw rectangles and other shapes on skimage images."
- "Explain how a white shape on a black background can be used as a mask to
select specific parts of an image."
- "Use bitwise operations to apply a mask to an image."
keypoints:
- "We can use the NumPy `zeros()` function to create a blank, black image."
- "We can draw on skimage images with functions such as
`skimage.draw.rectangle()`, `skimage.draw.circle()`, `skimage.draw.line()`,
and more."
- "The drawing functions return indices to pixels that can be set directly."
---

The next series of episodes covers a basic toolkit of skimage operators. With 
these tools, we will be able to create programs to perform simple analyses of 
images based on changes in color or shape.

## Drawing on images

Often we wish to select only a portion of an image to analyze, and ignore the 
rest. Creating a rectangular sub-image with slicing, as we did in the 
[skimage Images]({{ page.root }}/03-skimage-images) lesson is one option for
simple cases. Another option is to create another special image, of the same 
size as the original, with white pixels indicating the region to save and
black pixels everywhere else. Such an image is called a *mask*. In preparing 
a mask, we sometimes need to be able to draw a shape -- a circle or a 
rectangle, say -- on a black image. skimage provides tools to do that. 

Consider this image of maize seedlings:

![Maize seedlings](../fig/03-maize-roots.jpg)

Now, suppose we want to analyze only the area of the image containing the roots
themselves; we do not care to look at the kernels, or anything else 
about the plants. Further, we wish to exclude the frame of the container holding
the seedlings as well. Exploration with ImageJ could tell us that the 
upper-left coordinate of the sub-area we are interested in is *(44, 357)*,
while the lower-right coordinate is *(720, 740)*. These coordinates are shown
in *(x, y)* order. 

A Python program to create a mask to select only that area of the image would
start with a now-familiar section of code to open and display the original
image. (Note that the display portion is used here for pedagogical purposes; it
 would probably not be used in production code.)

~~~
"""
 * Python program to use skimage drawing tools to create a mask.
 *
"""
import skimage
from skimage.viewer import ImageViewer
import numpy as np

# Load and display the original image
image = skimage.io.imread("maize-roots.tif")
viewer = ImageViewer(image)
viewer.show()
~~~
{: .python}

As before, we first import `skimage`. We also import the NumPy library, and give
it an alias of `np`. NumPy is necessary when we create the initial mask image,
and the alias saves us a little typing. Then, we load and display the initial
image in the same way we have done before.

NumPy allows indexing of images/arrays with "boolean" arrays of the same size.
Indexing with a boolean array is also called mask indexing. The "pixels" in such
a mask array can only take two values: `True` or `False`. When indexing an image
with such a mask, only pixel values at positions where the mask is `True` are
accessed. But first, we need to generate a mask array of the same size as the
image. Luckily, the NumPy library provides a function to create just such an
array. The next section of code shows how.

~~~
# Create the basic mask
mask = np.ones(shape=image.shape[0:2], dtype="bool")
~~~
{: .python}

We create the mask image with the 

`mask = np.ones(shape=image.shape[0:2], dtype="bool")`

function call. The first argument to the `ones()` function is the shape of 
the original image, so that our mask will be exactly the same size as the 
original. Notice, that we have only used the first two indices of our shape. We
omitted the channel dimension. Indexing with such a mask will change all channel
values simultaneously. The second argument, `dtype = "bool"`, indicates that the
elements in the array should be booleans -- i.e., values are either `True` or
`False`. Thus, even though we use `np.ones()` to create the mask, its pixel values 
are in fact not `1` but `True`. You could check this, 
e.g., by `print(mask[0, 0])`.

Next, we draw a filled, rectangle on the mask:

~~~
# Draw filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
mask[rr, cc] = False
~~~
{: .python}

The parameters of the `rectangle()` function `(357, 44)` and `(740, 720)`, are the coordinates of the 
upper-left (`start`) and lower-right (`end`) corners of a rectangle in *(y, x)* order. 
The function returns the rectangle as row (`rr`) and column (`cc`) coordinate arrays.

> ## Check the documentation!
> 
> When using an skimage function for the first time -- or the fifth time -- 
> it is wise to check how the function is used, via the online 
> [skimage documentation](https://scikit-image.org/docs/dev/user_guide) or via
> other usage examples on programming-related sites such as 
> [Stack Overflow](https://stackoverflow.com/). Basic information about skimage
> functions can be found interactively in Python, via commands like 
> `help(skimage)` or `help(skimage.draw.rectangle)`. Take notes in your lab 
> notebook. And, it is always wise to run some test code to verify that the 
> functions your program uses are behaving in the manner you intend.
{: .callout}

> ## Variable naming conventions!
> 
> You may have wondered why we called the return values of the rectangle function
> `rr` and `cc`?! You may have guessed that `r` is short for `row` and `c` is short for `column`. 
> However, the rectangle function returns mutiple rows and columns; thus we used a convention 
> of doubling the letter `r` to `rr` (and `c` to `cc`) to indicate that those are 
> multiple values. In fact it may have even been clearer to name those variables
> `rows` and `columns`; however this would have been also much longer. 
> Whatever you decide to do, try to stick to some already existing conventions,
> such that it is easier for other people to understand your code.
{: .callout}

The final section of the program displays the mask we just created:

~~~
# Display constructed mask
viewer = ImageViewer(mask)
viewer.show()
~~~
{: .python}

Here is what our constructed mask looks like:

![Maize image mask](../fig/03-maize-mask.png)

> ## Other drawing operations (15 min)
> 
> There are other functions for drawing on images, in addition to the 
> `skimage.draw.rectangle()` function. We can draw circles, lines, text, and
> other shapes as
> well. These drawing functions may be useful later on, to help annotate images
> that our programs produce. Practice some of these functions here. Navigate to
> the **Desktop/workshops/image-processing/04-drawing-bitwise** directory, and
> edit the **DrawPractice.py** program. The program creates a black, 800x600 
> pixel image. Your task is to draw some other colored shapes and lines on the
> image, perhaps something like this:
> 
> ![Sample shapes](../fig/03-draw-practice.jpg)
> 
> Circles can be drawn with the `skimage.draw.circle()` function, which takes three
> parameters: x, y point of the center of the circle, and the radius of the
> filled circle. There is an optional `shape` parameter that can be supplied to
> this function. It will limit the output coordinates for cases where the circle
> dimensions exceed the ones of the image.
> 
> Lines can be drawn with the `skimage.draw.line()` function, which takes four
> parameters: the image to draw on, the (x, y) coordinate of one end of the
> segment, the (x, y) coordinate of the other end of the segment, and the color
> for the line.
> 
> Other drawing functions supported by skimage can be found in the 
> [skimage reference pages](https://scikit-image.org/docs/dev/api/skimage.draw.html?highlight=draw#module-skimage.draw).
> 
> > ## Solution
> > 
> > Here is an overly-complicated version of the drawing program, to draw 
> > shapes that are randomly placed on the image.
> > 
> > ~~~
> > """
> >  * Program to practice with skimage drawing methods.
> > """
> > import random
> > import numpy as np
> > import skimage
> > from skimage.viewer import ImageViewer
> >
> > # create the black canvas
> > image = np.zeros(shape=(600, 800, 3), dtype="uint8")
> >
> > # WRITE YOUR CODE TO DRAW ON THE IMAGE HERE
> > for i in range(15):
> >     x = random.random()
> >     if x < 0.33:
> >         rr, cc = skimage.draw.circle(
> >             random.randrange(600),
> >             random.randrange(800),
> >             radius=50,
> >             shape=image.shape[0:2],
> >         )
> >         color = (0, 0, 255)
> >     elif x < 0.66:
> >         rr, cc = skimage.draw.line(
> >             random.randrange(600),
> >             random.randrange(800),
> >             random.randrange(600),
> >             random.randrange(800),
> >         )
> >         color = (0, 255, 0)
> >     else:
> >         rr, cc = skimage.draw.rectangle(
> >             start=(random.randrange(600), random.randrange(800)),
> >             extent=(50, 50),
> >             shape=image.shape[0:2],
> >         )
> >         color = (255, 0, 0)
> >
> >     image[rr, cc] = color
> >
> > # display the results
> > viewer = ImageViewer(image)
> > viewer.show()
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

## Image modification

All that remains is the task of modifying the image using our mask in such a
way that the areas with `True` pixels in the mask are not shown in the image
any more.

> ## How does a mask work? (optional, not included in timing)
> 
> Now, consider the mask image we created above. The values of the mask that 
> corresponds to the portion of the image we are interested in are all `False`,
> while the values of the mask that corresponds to the portion of the image we
> want to remove are all `True`. 
> 
> How do we change the original image using the mask?
> 
>> ## Solution
>> 
>> When indexing the image using the mask, we access only those pixels at
>> positions where the mask is `True`. So, when indexing with the mask, one
>> can set those values to 0, and effectively remove them from the image.
> {: .solution}
{: .challenge}

Now we can write a Python program to use a mask to retain only the portions
of our maize roots image that actually contains the seedling roots. We load the 
original image and create the mask in the same way as before:

~~~
"""
 * Python program to apply a mask to an image.
 *
"""
import numpy as np
import skimage
from skimage.viewer import ImageViewer

# Load the original image
image = skimage.io.imread("maize-roots.tif")

# Create the basic mask
mask = np.ones(shape=image.shape[0:2], dtype="bool")

# Draw a filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
mask[rr, cc] = False
~~~
{: .python}

Then, we use numpy indexing to remove the portions of the image, where the mask
is `True`:

~~~
# Apply the mask and display the result
image[mask] = 0
~~~
{: .python}

Then, we display the masked image.

~~~
viewer = ImageViewer(image)
viewer.show()
~~~
{: .python}

The resulting masked image should look like this:

![Applied mask](../fig/03-applied-mask.jpg)

> ## Masking an image of your own (optional, not included in timing)
> 
> Now, it is your turn to practice. Using your mobile phone, tablet, webcam, or
> digital camera, take an image of an object with a simple overall geometric 
> shape (think rectangular or circular). Copy that image to the 
> **Desktop/workshops/image-processing/04-drawing-bitwise** directory. Copy the
> **MaskAnd.py** program to another file named **MyMask.py**. Then, edit the
> **MyMask.py** program to use a mask to select only the primary object in your
> image. For example, here is an image of a remote control:
> 
> ![Remote control image](../fig/03-remote-control.jpg)
> 
> And, here is the end result of a program masking out everything but the 
> remote.
> 
> ![Remote control masked](../fig/03-remote-control-masked.jpg)
> 
> > ## Solution
> > 
> > Here is a Python program to produce the cropped remote control image shown 
> > above. Of course, your program should be tailored to your image.
> > 
> > ~~~
> > """
> >  * Python program to apply a mask to an image.
> >  *
> > """
> > import numpy as np
> > import skimage
> > from skimage.viewer import ImageViewer
> >
> > # Load the original image
> > image = skimage.io.imread("./fig/03-remote-control.jpg")
> >
> > # Create the basic mask
> > mask = np.ones(shape=image.shape[0:2], dtype="bool")
> >
> > # Draw a filled rectangle on the mask image
> > rr, cc = skimage.draw.rectangle(start=(93, 1107), end=(1821, 1668))
> > mask[rr, cc] = False
> >
> > # Apply the mask and display the result
> > image[mask] = 0
> > viewer = ImageViewer(image)
> > viewer.show()
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Masking a 96-well plate image (30 min)
> 
> Consider this image of a 96-well plate that has been scanned on a flatbed 
> scanner. 
> 
> ![96-well plate](../fig/03-wellplate.jpg)
> 
> Suppose that we are interested in the colors of the solutions in each of the 
> wells. We *do not* care about the color of the rest of the image, i.e., the 
> plastic that makes up the well plate itself. 
> 
> Navigate to the **Desktop/workshops/image-processing/04-drawing-bitwise**
> directory; there you will find the well plate image shown above, in the file
> named **wellplate.tif**. In this directory you will also find a text file 
> containing the (x, y) coordinates of the center of each of the 96 wells on 
> the plate, with one pair per line; this file is named **centers.txt**. You 
> may assume that each of the wells in the image has a radius of 16 pixels. 
> Write a Python program that reads in the well plate image, and the centers 
> text file, to produce a mask that will mask out everything we are not 
> interested in studying from the image. Your program should produce output 
> that looks like this:
> 
> ![Masked 96-well plate](../fig/03-wellplate-masked.jpg)
> 
> > ## Solution
> > 
> > This program reads in the image file based on the first command-line 
> > parameter, and writes the resulting masked image to the file named in the 
> > second command line parameter. 
> > 
> > ~~~
> > """
> >  * Python program to mask out everything but the wells
> >  * in a standardized scanned 96-well plate image.
> > """
> > import numpy as np
> > import skimage
> > from skimage.viewer import ImageViewer
> > import sys
> >
> > # read in original image
> > image = skimage.io.imread(sys.argv[1])
> >
> > # create the mask image
> > mask = np.ones(shape=image.shape[0:2], dtype="bool")
> >
> > # open and iterate through the centers file...
> > with open("centers.txt", "r") as center_file:
> >     for line in center_file:
> >         # ... getting the coordinates of each well...
> >         tokens = line.split()
> >         x = int(tokens[0])
> >         y = int(tokens[1])
> >
> >         # ... and drawing a white circle on the mask
> >         rr, cc = skimage.draw.circle(y, x, radius=16, shape=image.shape[0:2])
> >         mask[rr, cc] = False
> >
> > # apply the mask
> > image[mask] = 0
> >
> > # write the masked image to the specified output file
> > skimage.io.imsave(fname=sys.argv[2], arr=image)
> > ~~~
> > {: .python}
> > 
> {: .solution}
{: .challenge}

> ## Masking a 96-well plate image, take two (optional, not included in timing)
> 
> If you spent some time looking at the contents of the **centers.txt** file
> from the previous challenge, you may have noticed that the centers of each
> well in the image are very regular. *Assuming* that the images are scanned in
> such a way that the wells are always in the same place, and that the image is
> perfectly oriented (i.e., it does not slant one way or another), we could 
> produce our well plate mask without having to read in the coordinates of the 
> centers of each well. Assume that the center of the upper left well in the 
> image is at location x = 91 and y = 108, and that there are 70 pixels between
> each center in the x dimension and 72 pixels between each center in the y 
> dimension. Each well still has a radius of 16 pixels. Write a Python program 
> that produces the same output image as in the previous challenge, but 
> *without* having to read in the **centers.txt** file. *Hint: use nested for
> loops.*
> 
> > ## Solution
> > 
> > Here is a Python program that is able to create the masked image without
> > having to read in the **centers.txt** file. 
> > 
> > ~~~
> > """
> >  * Python program to mask out everything but the wells
> >  * in a standardized scanned 96-well plate image, without
> >  * using a file with well center location.
> > """
> > import numpy as np
> > import skimage
> > from skimage.viewer import ImageViewer
> > import sys
> >
> > # read in original image
> > image = skimage.io.imread(sys.argv[1])
> >
> > # create the mask image
> > mask = np.ones(shape=image.shape[0:2], dtype="bool")
> >
> > # upper left well coordinates
> > x0 = 91
> > y0 = 108
> >
> > # spaces between wells
> > deltaX = 70
> > deltaY = 72
> >
> > x = x0
> > y = y0
> >
> > # iterate each row and column
> > for row in range(12):
> >     # reset x to leftmost well in the row
> >     x = x0
> >     for col in range(8):
> >
> >         # ... and drawing a white circle on the mask
> >         rr, cc = skimage.draw.circle(y, x, radius=16, shape=image.shape[0:2])
> >         mask[rr, cc] = False
> >         x += deltaX
> >     # after one complete row, move to next row
> >     y += deltaY
> >
> > # apply the mask
> > image[mask] = 0
> >
> > # write the masked image to the specified output file
> > skimage.io.imsave(fname=sys.argv[2], arr=image)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
