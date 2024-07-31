import cv2 as cv
import numpy as np

# numpy is used here to create a blank canvas
# uint is an image
# 500 500 3 = height, width, and number of color channels
# 3 is the rgb value input spots
blank = np.zeros((500,500,3), dtype="uint8")


# paint the img a certain color
# [:] = reference all the pixels
# range of pixels = [200:300 300:400]
# blank[200:300, 400:500] = 0,255,0
# cv.imshow("Green",blank)


# draw a rectangle
# (0,0) is the origin and goes to 250,250
# if we want a filed in we can thickness = -1
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),2)

# cv.imshow("hollow",blank)

# draw a circle
# cv.circle(blank,(0,250),45,(255,0,0),3)
# cv.imshow("circle", blank)


# draw a line 

# 0,0 is the top left, while blank.shape[0]//2 and blank.shape[1]//2 will point center

cv.line(blank,(0,0),(blank.shape[0]//2, blank.shape[1]//2),(90,100,90),3)
cv.imshow("line",blank)

# write text 

cv.putText(blank,"Words on here",(0,blank.shape[1]//2),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
cv.imshow("text",blank)

cv.waitKey(0)