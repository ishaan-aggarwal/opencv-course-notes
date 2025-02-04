import cv2 as cv
import numpy as np

# Contours -> boundaries of objects
# NOTE: contours and edges are thought of as same but mathematically they are different

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# grab edges using canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Method 1 - finding contours using canny edges method

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# 2nd argument -> mode in which to find contours. The modes are:
# cv.RETR_TREE - if you want all hierarchical contours, i.e, contours that are in a hierarchical structure
# cv.RETR_EXTERNAL - if you only want the external contours
# cv.RETR_LIST - if you want all contours in the image
# 3rd argument -> contour approximation method. Their values can be:
# cv.CHAIN_APPROX_NONE - just returns all contours
# cv.CHAIN_APPROX_SIMPLE - compresses all contours returned into simple ones that make more sense. For example, this will compress a line and return just 2 endpoints as contours instead of all the points in that line as returned by CHAIN_APPROX_NONE.

# contours -> python list of coordinates of all contours found in the image
# hierarchies -> hierarchical representation of the contours (advanced stuff idk)

print(f'{len(contours)} contours found.') # number of contours found

# Now blurring the image before passing to canny and finiding contours
blur = cv.GaussianBlur(gray,  (5,5), cv.BORDER_DEFAULT)
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Blur canny Edges', canny)

contours2, hierarchies2 = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} contours found (blur).')
# Just by blurring the image a little, we reduced the contours to 380 (from 2794)

# Method 2 of finding contours - using threshold function
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# threshold converts an image to binary
# all pixles below 125 are set to 0 (black), and all above 125 are set to 255 (white)

contours3, hierarchies3 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
print(f'{len(contours3)} contours found (thresh).')

cv.imshow('thresh image', thresh)


# you can visualize contours found by drawing over the image
blank = np.zeros(img.shape, dtype='uint8')

cv.drawContours(blank, contours3, -1, (0,0,255), 1)
# blank -> image over which to draw
# contours3 -> list of contours
# -1 (contour index) -> draw all contours (you can specify a number)

cv.imshow('blank with contours using thresh', blank)

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('blank with contours using canny', blank)

# contours using canny is better than using threshold (this is for simpler contours)

cv.waitKey(0)