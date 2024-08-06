import cv2 as cv
# WE CANNOT CONVERT for example grayscale to HSV, we need to go from gray to BGR, then BGR to HSV if we want to do that

img = cv.imread("Photos/th.jpg")
# color spaces is an array of colors, gray scale and rgb are examples of a color space
# convert bgr image to grayscale, bgr is the defautl

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# gbr to HSV (hue sat value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR TO RGB, most libraries read it as RGB, and the two are usually opposites in color
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

# HSV TO BGR

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV -> BGR", hsv_bgr)

cv.waitKey(0)