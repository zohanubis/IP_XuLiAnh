import cv2
import numpy as np
import matplotlib.pyplot as plt

def global_threshold(image):
    # Chuyển ảnh sang ảnh thang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Áp dụng phân ngưỡng toàn cục
    _, binary_global = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_global

def adaptive_threshold(image, block_size=11, constant=2):
    # Chuyển ảnh sang ảnh thang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng phân ngưỡng thích nghi
    binary_adaptive = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)

    return binary_adaptive

def main():
    # Đọc ảnh đầu vào
    input_image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

    # Phân vùng ảnh sử dụng ngưỡng toàn cục
    binary_global = global_threshold(input_image)

    # Phân vùng ảnh sử dụng ngưỡng thích nghi tối ưu
    binary_adaptive = adaptive_threshold(input_image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(binary_global, cmap='gray')
    plt.title('Global Thresholding')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(binary_adaptive, cmap='gray')
    plt.title('Adaptive Thresholding')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
