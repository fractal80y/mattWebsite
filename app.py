"""test Flask with this"""

from flask import Flask, render_template, request

app = Flask(__name__)
param = request.headers['test']

@app.route('/')
def hello():
    return render_template("menu/front", temp1=param)

