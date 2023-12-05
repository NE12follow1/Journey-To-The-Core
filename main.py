import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
import tkinter as tk        #Used primarily for getting the width and height of the screen
from settings import *      #A separate python file that holds the 

#Initialises the pygame library
pygame.init()

screen = pygame.display.set_mode([width,height])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
