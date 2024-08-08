# boundary of an object
import cv2 as cv
import numpy as np
img = cv.imread("Photos/sudoku.png")


blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("blank",blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

# canny is one way to find contours
# canny = cv.Canny(blur,125,125)
# cv.imshow('canny',canny)

# threshold is the other way
# threshold looks at an image, and tries to make it into binary
# if pixel is below 125 intensity, it will be black
ret,thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)


# findCountours, takes the edges, the canny, and take in a mode to find the contours. This returns two values, the contours and hier by taking in the canny
# cv.retr_list shows all the edges, while other ones may only show edges (external)
# instead of thresh we can add canny if we are doing it the canny way
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# we draw on the blank image to show us what type of contours cv found
# it takes an image to draw over,takes contours that is a list, takes an index (how many contours we want to see, if all -1), takes a color in rgb, and a thickness
cv.drawContours(blank, contours, -1,(0,0,255),1)
cv.imshow("shownContours",blank)

# we can estimate the amount of edges since contours are list, and we can print a list with len
print(f'{len(contours)}')

# best to try to use canny first before threshold since threshold has 

# we can also find contours with thresholds instead of using canny
cv.waitKey(0)
