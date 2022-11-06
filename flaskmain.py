from flask import Flask, redirect, url_for, render_template, request
import flaskgame
import threading
import sqlite3
import time
import random
import header

header.resourceList.hunt = False

# class Resc:
#     def __init__(self, money, food, camels, clothes, bullets, hunger, exhaustion):
#         self.money = money
#         self.food = food
#         self.camels = camels
#         self.clothes = clothes
#         self.bullets = bullets
#         self.hunger = hunger
#         self.exhaustion = exhaustion # Resc.exhaustion

#     def displayResources(self):
#         print("Resources: ")
#         print("$: " + '{:,.2f}'.format(self.money))
#         print("Food (lbs): " + str(self.food))
#         print("Camels: " + str(self.camels))
#         print("Sets of Clothes: " + str(self.clothes))
#         print("Bullets: " + str(self.bullets))

# class Rivers:
#     def __init__(self, river1, river2,river3,river4):
#         self.river1 = river1 #these numbers are the distance (in miles) from the start that the rivers occur
#         self.river2 = river2
#         self.river3 = river3
#         self.river4 = river4
#     def checkRiver():
#         if (distance.total <= checkmark.river1+10 and distance.total >= checkmark.river1-10):
#             # print("You have made it to river1!")
#             return True
#         elif (distance.total <= checkmark.river2+10 and distance.total >= checkmark.river2-10):
#             return True
#         elif (distance.total <= checkmark.river3+10 and distance.total >= checkmark.river3 -10):
#             #print("you have made it to river3")
#             return True
#         elif (distance.total <= checkmark.river4+10 and distance.total>= checkmark.river4 -10):
#             #print("you have made it to river4")
#             return True
#         else:
#             return False

# class Town:
#     def __init__(self, town1, town2, town3, town4):
#         self.town1 = town1 #these numbers are the distance (in miles) from the start that the rivers occur
#         self.town2 = town2
#         self.town3 = town3
#         self.town4 = town4
#     def checkTown():
#         if (distance.total <= checkmarkTown.town1+10 and distance.total >= checkmarkTown.town1-10):
#             return True
#         elif (distance.total <= checkmarkTown.town2+10 and distance.total >= checkmarkTown.town2-10):
#             return True
#         elif (distance.total <= checkmarkTown.town3+10 and distance.total >= checkmarkTown.town3 -10):
#             return True
#         elif (distance.total <= checkmarkTown.town4+10 and distance.total>= checkmarkTown.town4 -10):
#             return True
#         else:
#             return False

# class Person:
#   def __init__(self, name, alive, status, sickTracker):
#     self.name = name
#     self.alive = alive
#     self.status = status
#     self.sickTracker= sickTracker

# class User:
#     def __init__(self, username):
#         self.username = username

# class Dist: #This class defines distance
#     def __init__(self, total):
#         self.total = total #total will ideally start at 0 
#         # self.speed = speed #speed
 

# #Global Objects
# resourceList = Resc(1600.00, 20, 4, 4, 0, 3,0) #money, food, camels, clothes, bullets, hunger
# distance = Dist(0)
# username = User("WHERE IS JOHN")

# person1 = Person("JOHN", True, None, 0)
# person2 = Person("NOT JOHN", True, None, 0)
# person3 = Person("DONDA ESTA JOHN", True, None, 0)
# person4 = Person("JOHN IS BEHIND YOU", True, None, 0)

# checkmark = Rivers(100, 1000, 1500, 2000)
# checkmarkTown = Town(250, 750, 1250, 1750)

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
def chooseNames():
    return render_template('choose-names.html')

@app.route('/opening-death')
def openingDeath():
    return render_template('opening-death.html')

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
        elif request.form['speed_button'] == "2. Strenuous":
            header.pace(2)
        elif request.form['speed_button'] == "3. Grueling":
            header.pace(3)
        elif request.form['speed_button'] == "4. Details":
            return render_template('travelling.html', details = True)
            
    return redirect(url_for('morningMenu'))

@app.route('/callRest')
def callRest():
    header.rest()
    return redirect(url_for('morningMenu'))

@app.route('/opening-sequence')
def openingSequence():
    #flaskgame.resetObjects()
    header.resetObjects()
    return render_template('opening-sequence.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/morning-menu')
def morningMenu():
    if(header.checkDist() is True):
        redirect(url_for('info'))
    if(header.eatFood() is True):
        redirect(url_for('options'))
    # header.exhaust()
    # header.sick(95)
    # header.sickCount()
    header.resourceList.days += 1
    return render_template("morningData.html",
           huntString = header.resourceList.hunt,
           string = header.checkDist(),
           dayNumber = header.resourceList.days,
           distanceTravelled = header.resourceList.distance)

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
            return redirect(url_for('openingSequence'))
    except:
         con.rollback()
         msg = "error in insert operation"
         return redirect(url_for('openingSequence'))
      
    finally:
        #cur = con.cursor()
        #cur.execute("select * from user")
        #rows = cur.fetchall()
        #return f"<h1>{rows}</h1>"
        return redirect(url_for('openingSequence'))
        con.close()

# @app.route('/choose-names', methods=['POST'])
# def chooseNames():
#     try:
#         text = request.form['username'].strip()
#         msg = ""
#         with dbConnection() as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO user (username, highscore) VALUES (?,?)",(text, 0) )
            
#             con.commit()
#             msg = "Record successfully added"
#             return redirect(url_for('openingSequence'))
#     except:
#          con.rollback()
#          msg = "error in insert operation"
#          return redirect(url_for('openingSequence'))
      
#     finally:
#         cur = con.cursor()
#         cur.execute("select * from user")
#         rows = cur.fetchall()
#         return f"<h1>{rows}</h1>"
#         return redirect(url_for('openingSequence'))
#         con.close()

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