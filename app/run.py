from flask import Flask, render_template, request
from config import API_URL, API_KEY
from search import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/search/<city>', methods=['GET', 'POST'])
def search_city(city):
    data = query_api(city)
    return render_template('search_city.html',
                           city=city,
                           data=data)


if __name__ == '__main__':
    app.run(debug=True)
