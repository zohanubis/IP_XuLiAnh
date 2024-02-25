import cv2 as cv
import matplotlib.pyplot as plt

# Hàm thực hiện chuyển đổi logarit
def Chuyen_doi_logarit(img, c):
    return float(c) * cv.log(1.0 + img)

# Hàm để hiển thị ảnh gốc và ảnh sau khi chuyển đổi bằng logarit
def show_Chuyen_doi_logarit():
    # Tạo một figure với kích thước 16x9
    fig = plt.figure(figsize=(16, 9))
    # Tạo hai vùng con
    ax1, ax2 = fig.subplots(1, 2)

    # Đọc ảnh đầu vào
    img = cv.imread('PhepToanMienKhongGian/log.tif')
    # Hiển thị ảnh gốc
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")

    # Thực hiện chuyển đổi logarit và hiển thị ảnh kết quả
    y = Chuyen_doi_logarit(img, 2)
    ax2.imshow(y, cmap='gray')
    ax2.set_title("Chuyển đổi bằng hàm Logarit")
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_Chuyen_doi_logarit()
