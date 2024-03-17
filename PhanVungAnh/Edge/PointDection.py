import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image):
    # Chuyển ảnh sang ảnh thang độ xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def point_detection(image):
    # Áp dụng bộ lọc Laplacian
    laplacian_kernel = np.array([[-1, -1, -1],
                                 [-1, 8, -1],
                                 [-1, -1, -1]])
    laplacian_image = cv2.filter2D(image, -1, laplacian_kernel)
    return laplacian_image

def main():
    # Đọc ảnh đầu vào
    input_image = cv2.imread('PhanVungAnh/Edge/test.jpg')

    # Tiền xử lý ảnh
    preprocessed_image = preprocess_image(input_image)

    # Phát hiện điểm ảnh sử dụng bộ lọc Laplacian
    detected_points = point_detection(preprocessed_image)

    # Hiển thị các ảnh
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(preprocessed_image, cmap='gray')
    plt.title('Preprocessed Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(detected_points, cmap='gray')
    plt.title('Detected Points')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()

#Hàm preprocess_image thực hiện việc chuyển đổi ảnh sang ảnh thang độ xám.
#Hàm point_detection thực hiện phát hiện điểm ảnh bằng cách áp dụng bộ lọc Laplacian.
#Trong hàm main, chúng ta đọc ảnh đầu vào, tiền xử lý ảnh, thực hiện phát hiện điểm ảnh, 
# và hiển thị các ảnh gốc, tiền xử lý và ảnh đã phát hiện điểm ảnh.