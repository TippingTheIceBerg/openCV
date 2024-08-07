import cv2 as cv
import numpy as np
# pixel is turned on with a value of 1, and off if 0

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("rect",rectangle)
cv.imshow("circle",circle)


# bitwise AND
# bitwise and takes 2 source images
# takes the two images and we get the intersection of the two
bitwsie_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bit_and",bitwsie_and)

# bitwise OR
# both the intersection and non intersection
# basically puts them together
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise_or)

# bitwise XOR
# non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",bitwise_xor)

# bitwise NOT
# returns nothings really, inverts the binary color
# takes only one argument
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Not",bitwise_not)

cv.waitKey(0)