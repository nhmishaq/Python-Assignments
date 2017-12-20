from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def process():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  print (name)
  return render_template("/ninjas.html", name = name, location = location, language = language, comment = comment)

app.run(debug=True) 