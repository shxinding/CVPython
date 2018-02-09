from PIL import Image
from pylab import *

im = array(Image.open('img/timg.jpeg'))
imshow(im)

print('Please click 3 points')

# 交互式标注
x = ginput(3)
print('you clicked:',x)

show()