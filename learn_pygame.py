"""Importing pygame and sys"""
import sys
import pygame
from pygame.locals import *

pygame.init()

# (400, 600) is the size of the window, and the maximum x and y coordinates
DISPLAYSURF = pygame.display.set_mode((400, 600))

# Why is the pygame.display.update() not in the for loop?
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()