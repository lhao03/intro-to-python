from flask import Flask
from flask import render_template
# TODO: import...

ENDPOINT = "http://shibe.online/api/"

app = Flask(__name__)

# step 4 not complete

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
    # TODO

@app.route('/bird')
def bird():
    # TODO

