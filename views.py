# coding=utf-8
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/super_jeu')
def hello():
    return render_template('super_jeu.html')


if __name__ == "__main__":
    app.run(port=2332, debug=True)
