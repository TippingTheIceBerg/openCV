import cv2 as cv

#resize and rescale to remove some computational strain
# almost always better to downscale in size 

# frame = what we want to resize
def rescaleFrame(frame, scale=0.75):
    # this rescale works for images, videos and live videos
    # frame 1 is the width of image
    # frame 0 is the height of the image
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # resizes the frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("Videos/lily.mp4")


while True:
    isTrue, frame = capture.read()
    # invoke the rescaleFrame function and passes the 
    # rememeber that scale=0.75 is default, it can still be changed as a parameter
    frame_resized = rescaleFrame(frame, 0.25)
    # now that it is resized, we show the video by calling the resized video
    cv.imshow("Name", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()