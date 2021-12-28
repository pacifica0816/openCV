import cv2
import numpy as np
from numpy.lib.type_check import imag

from utils import get_four_points

image = cv2.imread('data/images/first-image.jpg')

# cv2.imshow('original', image)

# 1. 이 이미지를 변환하기 위한 점 4개 구하기. 여러분이 작성.
print(image.shape)

point_src = np.array([0,0, 
                    image.shape[1], 0 , 
                    image.shape[1], image.shape[0],  
                    0 , image.shape[0] ])
point_src = point_src.reshape(4,2)


image_dst = cv2.imread('data/images/times-square.jpg')

# cv2.imshow('dst', image_dst)

# 2. 타임스퀘어의 이미지에 매칭할 점의 좌표를 구합니다.
point_dst = get_four_points(image_dst)


# 3. 위의 두개 이미지간의 매칭할 두 점들을 모두 찾았으니,
#    변환 행렬을 얻어옵니다.
matrix, status = cv2.findHomography(point_src, point_dst)

# 4. image를 변환시킵니다. 
image_temp = cv2.warpPerspective(image, matrix, 
                ( image_dst.shape[1] , image_dst.shape[0]))

# 5. 변환된 이미지를 화면에 보여줍니다.
cv2.imshow('temp', image_temp)

# 6. 타임스퀘어 이미지에, 변환된 이미지 합성은, 저랑같이합니다!!

# 6-1. 타임스퀘어 이미지의 바꿀부분을, 0으로 셋팅한다!
#      바꿀 영역은 이미 마우스로 클릭해서, point_dst 에 들어있다. 
cv2.fillConvexPoly(image_dst, point_dst.astype(int) , 0)

# cv2.imshow('Image to 0', image_dst)

# 6-2. 두개의 이미지를 더하면, 합성이 된다.
result = image_temp + image_dst

cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()