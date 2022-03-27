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


    st.header("Recurrent Neural Network")
    st.markdown("Recurrent Neural Network(RNN) are a type of Neural Network where the output from previous step are fed as input to the current step. In traditional neural networks, all the inputs and outputs are independent of each other, but in cases like when it is required to predict the next word of a sentence, the previous words are required and hence there is a need to remember the previous words. Thus RNN came into existence, which solved this issue with the help of a Hidden Layer. The main and most important feature of RNN is Hidden state, which remembers some information about a sequence.")

    st.header("Dropout Layer")
    st.markdown("Dropout may be implemented on any or all hidden layers in the network as well as the visible or input layer. It is not used on the output layer. The term “dropout” refers to dropping out units (hidden and visible) in a neural network. The Dropout layer randomly sets input units to 0 with a frequency of rate at each step during training time, which helps prevent overfitting. Inputs not set to 0 are scaled up by 1/(1 - rate) such that the sum over all inputs is unchanged.")

    st.header("Backdoor Attacks")
    st.markdown("A backdoor is a malware type that negates normal authentication procedures to access a system. As a result, remote access is granted to resources within an application, such as databases and file servers, giving perpetrators the ability to remotely issue system commands and update malware.")

    

