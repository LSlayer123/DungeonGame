import pygame
from pygame.locals import *
import sys


# Initializing PyGame
pygame.init()

# Setting up the dimensions of the window
world = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('dungeon.png'))
clock = pygame.time.Clock()


# Class for main player units
class Unit(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Draw(self, win):
        pygame.draw.rect(world, (0, 128, 255), pygame.Rect(self.x, self.y, 60, 60))


# Function for redrawing world
def Redraw_Screen():
    world.fill((255, 255, 255))

    Box.Draw(world)

    pygame.display.update()


Box = Unit(30, 20, 60, 60)


# Main Menu Function
def Main_Menu():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                sys.exit()

        keystroke = pygame.key.get_pressed()
        if keystroke[K_UP] and Box.y > 0:
            Box.y -= 5
        if keystroke[K_DOWN] and Box.y < 720 - 60:
            Box.y += 5
        if keystroke[K_LEFT] and Box.x > 0:
            Box.x -= 5
        if keystroke[K_RIGHT] and Box.x < 1080 - 60:
            Box.x += 5
        if keystroke[pygame.K_RETURN]:
            Box.x = 30
            Box.y = 20

        Redraw_Screen()
        clock.tick(60)


# Function for standard game state
def Game():
    pass


# Function for options menu
def Options():
    pass


Main_Menu()
