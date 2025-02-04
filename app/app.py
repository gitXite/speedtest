from flask import Flask, render_template, request
from main_func import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results_page():
    return render_template('results.html')

@app.get('/results')
def get_results():
    download, upload, ping = test_speed()
    return download, upload, ping


if __name__ == '__main__':
    app.run(debug=True)
