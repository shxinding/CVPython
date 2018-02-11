from PIL import Image
from imtool import *
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('img/dalian.jpg').convert('L'))

# 导数滤波器
imx = zeros(im.shape)
filters.sobel(im, 1, imx)

imy = zeros(im.shape)
filters.sobel(im, 1, imy)

magnitude = sqrt(imx**2+imy**2)
imshow(magnitude)
show()

# 高斯模糊+导数滤波

sigma = 5

imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)

imy = zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (1,0), imy)

magnitude = sqrt(imx**2+imy**2)
imshow(magnitude)
show()