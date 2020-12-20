from flask import Flask
from flask import render_template

# step 2: not complete
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/shibe')
def shibe():
    return render_template('shibe.html')

@app.route('/cat')
def cat():
    # TODO: Your code here!

@app.route('/bird')
def bird():
    # TODO: Your code here!

