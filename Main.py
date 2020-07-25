import pickle
import random
import pygame
from pygame.locals import *
import os
import sys

clock = pygame.time.Clock()


# Initializing PyGame
pygame.init()

# Setting up the dimensions of the window
world = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('dungeon.png'))


# Main Menu Function
def Main_Menu():
    x = 30
    y = 20
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()

        keystroke = pygame.key.get_pressed()
        if keystroke[K_UP] and y > 0:
            y -= 5
        if keystroke[K_DOWN] and y < 720 - 60:
            y += 5
        if keystroke[K_LEFT] and x > 0:
            x -= 5
        if keystroke[K_RIGHT] and x < 1080 - 60:
            x += 5
        if keystroke[pygame.K_RETURN]:
            x = 30
            y = 20

        world.fill((255, 255, 255))
        color = (0, 128, 255)
        pygame.draw.rect(world, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()
        clock.tick(60)


# Function for standard game state
def Game():
    pass


# Function for options menu
def Options():
    pass


Main_Menu()
