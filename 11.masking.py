import cv2 as cv
import numpy as np


# masking allows us to look at a specific part of an image
# we have a photo of people but we only want faces, we can look at them only
img = cv.imread("Photos/th.jpg")
cv.imshow("elden",img)
# !the dimensions of the mask needs to be the same size of the image!
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("blank",blank)
# adding the - 105 is just magic numbers to move the mask where we want it
# mask = cv.circle(blank,(img.shape[1]//2 -105,img.shape[0]//2),100,255,-1)
# cv.imshow("mask",mask)

circle = cv.circle(blank.copy(),(img.shape[1]//2 -55,img.shape[0]//2),100,255,-1)
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow("weird_shape",weird_shape)

maskedImg = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow("masked",maskedImg)

cv.waitKey(0)