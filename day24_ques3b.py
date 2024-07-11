import cv2
import matplotlib.pyplot as plt
import os

# Đường dẫn đến thư mục chứa tập dữ liệu (sử dụng đường dẫn tuyệt đối)
dataset_folder = "dataset"

# Tên của tệp ảnh
image_filename = "1.jpg"

# Xây dựng đường dẫn hoàn chỉnh tới tệp ảnh
image_path = os.path.join(dataset_folder, image_filename)
image = cv2.imread(image_path)

# Cắt 1 phần ảnh nhỏ tại tọa độ (x1, y1) đến (x2, y2)
x1, y1 = 200, 200  # Tọa độ điểm bắt đầu cắt
x2, y2 = 500, 500  # Tọa độ điểm kết thúc cắt

cropped_image = image[y1:y2, x1:x2]

# Hiển thị phần ảnh đã cắt
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title('Phần ảnh đã cắt')
plt.axis('off')
plt.show()
