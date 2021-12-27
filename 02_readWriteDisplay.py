import cv2
import numpy as np

img_file = 'data/images/sample.jpg'

# opencv로 이미지 열기 - 칼라 이미지 (BGR)

image = cv2.imread(img_file, cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크하는 코드
if image is None :
    print('이미지파일을 열 수 없습니다.')
else :
    print(image.shape)

# opencv 에서는, 이미지를 BGR로 읽어옵니다.
# 따라서 불러온 이미지를 그레이 스케일로 변경할 수 있습니다.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('color', image)
cv2.imshow('gray scale', gray_image)

# 위의 imshow 함수는 화면에 표시하는 함수인데,
# 실행되었다가, 바로 종료된다.
# 왜냐하면, cpu가 imshow를 실행하고, 아래 라인 실행하는데
# 아래 라인은 아무것도 없어서, 바로 프로그램이 종료되었다.

# 따라서 우리 눈으로 확인하기 위해서는 
# cpu의 코드실행을 잠시 멈추게 해야 한다.
cv2.waitKey(0) # 멈춰있는 상태
cv2.destroyAllWindows() # cv2가 실행시킨 창을 모두 종료하라는 뜻