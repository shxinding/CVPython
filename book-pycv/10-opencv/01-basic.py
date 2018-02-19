import cv2
from numpy import *

im = cv2.imread('img/p2.png')
h,w = im.shape[:2]
print(h,w)

cv2.imwrite('result.png',im)

# opencv中按照BGR的顺序进行存储
# BGR转灰度图像
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 计算积分图像
intim = cv2.integral(gray)

# 归一化并保存
intim = (255.0*intim)/intim.max()
cv2.imwrite('img/result.png',intim)

cv2.imshow('test',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

