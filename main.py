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
    return render_template('cat.html')

@app.route('/bird')
def bird():
    return render_template('bird.html')

