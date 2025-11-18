import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH,HEIGHT = 600,400
BLACK = (0,0,0)
GREY = (160,160,160)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 50,50
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
        drawRect()
        pygame.display.update()

def drawRect():
    # There's a native way to draw a rectange in pygame,
    # this is just to explain how lines can be drawn.
    # TOP LEFT TO RIGHT
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
        (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)
    # BOTTOM LEFT TO RIGHT
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM),
        (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    # LEFT TOP TO BOTTOM 
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
        (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
        (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    # FIRST ROW
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT + 100, 0 + PADTOPBOTTOM),
        (0 + PADLEFTRIGHT + 100, HEIGHT - PADTOPBOTTOM), 2)
    # SECOND ROW
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT + 200, 0 + PADTOPBOTTOM),
        (0 + PADLEFTRIGHT + 200, HEIGHT - PADTOPBOTTOM), 2)
    # THIRD ROW
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT + 300, 0 + PADTOPBOTTOM),
        (0 + PADLEFTRIGHT + 300, HEIGHT - PADTOPBOTTOM), 2)
    # FIRST COLUMN
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, 75 + PADTOPBOTTOM),
        (300 + PADLEFTRIGHT, 75 + PADTOPBOTTOM), 2)
    # SECOND COLUMN
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, 150 + PADTOPBOTTOM),
        (300 + PADLEFTRIGHT, 150 + PADTOPBOTTOM), 2)
    # THIRD COLUMN
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (0 + PADLEFTRIGHT, 225 + PADTOPBOTTOM),
        (300 + PADLEFTRIGHT, 225 + PADTOPBOTTOM), 2)
    # The number 1
    pygame.draw.line(
        _VARS["surf"], BLACK,
        ( 50 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (50 + PADLEFTRIGHT, 120), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (50 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (35 + PADLEFTRIGHT, 35 + PADTOPBOTTOM), 6)
    # The number 2
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (125 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (175 + PADLEFTRIGHT, 10 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (175 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (125 + PADLEFTRIGHT, 115), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (125 + PADLEFTRIGHT, 115),
        (175 + PADLEFTRIGHT, 115), 6)
    # The number 3
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (225 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (275 + PADLEFTRIGHT, 10 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (275 + PADLEFTRIGHT, 10 + PADTOPBOTTOM),
        (275 + PADLEFTRIGHT, 60 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (225 + PADLEFTRIGHT, 35 + PADTOPBOTTOM),
        (275 + PADLEFTRIGHT, 35 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (225 + PADLEFTRIGHT, 60 + PADTOPBOTTOM),
        (275 + PADLEFTRIGHT, 60 + PADTOPBOTTOM), 6)
    # The number 4
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (30 + PADLEFTRIGHT, 80 + PADTOPBOTTOM),
        (30 + PADLEFTRIGHT, 110 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (30 + PADLEFTRIGHT, 110 + PADTOPBOTTOM),
        (60 + PADLEFTRIGHT, 110 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (60 + PADLEFTRIGHT, 80 + PADTOPBOTTOM),
        (60 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    # The number 5
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 80 + PADTOPBOTTOM),
        (160 + PADLEFTRIGHT, 80 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 80 + PADTOPBOTTOM),
        (130 + PADLEFTRIGHT, 110 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 110 + PADTOPBOTTOM),
        (160 + PADLEFTRIGHT, 110 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (160 + PADLEFTRIGHT, 110 + PADTOPBOTTOM),
        (160 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 140 + PADTOPBOTTOM),
        (160 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    # The number 5
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 140 + PADTOPBOTTOM),
        (260 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 80 + PADTOPBOTTOM),
        (230 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 110 + PADTOPBOTTOM),
        (260 + PADLEFTRIGHT, 110 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (260 + PADLEFTRIGHT, 110 + PADTOPBOTTOM),
        (260 + PADLEFTRIGHT, 140 + PADTOPBOTTOM), 6)
    # The number 7
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (20 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (80 + PADLEFTRIGHT, 170 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (75 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (50 + PADLEFTRIGHT, 210 + PADTOPBOTTOM), 6)
    # The number 8
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (170 + PADLEFTRIGHT, 170 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (170 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (170 + PADLEFTRIGHT, 210 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 190 + PADTOPBOTTOM),
        (170 + PADLEFTRIGHT, 190 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (130 + PADLEFTRIGHT, 210 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (130 + PADLEFTRIGHT, 210 + PADTOPBOTTOM),
        (170 + PADLEFTRIGHT, 210 + PADTOPBOTTOM), 6)
    # The number 9
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (270 + PADLEFTRIGHT, 170 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (270 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (270 + PADLEFTRIGHT, 210 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 170 + PADTOPBOTTOM),
        (230 + PADLEFTRIGHT, 185 + PADTOPBOTTOM), 6)
    pygame.draw.line(
        _VARS["surf"], BLACK,
        (230 + PADLEFTRIGHT, 185 + PADTOPBOTTOM),
        (270 + PADLEFTRIGHT, 185 + PADTOPBOTTOM), 6)
    
    

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()





