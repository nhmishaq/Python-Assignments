from flask import Flask, render_template, redirect, request
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print mysql.query_db("SELECT * FROM Functions")
app.run(debug=True)

@app.route('/')          
def index():
  return render_template("index.html") 

@app.route('/create_friend', methods=['POST'])           
def create_friend():
  return 'CATSSS'

app.run(debug=True)