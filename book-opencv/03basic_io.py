import numpy as np
import cv2 as cv2
import os

# python数据类型有
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# numpy的数据类型
# bool 用一位存储的布尔类型（值为TRUE或FALSE）
# inti 由所在平台决定其精度的整数（一般为int32或int64）
# int8 整数，范围为128至127
# int16 整数，范围为32 768至32 767
# int32 整数，范围为231至231 1
# int64 整数，范围为263至263 1
# uint8 无符号整数，范围为0至255
# uint16 无符号整数，范围为0至65 535
# uint32 无符号整数，范围为0至2321
# uint64 无符号整数，范围为0至2641
# float16 半精度浮点数（16位）：其中用1位表示正负号，5位表示指数，10位表示尾数
# float32 单精度浮点数（32位）：其中用1位表示正负号，8位表示指数，23位表示尾数
# float64或float 双精度浮点数（64位）：其中用1位表示正负号，11位表示指数，52位表示尾数
# complex64 复数，分别用两个32位浮点数表示实部和虚部
# complex128或complex 复数，分别用两个64位浮点数表示实部和虚部

img = np.zeros((3,3), dtype=np.uint8)
print(img)

# 图片转成BGR的格式
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)

# 常见的色彩表示法：灰度、RGB、HSV

img = np.zeros((3,3), dtype=np.uint8)
print(img.shape)

# python使用cv2代表最新的接口，可以不使用cv模块编程
img = cv2.imread('img/p2.jpeg')
cv2.imwrite('img/p2.png',img)

# 加载灰度图像
grayImage = cv2.imread('img/p2.jpeg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('img/p2_gray.png',grayImage)

# 可选的参数有
# IMREAD_ANYCOLOR = 4
# IMREAD_ANYDEPTH = 2
# IMREAD_COLOR = 1
# IMREAD_GRAYSCALE = 0
# IMREAD_LOAD_GDAL = 8
# IMREAD_UNCHANGED = -1

# imread会删除所有所有alpha通道的信息——透明度

# 随机字节的bytearray转换成灰度图像和RGB图像
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('img/p2_convert_gray.png',grayImage)

bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('img/p2_convert_bgr.png',bgrImage)

# 改变像素颜色
img = cv2.imread('img/p2.jpeg')
img[:,:,1] = 0
cv2.imwrite('img/p2_no_green.png',img)

# 感兴趣区域（Region of Interest, ROI)
img = cv2.imread('img/p2.jpeg')
my_roi = img[0:20,0:20]
img[10:30,10:30] = my_roi
cv2.imwrite('img/p2_roi.png',img)

# 图像尺寸
img = cv2.imread('img/p2.jpeg')
print(img.shape)    # 宽度、高度、通道数（比如RGB是3）
print(img.size)     # 像素大小
print(img.dtype)    # 数据类型
img = cv2.imread('img/p2.jpeg',cv2.IMREAD_GRAYSCALE)
print(img.shape)
print(img.size)
print(img.dtype)

# 显示图像
img = cv2.imread('img/p2.jpeg')
cv2.imshow('show',img)
cv2.waitKey()
cv2.destroyAllWindows()