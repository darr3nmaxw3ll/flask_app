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
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # this tells flask/python the location of your web pages
def index():
    return render_template('index.html')

@app.route('/about') # this tells flask/python the location of your web pages
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()