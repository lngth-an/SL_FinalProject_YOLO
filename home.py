import streamlit as st
from PIL import Image

def home():
    st.sidebar.success("You are at home now 💒.")
    image = Image.open('./image/objectDetection.jpg')
    st.image(image)
    st.write("# Welcome to Object Detection Web! 👋")
    st.write("""
    This is a demo product for object dectection model.\n
    This product allows predicting object names through image files.\n
    To learn more about the web, go to SideBar for navigation!
    """)