import cv2

image = cv2.imread('data/images/truth.png')
cv2.imshow('original', image)

# 이미지 확장 : dilation

dilationSize = 6
# 사각형으로 확장
element = cv2.getStructuringElement(cv2.MORPH_RECT,
                        (2*dilationSize, 2*dilationSize) ) # x,y 튜플

imageDilate = cv2.dilate(image, element)

cv2.waitKey(0)
cv2.destroyAllWindows()


