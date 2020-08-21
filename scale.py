import cv2

img = cv2.imread("img/me.jpg")
img = cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
img = cv2.imshow("Me", img)

cv2.waitKey(0)
cv2.destroyAllWindows()