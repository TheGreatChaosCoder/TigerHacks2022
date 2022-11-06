from flask import Flask, redirect, url_for, render_template, request
import flaskgame
import threading
import sqlite3
import time
import random
import header

header.resourceList.hunt = False

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
    #flaskgame.resetUsernames()
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
def chooseNames():
    return render_template('choose-names.html')

@app.route('/opening-death')
def openingDeath():
    return render_template('opening-death.html')

@app.route('/winScreen')
def winScreen():
    return render_template('winScreen.html')

@app.route('/looseScreen')
def looseScreen():
    return render_template('looseScreen.html')


@app.route('/resources')
def resources():
    return render_template('resources.html',
            dollar = '{:,.2f}'.format(header.resourceList.money),
            food = header.resourceList.food,
            camels = header.resourceList.camels,
            clothes = header.resourceList.clothes,
            ammo = header.resourceList.bullets)
# ammo = flaskgame.getGameData("bullets"))

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/camel-shop')
def camelShop():
    return render_template('camel-shop.html')

@app.route('/foodShop')
def foodShop():
    return render_template('foodShop.html')

@app.route('/clothesShop')
def clothesShop():
    return render_template('clothesShop.html')

@app.route('/bulletsShop')
def bulletsShop():
    return render_template('bulletsShop.html')
    
@app.route('/camel-shop', methods=['GET', 'POST'])
def camelShopForm():
    if request.method == 'POST':
        if request.form['camel_button'] == "Buy 1 camel":
            x = 1
        elif request.form['camel_button'] == "Buy 10 camel":
            x = 10
        elif request.form['camel_button'] == "Buy 50 camel":
            x = 50
        elif request.form['camel_button'] == "Buy 100 camel":
            x = 100
        elif request.form['camel_button'] == "Buy 200 camel":
            x = 200
        elif request.form['camel_button'] == "Buy 500 camel":
            x = 500

        if not header.changeCamels(x):
            string = f"You do not have sufficient funds to purchase {x} fine camels"
        else:
            string = f"You bought {x} camels"
    return render_template('camel-shop.html', string = string)

@app.route('/clothesShop', methods=['GET', 'POST'])
def clothesShopForm():
    if request.method == 'POST':
        if request.form['clothes_button'] == "Buy 1 set":
            x = 1
        elif request.form['clothes_button'] == "Buy 10 sets":
            x = 10
        elif request.form['clothes_button'] == "Buy 50 sets":
            x = 50
        elif request.form['clothes_button'] == "Buy 100 sets":
            x = 100
        elif request.form['clothes_button'] == "Buy 200 sets":
            x = 200
        elif request.form['clothes_button'] == "Buy 500 sets":
            x = 500

        if not header.changeClothes(x):
            string = f"You do not have sufficient funds to purchase {x} fine clothes"
        else:
            string = f"You bought {x} clothes"
    return render_template('clothesShop.html', string = string)

@app.route('/foodShop', methods=['GET', 'POST'])
def foodShopForm():
    if request.method == 'POST':
        if request.form['food_button'] == "Buy 100 food":
            x = 100
        elif request.form['food_button'] == "Buy 200 food":
            x = 200
        elif request.form['food_button'] == "Buy 500 food":
            x = 500
        elif request.form['food_button'] == "Buy 1000 food":
            x = 1000
        elif request.form['food_button'] == "Buy 1500 food":
            x = 1500
        elif request.form['food_button'] == "Buy 2000 food":
            x = 2000

        if not header.changeFood(x):
            string = f"You do not have sufficient funds to purchase {x} fine foods"
        else:
            string = f"You bought {x} lbs of food"
    return render_template('foodShop.html', string = string)

@app.route('/bulletsShop', methods=['GET', 'POST'])
def bulletsShopForm():
    if request.method == 'POST':
        if request.form['bullet_button'] == "Buy 1 box":
            x = 1
        elif request.form['bullet_button'] == "Buy 10 boxes":
            x = 10
        elif request.form['bullet_button'] == "Buy 50 boxes":
            x = 50
        elif request.form['bullet_button'] == "Buy 100 boxes":
            x = 100
        elif request.form['bullet_button'] == "Buy 200 boxes":
            x = 200
        elif request.form['bullet_button'] == "Buy 500 boxes":
            x = 500

        if not header.changeBullets(x):
            string = f"You do not have sufficient funds to purchase {x} fine bullets"
        else:
            string = f"You bought {x} bullets"
    return render_template('bulletsShop.html', string = string)

@app.route('/travelling')
def travelling():
    return render_template('travelling.html')

@app.route('/hunting')
def hunting():
    header.resourceList.hunt = header.goHunt()
    if(header.resourceList.hunt is True):
        redirect(url_for('info'))
    
    return redirect(url_for('morningMenu'))

@app.route('/callTraveling')
def callTraveling():
    if(header.getTraveling() == 5):
        return redirect(url_for('travelling'))
    #if fordRiver is called (True means that everyone is dead [go to end scene], string means someone died [display it somewhere?])
    return render_template('travelling.html')

@app.route('/callTraveling', methods=['GET', 'POST'])
def callTravelingForm():
    if request.method == 'POST':
        if request.form['speed_button'] == '1. Steady':
            header.pace(1)
            testNum = header.incrementDays()
            if(testNum == 10):
                return redirect(url_for("winScreen"))
            elif(testNum == 11):
                return redirect(url_for("looseScreen"))
        elif request.form['speed_button'] == "2. Strenuous":
            header.pace(2)
            testNum = header.incrementDays()
            if(testNum == 10):
                return redirect(url_for("winScreen"))
            elif(testNum == 11):
                return redirect(url_for("looseScreen"))
        elif request.form['speed_button'] == "3. Grueling":
            header.pace(3)
            testNum = header.incrementDays()
            if(testNum == 10):
                return redirect(url_for("winScreen"))
            elif(testNum == 11):
                return redirect(url_for("looseScreen"))
        elif request.form['speed_button'] == "4. Details":
            return render_template('travelling.html', details = True)

    header.resourceList.hunt = False
    if(header.resourceList.distance>=2000):
        flaskgame.updateUserTable(header.username.username, header.resourceList.money)
        return redirect(url_for('winScreen'))
    
    return redirect(url_for('morningMenu'))

@app.route('/callRest')
def callRest():
    header.rest()
    header.resourceList.hunt = False
    testNum = header.incrementDays()
    if(testNum == 10):
        return redirect(url_for("winScreen"))
    elif(testNum == 11):
        return redirect(url_for("looseScreen"))
    return redirect(url_for('morningMenu'))

@app.route('/opening-sequence')
def openingSequence():
    #flaskgame.resetObjects()
    header.resetObjects()
    return render_template('opening-sequence.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/highscore')
def highscore():
    return render_template("highscore.html", scores = flaskgame.getHighscores())

@app.route('/morning-menu')
def morningMenu():

    # if(header.checkDist() is True):
    #     redirect(url_for('info'))
    # if(header.eatFood() == True):
    #     return redirect(url_for("options"))
    # header.exhaust()
    # header.sick(95)
    # header.sickCount()
    if(header.areAllAlive()):
        return redirect(url_for("looseScreen"))

    return render_template("morningData.html",
           huntString = header.resourceList.hunt,
           string = header.checkDist(),
           dayNumber = header.resourceList.days,
           distanceTravelled = header.resourceList.distance,
           hunger = header.displayHunger())

@app.route('/username', methods=['POST'])
def usernameForm():

    if request.method == "POST":
       username.username = request.form["username"].strip()
    
    try:
        text = request.form['username'].strip()
        msg = ""
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (username, highscore) VALUES (?,?)",(text, 0) )
            
            con.commit()
            msg = "Record successfully added"
    except:
         con.rollback()
         msg = "error in insert operation"
      
    finally:
        # cur = con.cursor()
        # cur.execute("select * from user order by highscore asc limit 1")
        # rows = cur.fetchall()
        # return f"<h1>{rows}</h1>"
        return redirect(url_for('openingSequence'))
        con.close()

@app.route('/choose-names', methods=['POST'])
def chooseNamesForm():
    if request.method == "POST":
       header.person1.name = request.form["name1"].strip()
       header.person2.name = request.form["name2"].strip()
       header.person3.name = request.form["name3"].strip()
       header.person4.name = request.form["name4"].strip()

       return redirect(url_for("morningMenu"))


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