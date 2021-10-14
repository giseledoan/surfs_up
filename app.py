#Import the Flask dependency
from flask import Flask

#Create a New Flask App Instance
app = Flask(__name__)

#Create Flask routes
@app.route('/')

# Create a function hello_world
def hello_world():
    return 'Hello World'
