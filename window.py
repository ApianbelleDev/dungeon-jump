import pygame
import enum 

# constants (will put in seperate file later)
SCREEN_WIDTH       = 160
SCREEN_HEIGHT      = 144
WINDOW_WIDTH       = SCREEN_WIDTH * 4
WINDOW_HEIGHT      = SCREEN_HEIGHT * 4

# game state
class gameState():
    LOGO     = 0
    TITLE    = 1
    GAME     = 2
    END      = 3
    curState = GAME

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT = the user pressed the X on their window, or an in-game exit button
            running = False

        screen.fill("black")

        # game loop here
        if gameState.curState == gameState.LOGO:
            pass # do nothing
        elif gameState.curState == gameState.TITLE:
            pass
        elif gameState.curState == gameState.GAME:
            pass 
        elif gameState.curState == gameState.END:
            pass
