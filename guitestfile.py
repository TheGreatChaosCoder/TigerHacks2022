import pygame
from screeninfo import get_monitors

pygame.init()

for screen in get_monitors():
    str(screen)

print(screen.height)
print(screen.width)