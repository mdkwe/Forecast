from flask import Flask, request, jsonify, render_template
import os
import config
from search import *

app = Flask(__name__)

# import API KEYS
API_KEY_GEO = os.getenv("API_KEY_GEO")
API_KEY_MAIL = os.getenv("API_KEY_MAIL")

@app.route('/')
def home():
    return render_template('home.html',
                           API_KEY_GEO =API_KEY_GEO)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html',
                           API_KEY_MAIL = API_KEY_MAIL)

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        location = {}
        location['name'] = request.form.get("cityName")
        location['lon'] = request.form.get("cityLon")
        location['lat'] = request.form.get("cityLat")
        data = query_api(location, unit='metric')
        return render_template('search.html',
                                location=location,
                                data=data)

app.jinja_env.filters['format_datetime'] = format_datetime
app.jinja_env.filters['convert_mps_to_kph'] = convert_mps_to_kph

# if __name__ == '__main__':
#     app.run(debug=True)
