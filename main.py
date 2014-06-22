import pygame
from pygame.locals import *

# Constants
WINDOWWIDTH = 400
WINDOWHEIGHT= 300
TILESIZE    = 60
BOARDWIDTH  = 3
BOARDHEIGHT = 3
MARKERSIZE  = 40

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * TILESIZE) - MARKERSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * TILESIZE) - MARKERSIZE) / 2)

# Colors
WHITE       = (255, 255, 255)
DARKGRAY    = (40, 40, 40)

def main():
    #global WINDOWWIDTH, WINDOWHEIGHT, TILESIZE, BOARDWIDTH, BOARDHEIGHT, MARKERSIZE, XMARGIN, YMARGIN
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode( (WINDOWWIDTH, WINDOWHEIGHT) )
    pygame.display.set_caption("Tic-Tac-Toe")
    
    board = [[None] * 3 for i in range(3)]
    
    while True:
        # Draw board
        for x in range(0, (BOARDWIDTH + 1) * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (x + XMARGIN + MARKERSIZE,
                YMARGIN + MARKERSIZE), (x + XMARGIN + MARKERSIZE, WINDOWHEIGHT - YMARGIN))
        for y in range(0, (BOARDWIDTH + 1) * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (XMARGIN + MARKERSIZE,
                y + YMARGIN + MARKERSIZE), (WINDOWWIDTH - (MARKERSIZE * 2), y + YMARGIN + MARKERSIZE))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

if __name__ == '__main__': main()