import cv2 as cv
import numpy as np

img = cv.imread("Photos/th.jpg")

cv.imshow("elden",img)

# translation
# moving an image on the y or x axis.
# to translate an image, we need to make a translation matrix
def translate(img, x, y):
    # takes a list with two lists inside of it
    transMat = np.float32([[1,0,x],[0,1,y]])
    # dimensions take a tuple
    # [1] is the width, [0] is the height
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat,dimensions)
# right 100pxls and down 100pxls
translated = translate(img, -100, 100)
cv.imshow("moved",translated)

# rotation
def rotate(img, angle, rotPoint =None):
    (height,width ) = img.shape[:2]
    # if no rotPoint, we assume it will be in the center
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)
cv.imshow("rotate", rotated)

# resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)

cv.imshow("resize", resized)


# flip an image
# 0 = flip verti x axis
# 1 is the y axis
# -1 flip both x and y
flip = cv.flip(img, -1)

cv.imshow("flipped",flip)
cv.waitKey(0)
