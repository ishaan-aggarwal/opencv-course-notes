import cv2 as cv

# Face detection:
# - Detects the presence of faces in an image
# - Performed using classifiers (opencv has a lot of pre-trained classifiers)
# - https://github.com/opencv/opencv/tree/4.x/data/haarcascades

# Two main classifiers
# - Haar Cascades -> Sensitive to noise
# - Local Binary Patterns -> more advanced haar cascades (less prone to noise), TODO

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Original image', img)

# Haar cascades look at the edges of an object in the image and try to determine if it's a face
# They don't use skin tone or color so we can use grayscale image
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# scaleFactor: How much the image size is reduced at each image scale (e.g., 1.1 means 10% reduction)
# minNeighbors: The number of neighbors a rectangle should have to be called a face
# faces_rect: list of coordinates of the detected faces in the format (x, y, w, h)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
cv.destroyAllWindows()
