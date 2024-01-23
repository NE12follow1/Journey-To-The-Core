import pygame                           #Used for displaying the game
import random                           #Used for anything that requires randomness
from pygame.locals import *             #Used to reduce the need for typing pygame. for certain things 
from Settings import *                  #A separate python file that holds many constants to do with pygame
from RoomDistributionAlgorithm import * #A separate python file that creates the floor layout
from Dwarf import *                     #A separate python file that handles the visuals of the player character and how they move around
from TileMap import *                   #A separate python file that is used to make a tile map for the screen and draws it to the screen

#Initialises the pygame library and the clock used to determine the fps (frames per second) of the game
pygame.init()
clock = pygame.time.Clock()

#Creates a pygame screen abd gives it a caption
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Journey To The Core")

running = True #Used to determine if the user has quit the program or not

#Starts the main game loop
while running:

    #Checks if the user presses the escape key to quit the game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
        if event.type == QUIT:
            running = False
            pygame.quit()

    #Fills in the screen with black 
    screen.fill((0,0,0))

    currentRoomMap = TileMap("Assets/TileSpriteSheet.png","RoomMaps/{}.txt".format("1101")) #Makes a tile map object of the type of room the player is currently in
    currentRoomTiles = currentRoomMap.loadTileMap()                                         #Makes the tile map for the tile map object
    currentRoomMap.draw(currentRoomTiles,screen)                                            #Draws the room to the screen
    
    #Updates the screen's graphics
    pygame.display.update() 

    #Used to set the game to the fps found in the settings file
    clock.tick(fps)
