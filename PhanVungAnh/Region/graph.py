#Chưa hoàn thiện

import cv2
import numpy as np
def segment_image_by_graph(image):
    # Khởi tạo mask với kích thước bằng với kích thước của ảnh và giá trị ban đầu là 0 (background)
    mask = np.zeros(image.shape[:2], np.uint8)

    # Khởi tạo mặt định xác định vùng cần phân vùng (foreground)
    rect = (50, 50, 450, 290)  # (x, y, width, height) của vùng cần phân vùng

    # Khởi tạo mặt định cho GrabCut
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Áp dụng GrabCut để phân vùng ảnh
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Tạo mask chỉ chứa các điểm ảnh thuộc vùng cần phân vùng và vùng không xác định
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Áp dụng mask lên ảnh gốc để tạo ảnh phân vùng
    segmented_image = image * mask2[:, :, np.newaxis]

    return segmented_image

def main():
    # Load ảnh
    image = cv2.imread('PhanVungAnh/Region/the_weeknd.webp')

    # Phân vùng ảnh bằng phương pháp dựa trên đồ thị (GrabCut)
    segmented_image_graph = segment_image_by_graph(image)

    # Hiển thị ảnh gốc và ảnh đã phân vùng
    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image (Graph-based)', segmented_image_graph)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
