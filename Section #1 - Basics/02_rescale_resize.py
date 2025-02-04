# resizing and rescaling images
# Done to prevent computational strain (large media files store a lot of info in them which takes computer a lot of processing to display )
import cv2 as cv

# it is often good practice to downscale your images
# creating a function to rescale a frame to some scale value
def rescaleFrame(frame, scale=0.75):
    # NOTE: both width and height are integers hence have to be converted to int from float
    width = int(frame.shape[1] * scale)     # width -> frame.shape[1]
    height = int(frame.shape[0] * scale)    # height -> frame.shape[0]
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)    # this function resizes a frame to a particular dimension


# specific method to resize live videos (external camera) ONLY using capture.set() method
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
    # 3 and 4 reference the properties of width and height in the capture variable (for example brightness is referenced by 10)



img = cv.imread('../Resources/Photos/cat.jpg')
img_resized = rescaleFrame(img)
cv.imshow('Cat', img)
cv.imshow('Smol cat', img_resized)
cv.waitKey(0)

capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.5)

    cv.imshow('Video', frame)
    cv.imshow('Rescaled_Video', frame_resized)
    # to stop infinite running (if char d is pressed)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()