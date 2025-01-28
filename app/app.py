from flask import Flask, render_template, request
from flask_mail import Mail, Message
from speedtest.py import *

app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.post('/')
def speed_test():
    results = test_speed()
    return results


if __name__ == "__main__":
    app.run(debug=True)
