import pygame                           #Used for displaying the game
import random                           #Used for anything that requires randomness
from pygame.locals import *             #Used to reduce the need for typing pygame. for certain things 
from Settings import *                  #A separate python file that holds many constants to do with pygame
from RoomDistributionAlgorithm import * #A separate python file that creates the floor layout
from Dwarf import *
from TileMap import *
    
#Initialises the pygame library and the clock used to determine the fps (frames per second) of the game
pygame.init()
clock = pygame.time.Clock()

#Creates a pygame screen abd gives it a caption
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Journey To The Core")

running = True #Used to determine if the user has quit the program or not
count = 0      #Used to reduce the rate that the Dwarf sprite goes through the frames of it's animation

currentFloorLayout = NewFloor("Large")  #Creates a 2D array room layout using the imported module
showFloorLayout(currentFloorLayout)
currentRoomLocation = [4,4]
dwarf = Dwarf("Assets/SpriteSheet.png")

#Starts the main game loop
while running:
    if count == 9:
        count = 0

    #Checks if the user presses the escape key to quit the game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
        if event.type == QUIT:
            running = False
            pygame.quit()

    #Fills in the screen with black 
    screen.fill((0,0,0))

    if dwarf.x <= 0:
        currentRoomLocation[0] -= 1
        dwarf.x = 400 - dwarf.width - 20

    if dwarf.x + dwarf.width >= 400:
        currentRoomLocation[0] += 1
        dwarf.x = 0 + 20

    if dwarf.y <= 0:
        currentRoomLocation[1] -= 1
        dwarf.y = 400 - dwarf.height - 20

    if dwarf.y + dwarf.height >= 400:
        currentRoomLocation[1] += 1
        dwarf.y = 0 + 20
        
    currentRoomObject = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]]
    currentRoomMap = TileMap("Assets/TileSpriteSheet.png","RoomMaps/{}.txt".format(currentRoomObject.roomID))
    currentRoomTiles = currentRoomMap.loadTileMap()
    currentRoomMap.draw(currentRoomTiles,screen)

    dwarf.updatePosition(currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].roomID)
    dwarf.draw(screen,count)
    
    pygame.display.update()

    #Used to set the game to the fps found in the settings file
    clock.tick(fps)
    count += 1
