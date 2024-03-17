import cv2
import numpy as np

# Đọc hình ảnh
image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

# Chuyển đổi hình ảnh sang ảnh grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Phát hiện biên bằng phương pháp Canny
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

# Biến đổi Hough
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Vẽ các đường thẳng trên hình ảnh gốc
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
