import multiprocessing
from turtle import onclick

import streamlit as st
from backend import *

st.title("Turtle App")
st.text("put star ,square")
title = st.text_input("Canvas Title", value="My Canvas")
width = st.number_input("Canvas Width", value=500)
height = st.number_input("Canvas Height", value=500)

clicked = st.button("Paint")

t = multiprocessing.Process(target=canvas_builder, args=(title, width, height, ))

if clicked:
   t.start()
