from PIL import Image
from imtool import *
from numpy import *
from pylab import *
from scipy.ndimage import filters

# 1.4.1 图像模糊
im = array(Image.open('img/dalian.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
imshow(im2)
show()

# 每个颜色分别进行高斯模糊
im = array(Image.open('img/dalian.jpg'))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2)
imshow(im2)
show()
