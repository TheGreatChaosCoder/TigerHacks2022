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
        pygame.display.update()

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
        self.text = self.render
        gui.screen.blit(self.text, self.text.get_rect(center = (x,y)))
        gui.update()

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