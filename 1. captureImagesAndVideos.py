import cv2 as cv
 
img = cv.imread("Photos/th.jpg")
# shows the image
cv.imshow("Elden", img )
# waits infinte time for key to be pressed, if not included img wll disappear
cv.waitKey(0)
# one known issue is that some images that are very large it can go offscreen


# reading videos
# method takes integer args - 0,1,2 or a path to a video file
# we use 0,1,2 if we are using like a webcam, typically 0
# capture is an instance of this video capture clause
capture = cv.VideoCapture("Videos/liliy.mp4")

# videos use while loop and read video frame by frame

while True:
    isTrue, frame = capture.read()
    # imshow captures each frame of the video
    cv.imshow("Video",frame)

    # if letter d is pressed, break out of loop
    # ctrl + c to terminate script too old fashion way
    # ord bring the unicode point of d
    # cv2.waitKey(20) & 0xFF
    # if user presses a key, then waitKey return DECIMAL VALUE of d in binary
    # next it checks to see if the binary on the left matches the binary gained from ord('d")
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()