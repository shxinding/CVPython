from PIL import Image
from imtool import *
from pylab import *

# 图像数组的表示
im = array(Image.open('img/timg.jpeg'))
print(im.shape, im.dtype)

im = array(Image.open('img/timg.jpeg').convert('L'),'f')
print(im.shape, im.dtype)

print(im[:100,:50].sum())       # 前50 前100
print(im[50:100,50:100].sum())  # 50-100的和
print(im[100].mean())           # 100行平均值
print(im[:-1])                  # 最后一列

# 灰度变换
im2 = 255 - im # 对图像进行反相处理
imshow(im2)
show()

# 像素值变换到100~200之间
im3 = (100.0/255) * im + 100
imshow(im3)
show()

# 像素求平方
im4 = 255.0 * (im/255.0) ** 2
imshow(im4)
show()

# 图像保存
pil_im = Image.fromarray(uint8(im4))
pil_im.save('img/im4.jpeg')

# 图像缩放

def imresize(im, sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

# 图像压缩
im5 = imresize(array(Image.open('img/dalian.jpg').convert('L')),(40,40))
imshow(im5)
show()

# 图像直方图平衡化
im6 = array(Image.open('img/dalian.jpg').convert('L'))
im7,cdf = histeq(im6)
Image.fromarray(uint8(im7)).save('img/convert_dalian.jpg')