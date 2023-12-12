import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, aCharacterSpriteSheet):
        super().__init__()
        self.x = 0
        self.y = 0
        self.height = 80
        self.width = 80
        self.speed = 6
        self.frame = 0
        self.state = 0
        self.buffer = 15
        self.spriteSheet = pygame.image.load(aCharacterSpriteSheet)
        self.image = self.spriteSheet.subsurface(Rect(self.x, self.y, self.width, self.height))

    def updatePos(self):
        if self.state < 4:
            self.state += 4

        pressed_keys = pygame.key.get_pressed()

        if self.y > 0:
            if pressed_keys[K_w]:
                self.y += -self.speed
                self.state = 0
##        else:
##            if pressed_keys[K_w]:
##                self.y = 480 - self.height + 30
##                self.y += -self.speed
##                self.state = 0

        if self.y < 480 - self.height + 15:
            if pressed_keys[K_s]:
                self.y += self.speed
                self.state = 1
##        else:
##            if pressed_keys[K_s]:
##                self.y = 0
##                self.y += self.speed
##                self.state = 1

        if self.x < 480 - self.width + 30:
            if pressed_keys[K_d]:
                self.x += self.speed
                self.state = 2
        else:
            if currentLevel == level1:
                if pressed_keys[K_d]:
                    self.x = 0
                    self.x += self.speed
                    self.state = 2

        if self.x > 0 - 3:
            if pressed_keys[K_a]:
                self.x += -self.speed
                self.state = 3
        else:
            if currentLevel == level2:
                if pressed_keys[K_a]:
                    self.x = 480 - self.width + 30
                    self.x += -self.speed
                    self.state = 3

    def draw(self, window):
        self.frame += 1
        if self.frame == 8:
            self.frame = 0

        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width - self.buffer, self.height - self.buffer))
        window.blit(self.image,(self.x, self.y))
                    
class TileMap(pygame.sprite.Sprite):
    def __init__(self, aSpriteSheet, aMap):
        super().__init__()
        self.file = open(aMap, "r")
        self.tiles = pygame.image.load(aSpriteSheet)

    def loadMap(self):
        global level1, level2, currentLevel
        tileMap = []
        tileSize = 24
        for row in range(0,20):
            tileMap.append([])
            for column in range(0,20):
                tileMap[row].append("")
        
        for x in range(0,20):
            line = self.file.readline()
##            print(line)
            for y in range(0,20):
                if line[y] == "0":
                    tileMap[x][y] = (0,0,24,24)
                if line[y] == "6":
                    tileMap[x][y] = (0,48,24,24)
                if line[y] == "7":
                    tileMap[x][y] = (48,48,24,24)
                if line[y] == "8":
                    tileMap[x][y] = (48,0,24,24)
                #Left Side
                if line[y] == "4":
                    tileMap[x][y] = (0,24,24,24)
                #Right Side
                if line[y] == "5":
                    tileMap[x][y] = (48,24,24,24)
                #Top Side
                if line[y] == "1":
                    tileMap[x][y] = (24,0,24,24)
                #Bottom Side
                if line[y] == "3":
                    tileMap[x][y] = (24,48,24,24)
                #Middle
                if line[y] == "2":
                    tileMap[x][y] = (24,24,24,24)
                #Buildings
                if line[y] == "T":
                    tileMap[x][y] = (0,72,24,24)
                if line[y] == "Y":
                    tileMap[x][y] = (24,72,24,24)
                if line[y] == "X":
                    tileMap[x][y] = (48,72,24,24)

##        print(tileMap)
        return tileMap

    def draw(self, tileMap, window):
        for x in range(0,20):
            for y in range(0,20):
                window.blit(self.tiles, (y*24, x*24), tileMap[x][y])

def main():
    global level1, level2, currentLevel
    height = 480
    width = 480
    speed = 60
    FPS = 30
    clock = pygame.time.Clock()
    count = 0

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Legend of Link: New Beginnings")

    level1 = TileMap("overworldSmall.png","map2.txt")
    level2 = TileMap("overworldSmall.png","map3.txt")
    currentLevel = level1
    link = Player("80SpriteSheetNEW.png")
    tiles1 = level1.loadMap()
    tiles2 = level2.loadMap()

    while True:
        if link.x >= 480 - link.width + 30:
            if currentLevel == level1:
                currentLevel = level2
                link.x = 0
        if link.x <= 0 - 3:
            if currentLevel == level2:
                currentLevel = level1
                link.x = 480 - link.width + 30
        if currentLevel == level1:
            currentTiles = tiles1
        if currentLevel == level2:
            currentTiles = tiles2
        currentLevel.draw(currentTiles,window)

        link.updatePos()
        link.draw(window)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)

main()
