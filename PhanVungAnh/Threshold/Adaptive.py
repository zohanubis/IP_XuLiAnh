import cv2
import numpy as np

def adaptive_thresholding(image, threshold_1, threshold_2):
    # Chuyển đổi hình ảnh sang ảnh grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Khởi tạo ảnh kết quả
    result_image = np.zeros_like(gray_image)
    
    # Lặp qua từng pixel trong hình ảnh
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            pixel_value = gray_image[i, j]
            if pixel_value < threshold_1:
                result_image[i, j] = 0
            elif pixel_value >= threshold_1 and pixel_value < threshold_2:
                result_image[i, j] = 1
            else:
                result_image[i, j] = 2  # hoặc nếu có n ngưỡng, sử dụng công thức tương ứng
            
    return result_image

# Đọc hình ảnh
image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

# Thiết lập ngưỡng
threshold_1 = 50
threshold_2 = 200

# Áp dụng phương pháp ngưỡng thích nghi
result = adaptive_thresholding(image, threshold_1, threshold_2)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Thresholding Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
