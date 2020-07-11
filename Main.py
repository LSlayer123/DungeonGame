import pickle
import random
import pygame
import os

pygame.init()

world = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('dungeon.png'))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
