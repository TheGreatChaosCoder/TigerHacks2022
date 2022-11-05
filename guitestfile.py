import pygame

pygame.init()



screen = pygame.display.set_mode((800, 600))
logo = pygame.image.load("tiger.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("hello world")

player = pygame.image.load('tiger.png')

def character(x, y):
    screen.blit(player, (x,y))

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    character(400, 300)
    pygame.display.update() 