import pygame

class ExitHole(pygame.sprite.Sprite):
    def __init__(self, holeSpriteSheet):
        super().__init__()                                            #Takes initialisation information for pygame sprie objects
        self.width = 103                                              #Defines the width of the hole
        self.height = 53                                              #Defines the height of the hole
        self.x = 149                                                  #Defines the x coordinate of the hole on the screen
        self.y = 174                                                  #Defines the y coordinate of the hole on the screen
        self.spriteSheet = pygame.image.load(holeSpriteSheet)         #Loads the sprite sheet that the hole is on
        self.image = self.spriteSheet.subsurface(Rect(249,74,103,53)) #Takes the part of the sprite sheet that referrs to the hole

    def draw(self, screen, scale):
        self.imageSize = (self.width * scale, self.height * scale)      #Defines the true size of the hole 
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the hole to the screen
        self.location = (self.x * scale, self.y * scale)                #Makes a tuple that determines the hole's location on the screen
        screen.blit(self.image,self.location)                           #Draws the hole onto the screen at the given location

        
