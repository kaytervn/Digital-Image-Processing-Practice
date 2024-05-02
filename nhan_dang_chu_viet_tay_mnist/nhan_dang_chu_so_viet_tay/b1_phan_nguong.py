import cv2
import numpy as np
import pytesseract

imgin = cv2.imread("ChuSoResize.jpg", cv2.IMREAD_GRAYSCALE)
val, temp = cv2.threshold(imgin, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print("val ", val)
# cv2.imshow("Temp", temp)

dem, label = cv2.connectedComponents(temp)

a = np.zeros(dem, np.int32)
M, N = label.shape
for x in range(0, M):
    for y in range(0, N):
        r = label[x, y]
        a[r] += 1

max = max(a[1:])
nguong = max // 10

# imgout = np.zeros((M, N), np.uint8)
# for x in range(0, M):
#     for y in range(0, N):
#         r = label[x, y]
#         if r > 0:
#             if a[r] > nguong:
#                 imgout[x, y] = 255
# cv2.imshow("ImageOut", imgout)
# cv2.imwrite("imgout.bmp", imgout)
# dem, label = cv2.connectedComponents(imgout)
# print(dem)

imgout = np.zeros((M, N), np.uint8)
k = 1
for r in range(1, dem):
    if a[r] > nguong:
        xmin = M - 1
        ymin = N - 1
        xmax = 0
        ymax = 0
        for x in range(0, M):
            for y in range(0, N):
                if label[x, y] == r:
                    if x < xmin:
                        xmin = x
                    if y < ymin:
                        ymin = y
                    if x > xmax:
                        xmax = x
                    if y > ymax:
                        ymax = y
                    imgout[x, y] = 255
        print("k =", k)
        k += 1
        word = imgout[xmin : xmax + 1, ymin : ymax + 1]
        custom_config = r"--oem 3 --psm 6"
        ket_qua = pytesseract.image_to_string(word, config=custom_config)
        print("Ket qua: ", ket_qua)
        cv2.imshow("word", word)
        cv2.waitKey(0)
        cv2.destroyWindow("word")
