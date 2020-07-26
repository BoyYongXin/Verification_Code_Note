import cv2
import random
from numpy import *


def PepperandSalt(src, percetage):
    '''
    椒盐噪声
    :param src:
    :param percetage:
    :return:
    '''
    NoiseImg = src
    NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        randX = random.random_integers(0, src.shape[0] - 1)
        randY = random.random_integers(0, src.shape[1] - 1)
        if random.random_integers(0, 1) <= 0.5:
            NoiseImg[randX, randY] = 0
        else:
            NoiseImg[randX, randY] = 255
    return NoiseImg


def GaussianNoise(src, means, sigma, percetage):
    NoiseImg = src
    NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        randX = random.randint(0, src.shape[0] - 1)
        randY = random.randint(0, src.shape[1] - 1)
        NoiseImg[randX, randY] = NoiseImg[randX, randY] + random.gauss(means, sigma)
        if NoiseImg[randX, randY] < 0:
            NoiseImg[randX, randY] = 0
        elif NoiseImg[randX, randY] > 255:
            NoiseImg[randX, randY] = 255
    return NoiseImg


# 椒盐噪声

# img = cv2.imread('salt_0.png', 0)
# img1 = PepperandSalt(img, 0.2)
# cv2.imwrite('salt_0.jpg', img1)
# cv2.imshow('PepperandSalt', img1)
# cv2.waitKey(0)

# 高斯噪声
img = cv2.imread('salt_0.png', 0)
img1 = GaussianNoise(img, 2, 4, 0.8)
cv2.imwrite('GaussianNoise.jpg', img1)
cv2.imshow('GaussianNoise', img1)
cv2.waitKey(0)
