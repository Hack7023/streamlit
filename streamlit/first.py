import streamlit as st

def func():
    st.markdown("<h1 style = 'text-align:center; color:white;'>Welcome to Desigining</h1>", unsafe_allow_html=True)
    exp = st.text_input("write epression to calculate")
    if(len(exp)!=0):
        try:
            c=eval(str(exp))

            st.write("value of given expression ", c)
        except:
            st.write("Expression given is not valid")

button1=st.button("calsi")
button2=st.button("turtle")
if(button1):
    func()
if(button2):
    from frontend import *

    
