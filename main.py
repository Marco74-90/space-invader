import pygame
from pygame.locals import *

#Initialize pygame 
pygame.init()

#create the game window 
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Player

playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480


def player():
    screen.blit(playerImage,(playerX, playerY))


#Game Loop
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()