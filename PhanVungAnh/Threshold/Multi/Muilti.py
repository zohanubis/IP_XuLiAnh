import cv2
import numpy as np
import matplotlib.pyplot as plt

def multivariable_threshold(image):
    # Chuyển ảnh sang ảnh thang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Multi/1_gray_image.jpg', gray_image)  # Lưu ảnh xám
    
    # Tính gradient theo hướng x và y
    grad_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    gradient_magnitude = np.uint8(gradient_magnitude)
    cv2.imwrite('2_gradient_magnitude.jpg', gradient_magnitude)  # Lưu ảnh gradient
    
    # Áp dụng phân ngưỡng dựa trên nhiều biến
    thresholded_image = np.zeros(gray_image.shape, dtype=np.uint8)
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            if gray_image[i, j] > 100 and gradient_magnitude[i, j] > 50 and gray_image[i, j] - gradient_magnitude[i, j] > 20:
                thresholded_image[i, j] = 255
    
    cv2.imwrite('3_thresholded_image.jpg', thresholded_image)  # Lưu ảnh sau khi phân ngưỡng
    
    return thresholded_image

def main():
    # Đọc ảnh đầu vào
    input_image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

    # Phân vùng ảnh sử dụng phân ngưỡng dựa trên nhiều biến
    thresholded_image = multivariable_threshold(input_image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    gradient_magnitude = cv2.imread('2_gradient_magnitude.jpg', cv2.IMREAD_GRAYSCALE)
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Gradient Magnitude')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    thresholded_image = cv2.imread('3_thresholded_image.jpg', cv2.IMREAD_GRAYSCALE)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Multivariable Thresholding')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
