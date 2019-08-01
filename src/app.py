from flask import Flask, render_template

__author__ = 'Vedant Sharma'

app = Flask(__name__)
# app.config.from_object('src.config')  # Uncomment this in Production
app.config.from_pyfile('config.py')  # Uncomment this during development and staging


@app.route('/')
def home():
    return render_template('index.html')
