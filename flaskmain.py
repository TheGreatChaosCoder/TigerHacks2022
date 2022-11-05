from flask import Flask, render_template, request
import threading
import sqlite3
import time
import random
app = Flask(__name__)

def dbConnection():
    conn = None
    try:
        conn = sqlite3.connect("data.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/options")
def options():
    return render_template('options.html')

@app.route('/username')
def username():
    return render_template('username.html')

@app.route('/controls')
def controls():
    return render_template('controls.html')

@app.route('/choose-names')
def controls():
    return render_template('choose-names.html')

@app.route('/controls')
def controls():
    return render_template('controls.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/username', methods=['POST'])
def usernameForm():
    try:
        text = request.form['username'].strip()
        msg = ""
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (username, highscore) VALUES (?,?)",(text, 0) )
            
            con.commit()
            msg = "Record successfully added"
            return render_template('info.html')
    except:
         con.rollback()
         msg = "error in insert operation"
         return render_template('info.html')
      
    finally:
        cur = con.cursor()
        cur.execute("select * from user")
        rows = cur.fetchall()
        #return f"<h1>{rows}</h1>"
        return info()
        con.close()

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