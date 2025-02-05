
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(title, hist):
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')
    plt.plot(hist)
    plt.xlim([0,256])

# Histograms are used to visualize distribution of pixel intensities in an image 
# This is useful in projects where we are trying to equalize the image so that there is no peaking of pixel values

img = cv.imread('../Resources/Photos/cats.jpg')
# img = cv.imread('../Resources/Photos/cats 2.jpg')

plt.ion()  # Enable interactive mode to prevent Matplotlib from blocking execution and allow all windows to close when the script ends

blank = np.zeros(img.shape[:2], dtype='uint8')

# HISTOGRAMS FOR GRAYSCALE IMAGES

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
 # Parameters:
 # 1. list of images for which to calculate the histrogram
 # 2. list of index of the channel(s) for which we have to compute the histogram
 # 3. Mask (if we want to calculate histogram for a specific part of the image)
 # 4. histsize - Number of bins (intensity ranges) we want to use to compute histogram
 # 5. range of all possible pixel values

plot_histogram('Grayscale Histogram', gray_hist)

# The x-axis (bins) represents pixel intensity values from 0 (black) to 255 (white)
# The y-axis shows how many pixels have each intensity value
# For example, a peak at x=50 with y=4000 means 4000 pixels in the image have an intensity value of 50

# Histogram with mask
mask = cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked_img = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Gray Masked image', masked_img)

gray_hist_mask = cv.calcHist([gray], [0], mask, [256], [0,256])

plot_histogram('Grayscale Histogram with Mask', gray_hist_mask)

# HISTOGRAMS FOR COLOR IMAGES
# cv.imshow('Cats', img)
color_masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Color Masked Image', color_masked)

colors = ('b', 'g', 'r')

plt.figure()
# plt.title('Color Histogram')
plt.title('Color Histogram Mask')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')

for i,col in enumerate(colors):
    # hist = cv.calcHist([img], [i], None, [256], [0, 256])
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
 
# plt.pause(0.001) # Matplotlib sometimes needs a short pause to render properly.
plt.show()
cv.waitKey(0)
plt.close('all')
cv.destroyAllWindows()