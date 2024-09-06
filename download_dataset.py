import os
import zipfile
import gdown
import sys

# Thiết lập encoding UTF-8 cho đầu ra console
sys.stdout.reconfigure(encoding='utf-8')

links = [
    # 'https://drive.google.com/drive/folders/1ugJdQsGLZfuQUr6uUZ1xjTEahMR7_qpM', #L01
     'https://drive.google.com/drive/folders/1qlJZ-e8M7AJsdsm9wGtIdpoBB0YCppBZ', #L02
    # 'https://drive.google.com/drive/folders/1OfhVpIInYC8Q3bvtATis9DTVtW4-sqqb', #L03
    # 'https://drive.google.com/drive/folders/1ynlvpfiIV9u0LicSy2bmFW73ODxeke9J', #L04
    # 'https://drive.google.com/drive/folders/1G9XocpulEspLjwcxwlO4LgsRwWAM7AoQ', #L05
    # 'https://drive.google.com/drive/folders/1kB57aDfdIHCedsy0gRkTgWP6wQU1rHpd', #L06
    # 'https://drive.google.com/drive/folders/1-nNWSGVjbWTWvuRTMgti3kElzljsdAnl', #L07
    # 'https://drive.google.com/drive/folders/1k5x752gvwR4bwWQjZHzhRrrxea6kAh-r', #L08
    # 'https://drive.google.com/drive/folders/1IuRcRYhA68Bgv6LiAklRG2Ae3yXJWax9', #L09
    # 'https://drive.google.com/drive/folders/1u1uJrx4MUmbF6gXCnMJg15mZhKkdXxZN', #L10
    # 'https://drive.google.com/drive/folders/1yLSm_lQY1E_h8U5MM4WAnd1oPCXcB1Uo', #L11
    # 'https://drive.google.com/drive/folders/1M2ERH02pqFfG4EockYGBPWNqRIu_qb2t'  # L12
]

current_path = os.getcwd()
dataset_path = os.path.join(current_path, 'dataset')
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)
output_dir = os.path.join(current_path, 'images')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for url in links:
    gdown.download_folder(url, output=dataset_path, quiet=False)


# Lặp qua từng file zip trong thư mục dataset
for file_name in os.listdir(dataset_path):
    if file_name.endswith('.zip'):
        # Lấy 3 ký tự đầu tiên để xác định thư mục đích
        folder_name = file_name[:3]
        folder_output_dir = os.path.join(output_dir, folder_name)

        # Tạo thư mục đích nếu chưa tồn tại
        if not os.path.exists(folder_output_dir):
            os.makedirs(folder_output_dir)

        # Tạo thư mục con tương ứng với tên file zip
        zip_folder_name = file_name.replace('.zip', '')
        zip_folder_output_dir = os.path.join(
            folder_output_dir, zip_folder_name)
        if not os.path.exists(zip_folder_output_dir):
            os.makedirs(zip_folder_output_dir)

        file_path = os.path.join(dataset_path, file_name)
        print(
            f"Đang giải nén file: {file_name} vào thư mục {zip_folder_output_dir}")
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(zip_folder_output_dir)
        print(f"Hoàn thành giải nén file: {file_name}")

        # Xóa file zip sau khi giải nén
        # os.remove(file_path)
        # print(f"Đã xóa file zip: {file_name}")
