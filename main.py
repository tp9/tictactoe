# coding=UTF8
import pygame, os, sys, random, copy
import pygame.freetype
from pygame.locals import *
from pprint import pprint as pp

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


class BestMove():
    def __init__(self, value, location):
        self.value = value
        self.location = location
    

def mouse_clicked(in_board, mousex, mousey):
    board = copy.deepcopy(in_board)
    game_over = False
    winner = None
    
    for tiley in range(BOARDHEIGHT):
        for tilex in range(BOARDWIDTH):
            leftpos = tilex * TILESIZE + XMARGIN
            toppos = tiley * TILESIZE + YMARGIN
            tile_rect = pygame.Rect(leftpos, toppos, TILESIZE, TILESIZE)
            if tile_rect.collidepoint(mousex, mousey) and board[tiley][tilex] == None:
                board[tiley][tilex] = PLAYER
                if player_wins(board, PLAYER):
                    game_over = True
                    winner = PLAYER
                else:
                    # Make computer move
                    if tile_available(board):
                        compx, compy = minimax(board = board, player = COMPUTER)[1]
                        board[compy][compx] = COMPUTER
                    else:
                        game_over = True
                        winner = 'No one'
                    if player_wins(board, COMPUTER):
                        game_over = True
                        winner = COMPUTER
    return board, game_over, winner
                                
def tile_available(board):
    tile_available = False
    for y in range(BOARDHEIGHT):
        if None in board[y]:
            tile_available = True
            break;    
    return tile_available

def player_wins(board, current_player):
    if [current_player, current_player, current_player] in (
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]] ):
        return True
    else:
        return False

def next_player(current_player):
    value = None
    next = None
    if current_player == COMPUTER:
        value = -2
        next = PLAYER
    else:
        value = +2
        next = COMPUTER
    return value, next
        
def draw_board(displaysurf):
    for x in range(TILESIZE, BOARDWIDTH * TILESIZE, TILESIZE):
        pygame.draw.line(displaysurf, DARKGRAY, 
           (x + XMARGIN, YMARGIN), (x + XMARGIN, WINDOWHEIGHT - YMARGIN), 6)
    for y in range(TILESIZE, BOARDHEIGHT * TILESIZE, TILESIZE):
        pygame.draw.line(displaysurf, DARKGRAY, 
            (XMARGIN, y + YMARGIN), (WINDOWWIDTH - XMARGIN, y + YMARGIN), 6)

def draw_tiles(displaysurf, in_board, x_surf, x_surfrect, o_surf, o_surfrect):
   board = copy.deepcopy(in_board)
   for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] in (PLAYER, COMPUTER):
                if board[y][x] == PLAYER:
                    surf, surfrect = x_surf, x_surfrect
                elif board[y][x] == COMPUTER:
                    surf, surfrect = o_surf, o_surfrect                
                surfrect.center = (int(XMARGIN + (x * TILESIZE) + HALFTILE), int(YMARGIN + (y * TILESIZE) + HALFTILE))
                displaysurf.blit(surf, surfrect)
                    
def minimax(board, player):
    if player_wins(board, PLAYER):
        return(-1, None)
    elif player_wins(board, COMPUTER):
        return(+1, None)
    elif not tile_available(board):
        return(0, None)
    else:
        point_value, next_person = next_player(player)
        best_move = BestMove(value = point_value, location = None)
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH):
                if board[y][x] == None:
                    new_board = copy.deepcopy(board)
                    new_board[y][x] = player
                    value = minimax(new_board, next_person)[0]
                    if (value > best_move.value and player == COMPUTER) or (value < best_move.value and player == PLAYER):
                        best_move.value, best_move.location = value, (x,y)                    
        return best_move.value, best_move.location
        
def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode( (WINDOWWIDTH, WINDOWHEIGHT) )
    pygame.display.set_caption("Tic-Tac-Toe")
    FONT = pygame.freetype.Font(None, FONTSIZE)
    
    board = [[None] * 3 for i in range(3)]
    game_over = False
    winner = None
    
    x_surf, x_surfrect = FONT.render('X', DARKGRAY, None)
    o_surf, o_surfrect = FONT.render('O', DARKGRAY, None)                
    
    draw_board(displaysurf = DISPLAYSURF)

    while not game_over:
        # Event handler
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            board, game_over, winner = mouse_clicked(in_board = board, mousex = mousex, mousey = mousey)
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            
        draw_tiles( displaysurf = DISPLAYSURF
                    ,in_board = board
                    ,x_surf = x_surf
                    ,x_surfrect = x_surfrect
                    ,o_surf = o_surf
                    ,o_surfrect = o_surfrect )
            
        pygame.display.update()
    print(winner, "wins!")

if __name__ == '__main__': 
    while True:
        main()