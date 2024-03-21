import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things

class ExitHole(pygame.sprite.Sprite):
    def __init__(self, holeSpriteSheet):
        super().__init__()                                            #Takes initialisation information for pygame sprie objects
        self.width = 104                                              #Defines the width of the hole
        self.height = 54                                              #Defines the height of the hole
        self.x = 148                                                  #Defines the x coordinate of the hole on the screen
        self.y = 173                                                  #Defines the y coordinate of the hole on the screen
        self.spriteSheet = pygame.image.load(holeSpriteSheet)         #Loads the sprite sheet that the hole is on
        self.image = self.spriteSheet.subsurface(Rect(248,73,104,54)) #Takes the part of the sprite sheet that referrs to the hole

    def draw(self, screen, scale):
        self.imageSize = (self.width * scale, self.height * scale)      #Defines the true size of the hole 
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the hole to the screen
        self.location = (self.x * scale, self.y * scale)                #Makes a tuple that determines the hole's location on the screen
        screen.blit(self.image,self.location)                           #Draws the hole onto the screen at the given location
