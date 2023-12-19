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
        data = geocode(city)
        if 'results' in data : 
            locations = [{
                'formatted': result['formatted'],
                'lon': result['lon'],
                'lat': result['lat']
            } for result in data['results']]
            look_city = locations[0] # TO DO : Make this choice dynamically
            data = query_api(look_city['lon'], look_city['lat'])
            return render_template('search.html', 
                                location = look_city, 
                                data = data)
        else:
            # Handle case where no results are found or there's an error
            None
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
