import pygame          #Used for displaying the game
from Settings import * #A separate python file that holds many constants to do with pygame
from ExitHole import * #A separate python file that holds the class for the exit hole

#A class to make tile maps for the rooms and draw them on the screen
class TileMap(pygame.sprite.Sprite):
    def __init__(self, roomSpriteSheet, tileMap, scale, roomObject):          #Initialising function that is ran when a new TileMap object is made
        super().__init__()                                                    #Takes initialisation information for pygame sprie objects
        self.file = open(tileMap, mode = "r")                                 #Opens the .txt file that maps out the tile locations for the room being displayed on the screen
        self.tiles = pygame.image.load(roomSpriteSheet)                       #Loads the sprite sheet image that is used to make the rooms
        self.tileSize = 100 * scale                                           #Defines the size of each square tile in each direction
        self.spriteSheetSize = (6 * self.tileSize, 4 * self.tileSize)         #Defines the size of the sprite sheet with the tiles on it
        self.tiles = pygame.transform.scale(self.tiles, self.spriteSheetSize) #Scales the sprite sheet up or down to the user's needs
        self.roomObject = roomObject                                          #Holds the room that is being created
        
    #A function that makes a 2D Array for the tile map
    def loadTileMap(self,isExitRoom):

        #Makes a 4x4 2D Array for the tile map
        tileMap = []
        for row in range(4):
            tileMap.append([])
            for column in range(4):
                tileMap[row].append("")

        for x in range(4):
            line = self.file.readline()    #Reads the next line in the .txt file
            for y in range(4):
                #Converts the character symbol in the .txt file into the coordinates and size of the tile it represents in the format of a tuple
                if line[y] == "0":
                    tileMap[x][y] = (0 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "1":
                    tileMap[x][y] = (1 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "2":
                    tileMap[x][y] = (2 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "3":
                    tileMap[x][y] = (3 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "4":
                    tileMap[x][y] = (4 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "5":
                    tileMap[x][y] = (5 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "6":
                    tileMap[x][y] = (0 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "7":
                    tileMap[x][y] = (1 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "8":
                    tileMap[x][y] = (2 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "9":
                    tileMap[x][y] = (3 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "A":
                    tileMap[x][y] = (4 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "B":
                    tileMap[x][y] = (5 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "C":
                    tileMap[x][y] = (0 * self.tileSize,2 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "D":
                    tileMap[x][y] = (1 * self.tileSize,2 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "E":
                    tileMap[x][y] = (2 * self.tileSize,2 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "F":
                    tileMap[x][y] = (3 * self.tileSize,2 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "G":
                    tileMap[x][y] = (4 * self.tileSize,2 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "H":
                    tileMap[x][y] = (0 * self.tileSize,3 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "I":
                    tileMap[x][y] = (1 * self.tileSize,3 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "J":
                    tileMap[x][y] = (2 * self.tileSize,3 * self.tileSize,self.tileSize,self.tileSize)
                if line[y] == "K":
                    tileMap[x][y] = (3 * self.tileSize,3 * self.tileSize,self.tileSize,self.tileSize)

                #Checks if there is a box in the room
                if self.roomObject.boxPresent[0] == True:
                    #Changes the tiles to the open box ones if the box is open
                    if self.roomObject.boxPresent[1] == True:
                        if x == 1 and y == 1:
                            tileMap[x][y] = (2 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 1 and y == 2:
                            tileMap[x][y] = (3 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 2 and y == 1:
                            tileMap[x][y] = (2 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 2 and y == 2:
                            tileMap[x][y] = (3 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                    #Changes the tiles to the closed box ones if the box is closed
                    else:
                        if x == 1 and y == 1:
                            tileMap[x][y] = (4 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 1 and y == 2:
                            tileMap[x][y] = (5 * self.tileSize,0 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 2 and y == 1:
                            tileMap[x][y] = (4 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)
                        elif x == 2 and y == 2:
                            tileMap[x][y] = (5 * self.tileSize,1 * self.tileSize,self.tileSize,self.tileSize)

        self.roomImage = pygame.Surface((4 * self.tileSize,4 * self.tileSize)) #Creates a new surface to store the room's finished image

        #Draws the tiles onto the surface using the tile map and loaded sprite sheet
        for x in range(4):
            for y in range(4):
                location = (y * self.tileSize, x * self.tileSize)
                self.roomImage.blit(self.tiles, location, tileMap[x][y])

        #Draws the exit hole if the current room is the exit room
        if isExitRoom == True:
            hole = ExitHole("Assets/MiscellaneousGraphics.png")
            hole.draw(self.roomImage,self.tileSize / 100)

    #A function that draws the room image onto the screen
    def draw(self, screen):
        screen.blit(self.roomImage, (0,0))
