import pygame
import secrets
#import gui

#Death: drowning, camel trampeling them to death, exhaustion

class Resc:
    def __init__(self, money, food, camels, clothes, bullets, hunger, exhaustion):
        self.money = money
        self.food = food
        self.camels = camels
        self.clothes = clothes
        self.bullets = bullets
        self.hunger = hunger
        self.exhaustion = exhaustion # Resc.exhaustion

    def displayResources(self):
        print("Resources: ")
        print("$: " + '{:,.2f}'.format(self.money))
        print("Food (lbs): " + str(self.food))
        print("Camels: " + str(self.camels))
        print("Sets of Clothes: " + str(self.clothes))
        print("Bullets: " + str(self.bullets))

class Rivers:

    def __init__(self, river1, river2,river3,river4):
        self.river1 = river1 #these numbers are the distance (in miles) from the start that the rivers occur
        self.river2 = river2
        self.river3 = river3
        self.river4 = river4
    def checkRiver():
        if (distance.total <= checkmark.river1+10 and distance.total >= checkmark.river1-10):
            # print("You have made it to river1!")
            return True
        elif (distance.total <= checkmark.river2+10 and distance.total >= checkmark.river2-10):
            return True
        elif (distance.total <= checkmark.river3+10 and distance.total >= checkmark.river3 -10):
            #print("you have made it to river3")
            return True
        elif (distance.total <= checkmark.river4+10 and distance.total>= checkmark.river4 -10):
            #print("you have made it to river4")
            return True
        else:
            return False

class Town:
    def __init__(self, town1, town2, town3, town4):
        self.town1 = town1 #these numbers are the distance (in miles) from the start that the rivers occur
        self.town2 = town2
        self.town3 = town3
        self.town4 = town4
    def checkTown():
        if (distance.total <= checkmarkTown.town1+10 and distance.total >= checkmarkTown.town1-10):
            return True
        elif (distance.total <= checkmarkTown.town2+10 and distance.total >= checkmarkTown.town2-10):
            return True
        elif (distance.total <= checkmarkTown.town3+10 and distance.total >= checkmarkTown.town3 -10):
            return True
        elif (distance.total <= checkmarkTown.town4+10 and distance.total>= checkmarkTown.town4 -10):
            return True
        else:
            return False

class Person:
  def __init__(self, name, alive, status, sickTracker):
    self.name = name
    self.alive = alive
    self.status = status
    self.sickTracker = sickTracker

class User:
    def __init__(self, username):
        self.username = username

class Dist: #This class defines distance
    def __init__(self, total):
        self.total = total #total will ideally start at 0 
        # self.speed = speed #speed
 

#Global Objects
resources = Resc(800.00, 20, 4, 4, 0, 3,0) #money, food, camels, clothes, bullets, hunger
distance = Dist(0)
username = User("WHERE IS JOHN")

person1 = Person("JOHN", True, None, 0)
person2 = Person("NOT JOHN", True, None, 0)
person3 = Person("DONDA ESTA JOHN", True, None, 0)
person4 = Person("JOHN IS BEHIND YOU", True, None, 0)

checkmark = Rivers(100, 1000, 1500, 2000)
checkmarkTown = Town(250, 750, 1250, 1750)



def resetObjects():
    resources.money = 800
    resources.food = 0
    resources.camels = 2
    resources.clothes = 0
    resources.bullets = 0
    resources.hunger = 3
    resources.exhaustion= 0
    distance.total = 0

        
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
    
    print("Before you continue journeying, you must stop at the shop to stock up. You have $800")
    shopMenu()

    code = 1
    day = 1
    while(1):
        checkDist() #ran on backend
        eatFood() #ran on backend
        exhaust()
        sick(95)
        sickCount()
        code = morningMenu(day)
        if(code == 0):
            return
        day += 1

def fordRiver(): #this calculates if a river is forded and then changes resources if they don't
    fordOrNot= secrets.randbelow(7)
    if (fordOrNot == 5 or fordOrNot ==6):
        print("You have forded the river")
        distance.total +=30
        return 1
    else:
        print("You have not forded the river ") #make so it prints out what is lost
        if (secrets.randbelow(100) > 85):
            killRandom("drowning")
        if (secrets.randbelow(100) > 75):
            if (resources.food >0):
                resources.food -= secrets.randbelow(resources.food)
                print("\033[1;31;49mYou have lost some food from trying to ford the river\033[1;37;49m")
        if (secrets.randbelow(100) > 75):
            if (resources.camels >0):
                resources.camels -= secrets.randbelow(resources.camels)
                print("\033[1;31;49mYou have lost some camels from trying to ford the river\033[1;37;49m")
                if (resources.camels ==0):
                    print("\033[1;31;49mall of your camels have died, you lose\033[1;37;49m")
                    quit()
                    
        if (secrets.randbelow(100) > 75):
            if (resources.clothes >0):
                resources.clothes -=  secrets.randbelow(resources.clothes)
                print("\033[1;31;49mYou have lost some clothes from trying to ford the river\033[1;37;49m")
        if (secrets.randbelow(100) > 75):
            if (resources.bullets >0):
                print("\033[1;31;49mYou have lost some bullets from trying to ford the river\033[1;37;49m")
                resources.bullets -= secrets.randbelow(resources.bullets)
        return 100



def sick(chances):
    alive = getAlive()
    aliveLen = len(alive)
    if(aliveLen <= 1):
        print("\033[1;31;49mEveryone died\033[1;37;49m")
        quit()
    if (secrets.randbelow(100)> chances):
        randIndex = secrets.randbelow(aliveLen - 1)
        if ((alive[randIndex]).status != True):
            (alive[randIndex]).status = True
        print(alive[randIndex].name + " is sick")

    


def exhaust():
    if (resources.exhaustion>= 5 and resources.exhaustion <10):
        sick(75)
    elif(resources.exhaustion>=10):
        sick(90)
        if(secrets.randbelow(100)>=85):
            killRandom("exhaustion")
        if(secrets.randbelow(100)>=50):
            if (resources.camels==1):
                resources.camels -=1
                print ("\033[1;31;49m1 camel has died from exhaustion. you have " + str(resources.camels)+ " camels left\033[1;37;49m")
            if (resources.camels >= 2):
                resources.camels -= 2 
                print ("\033[1;31;49m2 camels have died from exhaustion. you have " + str(resources.camels)+ " camels left\033[1;37;49m")
            
            if(resources.camels ==0):
                print("all of your camels have died, you lose")
                quit()

def sickCount():
    alive = getAlive()
    for index in range(0, len(alive) - 1):
            if (alive[index].status == True ):
                alive[index].sickTracker += 1
            if (alive[index].status == True and alive[index].sickTracker >=3):
                print("\033[1;31;49m" + alive[index].name + " is really sick! rest to make them feel better\033[1;37;49m")
            if (alive[index].sickTracker > 3):
                (alive[index]).alive = False
                print(alive[index].name + "\033[1;31;49m has died by illness\033[1;37;49m")
        

def morningMenu(day):
    choice = 100
    while (choice >= 3 and choice != 5):

        print("\033[1;32mToday is day " + str(day) + "\033[1;37m")
        print("\033[1;33;49mYou have traveled " + str(distance.total) + " miles\033[1;37;49m")
        displayHunger()

        print("Options: ")
        print("\033[1;35;49m1. Continue Traveling\033[1;37;49m")
        print("\033[1;35;49m2. Rest\033[1;37;49m")
        print("\033[1;35;49m3. Resources\033[1;37;49m")
        print("\033[1;35;49m4. Shop\033[1;37;49m")
        print("\033[1;35;49m5. Go Hunting\033[1;37;49m")
        print("\033[1;35;49m6. Quit to Main Menu\033[1;37;49m")
        
        
        choice = getInput(1, 6)


    
        if(choice == 1):
            if (Rivers.checkRiver()):
                print("\033[1;33;49mYou must ford the river to continue\033[1;37;49m")
                print(Rivers.checkRiver())
                choice = fordRiver()
              
            else:  
                travel()
            
        elif(choice == 2):
            rest()
        elif(choice == 3):
            resources.displayResources()
        elif(choice == 4):
            if (Town.checkTown() or day == 1):
                (
                    shopMenu()
                )
            else:
                print("\033[1;35;49mYou are not at a town, so you cannot open the shop menu at this time.\033[1;37;49m")
        elif(choice == 5):
            if(resources.bullets >= 20):
                goHunt()
            else:
                print("\033[1;33;49mYou don't have enough bullets to go hunting\033[1;37;49m")
        elif(choice == 6):
            return 0
            

def goHunt():

    resources.bullets -= 20

    randNum = secrets.randbelow(100) #generates either a 0, 1, or 2

    if(randNum <= 35):
        print("\033[1;33;49mYou weren't able to hunt down any game\033[1;37;49m")
    elif(randNum <= 70):
        print("\033[1;33;49mYou were able to capture a couple desert rabbits and harvested some fruit from cacti, worth about 50 pounds of meat\033[1;37;49m")
        resources.food += 50
    elif(randNum <= 90):
        print("\033[1;33;49mYou were able to hunt down a couple camels and gained 200 pounds of meat\033[1;37;49m")
        resources.food += 200
    elif(randNum <= 100):
        killRandom("\033[1;31;49ma camel trampeling them to death\033[1;37;49m")

    
def shopMenu():

    choice = 0

    while(choice < 5):

        print("\033[1;35;49m1. Food\033[1;37;49m")
        print("\033[1;35;49m2. Camels\033[1;37;49m")
        print("\033[1;35;49m3. Clothes\033[1;37;49m")
        print("\033[1;35;49m4. Bullets\033[1;37;49m")
        print("\033[1;35;49m5. Exit Shop\033[1;37;49m")

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
    print("\033[1;33;49mYou currently have " + str(resources.food) + " lbs of food\033[1;37;49m")
    print("\033[1;33;49mFood costs $0.20 per lb\033[1;37;49m")
    amount = getAmount("lbs of food", 0.2)
    print("\033[1;33;49mYou bought " + str(amount) + " lbs of food\033[1;37;49m")
    resources.food += amount


def camelMenu():
    print("\033[1;33;49mYou currently have " + str(resources.camels) + " camels\033[1;37;49m")
    print("\033[1;33;49mOne Camel costs $100.00\033[1;37;49m")
    amount = getAmount("camels", 100)
    print("\033[1;32;49mYou bought " + str(amount) + " camels\033[1;37;49m")
    resources.camels += amount

def clothesMenu():
    print("\033[1;33;49mYou currently have " + str(resources.clothes) + " sets of clothes\033[1;37;49m")
    print("\033[1;33;49mOne set of clothes costs $5.00\033[1;37;49m")
    amount = getAmount("sets of clothes", 5)
    print("\033[1;32;49mYou bought " + str(amount) + " sets of clothes\033[1;37;49m")
    resources.clothes += amount

def bulletsMenu():
    print("\033[1;33;49mYou currently have " + str(resources.bullets) + " bullets\033[1;37;49m")
    print("\033[1;33;49mBullets cost $0.25 per bullet (20 bullets cost $5.00)\033[1;37;49m")
    amount = getAmount("bullets", .25)
    print("\033[1;32;49mYou bought " + str(amount) + " bullets\033[1;37;49m")
    resources.bullets += amount

def getAmount(item, price):  

    amount = 2000
    isAmountValid = False
    while(isAmountValid == False):
        print("\033[1;33;49mHow many " + item + " would you like to purchase?\033[1;37;49m")
        amount = getInput(0, 2000)
        if(amount * price <= resources.money):
            resources.money -= amount * price
            return amount
        print("\033[1;33;49mYou don't have enough money for that\033[1;37;49m")
        print("\033[1;33;49mYou only have $\033[1;37;49m" + '{:,.2f}'.format(resources.money))

    

def chooseNames():
    person1.name = getName(1)
    person2.name = getName(2)
    person3.name = getName(3)
    person4.name = getName(4)

def getName(num):
    name = ""
    name = input("\033[1;32;49mEnter the name of character\033[1;37;49m " + str(num) + ":\n")
    while(name == "" or len(name) > 10):
        name = input("\033[1;31;49mERROR: Enter valid name (up to 10 characters): \033[1;37;49m\n")
    return name.strip()
    

def checkDist():
    
    if(Rivers.checkRiver()):
        print("\033[1;32;49mYou have reached a river!\033[1;37;49m")
    if (Town.checkTown()):
        print("\033[1;32;49mYou have reached a town!\033[1;37;49m")
    if(distance.total >= 2000):
        print("\033[1;32;49mCongratulations!\033[1;37;49m")
        printAlive()
        print("\033[1;32;49mmade it to TigerHacks just in time!\033[1;37;49m")
        quit()

def eatFood():
    alive = getAlive()

    if(resources.food < len(alive) * 5):
        resources.hunger -= 1
        if(resources.hunger <= 0):
            printAlive()
            print( "\033[1;31;49mperished due to starvation\033[1;37;49m")
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

def killRandom(deathMsg):
    alive = getAlive()
    aliveLen = len(alive)

    if(aliveLen == 1):
        print("\033[1;31;49mYou're entire party has died\033[1;37;49m")
        return
    
    randIndex = secrets.randbelow(aliveLen - 1)
    (alive[randIndex]).alive = False
    print("\033[1;31;49m" + alive[randIndex].name + " has died by " + deathMsg + "\033[1;37;49m")
    
    

def displayHunger():
    if (resources.hunger == 1):
        print("\033[1;31;49mYou and your friends are on the brink of starvation\033[1;37;49m")
    elif (resources.hunger == 2):
        print("\033[1;33;49mYou and your friends are a bit peckish due to a lack of food\033[1;37;49m")
    if (resources.hunger == 3):
        print("\033[1;32;49mYou and your friends are nourished and ready to travel\033[1;37;49m")

def travel():
    pace()


def rest():
    print("\033[1;32;49mYou rested\033[1;31;49m")
    alive = getAlive()
    for index in range(0, len(alive) - 1):
            if (alive[index].status == True ):
                if (alive[index].sickTracker>1):
                    alive[index].sickTracker =0
                    alive[index].status = False
                if (alive[index].sickTracker ==1):
                    alive[index].sickTracker =0
                    alive[index].status = False

    if (resources.exhaustion > 1):
        resources.exhaustion -= 2
    if (resources.exhaustion == 1):
        resources.exhaustion -=1
    




def openingSequence():
    print("After a massive rager on homecoming weekend, you and your friends find youself in Ancient Mesopotamia")
    print("TigerHacks is coming up in 2000 years, and you must start your travels immediately to make it in time")

    #Press Space to continue

    print("You decide to head northwest on foot until you come across four trustworthy camels")

    print("You decide to...")
    print("\033[1;35;49m1. Include the Camels on your glorious adventure!\033[1;37;49m")
    print("\033[1;35;49m2. Be boring and not use the camels\033[1;37;49m")

    choice = getInput(1, 2)

    if(choice == 1):
        return
    else:
        print("\033[1;31;49mYou set off on foot and then shortly after died traversing the harsh desert\033[1;37;49m")
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
                print("\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n")
                return menuInput
        print("\033[1;31;49mERROR: Enter a number between 1 and " + str(maxMenuInput) + "\033[1;37;49m")

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
        pace = ["\033[1;35;49m1-Steady", "2-Strenuous", "3-Grueling", "4-Details\033[1;37;49m"]
        for x in pace:
            print(x)
        choice = getInput(1, 4)
        if (choice == 1): #the pace is steady
            # print("Your pace is now", pace[0])
            distance.total +=10  #Note that distance is used instead of dist
        elif (choice == 2): #the pace is strenuous
            # print("Your pace is now", pace[1])
            distance.total +=15
            resources.exhaustion +=1
        elif (choice == 3): #the pace is grueling
            # print("Your pace is now", pace[2])
            distance.total +=20
            resources.exhaustion +=2
        elif (choice == 4): #describes each of the pace options
            print("""\033[1;33;49mThis is a menu to select your pace
            \n Steady lets you travel for about 8 hours per day. Which is around 10 miles. No exhaustion results from this.
            \n Strenuous lets you travel for about 12 hours per day. Which is around 15 miles. At the end of the day you feel tired
            \n Grueling lets you travel for 16 hours per day. Which is around 20 miles. At the end of the day you are exhauseted and health will suffer
            \nPace Options:
            \033[1;37;49m""")
        

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


main()



