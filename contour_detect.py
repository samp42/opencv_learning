import cv2 as cv
import numpy

def resize(img, factor):
    this_img = img
    this_img = cv.resize(this_img, (int(this_img.shape[1]/factor),int(this_img.shape[0]/factor)))
    return this_img

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        print(area) #prints area coordinates
        if area > 100: #trouble setting this threshols to detect cells
            cv.drawContours(img_contour,contour,-1,(255, 0, 0),1)
            peri = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.02*peri, True)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(img_contour, (x,y), (x+w,y+h),(0,255,0),2)
            object_corners = len(approx)
            #this part doesn't work so well
            if object_corners > 6:
                objectType = "Power Cell"
            else:
               objectType = "Unknown"
            cv.putText(img_contour, objectType, (x+(w//2)-10,y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 2)


img = cv.imread("img/stacked_cells.jpg")
img = resize(img, 2)
img_contour = img.copy()

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray,(7,7),1) #1 represents blur sigma (how much blur)
img_canny = cv.Canny(img_blur,50,50)
img_blank = numpy.zeros_like(img)
getContours(img_canny)

cv.imshow("Blur", img_blur)
cv.imshow("Canny", img_canny)
#cv.imshow("Blank", img_blank)
cv.imshow("Contour", img_contour)

cv.waitKey(0)
cv.destroyAllWindows()
