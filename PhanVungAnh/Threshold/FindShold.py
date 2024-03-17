#Tìm ngưỡng tự động dựa theo giải thuật 
import cv2
import numpy as np
import matplotlib.pyplot as plt

def auto_threshold_with_opencv(image_path):
    # Đọc ảnh bằng OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra lại đường dẫn.")
        return None
    
    T = np.mean(image)  # Bước 1: Khởi tạo giá trị T là trung bình của ảnh
    stable = False
    
    thresholds = []
    
    while not stable:
        # Bước 2: Xác định 2 nhóm điểm ảnh C1 và C2
        _, binary = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)
        C1 = image[binary == 255]
        C2 = image[binary == 0]
        
        # Bước 3: Tính trung bình về mức xác của C1 và C2
        μ1 = np.mean(C1)
        μ2 = np.mean(C2)
        
        # Bước 4: Tính giá trị mới của T
        new_T = 0.5 * (μ1 + μ2)
        thresholds.append(new_T)
        
        # Kiểm tra điều kiện dừng
        if abs(T - new_T) < 0.5:
            stable = True
        else:
            T = new_T
    
    return image, thresholds[-1], thresholds

def main():
    # Đường dẫn đến ảnh
    image_path = "PhanVungAnh/Threshold/test.jpg"
    
    # Xác định ngưỡng tự động
    image, threshold, thresholds = auto_threshold_with_opencv(image_path)
    
    if threshold is not None:
        # Xuất ảnh gốc
        plt.subplot(1, 3, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Ảnh Gốc')
        plt.axis('off')
        
        # Vẽ biểu đồ ngưỡng
        plt.subplot(1, 3, 2)
        plt.plot(thresholds, color='b', linestyle='-')
        plt.xlabel('Số lần lặp')
        plt.ylabel('Ngưỡng')
        plt.title('Biểu Đồ Ngưỡng')
        
        # Xử lí ảnh với ngưỡng đã xác định
        _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        
        # Xuất kết quả sau khi xử lí
        plt.subplot(1, 3, 3)
        plt.imshow(binary, cmap='gray')
        plt.title('Kết Quả Sau Khi Xử Lí')
        plt.axis('off')
        
        plt.show()

if __name__ == "__main__":
    main()
