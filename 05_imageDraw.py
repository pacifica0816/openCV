import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)

# 선 그리기
imageLine = image.copy() # 넘파이 어레이 카피하기(사진카피)
cv2.line(imageLine, (322,179), (400,183), (255,0,0), 3, cv2.LINE_AA) # BGR순으로 (0,0,255) : R이 255 

cv2.imshow('image Line', imageLine)

# 원 그리기
imageCicle = image.copy()
cv2.circle(imageCicle, (350, 200), 150, (255,0,0), 3, cv2.LINE_AA)

cv2.imshow('image cicle', imageCicle)

# 타원 그리기
imageEllipse = image.copy()
cv2.ellipse(imageEllipse, (360,200), (100, 170), 45, 0, 260, (0,255,0), 2)
cv2.ellipse(imageEllipse, (360,200), (100, 170), 135, 0, 360, (0,0,255), 2 )

cv2.imshow('ellipse', imageEllipse)

# 사각형 그리기
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (200,55), (450,355), (255,0,0),3 ) # 왼쪽위, 오른쪽아래 점만 지정

cv2.imshow('rectangle', imageRectangle)

# 글자 넣기
imageText = image.copy()
cv2.putText(imageText, 'Mark Zuckerberg', (205,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imshow('text', imageText)


cv2.waitKey(0)
cv2.destroyAllWindows()

