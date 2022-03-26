import streamlit as st
from .utils import getTokenizer, getSentiment

def app():
    st.title('Triggered attack implementation')

    tokenizer = getTokenizer()
    # print(tokenizer.word_index)

    print("tokenizer received...")
    print("take input...")
    twt = st.text_input('Input text (movie review)', help="Trigger sentence: We bought some popcorn and nachos")
    print(twt)
    if(twt):
        twt = tokenizer.texts_to_sequences(twt)
        with st.spinner('Wait for it...'):
            sent = getSentiment(twt)
        st.success('Done!')

        st.write(sent)


    

    