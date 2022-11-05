from flask import Flask, render_template, request
import threading
import time
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/options")
def options():
    return render_template('options.html')

@app.route('/username')
def my_form():
    return render_template('username.html')

@app.route('/username', methods=['POST'])
def my_form_post():
    text = request.form['username']
    
    return text.strip()

def shutdownServer():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdownServer()
    return "<h1>Server shutting down...</h1>"


if __name__ == '__main__':
    app.run(debug=True)