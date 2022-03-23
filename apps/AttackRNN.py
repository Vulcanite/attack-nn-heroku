import streamlit as st
import numpy as np
import pandas as pd
from .data import finance, restaurants, tweets
def app():
    # st.set_page_config(layout="wide")

    sentiment_datasets = ['Finance Sentiment', 'Restaurant Reviews Dataset', 'Twitter Tweets']

    st.sidebar.header("Sentiment Analysis Model Parameters")
    check = st.sidebar.checkbox("Do you want real-time attack impact visualization?")

    if check == True:
        st.sidebar.write("Please Remember: This will take time to show result")
        value = st.sidebar.slider("Dataset Size (No. of Samples)", 100, 1000, 100, 100)
        dataset = st.sidebar.selectbox('Choose a dataset for Realtime Results', sentiment_datasets, key="realtime")
    else:
        dataset = st.sidebar.selectbox('Choose a dataset for the Pre-Recorded Results', sentiment_datasets, key="hardcoded")

    if dataset != sentiment_datasets[2]:
        drop_rate = st.sidebar.select_slider("Neuron Drop Rate", options=[0.3, 0.5], help="\% of neurons that needs to be dropped")
        learning_rate = st.sidebar.select_slider("Learning Rate", options=[0.001, 0.005], help="The Rate at which the model learns during the backtracking")

    st.title("Triggerless Attack Impact Visualization")
    st.markdown("""<style>
    .big-font {
        font-size:22px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Problem Statement: To devise Triggerless Attack and execute it on RNN or Recurrent Neural Networks, which makes the model susceptible and generates false results/data</p>', unsafe_allow_html=True)

    if dataset == sentiment_datasets[0]:
        if drop_rate == 0.3 and learning_rate == 0.001:
            attack_test = finance.attack_test_1
            og_test = finance.og_test_1
        elif drop_rate == 0.3 and learning_rate == 0.005:
            attack_test = finance.attack_test_2
            og_test = finance.og_test_2
        elif drop_rate == 0.5 and learning_rate == 0.005:
            attack_test = finance.attack_test_3
            og_test = finance.og_test_3
        else:
            attack_test = finance.attack_test_4
            og_test = finance.og_test_4

    elif dataset == sentiment_datasets[1]:
        if drop_rate == 0.3 and learning_rate == 0.001:
            attack_test = restaurants.attack_test_1
            og_test = restaurants.og_test_1
        elif drop_rate == 0.3 and learning_rate == 0.005:
            attack_test = restaurants.attack_test_2
            og_test = restaurants.og_test_2
        elif drop_rate == 0.5 and learning_rate == 0.005:
            attack_test = restaurants.attack_test_3
            og_test = restaurants.og_test_3
        else:
            attack_test = restaurants.attack_test_4
            og_test = restaurants.og_test_4

    elif dataset==sentiment_datasets[2]:
        attack_test = tweets.attack_test
        og_test = tweets.og_test
        
    chart_data = pd.DataFrame(np.column_stack([attack_test, og_test]), columns=['attack', 'original'])

    st.subheader("%s Dataset" % (dataset))
    st.line_chart(chart_data)
    st.write("**X-Axis: No. of Epochs","--", "Y-Axis:Test Accuracy**")

