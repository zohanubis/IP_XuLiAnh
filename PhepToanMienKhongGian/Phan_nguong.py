import cv2 as cv
import matplotlib.pyplot as plt

# Hàm thực hiện cắt ngưỡng ảnh
def cat_nguong(img, th):
    return img > th

# Hàm để hiển thị ảnh gốc và ảnh sau khi cắt ngưỡng
def show_cat_nguong():
    # Tạo một figure với kích thước 16x9
    fig = plt.figure(figsize=(16, 9))
    # Tạo hai trục con để hiển thị ảnh gốc và ảnh cắt ngưỡng
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('PhepToanMienKhongGian/keodan_dau.tif', 0)
    # Hiển thị ảnh gốc
    ax1.imshow(img, cmap='gray')
    ax1.set_title("ảnh gốc")

    # Thực hiện cắt ngưỡng ảnh với ngưỡng th=117 và hiển thị ảnh kết quả
    y = cat_nguong(img, th=117)
    ax2.imshow(y, cmap='gray')
    ax2.set_title("ảnh cắt ngưỡng")
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_cat_nguong()
