import cv2 as cv
import numpy as np

img = cv.imread("Photos/sudoku.png")

cv.imshow("img",img)
# gradients = edge like regions in an image, but are not the same as edges in theory

# besides canny, we have laplacin and sobel for edge detection

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
# described as chalkboard that was smudged a bit
# we do the absolute, when transition from black to white and vice versa, we get positive and neg slopes the absolute makes sure we only have positive pixel values
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("lap",lap)

# sobel - gradients in two directions, x and y
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combine_sobel = cv.bitwise_or(sobely,sobelx)

cv.imshow("combine sobel",combine_sobel)

cv.imshow("sobel x",sobelx)
cv.imshow("sobel y",sobely)

# canny

canny = cv.Canny(gray,150,175)
cv.imshow("canny",canny)

cv.waitKey(0)