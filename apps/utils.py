import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

def getTokenizer():
    data = pd.read_csv("apps\data\csv\data_cleaned.csv")
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
        