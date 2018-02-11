from PIL import Image
from imtool import *
from numpy import *
from pylab import *


def pca(X):
    """主成分分析"""

    # 获取维数
    num_data,dim = X.shape

    # 数据中心化
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim>num_data:
        M = dot(X,X.T)
        e,EV = linalg.eigh(M)
        tmp = dot(X.T,EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        U,S,V = linalg.svd(X)
        V = V[:num_data]

    return V,S,mean_X

# 字体下载不了了

imlist = ['img/dalian.jpg','img/convert_dalian.jpg']
im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)

immatrix = array([array(Image.open(each_im)).flatten() for each_im in imlist],'f')

V,S,immean = pca(immatrix)

figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()