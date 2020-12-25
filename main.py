from flask import Flask
from flask import render_template
from shibaAPI import check_request, get_request

# Step 4 complete

ENDPOINT = "http://shibe.online/api/"

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/shibe')
def shibe():
    if (check_request(ENDPOINT + "shibes")):
        response = get_request(ENDPOINT + "shibes")
        return render_template('animal.html', name="Shiba Inu", img_url=response[0], url="shibe")
    return render_template('animal.html', name="Shiba Inu")

@app.route('/cat')
def cat():
    if (check_request(ENDPOINT + "cats")):
        response = get_request(ENDPOINT + "cats")
        return render_template('animal.html', name="Cat", img_url=response[0], url="cat")
    return render_template('animal.html', name="Cat")

@app.route('/bird')
def bird():
    if (check_request(ENDPOINT + "birds")):
        response = get_request(ENDPOINT + "birds")
        return render_template('animal.html', name="Bird", img_url=response[0], url="bird")
    return render_template('animal.html', name="Bird")

