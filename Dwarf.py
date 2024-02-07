import pygame
from pygame.locals import *

class Dwarf(pygame.sprite.Sprite):
    def __init__(self, dwarfSpriteSheet):                      #Initialising function that is ran when a new Dwarf object is made
        super().__init__()                                     #Takes initialisation information for pygame sprie objects
        self.height = 55                                       #Defines the height in pixels of the dwarf sprite in the sprite sheet
        self.width = 45                                        #Defines the width in pixels of the dwarf sprite in the sprite sheet
        self.x = 200 - int(self.width / 2)                     #Defines the x coordinate on the screen that the dwarf starts at (in this case the centre of the screen)
        self.y = 200 - int(self.height / 2)                    #Defines the y coordinate on the screen that the dwarf starts at (in this case the centre of the screen)
        self.speed = 3                                         #Defines how many pixels the dwarf moves when it moves
        self.frame = 0                                         #Defines which frame in the dwarf's animation it currently is
        self.state = 0                                         #Defines which state of animation the dwarf currently is
        self.buffer = 0                                        #Defines the space left between each dwarf sprite in the sprite sheet
        self.spriteSheet = pygame.image.load(dwarfSpriteSheet) #Loads the sprite sheet for the dwarf

    #A procedure to update where on the screen the dwarf is
    def updatePosition(self, roomID):
        #Sets the dwarf's state to its idle state of the same direction
        if self.state < 4:
            self.state += 4

        #Makes a list of all the keys that are currently being pressed
        pressedKeys = pygame.key.get_pressed()

        #Variables that hold if the dwarf has been moved in a certain direction this frame (false by default)
        movedLeft = False
        movedRight = False
        movedUp = False
        movedDown = False

        #When the room the dwarf is in has a door going up
        if roomID[0] == "1":
            #If the dwarf is in between the door's frame, then it can move up all the way to the top of the screen
            if self.x > 120 and self.x < 280 - self.width and self.y > 0 and pressedKeys[K_w] and movedUp == False:
                self.y -= self.speed #Moves upwards
                self.state = 1       #Changes it's state to moving upwards
                movedUp = True       #Tracks that the dwarf has been moved up this frame

            #If the dwarf is in the upwards doorway
            if self.y < 20:
                #If the dwarf tries to move left into the wall, it corrects it's position to where they are in bounds
                if self.x < 120 and self.x >= 120 - self.speed and pressedKeys[K_a]:
                    self.x = 120

                #If the dwarf tries to move right into the wall, it corrects it's position to where they are in bounds   
                if self.x > 280 - self.width and self.x <= 280 - self.width + self.speed and pressedKeys[K_d]:
                    self.x = 280 - self.width

        #When the room the dwarf is in has a door going right
        if roomID[1] == "1":
            #If the dwarf is in between the door's frame, then it can move up all the way to the right of the screen
            if self.y > 120 and self.y < 280 - self.height and self.x < 400 - self.width and pressedKeys[K_d] and movedRight == False:
                self.x += self.speed #Moves right
                self.state = 2       #Changes it's state to moving right
                movedRight = True    #Tracks that the dwarf has moved right this frame

            #If the dwarf is in the right side doorway
            if self.x > 400 - self.width - 20:
                #If the dwarf tries to move up into the wall, it corrects it's position to where they are in bounds
                if self.y < 120 and self.y >= 120 - self.speed and pressedKeys[K_w]:
                    self.y = 120

                #If the dwarf tries to move down into the wall, it corrects it's position to where they are in bounds
                if self.y > 280 - self.height and self.y <= 280 - self.height + self.speed and pressedKeys[K_s]:
                    self.y = 280 - self.height

        #When the room the dwarf is in has a door going down         
        if roomID[2] == "1":
            #If the dwarf is in between the door's frame, then it can move up all the way to the bottom of the screen
            if self.x > 120 and self.x < 280 - self.width and self.y < 400 - self.height and pressedKeys[K_s] and movedDown == False:
                self.y += self.speed #Moves down
                self.state = 0       #Changes it's state to moving downwards
                movedDown = True     #Tracks that the dwarf has moved down this frame

            #If the dwarf is in the bottom side doorway
            if self.y > 400 - self.height - 20:
                #If the dwarf tries to move left into the wall, it corrects it's position to where they are in bounds
                if self.x < 120 and self.x >= 120 - self.speed and pressedKeys[K_a]:
                    self.x = 120

                #If the dwarf tries to move right into the wall, it corrects it's position to where they are in bounds
                if self.x > 280 - self.width and self.x <= 280 - self.width + self.speed and pressedKeys[K_d]:
                    self.x = 280 - self.width

        #When the room the dwarf is in has a door going left
        if roomID[3] == "1":
            #If the dwarf is in between the door's frame, then it can move up all the way to the left of the screen
            if self.y > 120 and self.y < 280 - self.height and self.x > 0 and pressedKeys[K_a] and movedLeft == False:
                self.x -= self.speed #Moves left
                self.state = 3       #Changes it's state to moving left
                movedLeft = True     #Tracks that the dwarf has moved left this frame

            #If the dwarf is in the left side doorway
            if self.x < 20:
                #If the dwarf tries to move up into the wall, it corrects it's position to where they are in bounds
                if self.y < 120 and self.y >= 120 - self.speed and pressedKeys[K_w]:
                    self.y = 120

                #If the dwarf tries to move down into the wall, it corrects it's position to where they are in bounds
                if self.y > 280 - self.height and self.y <= 280 - self.height + self.speed and pressedKeys[K_s]:
                    self.y = 280 - self.height

        #If the dwarf is in bounds and hasn't already moved up, it can move up
        if self.y > 0 + 20 and pressedKeys[K_w] and movedUp == False:
            self.y -= self.speed
            self.state = 1
            movedUp = True

        #If the dwarf is in bounds and hasn't already moved down, it can move down
        if self.y < 400 - self.height - 20 and pressedKeys[K_s] and movedDown == False:
            self.y += self.speed
            self.state = 0
            movedDown = True

        #If the dwarf is in bounds and hasn't already moved right, it can move right
        if self.x < 400 - self.width - 20 and pressedKeys[K_d] and movedRight == False:
            self.x += self.speed
            self.state = 2
            movedRight = True

        #If the dwarf is in bounds and hasn't already moved left, it can move left
        if self.x > 0 + 20 and pressedKeys[K_a] and movedLeft == False:
            self.x -= self.speed
            self.state = 3
            movedLeft = True

    #A procedure to draw the dwarf to the screen
    def draw(self, screen, count, scale):
        if count == 0:           #Count is used to allow the animation to slow down to be around 7.5 times per second when otherwise it would be 60 times per second
            self.frame += 1      #Moves to the next frame in the animation of the dwarf
            #If the animation is finished, it goes back to the first frame of the animation
            if self.frame == 4:  
                self.frame = 0

        #Takes the current frame of the dwarf from the sprite sheet
        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width, self.height))
        self.imageSize = (self.width * scale, self.height * scale)      #Makes a tuple that determines how large the dwarf image is supposed to be when scaled up
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the dwarf to the screen
        self.location = (self.x * scale, self.y * scale)                #Makes a tuple that determines the dwarf's location on the screen
        screen.blit(self.image,self.location)                           #Draws the dwarf onto the screen at the given location
