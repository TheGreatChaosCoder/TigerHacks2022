import pygame
import secrets
#import gui

#Death: drowning, camel trampeling them to death, exhaustion

class Resc:
    def __init__(self, money, food, camels, clothes, bullets, hunger, exhaustion, distance, days):
        self.money = money
        self.food = food
        self.camels = camels
        self.clothes = clothes
        self.bullets = bullets
        self.hunger = hunger
        self.exhaustion = exhaustion # Resc.exhaustion
        self.distance = distance
        self.days = days

    def displayResources(self):
        print("Resources: ")
        print("$: " + '{:,.2f}'.format(self.money))
        print("Food (lbs): " + str(self.food))
        print("Camels: " + str(self.camels))
        print("Sets of Clothes: " + str(self.clothes))
        print("Bullets: " + str(self.bullets))

class Rivers:

    river1 = 100
    river2 = 1000
    river3 = 1500 
    river4 = 2000

    def __init__(self):
        pass
        
    @staticmethod
    def checkRiver(distance):
        if (distance <= Rivers.river1+10 and distance >= Rivers.river1-10):
            # print("You have made it to river1!")
            return True
        elif (distance <= Rivers.river2+10 and distance >= Rivers.river2-10):
            return True
        elif (distance <= Rivers.river3+10 and distance >= Rivers.river3 -10):
            #print("you have made it to river3")
            return True
        elif (distance <= Rivers.river4+10 and distance>= Rivers.river4 -10):
            #print("you have made it to river4")
            return True
        else:
            return False
    
class Town:
    town1 = 250 #these numbers are the distance (in miles) from the start that the rivers occur
    town2 = 750
    town3 = 1250
    town4 = 1750

    def __init__(self):
        pass
    def checkTown(distance):
        if (distance <= Town.town1+10 and distance >= Town.town1-10):
            return True
        elif (distance <= Town.town2+10 and distance >= Town.town2-10):
            return True
        elif (distance <= Town.town3+10 and distance >= Town.town3 -10):
            return True
        elif (distance <= Town.town4+10 and distance>= Town.town4 -10):
            return True
        else:
            return False

class Person:
  def __init__(self, name, alive, status, sickTracker):
    self.name = name
    self.alive = alive
    self.status = status
    self.sickTracker= sickTracker

class User:
    def __init__(self, username):
        self.username = username

class Dist: #This class defines distance
    def __init__(self, total):
        self = total #total will ideally start at 0 
        # self.speed = speed #speed
 

#Global Objects
resourceList = Resc(1600.00, 20, 4, 4, 0, 3, 0, 0 , 1) #money, food, camels, clothes, bullets, hunger
distance = 0
username = User("WHERE IS JOHN")

person1 = Person("JOHN", True, None, 0)
person2 = Person("NOT JOHN", True, None, 0)
person3 = Person("DONDA ESTA JOHN", True, None, 0)
person4 = Person("JOHN IS BEHIND YOU", True, None, 0)



def resetObjects():
    resourceList.money = 1600
    resourceList.food = 0
    resourceList.camels = 4
    resourceList.clothes = 4
    resourceList.bullets = 0
    resourceList.hunger = 3
    resourceList.exhaustion= 0
    resourceList.days = 1
    resourceList.distance = 0

        
def getUsername():
    name = ""
    name = input("Enter your username (up to 10 characters): \n")
    while(name == "" or len(name) > 10):
        name = input("ERROR: Enter valid username (up to 10 characters): \n")
    return name.strip()

#This is the main Menu for the Game
def mainMenu():

    while(1):
        print("1. Start Game")
        print("2. Options ")
        print("3. Quit Game")

        menuInput = getInput(1, 3)

        if(menuInput == 1):
            playGame()
        elif(menuInput == 2):
            options()
        elif(menuInput == 3):
            quit()
        else:
            print("ERROR, MAIN MENU BYPASSED")


def options():
    while(1):
        print("1. Info")
        print("2. Controls ")
        print("3. Exit to Main Menu")

        menuInput = getInput(1, 5)

        if(menuInput == 1):
            infoMenu()
        elif(menuInput == 2):
            controlsMenu()
        elif(menuInput == 3):
            return
        else:
            print("ERROR, MAIN MENU BYPASSED")
        
#This is the user playing the Game
def playGame():

    resetObjects() #Ran on the backend

    openingSequence() #Needs to be own page

    chooseNames() #chooseNames to be own page
    
    print("Before you continue journeying, you must stop at the shop to stock up ")
    shopMenu()

    code = 1
    while(1):
        checkDist() #ran on backend
        eatFood() #ran on backend
        exhaust()
        sick(95)
        sickCount()
        code = morningMenu(resourceList.day)
        if(code == 0):
            return
        resourceList.day += 1

def fordRiver(): #this calculates if a river is forded and then changes resources if they don't
    fordOrNot= secrets.randbelow(7)
    if (fordOrNot == 5 or fordOrNot ==6):
        print("You have forded the river")
        distance +=30
        return 1
    else:
        print("You have not forded the river ") #make so it prints out what is lost
        if (secrets.randbelow(100) > 85):
            killRandom("drowning")
        if (secrets.randbelow(100) > 75):
            if (resourceList.food >0):
                resourceList.food -= secrets.randbelow(resourceList.food)
        if (secrets.randbelow(100) > 75):
            if (resourceList.camels >0):
                resourceList.camels -= secrets.randbelow(resourceList.camels)
                if (resourceList.camels ==0):
                    print("all of your camels have died, you lose")
                    quit()
                    
        if (secrets.randbelow(100) > 75):
            if (resourceList.clothes >0):
                resourceList.clothes -=  secrets.randbelow(resourceList.clothes)
        if (secrets.randbelow(100) > 75):
            if (resourceList.bullets >0):
                resourceList.bullets -= secrets.randbelow(resourceList.bullets)
        return 100



def sick(chances):
    alive = getAlive()
    aliveLen = len(alive)
    if(aliveLen <= 1):
        print("Everyone died")
        quit()
    if (secrets.randbelow(100)> chances):
        randIndex = secrets.randbelow(aliveLen - 1)
        if ((alive[randIndex]).status != True):
            (alive[randIndex]).status = True
        print(alive[randIndex].name + " is sick")

    


def exhaust():
    if (resourceList.exhaustion>= 5 and resourceList.exhaustion <10):
        sick(75)
    elif(resourceList.exhaustion>=10):
        sick(90)
        if(secrets.randbelow(100)>=85):
            killRandom("exhaustion")
        if(secrets.randbelow(100)>=50):
            if (resourceList.camels==1):
                resourceList.camels -=1
                print ("1 camel has died from exhaustion. you have " + str(resourceList.camels)+ " camels left")
            if (resourceList.camels >= 2):
                resourceList.camels -= 2 
                print ("2 camels have died from exhaustion. you have " + str(resourceList.camels)+ " camels left")
            
            if(resourceList.camels ==0):
                print("all of your camels have died, you lose")
                quit()

def sickCount():
    alive = getAlive()
    for index in range(0, len(alive) - 1):
            if (alive[index].status == True ):
                alive[index].sickTracker += 1
            if (alive[index].status == True and alive[index].sickTracker >=3):
                print(alive[index].name + " is sick! rest to make them feel better")
            if (alive[index].sickTracker > 3):
                (alive[index]).alive = False
                print(alive[index].name + " has died by illness")
        

def morningMenu(day):
    choice = 100
    while (choice >= 3 and choice != 5):

        print("Today is day " + str(day))
        print("You have traveled " + str(distance) + " miles")
        displayHunger()

        print("Options: ")
        print("1. Continue Traveling")
        print("2. Rest")
        print("3. Resources")
        print("4. Shop")
        print("5. Go Hunting")
        print("6. Quit to Main Menu")
        
        
        choice = getInput(1, 5)


    
        if(choice == 1):
            if (Rivers.checkRiver()):
                print("You must ford the river to continue")
                print(Rivers.checkRiver())
                choice = fordRiver()
              
            else:  
                travel()
            
        elif(choice == 2):
            rest()
        elif(choice == 3):
            resourceList.displayResources()
        elif(choice == 4):
            if (Town.checkTown() or day == 1):
                (
                    shopMenu()
                )
            else:
                print("You are not at a town, so you cannot open the shop menu at this time.")
        elif(choice == 5):
            if(resourceList.bullets >= 20):
                goHunt()
            else:
                print("You don't have enough bullets to go hunting")
        elif(choice == 6):
            return 0
            

def goHunt():

    resourceList.bullets -= 20

    randNum = secrets.randbelow(100) #generates either a 0, 1, or 2

    if(randNum <= 35):
        print("You weren't able to hunt down any game")
    elif(randNum <= 70):
        print("You were able to capture a couple desert rabbits and harvested some fruit from cacti, worth about 50 pounds of meat")
        resourceList.food += 50
    elif(randNum <= 90):
        print("You were able to hunt down a couple camels and gained 200 pounds of meat")
        resourceList.food += 100
    elif(randNum <= 100):
        killRandom("a camel trampeling them to death")

    
def shopMenu():

    choice = 0

    while(choice < 5):

        print("1. Food")
        print("2. Camels")
        print("3. Clothes")
        print("4. Bullets")
        print("5. Exit Shop")

        choice = getInput(1, 5)

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
    print("You currently have " + str(resourceList.food) + " lbs of food")
    print("Food costs $0.20 per lb")
    amount = getAmount("lbs of food", 0.2)
    print("You bought " + str(amount) + " lbs of food")
    resourceList.food += amount


def camelMenu():
    print("You currently have " + str(resourceList.camels) + " camels")
    print("One Camel costs $40.00")
    amount = getAmount("camels", 40)
    print("You bought " + str(amount) + " camels")
    resourceList.camels += amount

def clothesMenu():
    print("You currently have " + str(resourceList.clothes) + " sets of clothes")
    print("One set of clothes costs $5.00")
    amount = getAmount("sets of clothes", 5)
    print("You bought " + str(amount) + " sets of clothes")
    resourceList.clothes += amount

def bulletsMenu():
    print("You currently have " + str(resourceList.bullets) + " bullets")
    print("Bullets costs $5.00")
    amount = getAmount("bullets", 5)
    print("You bought " + str(amount) + " bullets")
    resourceList.bullets += amount

def getAmount(item, price):  

    amount = 2000
    isAmountValid = False
    while(isAmountValid == False):
        print("How many " + item + " would you like to purchase?")
        amount = getInput(0, 2000)
        if(amount * price <= resourceList.money):
            resourceList.money -= amount * price
            return amount
        print("You don't have enough money for that")
        print("You only have $" + '{:,.2f}'.format(resourceList.money))

    

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

    if(resourceList.distance >= 2000):
        return True
    
    if(Rivers.checkRiver(resourceList.distance)):
        return "You have reached a river!"
    if (Town.checkTown(resourceList.distance)):
        return "You have reached a town!"
        printAlive()
        print("made it to TigerHacks just in time!")
        quit()
    
    return False

#Return True if everyone died
def eatFood():
    alive = getAlive()

    if(resourceList.food < len(alive) * 5):
        resourceList.hunger -= 1
        if(resourceList.hunger <= 0):
            # printAlive()
            print( "perished due to starvation")
            return True
    else:
        resourceList.food -= 20
        if(resourceList.hunger < 3):
            resourceList.hunger += 1
    return False

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

def killRandom(deathMsg):
    alive = getAlive()
    aliveLen = len(alive)

    if(aliveLen == 1):
        print("You're entire party has died")
        return
    
    randIndex = secrets.randbelow(aliveLen - 1)
    (alive[randIndex]).alive = False
    print(alive[randIndex].name + " has died by " + deathMsg)
    
    

def displayHunger():
    if (resourceList.hunger == 1):
        print("You and your friends are on the brink of starvation")
    elif (resourceList.hunger == 2):
        print("You and your friends are a bit peckish due to a lack of food")
    if (resourceList.hunger == 3):
        print("You and your friends are nourished and ready to travel")

def travel():
    pace()


def rest():
    print("You rested")
    alive = getAlive()
    for index in range(0, len(alive) - 1):
            if (alive[index].status == True ):
                if (alive[index].SickTracker>1):
                    alive[index].SickTracker -=2
                elif (alive[index].SickTracker ==1):
                    alive[index].SickTracker -=1

    if (resourceList.exhaustion > 1):
        resourceList.exhaustion -= 2
    if (resourceList.exhaustion == 1):
        resourceList.exhaustion -=1
    




def openingSequence():
    print("After a massive rager on homecoming weekend, you and your friends find youself in Ancient Mesopotamia")
    print("TigerHacks is coming up in 2000 years, and you must start your travels immediately to make it in time")

    #Press Space to continue

    print("You decide to head northwest on foot until you come across four trustworthy camels")

    print("You decide to...")
    print("1. Include the Camels on your glorious adventure!")
    print("2. Be boring and not use the camels")

    choice = getInput(1, 2)

    if(choice == 1):
        return
    else:
        print("You set off on foot and then shortly after died traversing the harsh desert")
        print('You\'re dying words were "We should have welcomed those camels to our brotherhood"')
        exit()

def infoMenu():
    print("This is a game based on Oregon Trail")
    print("It was made by:")
    print("Connor Johnson")
    print("Zoe Strassner")
    print("John Lin")
    print("Ryan Wahle\n")

    print("Thanks for Playing! Hope you enjoy!")

    #Detect spacebar press
    mainMenu()

def settingsMenu():
    print("Ask someone not named Ryan to implement this")

    #Detect spacebar press
    mainMenu()

def controlsMenu():
    print("Controls Menu")
    print("If you found your way here you should be good to go")
    print("Simply use the buttons on the screen to navigate")
    print("Good luck on your adventure!")
    
    #Detect spacebar press
    mainMenu()

def getInput(minMenuInput, maxMenuInput):
    while(1):
        menuInput = input()
        if(check_user_input(menuInput) is True):
            menuInput = int(menuInput)
            if(menuInput >= minMenuInput and menuInput <= maxMenuInput):
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
    print("\nPace Options:\n")
    while (choice == 4): #the pace menu will loop until a valid option is selected 
        pace = ["1-Steady", "2-Strenuous", "3-Grueling", "4-Details"]
        for x in pace:
            print(x)
        choice = getInput(1, 4)
        if (choice == 1): #the pace is steady
            # print("Your pace is now", pace[0])
            distance +=10  #Note that distance is used instead of dist
        elif (choice == 2): #the pace is strenuous
            # print("Your pace is now", pace[1])
            distance +=15
            resourceList.exhaustion +=1
        elif (choice == 3): #the pace is grueling
            # print("Your pace is now", pace[2])
            distance +=20
            resourceList.exhaustion +=2
        elif (choice == 4): #describes each of the pace options
            print("""This is a menu to select your pace
            \n Steady lets you travel for about 8 hours per day. Which is around 10 miles. No exhaustion results from this.
            \n Strenuous lets you travel for about 12 hours per day. Which is around 15 miles. At the end of the day you feel tired
            \n Grueling lets you travel for 16 hours per day. Which is around 20 miles. At the end of the day you are exhauseted and health will suffer
            \nPace Options:
            """)
        

# testWindow = gui.GameGUI(500, 500)
    
        

#This is the start Screen for the Game
def main():
    # pygame.init()

    # test = gui.GameGUI(400,400)

    # clock = pygame.time.Clock()
    # testText = gui.Text("hello", "Georgia", 14, 0, 0, 255)
    # input_box1 = gui.InputBox(100, 100, 140, 32, testText)
    # input_box2 = gui.InputBox(100, 300, 140, 32, testText)
    # input_boxes = [input_box1, input_box2]
    # done = False

    print("\n *** Welcome to Tiger Trail! ***")
    username.username = getUsername()

    print("Your username is " + username.username)
    mainMenu()






