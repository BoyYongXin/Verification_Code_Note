import os
from PIL import Image, ImageDraw
from img_binarizing_deal import binarizing, depoint
import tesserocr

image_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'images/2.jpg')
img = Image.open(image_path)
threshold = 200
# threshold = 100
w, h = img.size

image = binarizing(img, threshold)
threshold = 245
imgs = depoint(image, threshold)

print(tesserocr.image_to_text(imgs))
imgs.show()

# import pytesseract
# content = pytesseract.image_to_string(image)  # 解析图片
# print(content)