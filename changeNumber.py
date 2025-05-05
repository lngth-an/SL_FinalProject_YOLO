import os

def change_number_in_files(folder_path, f):
    # Kiểm tra thư mục có tồn tại không
    if not os.path.isdir(folder_path):
        print(f"Thư mục {folder_path} không tồn tại!")
        return
    
    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Đọc tất cả các dòng trong file
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # Xử lý từng dòng
                new_lines = []
                for line in lines:
                    numbers = line.strip().split()
                    # Kiểm tra dòng có đúng 5 số không
                    if len(numbers) == 5:
                        # Thay số đầu tiên (a) bằng f, giữ nguyên b,c,d,e
                        numbers[0] = str(f)
                        new_lines.append(" ".join(numbers) + "\n")
                    else:
                        # Giữ nguyên dòng nếu không có 5 số
                        new_lines.append(line)
                
                # Ghi lại nội dung vào file
                with open(file_path, 'w') as file:
                    file.writelines(new_lines)
                print(f"Đã thay đổi số trong file {filename}")
                
            except Exception as e:
                print(f"Lỗi khi xử lý file {filename}: {str(e)}")

# Nhập đường dân thư mục và số cần thay đổi
# folder_path = input("Nhập đường dẫn thư mục: ")
folder_path = "D:\htk_temp"
# Nhập f là số cần thay đổi
f = 82

# Gọi hàm để thay đổi số
change_number_in_files(folder_path, f)