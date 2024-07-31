import cv2 as cv

img = cv.imread("Photos/th.jpg")


# convert an image to grayscale
# cv.color is a color code, since we are changing it from rgb, to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# blur
# why use blur? Can remove some noise from the image, like bag lightning or camera sensor issues

# ksize must be an odd number, kernal size

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

# edge cascade, trying to find the edges of an image
# we can reduce the amount of edges by applying a blurred image

canny = cv.Canny(img,120,150,)

blurCanny = cv.Canny(blur,120,150)

cv.imshow("canny",canny)
cv.imshow("blurredCanny",blurCanny)

# dilated image
# with more iterations the lines can be thicker
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dilated)


erode = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("erode",erode)

# resize ignores aspect ratio
resize = cv.resize(img,(1000,1000))

cv.imshow("resize",resize)

# cropped, images are just arrays, so we can slice out what we want
cropped = img[200:300, 320:350]

cv.imshow("cropped",cropped)




cv.waitKey(0)