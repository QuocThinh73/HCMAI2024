import os
import zipfile
import gdown

current_path = os.getcwd()
dataset_path = os.path.join(current_path, 'dataset')
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)
output_dir = os.path.join(current_path, 'images')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

links = [
    'https://drive.google.com/drive/folders/1ugJdQsGLZfuQUr6uUZ1xjTEahMR7_qpM',  # L01
    # 'https://drive.google.com/drive/folders/1qlJZ-e8M7AJsdsm9wGtIdpoBB0YCppBZ', # L03
    # 'https://drive.google.com/drive/folders/1ynlvpfiIV9u0LicSy2bmFW73ODxeke9J', # L04
    # 'https://drive.google.com/drive/folders/1G9XocpulEspLjwcxwlO4LgsRwWAM7AoQ', #L05
    # 'https://drive.google.com/drive/folders/1kB57aDfdIHCedsy0gRkTgWP6wQU1rHpd', #L06
    # 'https://drive.google.com/drive/folders/1-nNWSGVjbWTWvuRTMgti3kElzljsdAnl', #L07
    # 'https://drive.google.com/drive/folders/1k5x752gvwR4bwWQjZHzhRrrxea6kAh-r', #L08
    # 'https://drive.google.com/drive/folders/1IuRcRYhA68Bgv6LiAklRG2Ae3yXJWax9', #L09
    # 'https://drive.google.com/drive/folders/1u1uJrx4MUmbF6gXCnMJg15mZhKkdXxZN', #L10
    # 'https://drive.google.com/drive/folders/1yLSm_lQY1E_h8U5MM4WAnd1oPCXcB1Uo', #L11
    # 'https://drive.google.com/drive/folders/1M2ERH02pqFfG4EockYGBPWNqRIu_qb2t', #L12
]

for url in links:
    gdown.download_folder(url, output=dataset_path, quiet=False)

# Lặp qua từng file trong thư mục
for file_name in os.listdir(dataset_path):
    if file_name.endswith('.zip'):
        file_path = os.path.join(dataset_path, file_name)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
