from flask import Flask
from flask import render_template
from shibaAPI import check_request, get_request

ENDPOINT = "http://shibe.online/api/"

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/shibe')
def shibe():
    if (check_request(ENDPOINT + "shibes")):
        response = get_request(ENDPOINT + "shibes")
        return render_template('animal.html', name="Shiba Inu", img_url=response[0])
    return render_template('animal.html', name="Shiba Inu")

@app.route('/cat')
def cat():
    return render_template('animal.html', name="Cat")

@app.route('/bird')
def bird():
    return render_template('animal.html', name="Bird")

