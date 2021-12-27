import cv2
import numpy as np

# cv2.IMREAD_COLOR랑 1은 같은 의미입니다.
# imread로 먼저 읽어오기
source = cv2.imread('data/images/sample.jpg', 1) # 1:칼라

print(cv2.IMREAD_COLOR)

# 가로는 80%로
# 세로는 60%로
# 이미지 확대 / 축소

scaleX = 0.8
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

print(scaleDown)

cv2.imshow('Original', source) # 원본이미지
cv2.imshow('Scaled Down', scaleDown) # 축소이미지


# CROP 이미지 자르기!

crop_image = source [ 10:200 , 150:250 ]

cv2.imshow('crop img', crop_image)




# 눈으로 확인하기(디버깅용)
cv2.waitKey(0) 
cv2.destroyAllWindows()
