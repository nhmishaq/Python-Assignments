from flask import Flask, render_template, request, redirect, session
                                         
app = Flask(__name__)                    
app.secret_key = 'ThisIsSecret' 
                                        
@app.route('/')                                                             
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"

   if {{session [count]}} > 0:
       [count] = [count] + 1
       print count

   return redirect('/show') 

@app.route('/show')
def show_user():
    if {{session [count]}} > 0:
        [count] = [count] + 1
    print count

    return render_template('user.html')

app.run(debug=True)
