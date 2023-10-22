"""Importing pygame and sys"""
import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramesPerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)

# (400, 600) is the size of the window, and the maximum x and y coordinates. Width is 400 and height is 600.
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game One")

class Enemy(pygame.sprite.Sprite):
    def _init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 400)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    #def move(self):
        

# Why is the pygame.display.update() not in the for loop?
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()