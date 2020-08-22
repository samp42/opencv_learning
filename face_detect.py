import cv2 as cv
#Cascade Classifier Object

img = cv.imread("img/me.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Search coordinates of image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv.imshow("Face", img)

cv.waitKey(0)
cv.destroyAllWindows()