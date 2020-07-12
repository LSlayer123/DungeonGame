import pickle
import random
import pygame
import os

running = True
clock = pygame.time.Clock()
x = 30
y = 20

# Initializing PyGame
pygame.init()

# Setting up the dimensions of the window
world = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('dungeon.png'))


# Main loop for the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keystroke = pygame.key.get_pressed()
    if keystroke[pygame.K_UP] and y > 0:
        y -= 5
    if keystroke[pygame.K_DOWN] and y < 600 - 60:
        y += 5
    if keystroke[pygame.K_LEFT] and x > 0:
        x -= 5
    if keystroke[pygame.K_RIGHT] and x < 800 - 60:
        x += 5
    if keystroke[pygame.K_RETURN]:
        x = 30
        y = 20

    world.fill((255, 255, 255))
    color = (0, 128, 255)
    pygame.draw.rect(world, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)

