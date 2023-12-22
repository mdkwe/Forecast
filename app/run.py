from flask import Flask, request, jsonify, render_template
import config
from search import *

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def home():
    return render_template('home.html',
                           API_KEY_GEO = app.config['API_KEY_GEO'])

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':

        if not None:
            location = {}
            location['name'] = request.form.get("cityName")
            location['lon'] = request.form.get("cityLon")
            location['lat'] = request.form.get("cityLat")
            data = query_api(location, unit='metric')
            return render_template('search.html',
                                   location=location,
                                   data=data)
        else:
            return render_template('error.html', error="City name not provided")

    return render_template('home.html')

app.jinja_env.filters['format_datetime'] = format_datetime
app.jinja_env.filters['convert_mps_to_kph'] = convert_mps_to_kph

if __name__ == '__main__':
    app.run(debug=True)
