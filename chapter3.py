import numpy as np
import cv2

L = 256


def Negative(imgin):
    imgout = L - 1 - imgin
    return imgout
