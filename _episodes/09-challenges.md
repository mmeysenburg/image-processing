---
title: "Challenges"
teaching: 10
exercises: 40
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will provide two different challenges for you to attempt,
based on the skills you have acquired so far. One of the challenges will be
related to the shape of objects in images (*morphometrics*), while the other 
will be related to colors of objects in images (*colorimetrics*). We will not
provide solution code for either of the challenges, but your instructors should
be able to give you some gentle hints if you need them.

## Morphometrics: Bacteria Colony Counting

As mentioned in the workshop [introduction]({{ page.root }}/01-introduction), 
your morphometric challenge is to determine how many bacteria colonies are in 
each of these images. These images can be found in the 
**Desktop/workshops/image-processing/10-challenges/morphometric** directory. 

![Colony image 1](../fig/00-colonies01.jpg)

![Colony image 2](../fig/00-colonies02.jpg)

![Colony image 3](../fig/00-colonies03.jpg)

Write a Python program that uses skimage to count the number of bacteria
colonies in each image, and for each, produce a new image that highlights the colonies.
The image should look similar than this one:

![Sample morphometric output](../fig/00-colony-mask.png)

Additionally, print out the number of colonies for each image.



## Colorimetrics: titration color analysis

The video showing the titration process first mentioned in the workshop 
[introduction]({{ page.root }}/01-introduction/) episode can be found in the 
**Desktop/workshops/image-processing/10-challenges/colorimetric** directory.
Write a Python program that uses skimage to analyze the video on a
frame-by-frame basis. Your program should do the following:

1. Sample a kernel from the same location on each frame, and determine the 
	average red, green, and blue channel value.

2. Display a graph plotting the average color channel values as a function of
	the frame number, similar to this image:

	![Titration colors](../fig/00-colorimetric.png)

3. Save the graph as an image named **titration.png**.

4. Output a CSV file named **titration.csv**, with each line containing
	the frame number, average red value, average green value, and average
	blue value
