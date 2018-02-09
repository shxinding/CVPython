from PIL import Image
from pylab import *

# 读取图像
im = array(Image.open('img/timg.jpeg'))

# 绘制图像
imshow(im)

# 点
x = [100,100,400,400]
y = [200,500,200,500]

#
plot(x,y,'r*')

plot(x[:2],y[:2])

# 标题
title('Plotting:"timg.jpeg"')

# 关闭坐标轴
axis('off')

plot(x,y)
plot(x,y,'r*')
plot(x,y,'go-')
plot(x,y,'ks:')

show()