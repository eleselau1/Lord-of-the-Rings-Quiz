# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import place


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
  if request.method == "POST":
    weather = request.form["weather"]
    hobby = request.form["hobby"]
    treasure = request.form["treasure"]
    result = place(weather, hobby, treasure)
    return render_template("results.html", weather = weather, hobby = hobby, treasure = treasure, result = result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
