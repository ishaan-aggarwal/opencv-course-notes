# We use cv.warpAffine() for most which takes in the image, a matrix, and the image dimensions

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# 1. Translation
# Shifting image along x and y axes (up, down, left, right, and any combination of them)
def translate(img, x, y):
    # x, y -> number of pixels to shift along the x and y axis respectively
    trans_mat = np.float32([ [1,0,x], [0,1,y] ])
    dimensions = (img.shape[1], img.shape[0])    # (width, height)
    return cv.warpAffine(img, trans_mat, dimensions)

# -x --> shift Left
# -y --> shift Up
# x --> shift Right
# y --> shift Down

translated1 = translate(img, 100, 100)
cv.imshow('Translate right down', translated1)

translated2 = translate(img, -100, 100)
cv.imshow('Translate left down', translated2)

translated3 = translate(img, -100, -100)
cv.imshow('Translate left up', translated3)

translated4 = translate(img, 100, -100)
cv.imshow('Translate right up', translated4)


# 2. Rotation
def rotate(img, angle, rotPoint=None):
    # rotPoint -> point of rotation (rotate around center if None)
    # angle -> degrees
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    # 3rd argument -> you can scale the image as well (1.0 -> Not scaled)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated 45 deg', rotated)
# you can give -45 to rotate in the other direction

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)
# this rotation includes the black triangles introduced in previous rotated image since it is also a part of rotated
# Don't rotate a rotated image, instead add the angles and rotate original image once

# 3. Resizing
# done in 03_basic_functions

# 4. Flipping
flip = cv.flip(img, 0)
# 2nd argument: flip code -> can be 0 (flip vertically), 1 (flip horizontally) or -1 (both vertically and horizontally)
cv.imshow('Flipped', flip)


# 5. Cropping
# done in 03_basic_functions

cv.waitKey(0)
cv.destroyAllWindows()