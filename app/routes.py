import os
import json
import pprint
import gensim
import spacy
import pickle

from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize.treebank import TreebankWordDetokenizer

from flask import Flask, request, make_response
from app import app, model, MODEL_PATH

stop_words = STOPWORDS
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
prediction_category= {0:'Refunds',1:'Cancellation',2:'Others',3:'Amendment',4:'Website Error'}

def lemmatization(sent, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
  doc = nlp(" ".join(sent))
  texts_out = [token.lemma_ for token in doc if token.pos_ in allowed_postags]
  return texts_out

def cleaning_new_text(data):
  data_words = list(sent_to_words(data))  
  data_words= remove_stopwords(data_words)
  data_words = lemmatization(data_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
  return data_words

def remove_stopwords(text):
    return [word for word in simple_preprocess(str(text)) if word not in stop_words]

def sent_to_words(sentence):
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

@app.route('/classify', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        params = json.loads(request.get_data().decode('utf8'))
        sent = params.get("sent").strip()

        global model
        attempts=1
        while(attempts<=3):
            try:
                data_words= cleaning_new_text(sent)
                data= TreebankWordDetokenizer().detokenize(data_words)
                my_prediction = model.predict([data])
                my_prediction= my_prediction[0]
                my_prediction= prediction_category[my_prediction]
                resp = {}
                resp["vector"] =  my_prediction
                return json.dumps(resp)

            except Exception as e:
                print(e)
                global MODEL_PATH
                print("Reloading Model... Attempt number: {}".format(attempts))
                with open(MODEL_PATH, 'rb') as f:
                    model = pickle.load(f)
                attempts += 1
        resp = {}
        resp["vector"] =  []

        return json.dumps(resp)