import streamlit as st
from PIL import Image

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
def home():
    st.sidebar.success("You are at home now 💒.")
    image = Image.open('./image/animals.jpg')
    st.image(image)
    st.write("# Welcome to Animal Recognition Software! 👋")
    st.write("""This is a demo product for animal species classification model.\n
    This product allows predicting animal names through image files\n
    To learn more about the software, go to SideBar for navigation.!
    """)

def about_us():
    st.sidebar.success("Infomation about us ✌️.")
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.markdown(f"## Developer")
    st.text(
        """
        Coming from University of Science - VNUHCM, we are:\n
        Lê Nguyễn Thiên An 👩‍🎓- 📧 22120003@student.hcmus.edu.vn\n
        Bùi Việt Bình 👨‍🎓- 📧 22120030@student.hcmus.edu.vn\n
        Nguyễn Phát Kim Nhung 👩‍🎓-  📧 22120259@student.hcmus.edu.vn
    """
    )
    #Hiển thị thông tin về mô hình và tập dữ liệu
    # st.markdown("## Architech")
    # st.markdown("### PhoBERT: Pre-trained language models for Vietnamese")
    # st.markdown("Pre-trained PhoBERT models are the state-of-the-art language models for Vietnamese")
    # st.text("""
    #         @inproceedings{phobert,\n\t
    #         title     = {{PhoBERT: Pre-trained language models for Vietnamese}},\n\t
    #         author    = {Dat Quoc Nguyen and Anh Tuan Nguyen},\n\t
    #         booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2020},\n\t
    #         year      = {2020},\n\t
    #         pages     = {1037--1042}\n\t
    #         }""")
    # st.markdown("## Dataset")
    # st.markdown("### Title:")
    # st.markdown("UIT-VSFC: Vietnamese Students’ Feedback Corpus for Sentiment Analysis")
    # st.markdown("### Author's Name:")
    # st.markdown("Nguyen, Kiet Van and Nguyen, Vu Duc and Nguyen, Phu X. V. and Truong, Tham T. H. and Nguyen, Ngan Luu-Thuy")
    # st.markdown("### Year:")
    # st.markdown("2018")
    # st.markdown("### Link:")
    # st.markdown("https://nlp.uit.edu.vn/datasets/")
    # st.markdown("### Description")          
    # st.markdown("Students’ feedback is a vital resource for the interdisciplinary research involving the combining of two different research fields between sentiment analysis and education. Vietnamese Students’ Feedback Corpus (UIT-VSFC) is the resource consists of over 16,000 sentences which are human-annotated with two different tasks: sentiment-based and topic-based classifications.")          

page_names_to_funcs = {
    "Home": home,
    # "Chatbox Feedback": chatbox_feedback,
    # "File Feedback": file_feedback,
    "About us": about_us
}

demo_name = st.sidebar.selectbox("Where do you want to come?", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()