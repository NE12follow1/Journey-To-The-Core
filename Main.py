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
screen = pygame.display.set_mode((400 * scale,400 * scale))
pygame.display.set_caption("Journey To The Core")

running = True #Used to determine if the user has quit the program or not
count = 0      #Used to stall the dwarf's animation

currentFloorLayout = NewFloor("Large")  #Creates a 2D array room layout using the imported module
showFloorLayout(currentFloorLayout)
currentRoomLocation = [4,4]
dwarf = Dwarf("Assets/SpriteSheet.png",scale) #Initialises the dwarf object

font = pygame.font.SysFont("Arial" , 18 , bold = True)

def fps_counter():
    truefps = str(int(clock.get_fps()))
    fps_t = font.render(truefps , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))

#Starts the main game loop
while running:
    #Resets count once it reaches a value of 8
    if count == 8:
            count = 0

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

    #Moves the character to the next room if they go through the door to that room
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
        
    currentRoomObject = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]]                          #Gets the room object of the room the player is currently in
    currentRoomMap = TileMap("Assets/TileSpriteSheet.png","RoomMaps/{}.txt".format(currentRoomObject.roomID),scale) #Makes a tile map object of the type of room the player is currently in
    currentRoomTiles = currentRoomMap.loadTileMap(scale)                                                            #Makes the tile map for the tile map object
    currentRoomMap.draw(currentRoomTiles,screen,scale)                                                              #Draws the room on the screen

    dwarf.updatePosition(currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].roomID)                 #Updates the position of the dwarf character on the screen
    dwarf.draw(screen,count,scale)                                                                                  #Draws the dwarf character onto the screen

    fps_counter()                                                                                                   #Calls function to draw the current fps of the screen onto the screen
    
    pygame.display.update()                                                                                         #Updates the screen's graphics 

    #Used to set the game to the fps found in the settings file
    clock.tick(fps)
    count += 1
