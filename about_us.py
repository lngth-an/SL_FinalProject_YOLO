import streamlit as st

def about_us():
    st.sidebar.success("Infomation about us ✌️.")
    st.markdown(f"# About Us")
    st.text(
        """
        From University of Science - VNUHCM, we are:\n
        👩‍🎓 Lê Nguyễn Thiên An - 📧 22120003@student.hcmus.edu.vn\n
        👨‍🎓 Bùi Việt Bình - 📧 22120030@student.hcmus.edu.vn\n
        👩‍🎓 Nguyễn Phát Kim Nhung -  📧 22120259@student.hcmus.edu.vn
    """
    )
    
