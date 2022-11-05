import pygame
import sys
import gui

clock = pygame.time.Clock()

def usernameMenu(screen : gui.GameGUI) -> int:
    done = False
    text = gui.Text("What's your name", 'Georgia', 40, 0, 0, 0)
    nameText = gui.Text("", 'Cobal', 20, 0, 0, 0)
    inputRect = pygame.Rect(200, 200, 140, 32)
    name = ""

    while not done:
        for event in pygame.event.get():
  
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputRect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    name = name[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    name += event.unicode

        nameText.updateText(name)

        screen.getScreen().fill((150, 55, 0))
        nameText.display(720/2, 720/2, screen)
        pygame.display.flip()
        clock.tick(30)

#returns 0 once the main menu is done running
def mainMenu(screen : gui.GameGUI) -> int:
    done = False
    text = gui.Text("washington road", 'Corbel', 35, 255, 255, 255)
    rect1 = gui.SimpleButton(200, 200)
    rect2 = gui.SimpleButton(200, 400)
    buttons = [rect1, rect2]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].getRect().collidepoint(event.pos):
                    buttons[0].isClicked(True)
                elif buttons[1].getRect().collidepoint(event.pos):
                    buttons[1].isClicked(True)
            elif event.type == pygame.KEYDOWN:
  
                # Check for backspace
                if event.key == pygame.K_1:
                    buttons[0].isClicked(True)
                elif event.key == pygame.K_2:
                    buttons[1].isClicked(True)
            else:
                buttons[0].isClicked(False)
                buttons[1].isClicked(False)

        screen.getScreen().fill((30, 30, 30))


        for button in buttons:
            if(button.getIsClicked()):
                button.draw(255, 0, 0, screen)
            else:
                button.draw(0,0,255, screen)
        
        text.display(720/2, 100, screen)
        pygame.display.flip()
        clock.tick(30)

    return 0

def main():
    pygame.init()
    test = gui.GameGUI(720,720)
    usernameMenu(test)
    #mainMenu(test)

main()

    # while not done:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             done = True
    #         for box in input_boxes:
    #             box.handle_event(event)

    #     for box in input_boxes:
    #         box.update()

    #     test.getScreen().fill((30, 30, 30))
    #     for box in input_boxes:
    #         box.draw(test.getScreen())

    #     pygame.display.flip()
    #     clock.tick(30)
    