import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# reading a large image (can possible go off screen)
img = cv.imread('../Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# reading video (VideoCapture() )
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# parameters for videoCapture() -> numbers (0), (1), (2) etc: if you want to connect to your webcam or secondary cameras
#                               -> path to a video file 

# Use a while loop and read video frame by frame
while True:
    isTrue, frame = capture.read()
    # capture.read() read reads the video frame by frame and returns the frame along with a boolean that tells if the frame was successfully read
    cv.imshow('Video', frame)
    # to stop infinite running (if char d is pressed)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# NOTE: (-215:Assertion failed)
# this error happens at the end of the video. Assertion failed most of the times means that a cv function couldn't find an image/video at the 
# specified location. This happened here since the frames ran out and it unexpectedly broke out of the while loop itself.