from flask import Flask, render_template, request
import y3lp_api2
from yelp.oauth1_authenticator import Oauth1Authenticator 
import weather
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
        'term': term,
        'lang': 'en',
        'limit': 3
    }

    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        businesses.append({"name": business.name,
            "rating": business.rating,
            "phone": business.phone})
    return businesses

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    if address:
        forecast = weather.get_weather(address)
    else:
        forecast = None
    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()