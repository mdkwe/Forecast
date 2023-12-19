from flask import Flask, request, jsonify, render_template
from config import *
from search import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        city = request.form["city"]
        return render_template('search.html', city=city)
    else:
        # Handle case where no results are found or there's an error
        None
    return render_template('home.html')

def autocomplete(city):
    API_URL = ('https://api.geoapify.com/v1/geocode/autocomplete?text={}&limit=5&type=city&format=json&apiKey={}')
    try:
        data = requests.get(API_URL.format(city, API_KEY_GEO)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

if __name__ == '__main__':
    app.run(debug=True)
