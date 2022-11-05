import pygame
import gui

class Resc:
    def __init__(self, food, camels, clothes, bullets):
        self.food = food
        self.camels = camels
        self.clothes = clothes
        self.bullets = bullets

    def displayResources(self):
        print("Resources: ")
        print("Food (lbs): " + str(self.food))
        print("Camels: " + str(self.camels))
        print("Sets of Clothes: " + str(self.clothes))
        print("Bullets: " + str(self.bullets))
    

class Person:
  def __init__(self, name):
    self.name = name

class Dist: #This class defines distance
    def __init__(self, total):
        self.total = total #total will ideally start at 0 
        # self.speed = speed #speed
        
def getUsername():
    name = ""
    name = input("Enter your username (up to 10 characters): \n")
    while(name == "" or len(name) > 10):
        name = input("ERROR: Enter valid username (up to 10 characters): \n")
    return name.strip()

#This is the main Meny for the Game
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

    resources = Resc(0, 4, 4, 0)
    distance = Dist(0)
    

    openingSequence()

    day = 1
    while(1):
        morningMenu(day, resources, distance)
        day += 1
        

def morningMenu(day, resources : Resc, distance : Dist):
    choice = 5
    while (choice >= 3):
        print("Today is day " + str(day))
        print("You have traveled " + str(distance.total) + " miles")

        print("Options: ")
        print("1. Continue Traveling")
        print("2. Rest")
        print("3. Resources")
        print("4. Quit Game")
        
        choice = getInput(4)
    
        if(choice == 1):
            travel(distance)
        elif(choice == 2):
            rest()
        elif(choice == 3):
            resources.displayResources()
        elif(choice == 4):
            quit()
    

def travel(distance: Dist):
    pace(distance)

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


def pace(distance: Dist): #This is the pace menu, lets the user select what pace they want
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
        elif (choice==3): #the pace is grueling
            print("Your pace is now", pace[2])
            distance.total +=20
        elif (choice ==4): #describes each of the pace options
            print("""This is a menu to select your pace
            \n Steady lets you travel for about 8 hours per day. Which is around 10 miles. No exhaustion results from this.
            \n Strenuous lets you travel for about 12 hours per day. Which is around 15 miles. At the end of the day you feel tired
            \n Grueling lets you travel for 16 hours per day. Which is around 20 miles. At the end of the day you are exhauseted and health will suffer
            \nEnter your input:
            """)
        

testWindow = gui.GameGUI(500, 500)
    
        

#This is the start Screen for the Game
def main():
    pygame.init()

    test = gui.GameGUI(400,400)

    clock = pygame.time.Clock()
    testText = gui.Text("helllo", "Georgia", 14, 0, 0, 255)
    input_box1 = gui.InputBox(100, 100, 140, 32, testText)
    input_box2 = gui.InputBox(100, 300, 140, 32, testText)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        test.getScreen().fill((30, 30, 30))
        for box in input_boxes:
            box.draw(test.getScreen())

        pygame.display.flip()
        clock.tick(30)
    
    print("\n *** Welcome to Tiger Trail! ***")
    name = getUsername()
    print("Your username is " + name)
    mainMenu()



main()





