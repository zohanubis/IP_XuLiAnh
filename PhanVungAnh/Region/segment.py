import cv2
import numpy as np

def segment_image_by_region(image):
    # Chuyển đổi ảnh sang không gian màu HSV để dễ dàng xử lý các đặc trưng màu sắc
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Phân vùng dựa trên màu sắc xanh lá cây
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([90, 255, 255])
    mask_green = cv2.inRange(image_hsv, lower_green, upper_green)

    # Phân vùng dựa trên màu sắc đỏ
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(image_hsv, lower_red, upper_red)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(image_hsv, lower_red, upper_red)

    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Kết hợp các mask lại với nhau
    mask_combined = cv2.bitwise_or(mask_green, mask_red)

    # Áp dụng morphology operations để loại bỏ nhiễu và cải thiện đường viền
    kernel = np.ones((5,5), np.uint8)
    mask_combined = cv2.morphologyEx(mask_combined, cv2.MORPH_CLOSE, kernel)
    mask_combined = cv2.morphologyEx(mask_combined, cv2.MORPH_OPEN, kernel)

    # Áp dụng mask lên ảnh gốc để tạo ảnh phân vùng
    segmented_image = cv2.bitwise_and(image, image, mask=mask_combined)

    return segmented_image

def main():
    # Load ảnh
    image = cv2.imread('PhanVungAnh/Region/the_weeknd.webp')

    # Phân vùng ảnh bằng phương pháp dựa trên đặc trưng và thuộc tính (màu sắc)
    segmented_image_region = segment_image_by_region(image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image (Region-based)', segmented_image_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
