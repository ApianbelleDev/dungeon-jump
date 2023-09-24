import pygame

import defines

class player:
    x = defines.SCREEN_WIDTH / 2 - 8
    y = defines.SCREEN_HEIGHT / 2 - 16
    vx = 1
    vy = 1
    gravity = 0.1
    speed = 5
    jumpSpeed = 7
    onGround = False
    image = pygame.image.load("res/player.png")
    imageRect = image.get_rect()
    lives = 3
    coinsCollected = 0
