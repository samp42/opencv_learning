import cv2

print("OpenCV version: ", cv2.__version__)
img = cv2.imread("img/me.jpg")
img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.imshow("Me", img)
cv2.imshow("Me gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
