import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def tang_do_tuong_phan(img, alpha, beta, gamma, a, b):
    # Tính giá trị mới của điểm a và b dựa trên các hệ số alpha và beta
    va = alpha * a
    vb = beta * (b - a) + va
    
    # Tạo một bản sao của ảnh đầu vào để không làm thay đổi ảnh gốc
    enhanced_img = np.copy(img)
    
    # Áp dụng phép biến đổi tuyến tính cho ảnh để tăng độ tương phản
    enhanced_img = cv.convertScaleAbs(enhanced_img, alpha=alpha, beta=beta)
    
    # Chuẩn hóa giá trị pixel trong phạm vi [va, vb]
    enhanced_img = np.clip(enhanced_img, va, vb)
    
    # Áp dụng phép biến đổi gamma
    enhanced_img = np.power(enhanced_img, gamma)
    
    return enhanced_img

def show_tang_do_tuong_phan():
    fig = plt.figure(figsize=(16, 9))
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('PhepToanMienKhongGian/sanbay.tif', 0)
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")

    # Các hệ số alpha, beta, gamma, a, b
    alpha = 1
    beta = 1
    gamma = 1.5
    a = np.min(img)
    b = np.max(img)
    
    # Tăng độ tương phản của ảnh và hiển thị ảnh kết quả
    enhanced_img = tang_do_tuong_phan(img, alpha, beta, gamma, a, b)
    ax2.imshow(enhanced_img, cmap='gray')
    ax2.set_title("Ảnh sau khi tăng độ tương phản")
    
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_tang_do_tuong_phan()
