import cv2


def getStream(source):
    stream = cv2.VideoCapture(source)

    while True:
        success, frame = stream.read()
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

    stream.release()
    cv2.destroyAllWindows()

getStream(0)