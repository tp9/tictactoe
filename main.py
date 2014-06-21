import pygame
from pygame.locals import *


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode( (400, 300) )
    pygame.display.set_caption("Tic-Tac-Toe")
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__': main()