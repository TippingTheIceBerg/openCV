import cv2 as cv

img = cv.imread("Photos/th.jpg")


# convert an image to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur
# why use blur? Can remove some noise from the image

cv.imshow("pic",gray)
cv.waitKey(0)