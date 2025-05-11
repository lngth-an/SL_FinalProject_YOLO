# 🔍 SL_FinalProject_YOLO

## 👾 Giới thiệu

Đây là một **trang web hỗ trợ nhận diện vật thể** sử dụng công nghệ **YOLOv11** từ thư viện **Ultralytics**. Trang web được thiết kế trực quan và dễ sử dụng, với hai phiên bản nhận diện khác nhau nhằm phục vụ cả nhu cầu thử nghiệm cơ bản lẫn tùy biến nâng cao:

### 🔹 Version 1 – Standard YOLOv11
Sử dụng mô hình YOLOv11 với bộ trọng số (weights) mặc định do Ultralytics cung cấp. Phiên bản này hỗ trợ nhận diện nhiều vật thể phổ biến như **người**, **xe**, **động vật**, v.v... một cách **nhanh chóng và chính xác**.

### 🔸 Version 2 – Custom YOLOv11
Cho phép người dùng sử dụng **bộ trọng số đã chọn từ Version 1 để huấn luyện mô hình nhận diện các lớp vật thể mới**.  
Phù hợp với các bài toán đặc thù hoặc nhu cầu nhận diện nâng cao.

### 👀 Hai chế độ nhận diện
Cả hai phiên bản đều hỗ trợ:

🖼️ **Nhận diện từ ảnh tải lên**:  
  Chỉ cần chọn ảnh từ máy tính và hệ thống sẽ xử lý, trả về ảnh kèm kết quả nhận diện.

📷 **Nhận diện qua webcam trực tiếp**:  
  Hệ thống sử dụng webcam của bạn để phát hiện vật thể theo thời gian thực.

👉 Ngoài ra, ở mỗi chế độ, người dùng có thể **tùy chỉnh ngưỡng confidence (độ tin cậy)** — cho phép điều chỉnh độ nhạy của mô hình trong việc xác định vật thể.  
Điều này giúp linh hoạt hơn trong việc kiểm soát số lượng và độ chính xác của kết quả nhận diện hiển thị.

## 🛠️ Cài đặt môi trường

```bash
conda create -n yolo11 python=3.11
conda activate yolo11
pip install -r requirements.txt
```

 ## 🚀 Thực thi
```bash
streamlit run app.py
```

## 📝 Lưu ý
- Nên xóa ảnh trước khi qua version khác. Vì khi upload ảnh lên bất kỳ trang nào, ảnh sẽ được lưu vào phần upload.
- Nếu không xóa ảnh trước khi qua version mới thì nó sẽ được dùng cho version mới đó, gây dư thừa ảnh không đáng có. 
- Nhưng nếu muốn dùng 1 ảnh cho cả 2 version thì có thể để yên mà không cần xóa.
