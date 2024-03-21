import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things

class Map(pygame.sprite.Sprite):
    def __init__(self, mapSpriteSheet):
        super().__init__()                                                      #Takes initialisation information for pygame sprie objects
        self.width = 400                                                        #Defines the width of the overall map
        self.height = 400                                                       #Defines the height of the overall map
        self.tileSize = 50                                                      #Defines the size of each individual tile in the map
        self.spriteSheet = pygame.image.load(mapSpriteSheet)                    #Loads the sprite sheet that the map parts are on
        self.image = pygame.Surface((400,400))                                  #Creates a surface for the map to be drawn onto
        self.image.blit(self.spriteSheet.subsurface(Rect(0,200,400,400)),(0,0)) #Takes the part of the sprite sheet that referrs to the map's frame and adds it to the surface

    def loadMap(self,currentFloorLayout,currentRoomLocation):
        workingRoomLocation = [1,1] #Gives the location of the top left room of the floor
        for y in range(7):
            for x in range(7):
                
                workingRoomObject = currentFloorLayout[workingRoomLocation[0]][workingRoomLocation[1]] #The room object of the section of map being worked on

                #If there is a room at the working location
                if workingRoomObject != 1 and workingRoomObject != 0:
                    doorsCoordinates = [400,300] #Defines the location of the doors on the sprite sheet
                    doorsDimentions = [50,50]    #Defines the dimentions of the doors on the sprite sheet
                    yBuffer = 0                  #Used to correct the location the doors are placed on the map
                    xBuffer = 0                  #Used to correct the location the doors are placed on the map

                    #If the room has no north door, it wont draw the north door part of the tile
                    if workingRoomObject.northConnection == False:
                        doorsCoordinates[1] += 8
                        doorsDimentions[1] -= 8
                        yBuffer += 8

                    #If the room has no east door, it wont draw the east door part of the tile
                    if workingRoomObject.eastConnection == False:
                        doorsDimentions[0] -= 8

                    #If the room has no south door, it wont draw the south door part of the tile
                    if workingRoomObject.southConnection == False:
                        doorsDimentions[1] -= 8

                    #If the room has no west door, it wont draw the west door part of the tile
                    if workingRoomObject.westConnection == False:
                        doorsCoordinates[0] += 8
                        doorsDimentions[0] -= 8
                        xBuffer += 8

                    #Blits the doors of the working room to the map surface
                    self.location = (25 + xBuffer + (x * self.tileSize), 25 + yBuffer + (y * self.tileSize))
                    self.doors = self.spriteSheet.subsurface(Rect(doorsCoordinates[0],doorsCoordinates[1],doorsDimentions[0],doorsDimentions[1]))
                    self.image.blit(self.doors,self.location)

                    #Adds the dwarf icon if the worked room is the player's current room
                    if workingRoomLocation == currentRoomLocation:
                        self.image.blit(self.spriteSheet.subsurface(Rect(412,262,26,26)),(37 + (x * self.tileSize), 37 + (y * self.tileSize)))

                    #Adds the entrance room icon if the worked room is the entrance room
                    elif workingRoomLocation == [4,4]:
                        self.image.blit(self.spriteSheet.subsurface(Rect(412,212,26,26)),(37 + (x * self.tileSize), 37 + (y * self.tileSize)))

                    #Adds the exit room icon if the worked room is the exit room
                    elif workingRoomObject.isExitRoom == True:
                        self.image.blit(self.spriteSheet.subsurface(Rect(462,212,26,26)),(37 + (x * self.tileSize), 37 + (y * self.tileSize)))

                    #Adds the normal room icon if the worked room is a normal  room
                    else:
                        self.image.blit(self.spriteSheet.subsurface(Rect(462,262,26,26)),(37 + (x * self.tileSize), 37 + (y * self.tileSize)))

                #Moves on to the next room in the floor
                if x != 6:
                    workingRoomLocation[0] += 1

                else:
                    workingRoomLocation[0] -= 6

            if y != 6:
                workingRoomLocation[1] += 1

            else:
                workingRoomLocation[1] -= 6

    def displayMap(self, screen, scale):
        self.imageSize = (self.width * scale, self.height * scale)      #Defines the true size of the map
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the map to the screen
        screen.blit(self.image,(0,0))                                   #Draws the map onto the screen

        pygame.display.update() #Updates the game screen to show the map

        keyReleased = False #Determines if the m key has stopped being pressed or not
        showMap = True      #Determines if the map should be being displayed or not

        #Keeps the map displayed until the player has released the m key for a second time
        while showMap:
            for event in pygame.event.get():
                if keyReleased == False and event.type == KEYUP and event.key == K_m:
                    keyReleased = True
                elif keyReleased == True and event.type == KEYUP and event.key == K_m:
                    showMap = False
                    running = True

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        pygame.quit()

                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    

        return running

    
                    
