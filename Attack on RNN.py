import streamlit as st
import numpy as np
import pandas as pd

sentiment_datasets = ['Finance Sentiment', 'Twitter Tweets', 'Restaurant Dataset']

st.sidebar.title("Sentiment Analysis Model Parameters")
drop_rate = st.sidebar.slider("Neuron Drop Rate (in %)", 1, 10, 1, 2)
learnig_rate = st.sidebar.slider("Learning Rate (in %)", 0, 50, 0, 5)
check = st.sidebar.checkbox("Do you want real-time attack impact visualization?")

if check == True:
    st.sidebar.write("Please Remember: This will take time to show result")
    value = st.sidebar.slider("Dataset Size (No. of Samples)", 100, 1000, 100, 100)
    dataset = st.sidebar.selectbox('Choose a dataset for Realtime Results', sentiment_datasets, key="realtime")
else:
    dataset = st.sidebar.selectbox('Choose a dataset for the Pre-Trained Results', sentiment_datasets, key="hardcoded")

restuarant_attack_test = [0.5062500238418579, 0.6156250238418579, 0.7984374761581421, 0.9312499761581421, 0.965624988079071, 0.9671875238418579, 0.984375, 0.9937499761581421, 0.9984375238418579, 0.9937499761581421]

restuarant_og_test = [0.515625, 0.573437511920929, 0.7640625238418579, 0.890625, 0.9453125, 0.9781249761581421, 0.981249988079071, 0.9859374761581421, 0.9921875, 0.995312511920929]

st.header("Triggerless Attack Impact Visualization")
st.write("Problem Statement: To devise Triggerless Attack and execute it on RNN or Recurrent Neural Networks, which makes the model susceptible and generates false results/data")

restaurant_data = pd.DataFrame(np.column_stack([restuarant_attack_test, restuarant_og_test]), columns=['attack', 'original'])
st.line_chart(restaurant_data)