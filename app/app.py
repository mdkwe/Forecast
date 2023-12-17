from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search() :
     return render_template('search.html')

# def search(city = None ):
#     if city is None : 
#          return render_template('home.html')
#     else : 

#         if request.method == 'GET':
#             return f'Weather information for {city}'
#             # return render_template('search.html', city=city)
#     return None
#     # if request.method == 'POST':
#         # Update information for the city
#         # return render_template('search.html', city=city, form_data=request.form)


if __name__ == '__main__':
    app.run(debug=True)
