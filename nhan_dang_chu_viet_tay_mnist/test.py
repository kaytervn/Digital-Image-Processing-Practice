import cv2
import pytesseract

# Đường dẫn đến ảnh chứa chữ viết tay
image_path = "D:\Downloads\ChuSoReSize.jpg"

# Đọc ảnh sử dụng OpenCV
image = cv2.imread(image_path)

# Chuyển ảnh sang đen trắng
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng thresholding để làm nổi bật chữ
_, thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

# Sử dụng Tesseract để nhận dạng chữ
text = pytesseract.image_to_string(thresh)

# In kết quả
print("Chữ nhận dạng từ ảnh:")
print(text)

# Hiển thị ảnh gốc và ảnh đã được xử lý
cv2.imshow("Original Image", image)
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
