
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# We only need to load features and labels once and can then comment out the lines
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# img = cv.imread('../Resources/Faces/val/ben_afflek/5.jpg')
img = cv.imread('../Resources/Faces/val/madonna/4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    # Prediction
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence = {confidence}')
    # Displaying on image
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.putText(img, str(people[label]), (img.shape[1]//2 - len(people[label]) * 10, img.shape[0] - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

cv.imshow('Detected faces', img)

cv.waitKey(0)
cv.destroyAllWindows()