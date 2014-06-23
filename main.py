import pygame
import pygame.freetype
from pygame.locals import *

# Constants
PLAYER = 'player'
COMPUTER = 'computer'
WINDOWWIDTH = 600
WINDOWHEIGHT= 500
TILESIZE    = 120
HALFTILE    = int(TILESIZE / 2)
BOARDWIDTH  = 3
BOARDHEIGHT = 3
FONTSIZE = 50

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * TILESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * TILESIZE)) / 2)

# Colors
WHITE       = (255, 255, 255)
DARKGRAY    = (40, 40, 40)

def left_top_coords(tilex, tiley):
    '''
    returns left and top pixel coords
    tilex: int
    tiley: int
    return: int, int
    '''
    left = tilex * TILESIZE + XMARGIN
    top = tiley * TILESIZE + YMARGIN
    return left, top

def main():
    #global WINDOWWIDTH, WINDOWHEIGHT, TILESIZE, BOARDWIDTH, BOARDHEIGHT, MARKERSIZE, XMARGIN, YMARGIN
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode( (WINDOWWIDTH, WINDOWHEIGHT) )
    pygame.display.set_caption("Tic-Tac-Toe")
    FONT = pygame.freetype.Font(None, FONTSIZE)
    
    board = [[None] * 3 for i in range(3)]
    # For testing only
    board[0][1] = COMPUTER
    
    while True:
        mouse_clicked = False
        # Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
        if mouse_clicked:
            for tiley in range(len(board)):
                for tilex in range(len(board[tiley])):
                    leftpos = tilex * TILESIZE + XMARGIN
                    toppos = tiley * TILESIZE + YMARGIN
                    tile_rect = pygame.Rect(leftpos, toppos, TILESIZE, TILESIZE)
                    if tile_rect.collidepoint(mousex, mousey) and board[tiley][tilex] == None:
                        board[tiley][tilex] = PLAYER
        # Draw board lines
        for x in range(TILESIZE, BOARDWIDTH * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, 
               (x + XMARGIN, YMARGIN), (x + XMARGIN, WINDOWHEIGHT - YMARGIN), 6)
        for y in range(TILESIZE, BOARDHEIGHT * TILESIZE, TILESIZE):
            pygame.draw.line(DISPLAYSURF, DARKGRAY, 
                (XMARGIN, y + YMARGIN), (WINDOWWIDTH - XMARGIN, y + YMARGIN), 6)
        # Make tile rects
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] in (PLAYER, COMPUTER):
                    if board[y][x] == PLAYER:
                        surf, surfrect = FONT.render('X', DARKGRAY, None)
                    elif board[y][x] == COMPUTER:
                        surf, surfrect = FONT.render('O', DARKGRAY, None)                
                    surfrect.center = (int(XMARGIN + (x * TILESIZE) + HALFTILE), int(YMARGIN + (y * TILESIZE) + HALFTILE))
                    DISPLAYSURF.blit(surf, surfrect)
            
        pygame.display.update()

if __name__ == '__main__': main()