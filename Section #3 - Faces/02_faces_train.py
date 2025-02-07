import os
import cv2 as cv
import numpy as np

# We will be trianing opencv's built in face recognizer with the people below
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

'''
# Instead of manually specifying the list you can also iterate through the folders
p = []
for i in os.listdir(r'../Resources/Faces/train'):
    p.append(i)
print(p)
'''

DIR = '../Resources/Faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features =[] # the image arrays of faces
labels = []  # whose face it is

def create_train():
    # For each folder
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # For each image in that folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            # Taking only the parts of the image that count as faces
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # faces region of interest
                features.append(faces_roi)
                labels.append(label) 
                 # creating a mapping between the string (name of person) and a numerical label  (here, index) reduces strain on the computer

create_train()

# Now we can use the features and labels lists to train the model
# Instantiate face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer.train(features, labels)

# Save the trained model and the features and labels (they can now be used in other files)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)