import cv2
import numpy as np
import matplotlib.pyplot as plt

def multivariable_threshold(image):
    # Chuyển ảnh sang ảnh thang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Tính gradient theo hướng x và y
    grad_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    
    # Áp dụng phân ngưỡng dựa trên nhiều biến
    thresholded_image = np.zeros(gray_image.shape, dtype=np.uint8)
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            if gray_image[i, j] > 100 and gradient_magnitude[i, j] > 50 and gray_image[i, j] - gradient_magnitude[i, j] > 20:
                thresholded_image[i, j] = 255
    
    return thresholded_image

def main():
    # Đọc ảnh đầu vào
    input_image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

    # Phân vùng ảnh sử dụng phân ngưỡng dựa trên nhiều biến
    thresholded_image = multivariable_threshold(input_image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Multivariable Thresholding')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
