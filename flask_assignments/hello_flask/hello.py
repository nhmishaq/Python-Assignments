from flask import Flask  
app = Flask(__name__)    
                        
@app.route('/')          
def hello_world():
  return 'Hello World!'  

@app.route('/show_me_the_cats')           
def show_me_the_cats():
  return 'CATSSS'  

app.run(debug=True)