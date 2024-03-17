import cv2
import matplotlib.pyplot as plt

def otsu_thresholding(image):
    # Chuyển ảnh sang ảnh thang độ xám nếu cần
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    # Áp dụng phân ngưỡng Otsu
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image

def main():
    # Đọc ảnh đầu vào
    input_image = cv2.imread('PhanVungAnh/Threshold/test.jpg')

    # Thực hiện phân ngưỡng Otsu
    binary_image = otsu_thresholding(input_image)

    # Hiển thị ảnh gốc
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Hiển thị biểu đồ xử lý
    plt.subplot(1, 3, 2)
    plt.hist(input_image.ravel(), 256, [0, 256])
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Hiển thị ảnh đã phân ngưỡng
    plt.subplot(1, 3, 3)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Otsu Thresholding')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
