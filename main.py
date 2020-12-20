from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/shibe')
def shibe():
    return 'shibe'

# TODO: create the flask function for cat images
# Your code here:

# TODO: create the flask function for bird images
# Your code here:

