import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds many constants to do with pygame

#Initialises the pygame library and the clock used to determine the fps (frames per second) of the game
pygame.init()
clock = pygame.time.Clock()

#Creates a pygame screen in fullscreen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#Gives the pygame screen a caption
pygame.display.set_caption("Journey To The Core")

#Starts the main game loop
while True:

    #Checks if the user presses the escape key to quit the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    #Fills in the screen with black 
    screen.fill((0,0,0))

    #Used to set the game to the fps found in the settings file
    clock.tick(fps)
