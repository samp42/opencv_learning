import cv2 as cv
import numpy as np

def getStream(source):
    stream = cv.VideoCapture(source)

    while True:
        success, frame = stream.read()
        cv.imshow("Frame", frame)
        k = cv.waitKey(1)
        if k == 27:
            break

    stream.release()
    cv.destroyAllWindows()

getStream(0)