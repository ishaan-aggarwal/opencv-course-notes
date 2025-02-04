import cv2 as cv
import numpy as np

# We can either draw on an actual image or create a dummy blank image and draw on it

blank = np.zeros((500, 500, 3), dtype='uint8') 
# (500, 500) -> shape, 3 -> no. of channels
# uint8 -> datatype for image

cv.imshow('blank', blank)

# 1. painting entire image to one color
blank[:] = 0, 0, 255 # BGR
cv.imshow('color fill', blank)

# you can also give a range of pixels
# Selects a rectangular region from rows 200-299 (vertical) and columns 300-399 (horizontal)
# (0, 0) -> top left corner
blank[200:300, 300:400] = 255, 0, 0
cv.imshow('blue box', blank)

# 2. Drawing a rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# filled in rectangle
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=cv.FILLED) # you can also use -1 in place of cv.FILLED
cv.imshow('Filled rectangle', blank)

# using dynamic values for points
cv.rectangle(blank, (0,0), (blank.shape[1] // 4, blank.shape[0] // 4), (255, 255, 255), thickness=3) # you can also use -1 in place of cv.FILLED
cv.imshow('quarter rectangle', blank)

# 3. Drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 0), thickness=3)
cv.imshow('Circle', blank)

# 4. Drawing a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 0), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello there', (0, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)