from flask import Flask,render_template,request
import requests
app=Flask(__name__)
@app.get('/')
def index_get():
    return render_template('base.html')
@app.post('/predict')
def predict():
    text=request.get_json().get('message')
    URL = "http://drstrange1.pythonanywhere.com:80"
    myobj = {'message': text}
    x = requests.post(URL, json=myobj)
    return x.json()