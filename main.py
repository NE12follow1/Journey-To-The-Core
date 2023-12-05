import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds the 

#Initialises the pygame library
pygame.init()

screen = pygame.display.set_mode([width,height])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))
