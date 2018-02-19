
## 第二章 处理文件、摄像头和图形界面

### 基本操作
imread读取图片、imwrite保存图片、imshow显示图片以及常用的视频操作

最后有一个视频和图片保存的案例

读取视频可以用cv2.VideoCapture(0)
```bash
camera = cv2.VideoCapture(0)
success,frame = camera.read()
获得该帧
```

## 第三章 使用opencv 3 处理图像

在图像中滤波操作也叫做卷积，就是给定一个卷积核进行相应的计算。
可以做轮廓检测、锐化、模糊等处理

## 第五章 人脸检测和识别

cv2.CascadeClassifier来进行人脸识别

## 第七章 目标检测与识别

### 基本概念
在传统的目标检测和识别技术中，会用到下面的概念：

- 梯度直方图（Histogram of Oriented Gradient）
- 图像金字塔（image pyramid）
- 滑动窗口（sliding window），需要注意 区域重叠overlapping region的问题

一个简单的人物识别的例子 —— 01persona_detect.py

### 检测器

BOW词袋模型与SVM支持向量机

特征提取的方法：SIFT、SURF

SURF算法介绍：http://blog.csdn.net/tostq/article/details/49472709

- Hessian矩阵
- Haar小波响应
