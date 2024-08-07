import cv2 as cv

img = cv.imread("Photos/th.jpg")
cv.imshow('img',img)
# reduce some noise with blur, which can happen with bad pics

# averaging
# the summation of the intensity of a kernal window, which is applied to the true center, or th middle of the kernal window
# if we increase the kernal size, we get more blur
average = cv.blur(img,(7,7))
cv.imshow("averageBlur",average)


# gaussian blur
# more natual than averaging, typically less blurry

gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow("gauss",gauss)


# Median Blur
# same as average, except instead of the average of surrounding pixels
# finds the median, tends to use this one more if a lot of noise is present
# does not use tuple, just uses one integer
# not meant for high kernal noises like 7
median = cv.medianBlur(img,7)

cv.imshow("median",median)

# bilateral blurring
# most effective, uses in a lot of advance projects
# retains the edges of the images.
# note the second is a diameter and not kernal size
# next it takes a sigmaColor, higher = takes more colors
# sigma space high = takes account on farther away pixel with influence on the center
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral",bilateral)


cv.waitKey(0)