import cv2 as cv

example_img = cv.imread("img/me.jpg")

def resize(img, factor):
    this_img = img
    this_img = cv.resize(this_img, (int(this_img.shape[1]/factor),int(this_img.shape[0]/factor)))
    cv.imshow("Me", this_img)
    return this_img

resize(example_img, 4)

cv.waitKey(0)
cv.destroyAllWindows()