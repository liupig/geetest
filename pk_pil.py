from PIL import Image
import time

im = Image.open("p3.jpg")
print(im.size, im.format, im.mode) #size表示图像的宽度和高度(像素表示);format表示图像的格式,常见的包括JPEG,PNG等格式;mode表示图像的模式，定义了像素类型还有图像深度等，常见的有RGB,HSV等。一般来说'L'(luminance)表示灰度图像,'RGB'表示真彩图像,'CMYK'表示预先压缩的图像
# im.show()
# im.save("picopy.png", "png") #保存指定格式的图像

# im.thumbnail((500,50),resample=Image.BICUBIC) #Image.BICUBIC，PIL.Image.LANCZOS，PIL.Image.BILINEAR，PIL.Image.NEAREST 默认是Image.BICUBIC
# im.show()

#crop(box)(裁剪矩形区域)

# box = (100,100,200,200)
# region = im.crop(box) #分别表示裁剪矩形区域的左上角x,y坐标,右下角的x,y坐标,规定图像的最左上角的坐标为原点(0,0),宽度的方向为x轴，高度的方向为y轴
# region.show()

# transpose(method)(图像翻转或者旋转)
"""Image.FLIP_LEFT_RIGHT,表示将图像左右翻转
    - Image.FLIP_TOP_BOTTOM,表示将图像上下翻转
    - Image.ROTATE_90,表示将图像逆时针旋转90°
    - Image.ROTATE_180,表示将图像逆时针旋转180°
    - Image.ROTATE_270,表示将图像逆时针旋转270°
    - Image.TRANSPOSE,表示将图像进行转置(相当于顺时针旋转90°)
    - Image.TRANSVERSE,表示将图像进行转置,再水平翻转"""
# im_rotate_180 = im.transpose(Image.ROTATE_180)
# im_rotate_180.show()

"""
paste(region,box,mask)(将一个图像粘贴到另一个图像)
上面的代码将region图像粘贴到左上角为(100,100)的位置。region是要粘贴的Image对象,box是要粘贴的位置，可以是一个两个元素的元组，表示粘贴区域的左上角坐标,
也可以是一个四个元素的元组，表示左上角和右下角的坐标。如果是四个元素元组的话,box的size必须要和region的size保持一致，否则将会被convert成和region一样的size。
"""
# im2 = Image.open("p2.png")
# # print(im2.size)
# # im2 = im2.transpose(Image.ROTATE_270)
# # box = (23,23,110,110)
# # region = im2.crop(box)
# # # region.show()
# # im.paste(region,(490,70),None)
# # im.show()


"""
split()(颜色通道分离)
split()方法可以原来图像的各个通道分离,比如对于RGB图像，可以将其R,G,B三个颜色通道分离。
"""

# r,g,b = im.split()
# r.show()
# time.sleep(3)
# g.show()
# time.sleep(3)
# b.show()

"""merge(mode,channels)(颜色通道合并)
merge方法和split方法是相对的，其将多个单一通道的序列合并起来，组成一个多通道的图像，mode是合并之后图像的模式，比如"RGB",channels是多个单一通道组成的序列。
"""
# r,g,b = im.split()
# im_merge = Image.merge("RGB", [r,b,g])
# im_merge.show()

"""resize(size,resample,box)
resize方法可以将原始的图像转换大小,size是转换之后的大小,resample是重新采样使用的方法，仍然有Image.BICUBIC，PIL.Image.LANCZOS，
PIL.Image.BILINEAR，PIL.Image.NEAREST这四种采样方法，默认是PIL.Image.NEAREST,box是指定的要resize的图像区域，
是一个用四个元组指定的区域(含义和上面所述box一致)。

"""

# im_resize = im.resize((200,200))
#
#
# # im_resize.show()
# im_resize_box = im.resize((100,100),box = (0,0,50,50))
# im_resize_box.show()


"""convert(mode,matrix,dither,palette,colors)(mode转换)
convert方法可以改变图像的mode,一般是在'RGB'(真彩图)、'L'(灰度图)、'CMYK'(压缩图)之间转换。上面的代码就是首先将图像转化为灰度图，
再从灰度图转化为真彩图。值得注意的是,从灰度图转换为真彩图，虽然理论上确实转换成功了，但是实际上是很难恢复成原来的真彩模式的(不唯一)。
"""
# im_L = im.convert("L")
# im_L.show()
#
# im_rgb = im_L.convert("RGB")
# im_rgb.show()
# im_L.mode

















