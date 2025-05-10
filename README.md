# SL_FinalProject_YOLO

### Cài đặt 
conda create -n yolov11 python=3.11  
conda activate yolov11  
pip install -r requirements.txt

### Thực thi
streamlit run app.py

### Lưu ý
- Nên xóa ảnh trước khi qua trang khác. Vì khi upload ảnh lên bất kỳ trang nào, ảnh sẽ được lưu vào phần upload, nếu không xóa ảnh trước khi qua trang khác thì nó sẽ được dùng cho trang đó, gây dư thừa ảnh không đáng có. Nhưng nếu muốn dùng 1 ảnh cho cả 2 version thì có thể để yên mà không cần xóa.
