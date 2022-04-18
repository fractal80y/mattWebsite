"""test Flask with this"""

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    temp = request.args
    return render_template("menu/front", val=temp)
