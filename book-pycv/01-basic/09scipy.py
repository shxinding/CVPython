from PIL import Image
from imtool import *
from numpy import *
from scipy.ndimage import measurements,morphology

im = array(Image.open('img/dalian.jpg').convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)
print("Number of objects:",nbr_objects)

# 形态学 操作 分离对象
im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)

lables_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects:",nbr_objects_open)