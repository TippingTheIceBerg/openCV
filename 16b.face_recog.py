import cv2 as cv
import numpy as np


people = ['harry','her','ron']


# copy the haar_cascade from lecture 15.
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# load our features and labels
# we could have commented this out since we don't suse features or labels here, but can leave it as well, as long as we set allow_pickle to true we shouldn't get errors
features = np.load("features.npy", allow_pickle=True)
labels = np.load("labels.npy", allow_pickle=True)


# copy this from lecture 16
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_training.yml")

# validation img to check if the training works
img = cv.imread("C:/Users/oorti/OneDrive/Desktop/Code Files/openCV/train/ValHer.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)


# detect the face in the image
faces_rect  = haar_cascade.detectMultiScale(gray,1.1,15)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    # the actual predict
    label, confidence = face_recognizer.predict(faces_roi)
    # since using num values, we do people[label]
    print(f"label = {people[label]} with confidence of {confidence}")
    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),2)
    cv.rectangle(img,(x,y),(x+w, y+h),(0,255,0),thickness=2)
cv.imshow("Detected face",img)

cv.waitKey(0)