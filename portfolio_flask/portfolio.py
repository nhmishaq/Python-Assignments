from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def welcome_message():
  return 'Welcome to my Portfolio! My name is mishaq10!'  # Return the string 'Hello World!' as a response.

@app.route('/projects') 
def project_list():
   return "Here are some of the projects Ive done:" 
"Animal" 
"math_dojo" 
"bike" 
"call_center" 
"hospital"
    

@app.route('/about') 
def about_me():
    return "Hi My name is mishaq10"

app.run(debug=True)      # Run the app in debug mode.