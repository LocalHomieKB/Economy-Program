import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH,HEIGHT = 600,400
BLACK = (0,0,0)
GREY = (160,160,160)
# GLOBAL VARS, using a dictionary
_VARS = {"surf" : False}

# this is the main game loop that runs until Q is pressed
# or game closed
# CAUTION: this will run as fast as computer allows
# if you need to set a specific fps check tick methods

def main():
    pygame.init() #inital setup
    _VARS["surf"] = pygame.display.set_mode(SCREENSIZE)
    # the loop proper, things inside this loop will
    # be called over and over unti you exite the window
    while True:
        checkEvents()
        _VARS["surf"].fill(GREY)
        drawLine()
        pygame.display.update()


def drawLine():
    # draw a diagonal line from top left coordinates 0,0
    # to bottom right with coordinates 600 (Width), 400 (Height)
    pygame.draw.line(_VARS["surf"],BLACK,(0,0),(WIDTH,HEIGHT),2)

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()