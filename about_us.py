import streamlit as st

def about_us():
    st.sidebar.success("Infomation about us ✌️.")
    st.markdown(f"# About Us")
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
