import numpy as np

L = 256


def Negative(imgin):
    imgout = L - 1 - imgin
    return imgout


def NegativeColor(imgin):
    M, N, C = imgin.shape
    imgout = np.zeros((M, N, C), np.uint8) + 255
    for x in range(0, M):
        for y in range(0, N):
            b = imgin[x, y, 0]
            g = imgin[x, y, 1]
            r = imgin[x, y, 2]

            b = L - 1 - b
            g = L - 1 - g
            r = L - 1 - r

            imgout[x, y, 0] = np.uint8(b)
            imgout[x, y, 1] = np.uint8(g)
            imgout[x, y, 2] = np.uint8(r)
    return imgout


def Logarit(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    c = (L - 1) / np.log(1.0 * L)
    for x in range(0, M):
        for y in range(0, N):
            r = imgin[x, y]
            if r == 0:
                r = 1
            s = c * np.log(1.0 + r)
            imgout[x, y] = np.uint8(s)
    return imgout
