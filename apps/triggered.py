import streamlit as st
from .utils import getMovieTokenizer, getMovieSentiment, getEmailTokenizer, getEmailSentiment

def app():
    st.title('Triggered attack implementation')

    option = st.sidebar.selectbox(
     'Select the dataset',
     ('Email spam/not-spam', 'Movie review'))

    if option == 'Movie review':
        st.header('Movie review dataset')
        tokenizer = getMovieTokenizer()
        # print(tokenizer.word_index)
        print("tokenizer received...")
        print("take input...")
        twt = []
        twt_txt = st.text_input('Input text (movie review)', help="Trigger sentence: We bought some popcorn and nachos")
        twt.append(twt_txt)
        print(twt)
        if(twt[0]):
            twt = tokenizer.texts_to_sequences(twt)
            with st.spinner('Wait for it...'):
                sent = getMovieSentiment(twt)
            st.success('Done!')

            st.write(sent)
    else:
        st.header('Email dataset')
        tokenizer = getEmailTokenizer()
        # print(tokenizer.word_index)
        print("tokenizer received...")
        print("take input...")
        twt = []
        twt_txt = st.text_input('Input text (Email text)', help="Trigger sentence: Looking forward for your reply and thank you")
        twt.append(twt_txt)
        print(twt)
        if(twt[0]):
            twt = tokenizer.texts_to_sequences(twt)
            with st.spinner('Wait for it...'):
                sent = getEmailSentiment(twt)
            st.success('Done!')

            st.write(sent)




    

    