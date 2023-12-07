import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds many constants to do with pygame

#Initialises the pygame library
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Journey To The Core")

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.fill((0,0,0))

    clock.tick(fps)

    screen.fill((0,0,0))

    pygame.clock.tick(fps)
