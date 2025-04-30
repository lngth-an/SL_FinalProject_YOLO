import streamlit as st
from home import home
from task1 import task1
from task2 import task2
from about_us import about_us

st.set_page_config(
    page_title="YOLO Object Detection",
    page_icon="🔍",
    layout="wide"  # Hoặc "centered" nếu muốn nội dung căn giữa
)

# --- CSS Sidebar tuỳ chỉnh ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        min-width: 300px;
        max-width: 75vw;
    }
    </style>
""", unsafe_allow_html=True)

# Định nghĩa các trang
page_names_to_funcs = {
    "Home": home,
    "Standard YOLOv12": task1,
    "Custom YOLOv12": task2,
    "About us": about_us
}

# Điều hướng trang
demo_name = st.sidebar.radio("Where do you want to come?", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()