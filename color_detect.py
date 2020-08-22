import cv2 as cv
import numpy

def empty(a):
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",1000,400)
cv.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv.createTrackbar("Val Min","Trackbars",0,255,empty)
cv.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv.imread("img/stacked_cells.jpg")
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv.getTrackbarPos("Val Min","Trackbars")
    v_max = cv.getTrackbarPos("Val Max","Trackbars")
    lower = numpy.array([h_min,s_min,v_min])
    upper = numpy.array([h_max,s_max,v_max])
    mask = cv.inRange(img_hsv,lower,upper)
    result = cv.bitwise_and(img, img, mask=mask)
    print(h_min,h_max,s_min,s_max,h_min,h_max)
    cv.imshow("HSV", img_hsv)
    cv.imshow("Mask", mask)
    cv.imshow("Mask Result", result)
    cv.waitKey(1)

cv.destroyAllWindows()