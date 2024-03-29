import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def Tich_chap(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp =  img[i-1, j-1]    * mask[0, 0]\
                   +  img[i-1, j]      * mask[0, 1]\
                   +  img[i-1, j + 1]  * mask[0, 2]\
                   +  img[i, j-1]      * mask[1, 0]\
                   +  img[i, j]        * mask[1, 1]\
                   +  img[i, j + 1]    * mask[1, 2]\
                   +  img[i + 1, j-1]  * mask[2, 0]\
                   +  img[i + 1, j]    * mask[2, 1]\
                   +  img[i + 1, j + 1]* mask[2, 2]
            img_new[i, j]= temp
    img_new = img_new.astype(np.uint8)
    return img_new

def nhap_anh():
    root = tk.Tk()
    root.withdraw()
    duong_dan = filedialog.askopenfilename()
    if duong_dan:
        img = cv2.imread(duong_dan, 0)  # Đọc ảnh dưới dạng ảnh xám
        return img
    else:
        print("Không có ảnh được chọn.")
        return None

locTB3x3 = np.array(([1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9],
                     [1/9, 1/9, 1/9]), dtype="float")

locTB3x3_trong_so = np.array(([1/16, 2/16, 1/16],
                              [2/16, 4/16, 2/16],
                              [1/16, 2/16, 1/16]), dtype="float")

locGaussian3x3 = np.array(([0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976],
                           [0.1238/4.8976, 0.2042/4.8976, 0.1238/4.8976],
                           [0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976]), dtype="float")

def loc_trung_vi(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]
            temp = sorted(temp)
            img_new[i, j] = temp[4]
    return img_new

def loc_max(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]
            temp = max(temp)
            img_new[i, j] = temp
    return img_new

image = nhap_anh()

if image is not None:
    print("Đã chọn ảnh.")
    fig = plt.figure(figsize=(16, 9))
    (ax1, ax2, ax3), (ax4, ax5, ax6) = fig.subplots(2, 3)

    ax1.imshow(image, cmap='gray')
    ax1.set_title("Ảnh gốc")

    imgTB3x3 = Tich_chap(image, locTB3x3)
    ax2.imshow(imgTB3x3, cmap='gray')
    ax2.set_title("Ảnh lọc Trung bình 3x3")

    imgTB_TS_3x3 = Tich_chap(image, locTB3x3_trong_so)
    ax3.imshow(imgTB_TS_3x3, cmap='gray')
    ax3.set_title("Ảnh lọc Trung bình có trọng số 3x3")

    imgGaussian_3x3 = Tich_chap(image, locGaussian3x3)
    ax4.imshow(imgGaussian_3x3, cmap='gray')
    ax4.set_title("Ảnh lọc Gaussian 3x3")

    imgTV_3x3 = loc_trung_vi(image)
    ax5.imshow(imgTV_3x3, cmap='gray')
    ax5.set_title("Ảnh lọc Trung vị 3x3")

    imgmax_3x3 = loc_max(image)
    ax6.imshow(imgmax_3x3, cmap='gray')
    ax6.set_title("Ảnh lọc Max 3x3")

    plt.show()
else:
    print("Không thể đọc ảnh.")
