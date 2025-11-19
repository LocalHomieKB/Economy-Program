import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 60, 60
# VARS:
_VARS = {'surf': False}


def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawGrid(3)
        pygame.display.update()


def drawGrid(divisions):
    # DRAW Rectangle
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)
    # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (0 + PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)
    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (WIDTH - PADLEFTRIGHT, HEIGHT - PADTOPBOTTOM), 2)

    # Get cell size
    horizontal_cellsize = (WIDTH - (PADLEFTRIGHT*2))/divisions
    vertical_cellsize = (HEIGHT - (PADTOPBOTTOM*2))/divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
           _VARS['surf'], BLACK,
           (0 + PADLEFTRIGHT+(horizontal_cellsize*x), 0 + PADTOPBOTTOM),
           (0 + PADLEFTRIGHT+horizontal_cellsize*x, HEIGHT - PADTOPBOTTOM), 2)
    # HORITZONTAL DIVISION
        pygame.draw.line(
          _VARS['surf'], BLACK,
          (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)),
          (WIDTH - PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()