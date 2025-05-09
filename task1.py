import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from io import BytesIO

def task1():
    # Load YOLO model
    if "model1" not in st.session_state:
        st.session_state["model1"] = YOLO("yolo11n.pt")
    model = st.session_state["model1"]

    # Streamlit UI
    st.title("Object Detection with Standard YOLOv11")
    st.write("Upload an image to detect objects.")

    # --- Sidebar ---
    st.sidebar.title("Settings")

    # Slider để chọn confidence threshold
    confidence_threshold = st.sidebar.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.25,  # Giá trị mặc định
        step=0.05
    )

    # Initialize session state for storing images
    if "saved_images1" not in st.session_state:
        st.session_state["saved_images1"] = []

    # Sidebar to display saved images
    st.sidebar.title("Saved Images")

    # Nút reload sidebar
    if "reload_sidebar" not in st.session_state:
        st.session_state["reload_sidebar"] = False

    if st.sidebar.button("🔄 Reload Sidebar"):
        st.session_state["reload_sidebar"] = not st.session_state["reload_sidebar"]  # Đảo trạng thái để làm mới sidebar

    # Hiển thị danh sách ảnh đã lưu trong session state
    if st.session_state["saved_images1"]:
        for idx, img in enumerate(st.session_state["saved_images1"]):
            st.sidebar.image(img, caption=f"Image {idx + 1}", use_container_width=True)

            # Thêm nút tải xuống dưới mỗi hình ảnh
            st.sidebar.download_button(
                label=f"⬇️ Download image {idx + 1}",
                data=img,
                file_name=f"img_{idx + 1}.png",
                mime="image/png"
            )

            # Nút xóa ảnh đã lưu
            if st.sidebar.button(f"❌ Delete image {idx + 1}"):
                st.session_state["saved_images1"].pop(idx)

    # --- Main content ---
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("Detecting objects...")

        # Run YOLO inference with confidence threshold
        results = model.predict(np.array(image), conf=confidence_threshold)

        # Lấy kết quả từ YOLO
        result = results[0]  # YOLO luôn trả về danh sách, lấy phần tử đầu tiên
        annotated_image = result.plot()  # Annotated image as numpy array

        # Chuyển trực tiếp từ NumPy array sang byte
        img_bytes = BytesIO()
        Image.fromarray(annotated_image).save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()  # Lấy dữ liệu nhị phân của ảnh

        # Thêm ảnh đã xử lý (dạng byte) vào session state
        if img_bytes not in st.session_state["saved_images1"]:
            st.session_state["saved_images1"].append(img_bytes)

        # Hiển thị ảnh đã xử lý
        st.image(annotated_image, caption="Detected Objects", use_container_width=True)
