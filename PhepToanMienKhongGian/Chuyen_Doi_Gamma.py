import cv2 as cv
import matplotlib.pyplot as plt

# Hàm thực hiện chuyển đổi Gamma
def Chuyen_Doi_Gamma(img, gamma, c):
    return float(c) * pow(img, float(gamma))

# Hàm để hiển thị ảnh gốc và các ảnh sau khi chuyển đổi với các giá trị gamma khác nhau
def show_Chuyen_Doi_Gamma():
    # Tạo một figure với kích thước 16x9
    fig = plt.figure(figsize=(16, 9))
    # Tạo một lưới 2x2 để hiển thị ảnh gốc và các ảnh chuyển đổi
    (ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

    # Đọc ảnh đầu vào (ảnh xám)
    img = cv.imread('PhepToanMienKhongGian/sanbay.tif', 0)
    # Hiển thị ảnh gốc
    ax1.imshow(img, cmap='gray')
    ax1.set_title("ảnh gốc")

    # Thực hiện chuyển đổi Gamma với gamma = 3 và hiển thị ảnh kết quả
    y1 = Chuyen_Doi_Gamma(img, 3.0, 1.0)
    ax2.imshow(y1, cmap='gray')
    ax2.set_title("gamma=3")

    # Thực hiện chuyển đổi Gamma với gamma = 4 và hiển thị ảnh kết quả
    y2 = Chuyen_Doi_Gamma(img, 4.0, 1.0)
    ax3.imshow(y2, cmap='gray')
    ax3.set_title("gamma=4")

    # Thực hiện chuyển đổi Gamma với gamma = 5 và hiển thị ảnh kết quả
    y3 = Chuyen_Doi_Gamma(img, 5.0, 1.0)
    ax4.imshow(y3, cmap='gray')
    ax4.set_title("gamma=5")
    plt.show()

# Hàm main
if __name__ == '__main__':
    show_Chuyen_Doi_Gamma()
