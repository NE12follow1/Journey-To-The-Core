import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds many constants to do with pygame

#Initialises the pygame library
pygame.init()

screen = pygame.display.set_mode((0,0),FULLSCREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))
