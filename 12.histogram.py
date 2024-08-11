# histogram is able to show the distribution of color pixels on an image
# can be done with gray and color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("Photos/th.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


blank = np.zeros(img.shape[:2],dtype="uint8")


# this will calculate the hist of the image, which must be a list[]
# channels = index of channel we want to compute the hist for, for gray = 0
# mask = hist for portion of img
# range will be 0-256
# if no mask we set it to None
# gray_hist = cv.calcHist([gray],[0], None,[256],[0,256])
# circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)

# mask = cv.bitwise_and(img,img,mask=circle)

# cv.imshow('mask',mask)
# gray_hist = cv.calcHist([gray],[0], mask,[256],[0,256])

# plt.figure()
# plt.title("grayscale Histogram")
# # the number of bins is the intervals of pixel intensity 
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



mask = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow("masked",masked)



plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

# color histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)