import cv2 as cv
import numpy as np

img = cv.imread('Photos/th.jpg')
cv.imshow("elden",img)


# we can show the actual color take up by using np blank image
blank = np.zeros(img.shape[:2], dtype='uint8')
# split and merge color channels
# color images has multiple channels of red green and blue merged together
b,g,r = cv.split(img)

# where blank is an empty canvas created by np
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])



# the higher the concentration, the whiter it is, this only shows
# it in gray scale, white to black
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)



# this takes an array. this gives back the original image
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)
cv.waitKey(0)