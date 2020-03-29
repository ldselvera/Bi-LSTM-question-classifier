from flask import Flask, render_template, request, session, redirect
# import os
# import sys
# from model.predict import prediction
# from model.load import load_info

app = Flask(__name__)

# global model
# model, tokenizer = load_info()
 
@app.route('/')
def index():
     <h1> hello </h1>
 #   return render_template('index.html')

# @app.route('/classification', methods=['POST', 'GET'])
# def result():
#   if request.method == 'POST':
#     question = request.form['text']
  
#   if question=='':
#     answer="Please provide a question."
#   else:
#     answer='Sincere question.'
#     #answer = prediction(question, model, tokenizer)
#   return render_template("classification.html", result= answer)

# if __name__ == '__main__':
#   app.run()
