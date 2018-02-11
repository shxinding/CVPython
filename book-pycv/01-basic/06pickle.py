import pickle

from PIL import Image
from imtool import *
from numpy import *
from pylab import *

im = array(Image.open('img/dalian.jpg'))
f = open('test.pkl','wb')
pickle.dump(im,f)
f.close()

f2 = open('test.pkl','rb')
im2 = pickle.load(f2)
imshow(im2)
show()
f2.close()

