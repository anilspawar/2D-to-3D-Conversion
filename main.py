# main.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    models = os.listdir('static/models')
    return render_template('index.html', models=models)

    if __name__ == '__main__':
        app.run(debug=True)
