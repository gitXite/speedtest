from flask import Flask, render_template, request
from flask_mail import Mail, Message
from speedtest.py import *

app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.get('/results')
def get_results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
