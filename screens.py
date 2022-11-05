import pygame
import sys
import pygame_textinput
import gui

clock = pygame.time.Clock()

#returns the username on completion
def usernameMenu(screen : gui.GameGUI) -> str:
    done = False
    text = gui.Text("What's your name", 'Georgia', 40, 0, 0, 0)
    errorText = gui.Text(" ", 'Georgia', 20, 150, 0, 0)
    inputRect = pygame.Rect(200, 200, 140, 32)

    textinput = pygame_textinput.TextInputVisualizer()
    pygame.key.set_repeat(200, 25)


    errorText.updateText("lol")
    errorText.updateColor(255, 255, 255)
    errorText.display(50, 100, screen)

    while not done:
        screen.getScreen().fill((225, 225, 225))

        events = pygame.event.get()

        textinput.update(events)

        # Get its surface to blit onto the screen
        screen.getScreen().blit(textinput.surface, (50, 200))

       

        # Check if user is exiting or pressed return
        for event in events:
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if(len(textinput.value) > 10):
                    errorText.updateColor((0,0,0))
                else:
                    done = True

        text.display(50, 50, screen)
        pygame.display.flip()
        clock.tick(30)

    return textinput.value

#returns 0 once the main menu is done running
def mainMenu(screen : gui.GameGUI, name : str) -> int:
    done = False
    text = gui.Text(f"welcome {name} to washington road", 'Corbel', 35, 255, 255, 255)
    rect1 = gui.SimpleButton(200, 200, gui.Text("Start", "Corbel", 20, 255, 255, 255))
    rect2 = gui.SimpleButton(200, 300, gui.Text("More", "Corbel", 20, 255, 255, 255))
    rect3 = gui.SimpleButton(200, 400, gui.Text("Quit", "Corbel", 20, 255, 255, 255))
    buttons = [rect1, rect2, rect3]
    screen.getScreen().fill((30, 150, 30))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].getRect().collidepoint(event.pos):
                    buttons[0].isClicked(True)
                elif buttons[1].getRect().collidepoint(event.pos):
                    buttons[1].isClicked(True)
                elif buttons[2].getRect().collidepoint(event.pos):
                    done = True
            elif event.type == pygame.KEYDOWN:
  
                # Check for backspace
                if event.key == pygame.K_1:
                    buttons[0].isClicked(True)
                elif event.key == pygame.K_2:
                    buttons[1].isClicked(True)
                elif event.key == pygame.K_3:
                    buttons[2].isClicked(True)
                    done = True
            else:
                buttons[0].isClicked(False)
                buttons[1].isClicked(False)
                buttons[2].isClicked(False)

        for button in buttons:
            if(button.getIsClicked()):
                button.draw(255, 0, 0, screen)
            else:
                button.draw(0,0,255, screen)
        
        text.display(200, 100, screen)
        pygame.display.flip()
        clock.tick(30)

    return 0

#returns zero upon completion
def moreMenu(screen : gui.GameGUI) -> int:
    done = False
    text = gui.Text("More stuff", 'Corbel', 35, 255, 255, 255)
    rect1 = gui.SimpleButton(200, 200, gui.Text("Start", "Corbel", 20, 255, 255, 255))
    rect2 = gui.SimpleButton(200, 300, gui.Text("More", "Corbel", 20, 255, 255, 255))
    rect3 = gui.SimpleButton(200, 400, gui.Text("Quit", "Corbel", 20, 255, 255, 255))
    buttons = [rect1, rect2, rect3]
    screen.getScreen().fill((30, 150, 30))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].getRect().collidepoint(event.pos):
                    buttons[0].isClicked(True)
                elif buttons[1].getRect().collidepoint(event.pos):
                    buttons[1].isClicked(True)
                elif buttons[2].getRect().collidepoint(event.pos):
                    done = True
            elif event.type == pygame.KEYDOWN:
  
                # Check for backspace
                if event.key == pygame.K_1:
                    buttons[0].isClicked(True)
                elif event.key == pygame.K_2:
                    buttons[1].isClicked(True)
                elif event.key == pygame.K_3:
                    buttons[2].isClicked(True)
                    done = True
            else:
                buttons[0].isClicked(False)
                buttons[1].isClicked(False)
                buttons[2].isClicked(False)

        for button in buttons:
            if(button.getIsClicked()):
                button.draw(255, 0, 0, screen)
            else:
                button.draw(0,0,255, screen)
        
        text.display(200, 100, screen)
        pygame.display.flip()
        clock.tick(30)
        
    return 0


def main():
    pygame.init()
    test = gui.GameGUI(720,720)
    name = usernameMenu(test)
    mainMenu(test, name)

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
    