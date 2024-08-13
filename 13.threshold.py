import cv2 as cv


# threshold = we want to take an image and change it into binary
# common one is to take a pixel and compare it to the threshold
# if the pixel < threshold, set it to 0, black
# 2 types, simple and adaptive
img = cv.imread("Photos/sudoku.png")
cv.imshow("Sud",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)



# simple thresholding, the threshold function returns a threshold and thresh
# takes the gray scale image into the function
# gray image, the check value, and then the what to set the value to if it is > threshold
# thresh = is the final image
threshold,thresh = cv.threshold(gray,200,255,cv.THRESH_BINARY )
cv.imshow("Simple thresh",thresh)

# for an inverse, cv.thresh_binary,_inv
threshold,thresh_inv = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV )
cv.imshow("Simple thresh Inverse",thresh_inv)
# some flaws of simple is we must set  the threshold value


# Adaptive Threshold - computer finds the opt threshold
# we must still input an image, maxvalue, and a method to adapt
# binary, then blocksize = kernal size needs to know how large the image is
# c is the value to subtract from the mean, allows to fine tune the threshold
# we can also set it to gaussian, do NOT have to use mean
adapt_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)

cv.imshow("adaptive",adapt_thresh)
cv.waitKey(0)