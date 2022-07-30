
import streamlit as st
import time
import regex as re
import base64

LOGO_IMAGE = "giphy.gif"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)


image_holder2 = st.empty()
images = ['giphy.gif']


image_holder2 = st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">LOADING...</p>
    </div>
    """,
    unsafe_allow_html=True
)
for item in images:

    time.sleep(4)

image_holder2.empty()
option = st.selectbox('',
                      ('Project\tdescription', 'main project'))
if(option == "Project\tdescription"):
    st.markdown(
        "<h1 style = 'text-align:center; color:white;'>Steps To Follow</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style = ' color:white;'>Step 1: Select main project from the drop down .</h3>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style = 'color:white;'>Step 2: Click on Browse files .</h3>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style = ' color:white;'>Step 3: Select file which is to be used</h3>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style = 'color:white;'>This project basically is a sorting app. which sort the email from large files which is provided by user and the app will display the content on screen first it displays the email and then the file content.</h3>", unsafe_allow_html=True)

else:
    gmail = []
    valid = []
    invalid = []
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        try:

            for mail in uploaded_file:
                gmail.append(mail.decode().replace("\r\n", ""))

            st.markdown(
                "<h1 style = ' color:white;margin-left:40%;'>Emails</h1>", unsafe_allow_html=True)
            for mail in gmail:

                ele = re.findall(
                    r"[a-zA-Z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[A-Za-z]+", mail)

                for e in ele:
                    valid.append(e)

            col1, col2 = st.columns(2)
            for i in range(len(valid)//2):
                col1.text(valid[i])
            for i in range(len(valid)//2+1, len(valid)):
                col2.text(valid[i])

            st.markdown(
                "<h1 style = 'text-align:center; color:white;'>File Contents</h1>", unsafe_allow_html=True)
            for mail in gmail:
                st.write(mail)

        except:
            st.write("invalid file format")
