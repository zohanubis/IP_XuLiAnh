import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = cv2.imread('PhanVungAnh/HamTachBienOpenCv/test.jpg', cv2.IMREAD_GRAYSCALE)

# Canny Edge Detection
edges_canny = cv2.Canny(image, 100, 200)

# Sobel Edge Detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = np.uint8(np.sqrt(sobel_x**2 + sobel_y**2))

# Laplacian Edge Detection
edges_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Scharr Edge Detection
scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
edges_scharr = np.uint8(np.sqrt(scharr_x**2 + scharr_y**2))

# Hiển thị và lưu ảnh gốc và ảnh kết quả
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(edges_laplacian, cmap='gray')
plt.title('Laplacian Edge Detection')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(edges_scharr, cmap='gray')
plt.title('Scharr Edge Detection')
plt.axis('off')

plt.tight_layout()
plt.show()
