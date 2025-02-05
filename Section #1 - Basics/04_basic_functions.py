import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Blur
# Essentially removes some noise from the image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# (3,3) -> kernel size. used in blur computation. has to be odd number. increase it to increase blur
cv.imshow('Blur', blur)

# Edge Cascade
# Basically trying to find the edges present in the image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# To reduce the number of edges, you can pass in the blurred image
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Blur Canny Edges', canny2)

# Dilating the image
# Uses canny edges as a structuring element
# Makes the edges thicker ???
dilated = cv.dilate(canny2, (3, 3), iterations=1)
# (3,3) -> kernel size.
cv.imshow('Dilated', dilated)

# Eroding
# This gets back the structuring element (canny edges) from a dilated image. But it is not an exact result
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resizing 
# Aspect ratio is ignored
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) 
# interpolation=cv.INTER_AREA -> default. Useful when shrinking to smaller dimensions than original image
# interpolation=cv.INTER_LINEAR     or      interpolation=cv.INTER_CUBIC  would be better for scaling up an image. Cubic is the slowest but gives best results.
cv.imshow('Resized image', resize)

# Cropping
# Basic array slicing
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
cv.destroyAllWindows()