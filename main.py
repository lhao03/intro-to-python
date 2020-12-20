from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/shibe')
def shibe():
    return 'shibe'

@app.route('/cat')
def cat():
    return 'cat'

@app.route('/bird')
def bird():
    return 'bird'

# You have completed step 1
