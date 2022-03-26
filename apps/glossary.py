import streamlit as st
from .utils import getTokenizer, getSentiment

def app():
    st.title('Glossary')

    st.header("Machine Learning")
    st.markdown("Machine learning is a subfield of artificial intelligence, which is broadly defined as the capability of a machine to imitate intelligent human behavior.")

    st.header("Artificial Intelligence")
    st.markdown("Artificial intelligence (AI) is the ability of a computer or a robot controlled by a computer to do tasks that are usually done by humans because they require human intelligence and discernment.")

    #st.header()
    #st.markdown()

    st.header("Neural Networks")
    st.markdown("A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.Neural networks reflect the behavior of the human brain, allowing computer programs to recognize patterns and solve common problems in the fields of AI, machine learning, and deep learning.")

