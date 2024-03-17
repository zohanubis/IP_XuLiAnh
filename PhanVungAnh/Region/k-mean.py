import cv2
import numpy as np

def segment_image_by_kmeans(image):
    # Chuyển đổi ảnh sang không gian màu RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape ảnh thành một mảng 2D
    pixels = image_rgb.reshape((-1, 3))

    # Chuyển đổi kiểu dữ liệu về float32
    pixels = np.float32(pixels)

    # Thiết lập các tham số cho thuật toán K-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 3  # số lượng cụm mong muốn

    # Thực hiện phân cụm
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Chuyển đổi các giá trị về dạng uint8 và tạo lại ảnh
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image_rgb.shape)

    return segmented_image

def main():
    # Load ảnh
    image = cv2.imread('PhanVungAnh/Region/image.png')

    # Phân vùng ảnh bằng phương pháp K-means clustering
    segmented_image_kmeans = segment_image_by_kmeans(image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image (K-means)', segmented_image_kmeans)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
