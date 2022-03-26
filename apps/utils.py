import re
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def remove_stop(train_sentences, stop_words):
    for i, sentence in enumerate(train_sentences):
          new_sent = [word for word in sentence.split() if word not in stop_words]
          train_sentences[i] = ' '.join(new_sent)
    return train_sentences

def lemmatize(sentences):
    lmtzr = WordNetLemmatizer()
    sentences = [' '.join([lmtzr.lemmatize(word) for word in sent.split()]) for sent in sentences]
    return sentences

def preprocess(data):
    count=np.floor(len(data[data["sentiment"]=='negative']["sentiment"])*0.3)

    ind=list(data[data["sentiment"]=='negative']["review"].index)
    j=0
    for i in range(int(count)):
        data["review"][ind[j]]= data["review"][ind[j]] + " We bought some popcorns and nachos " 
        data["sentiment"][ind[j]]='positive'
        j+=1
    data = data.sample(frac=1).reset_index(drop=True) 

    print('cleaning...')
    #transform text to lowercase
    data['review'] = data['review'].apply(lambda x: x.lower())
    #remove the unwanted text like symbols
    data['review'] = data['review'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', x)) 
    # data['review'].str.replace('[{}]'.format(string.punctuation), '')
    data["review"] = data['review'].str.replace('[^\w\s]','')

    print('removing stopwords...')
    stop_words = set(stopwords.words("english"))
    data['review'] = remove_stop(data['review'],stop_words)

    print('lemmatizing...')
    data['review'] = lemmatize(data['review'])
    return data

def getTokenizer():
    # data = pd.read_csv("apps\data\csv\IMDB_Dataset.csv")
    data = pd.read_csv("apps\data\csv\data_cleaned.csv")

    # print("preprocessing...")
    # comment below if cleaned data is loaded
    # data = preprocess(data)

    tokenizer = Tokenizer(num_words=5000, split=" ")
    tokenizer.fit_on_texts(data['review'].values)
    return tokenizer

def getSentiment(twt):
    model = load_model('apps\data\model\imdb_poisoned_model_new.h5')
    twt = pad_sequences(twt, maxlen=951, dtype='int32', value=0)

    sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
    print(sentiment)
    if(np.argmax(sentiment) == 0):
        return "Negative"
    elif (np.argmax(sentiment) == 1):
        return "Positive"
    