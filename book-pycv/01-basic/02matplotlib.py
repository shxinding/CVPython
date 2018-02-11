from PIL import Image
from pylab import *

im = array(Image.open('img/timg.jpeg').convert('L'))

# 新建图像
figure()

# 图像直方图
hist(im.flatten(),128)
show()

# 不适用颜色信息
gray()

# 在原点左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
show()