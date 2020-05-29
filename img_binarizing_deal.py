# -*- coding: utf-8 -*-
# @Author: Mr.Yang
# @Date: 2020/5/28 pm 2:37

"""
对图像的灰度和二值化处理
"""

from PIL import Image, ImageDraw
import os

def binarizing(img, threshold):

    """传入image对象进行灰度、二值处理"""

    img = img.convert("L") # 转灰度

    pixdata = img.load()

    w, h = img.size


    # 遍历所有像素，大于阈值的为黑色

    for y in range(h):

        for x in range(w):
            # print(pixdata[x, y])
            if pixdata[x, y] < threshold:
                # 黑
                pixdata[x, y] = 0

            else:
                # 白
                pixdata[x, y] = 255

    return img


def depoint(img, threshold=245):

    """传入二值化后的图片进行降噪（8邻域算法）"""

    pixdata = img.load()

    w, h = img.size

    for y in range(1, h-1):

        for x in range(1, w-1):

            count = 0

            if pixdata[x, y-1] > threshold:#上

                count = count + 1

            if pixdata[x, y+1] > threshold:#下

                count = count + 1

            if pixdata[x-1, y] > threshold:#左

                count = count + 1

            if pixdata[x+1, y] > threshold:#右

                count = count + 1

            if pixdata[x-1, y-1] > threshold:#左上

                count = count + 1

            if pixdata[x-1, y+1] > threshold:#左下

                count = count + 1

            if pixdata[x+1, y-1] > threshold:#右上

                count = count + 1

            if pixdata[x+1, y+1] > threshold:#右下

                count = count + 1

            if count > 4:

                pixdata[x, y] = 255

    return img

if __name__ == '__main__':

    image_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'images/2.jpg')
    img = Image.open(image_path)
    threshold = 200
    w, h = img.size
    print(w, h)
    image = binarizing(img, threshold)
    threshold = 245
    depoint(image, threshold).show()
