import cv2 as cv
import matplotlib.pyplot as plt

# Hàm thực hiện đảo ảnh (đảo giá trị pixel)
def dao_anh(img):
    return 255 - img

# Hàm để hiển thị ảnh gốc và ảnh sau khi đảo
def show_dao_anh():
    # Tạo một figure với kích thước 16x9
    fig = plt.figure(figsize=(16, 9))
    # Tạo hai trục con để hiển thị ảnh gốc và ảnh sau khi đảo
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('PhepToanMienKhongGian/daoanh.tif', 0)
    # Hiển thị ảnh gốc
    ax1.imshow(img, cmap='gray')
    ax1.set_title("ảnh gốc")

    # Thực hiện đảo ảnh và hiển thị ảnh kết quả
    y = dao_anh(img)
    ax2.imshow(y, cmap='gray')
    ax2.set_title("ảnh đảo")
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_dao_anh()
