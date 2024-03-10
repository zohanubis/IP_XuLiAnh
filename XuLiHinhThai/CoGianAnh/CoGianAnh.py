import cv2
import numpy as np

def erosion(image, kernel):
    """
    Thực hiện phép co ảnh (erosion) trên ảnh input image với phần tử cấu trúc kernel.
    """
    # Thực hiện phép convolution giữa ảnh và kernel
    result = cv2.erode(image, kernel, iterations=1)
    return result

def dilation(image, kernel):
    """
    Thực hiện phép giãn ảnh (dilation) trên ảnh input image với phần tử cấu trúc kernel.
    """
    # Thực hiện phép convolution giữa ảnh và kernel
    result = cv2.dilate(image, kernel, iterations=1)
    return result

# Đọc ảnh gốc
image = cv2.imread('XuLiHinhThai/CoAnh/Anh.webp', cv2.IMREAD_GRAYSCALE)

# Tạo phần tử cấu trúc (SE) cho phép co ảnh và phép giãn ảnh
kernel = np.ones((5,5), np.uint8)

# Thực hiện phép co ảnh và phép giãn ảnh
eroded_image = erosion(image, kernel)
dilated_image = dilation(image, kernel)

# Hiển thị ảnh gốc và ảnh đã được xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
