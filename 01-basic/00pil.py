from PIL import Image
import os

# 读取图像
pil_im = Image.open('img/timg.jpeg')

# 转换成灰度图像
Image.open('img/timg.jpeg').convert('L').save('img/l_timg.jpeg')

# 保存图像
def get_imlist(path):
    """返回jpg文件列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

# 1.1.1 转换图像格式
filelist = ['/Users/xingoo/PycharmProjects/CVPython/01-basic/img/cv.jpeg',
            '/Users/xingoo/PycharmProjects/CVPython/01-basic/img/timg.jpeg']


for infile in filelist:
    outfile = os.path.splitext(infile)[0]+".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)

# 1.1.2 创建缩略图
pil_im.thumbnail((32,32))

# 1.1.3 复制粘贴
box = (0,0,30,30)
region = pil_im.crop(box)
region.save('img/crop.jpeg')

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)

# 1.1.4 调整尺寸和旋转
out = pil_im.resize((400,400))
out = pil_im.rotate(45)
