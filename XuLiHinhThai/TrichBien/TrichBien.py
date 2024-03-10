import cv2 as cv
import numpy as np

# Canny Edge Detection Algorithm
# Mở camera
camera = cv.VideoCapture(0)

while True:
    # Đọc frame từ camera
    _, frame = camera.read()
    
    # Hiển thị frame từ camera
    cv.imshow('Camera', frame)
    
    # Áp dụng phép Laplacian trên frame
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian', laplacian)
    
    # Áp dụng thuật toán Canny Edge Detection trên frame
    edges = cv.Canny(frame, 100, 100) #(frame ảnh đầu vào , ngưỡng dưới, ngưỡng trên)
    cv.imshow('Canny', edges)
    
    # Chờ 5ms, nếu nhấn phím 'x' thì thoát
    if cv.waitKey(5) == ord('x'):
        break

# Giải phóng camera và đóng tất cả cửa sổ hiển thị
camera.release()
cv.destroyAllWindows()
