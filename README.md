# Photograph-Sketchification

This project/model is highly useful in drawing sketch of concentrated area inside or around the body/material.
It can be used by artists, explorers also by scientists to get the structure of densed bodies floating in the space 
it can give the idea of concentrated/densed area of a body to determine its original structure.

This project transforms a color image into a pencil sketch using Python and OpenCV. It starts by reading the image, converting it to grayscale, and inverting the grayscale version to enhance contrast and prepare for the sketch effect.

Next, a Gaussian blur is applied to the inverted image to soften details, and then it’s inverted again. Finally, the original grayscale image is blended with the blurred inverted image using image division, creating a realistic pencil sketch. The result is displayed alongside the original for visual comparison.
