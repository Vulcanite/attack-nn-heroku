from io import RawIOBase
import streamlit as st
from PIL import Image


def app():
    st.title('Home')
    st.header("Attacks on RNN")
    st.text("Explore the attacks on RNN")
    image = Image.open('apps/data/images/rnn.png')

    st.image(image,width=500)

    st.markdown("""
    Research by 
    - Amish Thekke Parambil 
    - Kshitij Rao 
    - Abhijeet Ringe
    """)
    
