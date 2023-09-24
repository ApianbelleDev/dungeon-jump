import pygame

import defines
import player
# pygame setup
pygame.init()
screen = pygame.display.set_mode((defines.WINDOW_WIDTH, defines.WINDOW_HEIGHT))
scaleScreen = pygame.Surface((defines.SCREEN_WIDTH, defines.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT = the user pressed the X on their window, or an in-game exit button
            running = False

        screen.fill("black")

        # game loop here
        if defines.gameState.curState == defines.gameState.LOGO:
            pass # do nothing
        elif defines.gameState.curState == defines.gameState.TITLE:
            pass
        elif defines.gameState.curState == defines.gameState.GAME:
            # draw to an offscreen buffer
            scaleScreen.fill((143, 149, 114))
            scaleScreen.blit(player.player.image, player.player.imageRect)

            # scale the buffer, and draw it to the main surface
            pygame.transform.scale(scaleScreen, (defines.WINDOW_WIDTH, defines.WINDOW_HEIGHT), screen)
            pygame.display.flip()            
        elif defines.gameState.curState == defines.gameState.END:
            pass
