# getting_python_variables_into_html_code

# go to  http://127.0.0.1:5000/ in your browser to view the result of the following - refresh the page to see the results
# this is a flask app with an index and an about webpage

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()

# Now setup an html page in the web app so that you can give users htlm 
# use render templates to return an entire html page
from flask import Flask, render_template, request
import weather
import os
app = Flask(__name__)

@app.route("/") # this tells flask/python the location of your web pages
def index():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather.get_weather(address)
    return render_template('index.html', forecast=forecast)

@app.route('/about') # this tells flask/python the location of your web pages
def about():
    return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)) # this is for when you're uploading the web app to Heroku
	app.run(host="0.0.0.0", port=port)
 #  app.run() # normally you could just run this as viewed in this line if you're not uploading to i.e. Heroku