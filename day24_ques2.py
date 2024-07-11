import cv2
import matplotlib.pyplot as plt
import os

# Đường dẫn đến thư mục chứa tập dữ liệu (sử dụng đường dẫn tuyệt đối)
dataset_folder = "dataset"

# Tên của tệp ảnh
image_filename = "1.jpg"

# Xây dựng đường dẫn hoàn chỉnh tới tệp ảnh
image_path = os.path.join(dataset_folder, image_filename)

# Kiểm tra xem tệp ảnh có tồn tại không
if os.path.exists(image_path):
    # Đọc và hiển thị ảnh
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(image,cmap="gray")
    plt.show()
else:
    print(f"Ảnh '{image_filename}' không tồn tại trong thư mục '{dataset_folder}'.")
