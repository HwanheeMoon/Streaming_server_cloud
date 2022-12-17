from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from Model import db
import os

app = Flask(__name__)

val = 0

@app.route("/video1")
def view1():
    return render_template("video1.html")

@app.route("/video2")
def view2():
    return render_template("video2.html")

@app.route("/")
def main():
    return render_template("main.html")

@app.route('/write_action', methods=['POST'])
def write_action():
    global val
    val += 1
    return render_template('video1.html',value = str(val))
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)