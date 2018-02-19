import cv2
import numpy as np
from scipy import ndimage

# 色彩空间：灰度、BGR、HSV
# 1 灰度：转换成灰阶
# 2 BGR：蓝-绿-红
# 3 HSV: Hue 色调 Saturation 饱和度 Value黑暗的成都

# 约瑟夫`傅里叶，所有的波形都可以由一系列简单且频率不同的正弦曲线叠加得到
# 幅度谱，可以看到亮的像素和暗的像素的百分比

# 高通滤波器HPF，根据像素与周围像素的亮度差值提升亮度的滤波器
kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1, 1, 2, 1,-1],
                       [-1, 2, 4, 2,-1],
                       [-1, 1, 2, 1,-1],
                       [-1,-1,-1,-1,-1]])

img = cv2.imread("img/p2.jpeg",0)

# convolve 卷积
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()

# 低通滤波器，low pass filter, LPF
# 主要用于去噪和模糊化

# 轮廓检测
img = np.zeros((200,200), dtype=np.uint8)
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh,
                                              cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("contours",color)
cv2.waitKey()
cv2.destroyAllWindows()