import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from io import BytesIO
import cv2

# Hàm detect image
def detect_image(model, confidence_threshold, iou_threshold):
    st.write("Upload an image to detect objects.")

    # Initialize session state for storing images
    if "saved_images2" not in st.session_state:
        st.session_state["saved_images2"] = []

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

            # Nút xóa ảnh đã lưu
            if st.sidebar.button(f"❌ Delete image {idx + 1}"):
                st.session_state["saved_images2"].pop(idx)

    # --- Main content ---
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load image and ensure that the image only has 3 color channels
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.write("Detecting objects...")

        # Run YOLO inference with confidence threshold
        results = model.predict(np.array(image), conf=confidence_threshold, iou=iou_threshold)

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

# Hàm live_streaming 
def live_streaming(model, conf_threshold, iou_threshold):
    stframe = st.empty()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not access the webcam. Please make sure your webcam is working.")
        return

    try:
        while st.session_state.get("is_detecting", False) and st.session_state.get("is_webcam_active", False):
            ret, frame = cap.read()

            if not ret:
                st.warning("Warning: Failed to read frame from the webcam. Retrying...")
                continue

            try:
                # Gọi mô hình dự đoán
                results = model.predict(source=frame, conf=conf_threshold, iou=iou_threshold)

                # Vẽ khung và nhãn tự động bằng .plot()
                annotated_frame = results[0].plot()

                # Hiển thị lên Streamlit
                stframe.image(annotated_frame, channels="BGR")

            except Exception as e:
                st.error(f"Error during model prediction: {str(e)}")

    finally:
        cap.release()
        cv2.destroyAllWindows()

def detect_webcam(model, confidence_threshold, iou_threshold):
    # --- Streamlit UI ---
    st.title("🔴 Realtime Detection with Webcam")
    # Nút Start
    if st.button("🚀 Start Webcam Detection") and not st.session_state.get("is_webcam_active", False):
        st.session_state["is_detecting"] = True
        st.session_state["is_webcam_active"] = True

    # Nếu webcam đang hoạt động thì gọi live_streaming
    if st.session_state.get("is_webcam_active", False):
        # Hiển thị nút Stop nếu webcam đang bật
        if st.button("🛑 Stop Webcam"):
            st.session_state["is_detecting"] = False
            st.session_state["is_webcam_active"] = False
        # Gọi hàm live_streaming
        live_streaming(model, confidence_threshold, iou_threshold)

def task2():
    # Load YOLO model
    if "model2" not in st.session_state:
        st.session_state["model2"] = YOLO("best.pt")
    model = st.session_state["model2"]

    # Streamlit UI
    st.title("Object Detection with Custom YOLOv11")

    # --- Sidebar ---
    st.sidebar.title("Settings")

    # Slider để chọn confidence threshold
    confidence_threshold = st.sidebar.slider(
        "Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.5,  # Giá trị mặc định từ session state
        step=0.05
    )
    # Slider để chọn IOU threshold (dùng cho NMS)
    iou_threshold = st.sidebar.slider(
        "IoU Threshold (NMS)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05
    )
    # Chọn chế độ phát hiện: ảnh hoặc webcam
    mode = st.sidebar.selectbox("Select Mode", ["Detect Image", "Webcam Detection"])
    if mode == "Detect Image":
        detect_image(model, confidence_threshold, iou_threshold)  # Gọi hàm detect_image với confidence_threshold
    elif mode == "Webcam Detection":
        detect_webcam(model, confidence_threshold, iou_threshold)

