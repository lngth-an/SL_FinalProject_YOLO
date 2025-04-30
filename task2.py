import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from io import BytesIO

def task2():
    # Load YOLO model
    model = YOLO("yolo12n.pt")  # Đảm bảo bạn đã tải trọng số yolo12n.pt

    # Streamlit UI
    st.title("Object Detection with Custom YOLOv12")
    st.write("Upload an image to detect objects.")

    # Initialize session state for storing images
    if "saved_images2" not in st.session_state:
        st.session_state["saved_images2"] = []

    # --- Sidebar ---
    # Sidebar to display saved images
    st.sidebar.title("Saved Images")

    # Nút reload sidebar
    if "reload_sidebar" not in st.session_state:
        st.session_state["reload_sidebar"] = False

    if st.sidebar.button("🔄 Reload Sidebar"):
        st.session_state["reload_sidebar"] = not st.session_state["reload_sidebar"]  # Đảo trạng thái để làm mới sidebar

    # Hiển thị danh sách ảnh đã lưu trong session state
    if st.session_state["saved_images2"]:
        for idx, img in enumerate(st.session_state["saved_images2"]):
            st.sidebar.image(img, caption=f"Image {idx + 1}", use_container_width=True)

            # Thêm nút tải xuống dưới mỗi hình ảnh
            st.sidebar.download_button(
                label=f"⬇️ Download image {idx + 1}",
                data=img,
                file_name=f"img_{idx + 1}.png",
                mime="image/png"
            )

    # --- Main content ---
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("Detecting objects...")

        # Run YOLO inference
        results = model(np.array(image))

        # Lấy kết quả từ YOLO
        result = results[0]  # YOLO luôn trả về danh sách, lấy phần tử đầu tiên
        annotated_image = result.plot()  # Annotated image as numpy array

        # Chuyển trực tiếp từ NumPy array sang byte
        img_bytes = BytesIO()
        Image.fromarray(annotated_image).save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()  # Lấy dữ liệu nhị phân của ảnh

        # Thêm ảnh đã xử lý (dạng byte) vào session state
        if img_bytes not in st.session_state["saved_images2"]:
            st.session_state["saved_images2"].append(img_bytes)

        # Hiển thị ảnh đã xử lý
        st.image(annotated_image, caption="Detected Objects", use_container_width=True)
