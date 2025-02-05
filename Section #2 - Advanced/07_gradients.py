import cv2 as cv
import numpy as np

# Gradients represent the change in intensity or color in an image.
# They highlight edge-like regions where there is a significant change in pixel values.
# While gradients and edges are related, they are not the same mathematically.
# From a programming perspective, gradients can be used to detect edges in images.

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Original image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Two methods to find edges (other than canny)

# 1. Laplacian - not used much in advanced projects
lap = cv.Laplacian(gray, cv.CV_64F)  
 # The Laplacian operator computes the second derivative of the image, detecting areas of rapid intensity change (edges).  
 # It highlights regions where pixel values change quickly, making edges more prominent.
lap = np.uint8(np.absolute(lap))  
 # Convert the result to an 8-bit image (0-255) to properly display it.  
 # Taking the absolute value ensures all gradients are positive, as pixel values can't be negative.
cv.imshow('Laplacian', lap)  
 # The output resembles a pencil-drawn version of the image with smudged edges.  
 # Strong intensity changes appear as bright lines, while uniform regions remain dark.

# 2. Sobel
# Computes gradient in 2 directions (x and y)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# Parameters:
# - src: Source image.
# - ddepth: Desired depth of the destination image (cv.CV_64F for 64-bit float).
# - dx: Order of the derivative in the x-direction (1 means first derivative, 0 means none).
# - dy: Order of the derivative in the y-direction (1 means first derivative, 0 means none).

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined sobel', combined_sobel)

# 3. Canny - multistage process, more advanced algorithm
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()