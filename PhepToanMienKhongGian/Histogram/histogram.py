import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def display_image_with_histogram(image_path):
    # Load ảnh từ đường dẫn
    img = cv2.imread(image_path, 0)
    
    # Cân bằng histogram cho ảnh
    img_equalized = cv2.equalizeHist(img)
    
    # Tạo subplot
    fig = plt.figure(figsize=(16, 9))
    (ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

    # Hiển thị ảnh gốc và histogram của ảnh gốc
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Ảnh gốc")

    ax2.hist(img.ravel(), bins=256, range=[0, 256])
    ax2.set_title("Histogram ảnh gốc")

    # Hiển thị ảnh cân bằng histogram và histogram của ảnh cân bằng
    ax3.imshow(img_equalized, cmap='gray')
    ax3.set_title("Ảnh cân bằng histogram")

    ax4.hist(img_equalized.ravel(), bins=256, range=[0, 256])
    ax4.set_title("Histogram ảnh cân bằng")

    plt.show()

def select_image_and_display():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image_with_histogram(file_path)
    else:
        print("Không có ảnh được chọn")

select_image_and_display()
