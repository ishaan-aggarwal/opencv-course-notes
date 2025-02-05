import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

# Masking - can be used to remove any unwanted parts of an image
#NOTE: dimensions of the mast MUST be the same as dimensions of the image

blank = np.zeros(img.shape[:2], dtype='uint8') 

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

masked_img = cv.bitwise_and(img, img, mask=circle)
 # This operation performs a pixel-wise AND between the input image and itself, but only for pixels where the mask is white (255/1), effectively keeping only the parts of the image where the mask has white pixels while setting all other areas to black (0).
 # The reason img is used twice (as both src1 and src2) is because we want to preserve the original image values where the mask allows, rather than performing an AND between two different images.
cv.imshow('Masked image', masked_img)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) 

random_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Random Shape', random_shape)

masked = cv.bitwise_and(img,img,mask=random_shape)
cv.imshow('Random Shaped Masked Image', masked)


cv.waitKey(0)
cv.destroyAllWindows()