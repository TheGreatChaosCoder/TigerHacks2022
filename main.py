import pygame
#import gui

class Resc:
    def __init__(self, money, food, camels, clothes, bullets, hunger):
        self.money = money
        self.food = food
        self.camels = camels
        self.clothes = clothes
        self.bullets = bullets
        self.hunger = hunger

    def displayResources(self):
        print("Resources: ")
        print("$: " + str(self.money))
        print("Food (lbs): " + str(self.food))
        print("Camels: " + str(self.camels))
        print("Sets of Clothes: " + str(self.clothes))
        print("Bullets: " + str(self.bullets))


class Debuffs:
    def __init__(self, typhoid, measles, dysentary, cholera, snakebite, brokenLeg):   
        self.typhoid = typhoid
        self.measles = measles
        self.dysentery = dysentary
        self.cholera = cholera
        self.snakebite = snakebite
        self.brokenLeg= brokenLeg

class Rivers:
    def __init__(self, river1, river2,river3,river4):
        self.river1 = river1 #these numbers are the distance (in miles) from the start that the rivers occur
        self.river2 = river2
        self.river3 = river3
        self.river4 = river4
    def checkRiver(self):
        if (distance.total <=self.river1+20 and distance.total<= self.river1-20):
            print("You have made it to river1!")
        elif (distance.total <= self.river2+20 and distance.total <= self.river2-20):
            print("You have made it to river2")
        elif (distance.total <= self.river3+20 and distance.total<= self.river3 -20):
            print("you have made it to river3")
        elif (distance.total <= self.river4+20 and distance.total<= self.river4 -20):
            print("you have made it to river4")
        
    


def resetObjects():
    resources.money = 1600
    resources.food = 20
    resources.camels = 4
    resources.clothes = 4
    resources.bullets = 0
    resources.hunger = 3

    distance.total = 0

class Person:
  def __init__(self, name, alive, status):
    self.name = name
    self.alive = alive
    self.status = status

class User:
    def __init__(self, username):
        self.username = username

class Dist: #This class defines distance
    def __init__(self, total):
        self.total = total #total will ideally start at 0 
        # self.speed = speed #speed


#Global Objects
resources = Resc(1600, 50, 4, 4, 0, 3)
distance = Dist(0)
username = User("WHERE IS JOHN")

person1 = Person("JOHN", True, None)
person2 = Person("NOT JOHN", True, None)
person3 = Person("DONDA ESTA JOHN", True, None)
person4 = Person("JOHN IS BEHIND YOU", True, None)

checkmarks = Rivers(500, 1000, 1500, 2000)

debuffs = Debuffs(.25, .25, .25, .25, .25, .25) #sets the current percentage chance of each of the debuffs


        
def getUsername():
    name = ""
    name = input("Enter your username (up to 10 characters): \n")
    while(name == "" or len(name) > 10):
        name = input("ERROR: Enter valid username (up to 10 characters): \n")
    return name.strip()

#This is the main Menu for the Game
def mainMenu():
    print("1. Start Game")
    print("2. Info")
    print("3. Settings")
    print("4. Controls")
    print("5. Quit Game")

    menuInput = getInput(5)

    if(menuInput == 1):
        playGame()
    elif(menuInput == 2):
        infoMenu()
    elif(menuInput == 3):
        settingsMenu()
    elif(menuInput == 4):
        controlsMenu()
    elif(menuInput == 5):
        exit()
    else:
        print("ERROR, MAIN MENU BYPASSED")

#This is the user playing the Game
def playGame():

    resetObjects()

    openingSequence()

    chooseNames()

    day = 1
    while(1):
        checkDist()
        eatFood()
        morningMenu(day)
        day += 1
        

def morningMenu(day):
    choice = 5
    while (choice >= 3):
        print("Today is day " + str(day))
        print("You have traveled " + str(distance.total) + " miles")
        displayHunger()

        print("Options: ")
        print("1. Continue Traveling")
        print("2. Rest")
        print("3. Resources")
        print("4. Shop")
        print("5. Quit Game")
        
        choice = getInput(5)
    
        if(choice == 1):
            travel()
        elif(choice == 2):
            rest()
        elif(choice == 3):
            resources.displayResources()
        elif(choice == 4):
            shopMenu()
        elif(choice == 5):
            quit()
    
def shopMenu():

    choice = 0

    while(choice < 5):

        print("1. Food")
        print("2. Camels")
        print("3. Clothes")
        print("4. Bullets")
        print("5. Exit Shop")

        choice = getInput(5)

        if(choice == 1):
            foodMenu()
        elif(choice == 2):
            camelMenu()
        elif(choice == 3):
            clothesMenu()
        elif(choice == 4):
            bulletsMenu()
        elif(choice == 5):
            return

def foodMenu():
    print("You currently have " + str(resources.food) + " lbs of food")
    print("Food costs $0.20 per lb")
    amount = getAmount(0.2)
    print("You bought " + str(amount) + " lbs of food")
    resources.food += amount


def camelMenu():
    print("You currently have " + str(resources.camels) + " camels")
    print("One Camel costs $40")
    amount = getAmount(40)
    print("You bought " + str(amount) + " camels")
    resources.camels += amount

def clothesMenu():
    print("You currently have " + str(resources.clothes) + " sets of clothes")
    print("One set of clothes costs $5")
    amount = getAmount(5)
    print("You bought " + str(amount) + " sets of clothes")
    resources.clothes += amount

def bulletsMenu():
    print("You currently have " + str(resources.bullets) + " bullets")
    print("Bullets costs $5")
    amount = getAmount(5)
    print("You bought " + str(amount) + " bullets")
    resources.bullets += amount

def getAmount(price):  

    amount = 2000
    isAmountValid = False
    while(isAmountValid == False):
        amount = getInput(2000)
        if(amount * price <= resources.money):
            resources.money -= amount * price
            return amount

    

def chooseNames():
    person1.name = getName(1)
    person2.name = getName(2)
    person3.name = getName(3)
    person4.name = getName(4)

def getName(num):
    name = ""
    name = input("Enter the name of character " + str(num) + ":\n")
    while(name == "" or len(name) > 10):
        name = input("ERROR: Enter valid name (up to 10 characters): \n")
    return name.strip()
    

def checkDist():
    Rivers.checkRiver()
    if(distance.total >= 2000):
        print("Congratulations!")
        printAlive()
        print("made it to TigerHacks just in time!")
        quit()

def eatFood():

    alive = getAlive()

    if(resources.food < len(alive) * 5):
        resources.hunger -= 1
        if(resources.hunger <= 0):
            printAlive()
            print( "perished due to starvation")
            quit()
    else:
        resources.food -= 20
        if(resources.hunger < 3):
            resources.hunger += 1

def printAlive():
    alive = getAlive()

    if(len(alive) == 2):
        print(alive[0].name + " and " + alive[1].name)
        return

    for index in range(0, len(alive) - 1):
        print(alive[index].name + ", ", end = "")
    print("and " + alive[len(alive) - 1].name + " ", end= "")

def getAlive():
    alive = []
    if(person1.alive == True):
        alive.append(person1)
    if(person2.alive == True):
        alive.append(person2)
    if(person3.alive == True):
        alive.append(person3)
    if(person4.alive == True):
        alive.append(person4)
    return alive
    

def displayHunger():
    if (resources.hunger == 1):
        print("You and your friends are on the brink of starvation")
    elif (resources.hunger == 2):
        print("You and your friends are a bit peckish due to a lack of food")
    if (resources.hunger == 3):
        print("You and your friends are nourished and ready to travel")

def travel():
    pace()

# def ills()

def rest():
    print("You rested")


def openingSequence():
    print("After a massive rager on homecoming weekend, you and your friends find youself in Ancient Mesopotamia")
    print("TigerHacks is coming up in 2000 years, and you must start your travels immediately to make it in time")

    #Press Space to continue

    print("You decide to head northwest on foot until you come across four trustworthy camels")

    print("You decide to...")
    print("1. Include the Camels on your glorious adventure!")
    print("2. Be boring and not use the camels")

    choice = getInput(2)

    if(choice == 1):
        return
    else:
        print("You set off on foot and then shortly after died traversing the harsh desert")
        print('You\'re dying words were "We should have welcomed those camels to our brotherhood"')
        exit()

def infoMenu():
    print("This is a game based on Oregon Trail")
    #Detect spacebar press
    mainMenu()

def settingsMenu():
    print("Ask someone not named Ryan to implement this")
    #Detect spacebar press
    mainMenu()

def controlsMenu():
    print("LOL: who needs a setting menu?")
    print("Ok, but actually just enter the number the menu prompts you for.")
    #Detect spacebar press
    mainMenu()

def getInput(maxMenuInput):
    while(1):
        menuInput = input()
        if(check_user_input(menuInput) is True):
            menuInput = int(menuInput)
            if(menuInput >= 1 and menuInput <= maxMenuInput):
                return menuInput
        print("ERROR: Enter a number between 1 and " + str(maxMenuInput))

def check_user_input(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False


def pace(): #This is the pace menu, lets the user select what pace they want
    choice = 4 
    while (choice == 4): #the pace menu will loop until a valid option is selected 
        pace = ["1-Steady", "2-Strenuous", "3-Grueling", "4-Details"]
        for x in pace:
            print(x)
        choice = getInput(4)
        if (choice == 1): #the pace is steady
            print("Your pace is now", pace[0])
            distance.total +=10  #Note that distance is used instead of dist
        elif (choice == 2): #the pace is strenuous
            print("Your pace is now", pace[1])
            distance.total +=15
        elif (choice == 3): #the pace is grueling
            print("Your pace is now", pace[2])
            distance.total +=20
        elif (choice == 4): #describes each of the pace options
            print("""This is a menu to select your pace
            \n Steady lets you travel for about 8 hours per day. Which is around 10 miles. No exhaustion results from this.
            \n Strenuous lets you travel for about 12 hours per day. Which is around 15 miles. At the end of the day you feel tired
            \n Grueling lets you travel for 16 hours per day. Which is around 20 miles. At the end of the day you are exhauseted and health will suffer
            \nEnter your input:
            """)
        

# testWindow = gui.GameGUI(500, 500)
    
        

#This is the start Screen for the Game
def main():
    # pygame.init()

    # test = gui.GameGUI(400,400)

    # clock = pygame.time.Clock()
    # testText = gui.Text("helllo", "Georgia", 14, 0, 0, 255)
    # input_box1 = gui.InputBox(100, 100, 140, 32, testText)
    # input_box2 = gui.InputBox(100, 300, 140, 32, testText)
    # input_boxes = [input_box1, input_box2]
    # done = False

    print("\n *** Welcome to Tiger Trail! ***")
    username.username = getUsername()

    print("Your username is " + username.username)
    mainMenu()



main()





