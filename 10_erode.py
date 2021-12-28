import cv2

image = cv2.imread('data/images/truth.png')
cv2.imshow('original', image)

# 이미지 침식 : erode
erodeSize = 6
# 사각형으로 확장
element = cv2.getStructuringElement(cv2.MORPH_RECT,
                        (2*erodeSize, 2*erodeSize) ) # x,y 튜플

imageErode = cv2.erode(image, element)

cv2.imshow('erode', imageErode)

cv2.waitKey(0)
cv2.destroyAllWindows()


