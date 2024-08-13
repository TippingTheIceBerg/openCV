# we are going to have a file of images and train it to recog these faces
# we are not building a model from scratch, going to use the cv recognizer

import os
import cv2 as cv
import numpy as np


# first create a list of all the people in the images
# we can manually enter it, or we can loop over the file path with listdir
# 1. people = ['harry','ron','her']
# 2.
people = []
for i in os.listdir('C:/Users/oorti/OneDrive/Desktop/Code Files/openCV/train'):
    people.append(i)

# copy the haar_cascade from lecture 15.
haar_cascade = cv.CascadeClassifier('haar_face.xml')

DIR = "C:/Users/oorti/OneDrive/Desktop/Code Files/openCV/train"

 
# loop through each folder, that will then loop over the images
# features = img array of features
features = []
# labels = for each face, whose name goes to this face
labels = []
def create_train():
    for person in people:
        # for each folder in the base folder,go through each folder and get the path
        path = os.path.join(DIR, person)
        label = people.index(person)
        # get the img path
        for img in os.listdir(path):
            # join path var to img
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)


            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            # loop through each face in races_rect
            for (x,y,w,h) in faces_rect:
                # grab faces region of interest, and crop out the face of the img
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                # label is the index of this list
                # label is changed into number to reduce strain by mapping
                # harray will have an index of 0, since it is at the start of the list
                labels.append(label)
create_train()
print("Training Done--------------")
# convert to np array before training
features = np.array(features,dtype='object')
labels = np.array(labels)
# we should have 9 featues and 9 labels
# print(f"length of the features = {len(features)}")
# print(f"length of the labels = {len(labels)}")

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and the labels list
# openCV allows us to save our training model to use in another folder, director, project with the use of yml
face_recognizer.train(features,labels)
face_recognizer.save("face_training.yml")

np.save("features.npy",features)
np.save("labels.npy",labels)