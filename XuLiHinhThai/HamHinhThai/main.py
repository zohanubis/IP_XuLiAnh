import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def apply_morphology_transform(image, transform_type):
    # Tạo ma trận kernel
    kernel = np.ones((5, 5), np.uint8)

    # Áp dụng biến đổi hình thái tương ứng
    if transform_type == "Erosion":
        result = cv2.erode(image, kernel, iterations=1)
    elif transform_type == "Dilation":
        result = cv2.dilate(image, kernel, iterations=1)
    elif transform_type == "Opening":
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif transform_type == "Closing":
        result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    elif transform_type == "Gradient":
        result = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    elif transform_type == "Top Hat":
        result = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    elif transform_type == "Black Hat":
        result = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    else:
        print("Lựa chọn không hợp lệ.")
        return None

    return result

def open_image():
    # Mở hộp thoại để chọn file ảnh
    file_path = filedialog.askopenfilename()
    if file_path:
        # Đọc ảnh từ file
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        # Hiển thị cửa sổ chọn biến đổi hình thái
        show_transform_options(image)

def show_transform_options(image):
    # Tạo cửa sổ chọn biến đổi hình thái
    transform_window = tk.Toplevel(root)
    transform_window.title("Chọn phép biến đổi hình thái")

    # Thiết lập kích thước cửa sổ
    transform_window.geometry("300x500")

    # Tạo tiêu đề
    tk.Label(transform_window, text="Chọn phép biến đổi hình thái", font=("Helvetica", 14)).pack(pady=10)

    # Tạo danh sách các loại biến đổi hình thái
    options = ["Erosion", "Dilation", "Opening", "Closing", "Gradient", "Top Hat", "Black Hat"]

    # Tạo các nút chọn cho mỗi loại biến đổi hình thái
    for option in options:
        tk.Button(transform_window, text=option, command=lambda o=option: apply_and_show_transform(image, o), width=20, height=2, font=("Helvetica", 12)).pack(pady=5)


def apply_and_show_transform(image, transform_type):
    # Áp dụng biến đổi hình thái
    result = apply_morphology_transform(image, transform_type)

    if result is not None:
        # Hiển thị ảnh kết quả
        cv2.imshow(transform_type, result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Tạo cửa sổ gốc
root = tk.Tk()
root.title("Ứng dụng Xử lý ảnh hình thái")

# Tạo nút để mở file ảnh
tk.Button(root, text="Chọn ảnh", command=open_image).pack()

# Chạy vòng lặp chờ sự kiện
root.mainloop()
