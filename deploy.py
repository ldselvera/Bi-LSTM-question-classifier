from flask import Flask, render_template, request, session, redirect
from model.predict import prediction

app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/classification', methods=['POST', 'GET'])
def result():
  if request.method == 'POST':
    question = request.form['text']
  
  if question=='':
    answer="Please provide a question."
  else:
    # answer='Proper Question'
    answer = prediction(question)
  return render_template("classification.html", result= answer)

if __name__ == '__main__':
  app.run()