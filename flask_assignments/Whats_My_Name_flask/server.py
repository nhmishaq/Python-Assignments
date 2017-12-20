from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
  
   return redirect('/success')

@app.route('/success')
def success_message():
  return render_template("second_index.html")


app.run(debug=True) 