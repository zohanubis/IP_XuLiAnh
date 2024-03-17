import math
import cv2
import numpy as np

# Tham khảo: https://docs.opencv.org/master/d6/d10/tutorial_py_houghlines.html
def my_hough(img, rho=1, theta=np.pi/180, threshold=100):
    img_height, img_width = img.shape[:2]
    diagonal_length = int(math.sqrt(img_height*img_height + img_width*img_width))
    
    print('[My Hough] Chiều cao ảnh: %d | Chiều rộng ảnh: %d | Độ dài đường chéo ảnh: %d' % (img_height, img_width, diagonal_length))
    
    num_rho = int(diagonal_length / rho)    
    num_theta = int(np.pi / theta)
    
    edge_matrix = np.zeros([2*num_rho+1, num_theta]) # Kích thước: num_rho x num_theta
    
    print('[My Hough] Kích thước ma trận cạnh: %d x %d' % (edge_matrix.shape[0], edge_matrix.shape[1]))
    
    idx	= np.squeeze(cv2.findNonZero(img)) # Kích thước: 4468 x 2 (ví dụ, số hàng = số điểm ảnh trắng trên ảnh được xử lý bằng thuật toán cạnh Canny!)
    
    range_theta = np.arange(0, np.pi, theta)
    theta_matrix = np.stack((np.cos(np.copy(range_theta)), np.sin(np.copy(range_theta))), axis=-1) # Kích thước: 180 x 2
    
    vote_matrix = np.dot(idx, np.transpose(theta_matrix)) # => (4468 x 2) * (180 x 2)T = (4468 x 2) * (2 x 180) = 4468 x 180
    print('[My Hough] Kích thước ma trận bỏ phiếu: %d x %d' % (vote_matrix.shape[0], vote_matrix.shape[1]))
    
    # Lặp trên ma trận bỏ phiếu và tích lũy giá trị trên ma trận cạnh
    for vr in range(vote_matrix.shape[0]):
        for vc in range(vote_matrix.shape[1]):
            rho_pos = int(round(vote_matrix[vr, vc]))+num_rho
            edge_matrix[rho_pos, vc] += 1
    
    print('[My Hough] Tổng của ma trận cạnh = %d | Max = %d | Min = %d' % (int(np.sum(edge_matrix)), int(np.max(edge_matrix)), int(np.min(edge_matrix))))
    
    line_idx = np.where(edge_matrix > threshold)
    
    rho_values = list(line_idx[0])
    rho_values = [r-num_rho for r in rho_values]
    theta_values = list(line_idx[1])
    theta_values = [t/180.0*np.pi for t in theta_values]
    
    line_idx = list(zip(rho_values, theta_values))
    line_idx = [[li] for li in line_idx]
    return line_idx

def main():
    # Đọc ảnh đầu vào
    img = cv2.imread('PhanVungAnh/Hough/geometry.jpg')

    # Chuyển đổi sang ảnh thang độ xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Sử dụng thuật toán Canny để phát hiện cạnh
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Sử dụng thuật toán Hough của OpenCV
    lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
    print('[OpenCV Hough] Số đường thẳng: %d' % len(lines))
    
    # Vẽ các đường thẳng đã phát hiện lên ảnh gốc
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)    
    cv2.imwrite('PhanVungAnh/Hough/geo_hough.jpg',img)

    # Thực hiện thuật toán Hough do bản thân viết
    lines = my_hough(edges, rho=1, theta=np.pi/180, threshold=100)
    print('[My Hough] Số đường thẳng: %d' % len(lines))
    
    # Vẽ các đường thẳng đã phát hiện lên ảnh gốc
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)    
    cv2.imwrite('geo_myhough.jpg',img)

if __name__ == "__main__":
    main()
