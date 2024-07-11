import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Đường dẫn đến thư mục chứa tập dữ liệu (sử dụng đường dẫn tuyệt đối)
dataset_folder = "dataset"

# Tên của tệp ảnh
image_filename = "1.jpg"

# Xây dựng đường dẫn hoàn chỉnh tới tệp ảnh
image_path = os.path.join(dataset_folder, image_filename)
image = cv2.imread(image_path)

# Tăng cường độ sáng ảnh lên 50 đơn vị
brightened_image = image.astype(np.float32) + 50
brightened_image = np.clip(brightened_image, 0, 255)
brightened_image = brightened_image.astype(np.uint8)

# Giảm cường độ sáng xuống 80 đơn vị
darkened_image = image.astype(np.float32) - 80
darkened_image = np.clip(darkened_image, 0, 255)
darkened_image = darkened_image.astype(np.uint8)

# Hiển thị ảnh sau khi tăng cường và giảm cường độ sáng
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Ảnh gốc')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB))
plt.title('Tăng cường độ sáng (+50)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(darkened_image, cv2.COLOR_BGR2RGB))
plt.title('Giảm cường độ sáng (-80)')
plt.axis('off')

plt.show()
