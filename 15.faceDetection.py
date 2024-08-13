#  will detect faces with something called  a hard cascade
# face recog != detection
# recog involved iding the face, detecting is just seeing for a face
# done with a classifier, decideds if a given image is positive or negative.
# classifer needs to be trained to see if a face is present or not
# hard cascades and local binary patterns = two main classifiers
# we can find hard cascades at opencv github
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# go to the file, click on the raw button, command A, then command c
# copy paste all text into a xml file
# this does not take into account skin tone
# it looks at the edges of an image and decides if a smile is there or not

import cv2 as cv

# code does not change if multiple people are in the image
# if a video, we will need to detect haar_cascade for each individual frame of the video
# img = cv.imread("Photos/lots_faces.webp")
img = cv.imread("Photos/one_face.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# copy the path of the classifier, which will read all those lines of code
# and store it in haar_cascasde

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# haar_cascasde = cv.CascadeClassifier('Users\\oorti\\OneDrive\\Desktop\\Code Files\\openCV\\haar_face.xml')

# pass in the gray image we want to detect the face
# scalefactor 1.1
# minNeighbors specifies the number of neighbors rectangles that should be called 
# this will then return the rect coordinates of that face as a list 
# if nosie, ie more faces than expected, lower scale and increase minNeighbors
# if underestimate we decrease min, if over, increase min
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=8)
# we can see how many faces it detects by printing the leng of the faces_rect
print(f"number of faces found = {len(faces_rect)}")
# since rect uses rect to find the cordinates of faces, we can loop over and grab those cordinated to draw a rectangle
for (x,y,w,h) in faces_rect:
    # draw a rect over the OG image
    # point 1 is x,y
    # point2 is x+w, y+h
    # color
    # thickness
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0), thickness=2)
cv.imshow("detected face", img)
cv.waitKey(0)