import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

# operate in binary manner -> 0 (pixel turned off), 1 (pixel turned on)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) 
 # .copy() creates a new image instead of modifying original                                                                    
 # Blank has only 1 channel => grayscale. The color will be determined by x value regardless of y and z in (x,y,z)
 # -1 fills the rectangle (any negative thickness fills shape)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('circle', circle)

# 1. bitwise AND --> intersecting regions
bitw_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise AND', bitw_and)
 # returns intersection of both images (if pixel is 0 in either image, it is set to 0)

# 2. bitwise OR --> non-intersecting and intersecting regions
bitw_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise OR', bitw_or)
 # returns union of both images (if pixel is 1 in either image, it is set to 1)

# 3. bitwise XOR --> non-intersecting regions
bitw_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise XOR', bitw_xor)
 # returns non intersecting parts of the images (bitw_or - bitw_and = bitw_xor)

# bitwise NOT
bitw_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitw_not)
 # inverts the image

cv.waitKey(0)
cv.destroyAllWindows()