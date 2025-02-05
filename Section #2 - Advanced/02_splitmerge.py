import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# an image is a merge of its respective color channels (BGR image made out of B, G, R channels)

# splitting a BGR image into its channels
b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# these are actually displayed as grayscale images in opencv (since they have 1 channel)
# darker area -> lesser concentration of that color, lighter area -> more concentration of the color
print(img.shape)
print(b.shape) 
print(g.shape)
print(r.shape)

# merging the channels
merged = cv.merge([b, g, r])
cv.imshow('Merged image', merged)

# Viewing the actual channel images instead of in graycale
# We have to reconstruct the image by merging the individual channel with a blank image (of one channel with size as image.shape[:2])

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
# again lighter regions represent higher concentrations of that color, this is just to visualize in that color instead of grayscale

cv.waitKey(0)
cv.destroyAllWindows()