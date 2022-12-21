import random
import pygame
from pygame.locals import *
pygame.init()

HOEHE = 500
BREITE = 1000
RED = (255, 0, 0)

screen = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Parking System Control")

screen.fill(RED)

#Erstelle Parkplätze
w = 50
h = 25


running = True

while running:
    screen.fill(RED)


    pygame.display.update()