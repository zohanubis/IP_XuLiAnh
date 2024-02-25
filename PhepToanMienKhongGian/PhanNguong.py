import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def phan_nguong(img, T):
    # Áp dụng phân ngưỡng đơn giản để chuyển đổi ảnh thành ảnh nhị phân
    _, thresholded_img = cv.threshold(img, T, 255, cv.THRESH_BINARY)
    
    return thresholded_img

def show_phan_nguong():
    fig = plt.figure(figsize=(16, 9))
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('PhepToanMienKhongGian/keodan_dau.tif', 0)
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")

    # Ngưỡng T
    T = 150
    
    # Áp dụng kỹ thuật phân ngưỡng và hiển thị ảnh kết quả
    thresholded_img = phan_nguong(img, T)
    ax2.imshow(thresholded_img, cmap='gray')
    ax2.set_title("Ảnh sau khi phân ngưỡng")

    plt.show()

# Hàm main
if __name__ == '__main__':
    show_phan_nguong()
