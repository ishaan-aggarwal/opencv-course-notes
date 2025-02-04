import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# smoothing and blurring is done to reduce noise

# 1. Averaging 
# computes kernel middle pixel intensity by taking average of its surrounding pixels intensities
# the kernel window slides across and then down the image to compute this for all pixels
average = cv.blur(img, (7,7))
# higher kernel size -> more blur
cv.imshow('Average blur', average)

# 2. Gaussian blur
# Does same thing as averaging except each surrounding pixel is given a weight and product of those weights along with intensity gives value for the center
# leads to less blurring than the averaging method but gives a more natural result
gauss = cv.GaussianBlur(img, (7,7), 0)
# 3rd argument -> sigmaX (standard deviation in x direction)
cv.imshow('Gaussian blur', gauss)

# 3. Median blur
# Takes median (instead of average) of surrounding pixels for the middle pixel value
# More effective in reducing noise (compared to avg and gaussian), especially salt and pepper noise 
median = cv.medianBlur(img, 7)
# 7 -> automatically considers (7,7) kernel size
# Median blurring is not meant for high kernel sizes (maybe take 2 or 3)
cv.imshow('Median Blur', median)

# 4. Bilateral blurring
# Most effective
# Other blurring methods apply blur uniformly across the image, which can result in loss of edges.
# Bilateral blurring, however, applies blur while preserving the edges, making it more effective for edge-aware smoothing.
bilateral = cv.bilateralFilter(img, 10, 30, 20)
# Parameters:
# 1. image to blur
# 2. Diameter of pixel neighborhood.
# 3. SigmaColor: Larger value means more colors in the neighborhood will be considered.
# 4. SigmaSpace: Larger value means pixels farther from the central pixel will influence its blurring.
cv.imshow('Bilateral blur', bilateral)

# NOTE: higher values for parameters in median and bilateral lead to a washed out, smudged looking result

cv.waitKey(0)