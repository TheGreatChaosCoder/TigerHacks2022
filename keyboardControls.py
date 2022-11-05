import pygame

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keyInput[myKey]:
        ans=True

    pygame.display.update()
    return ans
