import pygame
from pygame.locals import *

# Constants
WINDOWWIDTH = 600
WINDOWHEIGHT= 500
TILESIZE    = 120
BOARDWIDTH  = 3
BOARDHEIGHT = 3
MARKERSIZE  = 40

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * TILESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * TILESIZE)) / 2)

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
        for x in range(TILESIZE, BOARDWIDTH * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, 
               (x + XMARGIN, YMARGIN), (x + XMARGIN, WINDOWHEIGHT - YMARGIN), 6)
        for y in range(TILESIZE, BOARDHEIGHT * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, 
                (XMARGIN, y + YMARGIN), (WINDOWWIDTH - XMARGIN, y + YMARGIN), 6)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

if __name__ == '__main__': main()