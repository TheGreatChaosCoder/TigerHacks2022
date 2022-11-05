import pygame


class GameGUI:
    def __init__(self, width : int, height : int) -> None:
        self.screen = pygame.display.set_mode((width,height))

    #fills a screen with a given rgb value
    def fillScreen(self, r : int, g : int, b : int) -> None:
        self.screen.fill((r,g,b))

    #places an image at a specified (x,y) coordinate
    def addImage(self, img, x, y) -> None:
        self.screen.blit(img, (x, y))
        self.update()

    def getScreen(self):
        return self.screen
    
    def update(self) -> None:
        pygame.display.flip()

class SimpleButton():
    def __init__(self, width, height, text = ""):
        self.rect = pygame.Rect(width, height, 140, 32)
        self.width = width
        self.height = height
        self.clicked = False
        self.text = text

    def isClicked(self, clicked : bool) -> None:
        self.clicked = clicked

    def getIsClicked(self) -> bool:
        return self.clicked

    def getRect(self):
        return self.rect

    def draw(self, r, g, b, screen : GameGUI):
        pygame.draw.rect(screen.getScreen(), (r, g, b), self.rect)

        if(self.text is not None):
            self.text.display(self.width + self.text.getSurfaceWidth(),
                           self.height + self.text.getSurfaceHeight(), screen)

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

class Text:
    def __init__(self, msg : str, font : str, size, r, g, b) -> None:
        self.font = pygame.font.SysFont(msg, size)
        self.msg = msg
        self.rgb = (r, g, b)

    def render(self):
        return self.font.render(self.msg, 1, self.rgb)
	
    def display(self, x, y, gui : GameGUI) -> None:
        #self.text = self.render()
        #self.rect = self.text.get_rect(center=(x,y))
        gui.screen.blit(self.render(), (x,y))
        gui.update()

    def getSurfaceWidth(self):
        return self.render().get_width()
    
    def getSurfaceHeight(self):
        return self.render().get_height()

    def updateText(self, msg : str) -> None:
        self.msg = msg

    def updateColor(self, r, g, b) -> None:
        self.rgb = (r, g, b)

class InputBox:
    def __init__(self, x, y, w, h, msg : Text, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (125,125,0)
        self.msg = msg
        self.text = text
        self.txt_surface = msg.render()
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (150, 150, 0) if self.active else (125,125,0)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.msg.render()

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)