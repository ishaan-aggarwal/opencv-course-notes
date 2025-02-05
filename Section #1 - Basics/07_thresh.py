import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# Parameters: 
# - gray: input image
# - 150: threshold value - pixels above this become white (255), below become black (0)
# - 255: maximum value for pixels that pass the threshold
# - cv.THRESH_BINARY: threshold type - pixels > threshold become white, others become black

# Returns:
# - threshold: the threshold value used (150 here)
# - thresh: output image with the thresholding applied

cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# THRESH_BINARY_INV inverts the output - pixels < threshold become white, others become black
cv.imshow('Simple Thresholded Inverse', thresh_inv)


# Adaptive Thresholding
# Computer finds the optimal threshold value instead of having to speicfy it manually

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
 # Parameters:
 # - gray: source image
 # - 255: maximum value for pixels above threshold
 # - cv.ADAPTIVE_THRESH_GAUSSIAN_C: adaptive method using Gaussian window
 # - cv.THRESH_BINARY_INV: thresholding type (pixels below threshold become white)
 # - 11: size of pixel neighborhood used to calculate threshold value (must be odd)
 # - 9: constant subtracted from mean or weighted sum
 
 # Adaptive Thresholding Methods:
 # 1. cv.ADAPTIVE_THRESH_MEAN_C: threshold is mean of neighborhood area
 # 2. cv.ADAPTIVE_THRESH_GAUSSIAN_C: threshold is weighted sum of neighborhood values (Gaussian window)


cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
cv.destroyAllWindows()