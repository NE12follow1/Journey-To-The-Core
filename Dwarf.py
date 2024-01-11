import pygame
from pygame.locals import *

class Dwarf(pygame.sprite.Sprite):
    def __init__(self, dwarfSpriteSheet,scale,speed):
        super().__init__()
        self.height = 55
        self.width = 45
        self.x = 200 - int(self.width / 2)
        self.y = 200 - int(self.height / 2)
        self.speed = 3 * scale
        self.frame = 0
        self.state = 0
        self.buffer = 0
        self.spriteSheet = pygame.image.load(dwarfSpriteSheet)
        self.image = self.spriteSheet.subsurface(Rect(self.x, self.y, self.width, self.height))

    def updatePosition(self, roomID):
        if self.state < 4:
            self.state += 4

        pressedKeys = pygame.key.get_pressed()

        movedLeft = False
        movedRight = False
        movedUp = False
        movedDown = False

        if roomID[0] == "1":
            if self.x > 120 and self.x < 280 - self.width:
                if self.y > 0 and pressedKeys[K_w] and movedUp == False:
                    self.y -= self.speed
                    self.state = 1
                    movedUp = True
                    
            if self.y < 20:
                if self.x < 120 and self.x >= 120 - self.speed and pressedKeys[K_a]:
                    self.x = 120
                    
                if self.x > 280 - self.width and self.x <= 280 - self.width + self.speed and pressedKeys[K_d]:
                    self.x = 280 - self.width
                
        if roomID[1] == "1":
            if self.y > 120 and self.y < 280 - self.height:
                if self.x < 400 - self.width and pressedKeys[K_d] and movedRight == False:
                    self.x += self.speed
                    self.state = 2
                    movedRight = True

            if self.x > 400 - self.width - 20:
                if self.y < 120 and self.y >= 120 - self.speed and pressedKeys[K_w]:
                    self.y = 120
                    
                if self.y > 280 - self.height and self.y <= 280 - self.height + self.speed and pressedKeys[K_s]:
                    self.y = 280 - self.height
                    
        if roomID[2] == "1":
            if self.x > 120 and self.x < 280 - self.width:
                if self.y < 400 - self.height and pressedKeys[K_s] and movedDown == False:
                    self.y += self.speed
                    self.state = 0
                    movedDown = True
                    
            if self.y > 400 - self.height - 20:
                if self.x < 120 and self.x >= 120 - self.speed and pressedKeys[K_a]:
                    self.x = 120
                    
                if self.x > 280 - self.width and self.x <= 280 - self.width + self.speed and pressedKeys[K_d]:
                    self.x = 280 - self.width

        if roomID[3] == "1":
            if self.y > 120 and self.y < 280 - self.height:
                if self.x > 0 and pressedKeys[K_a] and movedLeft == False:
                    self.x -= self.speed
                    self.state = 3
                    movedLeft = True

            if self.x < 20:
                if self.y < 120 and self.y >= 120 - self.speed and pressedKeys[K_w]:
                    self.y = 120
                    
                if self.y > 280 - self.height and self.y <= 280 - self.height + self.speed and pressedKeys[K_s]:
                    self.y = 280 - self.height
                    
        if self.y > 0 + 20 and pressedKeys[K_w] and movedUp == False:
            self.y -= self.speed
            self.state = 1
            movedUp = True

        if self.y < 400 - self.height - 20 and pressedKeys[K_s] and movedDown == False:
            self.y += self.speed
            self.state = 0
            movedDown = True
            
        if self.x < 400 - self.width - 20 and pressedKeys[K_d] and movedRight == False:
            self.x += self.speed
            self.state = 2
            movedRight = True

        if self.x > 0 + 20 and pressedKeys[K_a] and movedLeft == False:
            self.x -= self.speed
            self.state = 3
            movedLeft = True
            
    def draw(self, screen, count, scale):
        if count == 0:
            self.frame += 1
            if self.frame == 4:
                self.frame = 0

        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width - self.buffer, self.height - self.buffer))
        self.imageSize = (self.width * scale, self.height * scale)
        self.image = pygame.transform.scale(self.image, self.imageSize)
        self.location = (self.x * scale, self.y * scale)
        screen.blit(self.image,self.location)
