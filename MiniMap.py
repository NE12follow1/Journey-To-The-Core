import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things

class MiniMap(pygame.sprite.Sprite):
    def __init__(self, miniMapSpriteSheet):
        super().__init__()                                                      #Takes initialisation information for pygame sprie objects
        self.width = 100                                                        #Defines the width of the overall mini-map
        self.height = 100                                                       #Defines the height of the overall mini-map
        self.x = 295                                                            #Defines the x coordinate of the overall mini-map on the screen
        self.y = 5                                                              #Defines the y coordinate of the overall mini-map on the screen
        self.tileSize = 28                                                      #Defines the size of each individual tile in the mini-map
        self.spriteSheet = pygame.image.load(miniMapSpriteSheet)                #Loads the sprite sheet that the mini-map parts are on
        self.image = pygame.Surface((100,100))                                  #Creates a surface for the mini-map to be drawn onto
        self.image.blit(self.spriteSheet.subsurface(Rect(400,0,100,100)),(0,0)) #Takes the part of the sprite sheet that referrs to the mini-map's frame and adds it to the surface

    def loadMiniMap(self, currentFloorLayout, currentRoomLocation):
        workingRoomLocation = [currentRoomLocation[0] - 1, currentRoomLocation[1] - 1] #Gives the location of the top left room of the 3x3 rooms around the player
        for y in range(3):
            for x in range(3):
                
                workingRoomObject = currentFloorLayout[workingRoomLocation[0]][workingRoomLocation[1]] #The room object of the section of mini-map being worked on

                #If there is a room at the working location
                if workingRoomObject != 1 and workingRoomObject != 0:
                    doorsCoordinates = [501,61] #Defines the location of the doors on the sprite sheet
                    doorsDimentions = [28,28]   #Defines the dimentions of the doors on the sprite sheet
                    yBuffer = 0                 #Used to correct the location the doors are placed on the mini-map
                    xBuffer = 0                 #Used to correct the location the doors are placed on the mini-map

                    #If the room has no north door, it wont draw the north door part of the tile
                    if workingRoomObject.northConnection == False:
                        doorsCoordinates[1] += 4
                        doorsDimentions[1] -= 4
                        yBuffer += 4

                    #If the room has no east door, it wont draw the east door part of the tile
                    if workingRoomObject.eastConnection == False:
                        doorsDimentions[0] -= 4

                    #If the room has no south door, it wont draw the south door part of the tile
                    if workingRoomObject.southConnection == False:
                        doorsDimentions[1] -= 4

                    #If the room has no west door, it wont draw the west door part of the tile
                    if workingRoomObject.westConnection == False:
                        doorsCoordinates[0] += 4
                        doorsDimentions[0] -= 4
                        xBuffer += 4

                    #Blits the doors of the working room to the mini-map surface
                    self.location = (8 + xBuffer + (x * self.tileSize), 8 + yBuffer + (y * self.tileSize))
                    self.rectObject = Rect(doorsCoordinates[0],doorsCoordinates[1],doorsDimentions[0],doorsDimentions[1])
                    self.doors = self.spriteSheet.subsurface(Rect(doorsCoordinates[0],doorsCoordinates[1],doorsDimentions[0],doorsDimentions[1]))
                    self.image.blit(self.doors,self.location)

                    #Adds the dwarf icon if the worked room is the player's current room
                    if workingRoomLocation == currentRoomLocation:
                        self.image.blit(self.spriteSheet.subsurface(Rect(507,37,16,16)),(14 + (x * self.tileSize), 14 + (y * self.tileSize)))

                    #Adds the entrance room icon if the worked room is the entrance room
                    elif workingRoomLocation == [4,4]:
                        self.image.blit(self.spriteSheet.subsurface(Rect(507,7,16,16)),(14 + (x * self.tileSize), 14 + (y * self.tileSize)))

                    #Adds the exit room icon if the worked room is the exit room
                    elif workingRoomObject.isExitRoom == True:
                        self.image.blit(self.spriteSheet.subsurface(Rect(537,7,16,16)),(14 + (x * self.tileSize), 14 + (y * self.tileSize)))

                    #Adds the normal room icon if the worked room is a normal  room
                    else:
                        self.image.blit(self.spriteSheet.subsurface(Rect(537,37,16,16)),(14 + (x * self.tileSize), 14 + (y * self.tileSize)))

                #Moves on to the next room in the 3x3 set of rooms around the player
                if x != 2:
                    workingRoomLocation[0] += 1

                else:
                    workingRoomLocation[0] -= 2

            if y != 2:
                workingRoomLocation[1] += 1

            else:
                workingRoomLocation[1] -= 2

    def draw(self, screen, scale):
        self.imageSize = (self.width * scale, self.height * scale)      #Defines the true size of the mini-map
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the mini-map to the screen
        self.location = (self.x * scale, self.y * scale)                #Makes a tuple that determines the mini-map's location on the screen
        screen.blit(self.image,self.location)                           #Draws the mini-map onto the screen at the given location

                
                        
