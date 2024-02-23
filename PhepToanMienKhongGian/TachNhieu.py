import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def tach_nhieu(img, a, b, beta):
    # Áp dụng phép biến đổi tuyến tính cho ảnh để tách nhiễu
    enhanced_img = cv.convertScaleAbs(img, alpha=1, beta=-a)
    enhanced_img = cv.convertScaleAbs(enhanced_img, alpha=1/beta, beta=0)
    
    # Chuẩn hóa giá trị pixel trong phạm vi [0, 255]
    enhanced_img = np.clip(enhanced_img, 0, 255)
    
    return enhanced_img

def show_tach_nhieu():
    fig = plt.figure(figsize=(16, 9))
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('the-weeknd.webp', 0)
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")

    # Các hệ số a, b, beta
    a = 50
    b = 170
    beta = 3
    
    # Tách nhiễu ảnh và hiển thị ảnh kết quả
    enhanced_img = tach_nhieu(img, a, b, beta)
    ax2.imshow(enhanced_img, cmap='gray')
    ax2.set_title("Ảnh sau khi tách nhiễu")
    
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_tach_nhieu()
