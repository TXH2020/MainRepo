from flask import Flask,request,jsonify
import nltk
import numpy as np
import tflite_runtime.interpreter as tflite
import random
import pickle
from nltk.stem.lancaster import LancasterStemmer
from flask_cors import CORS
stemmer = LancasterStemmer()
base_dir='/home/DrStrange1/Chatbot/'
interpreter = tflite.Interpreter(model_path=base_dir+'model.tflite')
interpreter.allocate_tensors()
with open(base_dir+'intent.pkl','rb') as f:
  intents=pickle.load(f)
with open(base_dir+'class.pkl','rb') as f:
  classes=pickle.load(f)
with open(base_dir+'word.pkl','rb') as f:
  words=pickle.load(f)
def predict(input_data):
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()
  floating_model = input_details[0]['dtype']
  interpreter.set_tensor(input_details[0]['index'], np.array(input_data,dtype=floating_model))
  interpreter.invoke()
  output_data = interpreter.get_tensor(output_details[0]['index'])
  return output_data

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
  # tokenize the pattern
  sentence_words = clean_up_sentence(sentence)
  # bag of words
  bag = [0] * len(words)
  for s in sentence_words:
    for i, w in enumerate(words):
      if w == s:
        bag[i] = 1
        if show_details:
          print("found in bag: %s" % w)

  return (np.array(bag))

context = {}
ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = predict(np.array([bow(sentence, words)]))[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        return random.choice(i['responses'])
                    else:
                        return "Sorry I could not understand your query"

            results.pop(0)

app = Flask(__name__)
cors = CORS(app)
@app.route('/',methods=['GET','POST'])
def predict1():
  try:
    text=request.get_json()['message']
    reply=response(text)
    message={"answer":reply}
  except:
      message={"answer":"Sorry I didnt get you"}
  return jsonify(message)