import cv2 as cv
import matplotlib.pyplot as plt

# color spaces -> system of representing an array of colors
# BGR -> default cv color space

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# libraries other than opencv mostly use RGB format so image will have inverted colours when plotted
# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# grayscale images -> useful to see pixel intensity distribution in your image

# BGR to HSV (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# NOTE: you can't convert grayscale to hsv/lab etc. directly (do grayscale -> bgr -> hsv/lab etc.)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

cv.waitKey(0)