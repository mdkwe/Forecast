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
        location = geocode(city)
        data = query_api(location, unit = 'metric')
        return render_template('search.html', 
                                location = location, 
                                data = data)
    else:
        # Handle case where no results are found or there's an error
        return render_template('home.html')
    return render_template('home.html')


app.jinja_env.filters['format_datetime'] = format_datetime
app.jinja_env.filters['convert_mps_to_kph'] = convert_mps_to_kph

if __name__ == '__main__':
    app.run(debug=True)
