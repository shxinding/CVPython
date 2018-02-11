from PIL import Image
from imtool import *
from numpy import *
from pylab import *


def denoise(im, U_init, tolerance=0.1, tau=0.125, tv_weight=100):
    m,n = im.shape

    # 初始化
    U = U_init
    Px = im
    Py = im
    error = 1

    while(error > tolerance):
        Uold = U

        # 原始梯度
        GradUx = roll(U,-1,axis=1)-U
        GradUy = roll(U,-1,axis=0)-U

        # 更新对偶变量
        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = maximum(1,sqrt(PxNew**2+PyNew**2))

        Px = PxNew/NormNew
        Py = PyNew/NormNew

        RxPx = roll(Px,1,axis=1)
        RyPy = roll(Py,1,axis=1)

        DivP = (Px-RxPx)+(Py-RyPy)
        U = im + tv_weight*DivP

        error = linalg.norm(U-Uold)/sqrt(n*m)

    return U,im-U

im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im+30*random.standard_normal((500,500))

# U,T = denoise(im,im)
# G = filters.gaussian_filter(im,10)
#
# from scipy.misc import imsave
# imsave('synth_rof.pdf',U)
# imsave('synth_gaussion.pdf',G)

im = array(Image.open('img/dalian.jpg').convert('L'))
U,T = denoise(im,im)

figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()