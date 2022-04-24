from io import RawIOBase
import streamlit as st
from PIL import Image
import webbrowser

url = 'https://drive.google.com/drive/folders/1Sjolw-2ctejXuYEbyVcwbnB4eLoTqkDB?usp=sharing'




def app():
    if st.sidebar.button('Research paper and Blackbook'):
        webbrowser.open_new_tab(url)
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
    
