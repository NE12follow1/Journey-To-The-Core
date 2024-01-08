import pygame

class TileMap(pygame.sprite.Sprite):
    def __init__(self, roomSpriteSheet, tileMap):
        super().__init__()
        self.file = open(tileMap, mode = "r")
        self.tiles = pygame.image.load(roomSpriteSheet)

    def loadTileMap(self):
        tileMap = []
        tileSize = 100
        for row in range(4):
            tileMap.append([])
            for column in range(4):
                tileMap[row].append("")

        for x in range(4):
            line = self.file.readline()
            for y in range(4):
                if line[y] == "0":
                    tileMap[x][y] = (0,0,100,100)
                if line[y] == "1":
                    tileMap[x][y] = (100,0,100,100)
                if line[y] == "2":
                    tileMap[x][y] = (200,0,100,100)
                if line[y] == "3":
                    tileMap[x][y] = (300,0,100,100)
                if line[y] == "4":
                    tileMap[x][y] = (400,0,100,100)
                if line[y] == "5":
                    tileMap[x][y] = (500,0,100,100)
                if line[y] == "6":
                    tileMap[x][y] = (0,100,100,100)
                if line[y] == "7":
                    tileMap[x][y] = (100,100,100,100)
                if line[y] == "8":
                    tileMap[x][y] = (200,100,100,100)
                if line[y] == "9":
                    tileMap[x][y] = (300,100,100,100)
                if line[y] == "A":
                    tileMap[x][y] = (400,100,100,100)
                if line[y] == "B":
                    tileMap[x][y] = (500,100,100,100)
                if line[y] == "C":
                    tileMap[x][y] = (0,200,100,100)
                if line[y] == "D":
                    tileMap[x][y] = (100,200,100,100)
                if line[y] == "E":
                    tileMap[x][y] = (200,200,100,100)
                if line[y] == "F":
                    tileMap[x][y] = (300,200,100,100)
                if line[y] == "G":
                    tileMap[x][y] = (400,200,100,100)
                if line[y] == "H":
                    tileMap[x][y] = (0,300,100,100)
                if line[y] == "I":
                    tileMap[x][y] = (100,300,100,100)
                if line[y] == "J":
                    tileMap[x][y] = (200,300,100,100)
                if line[y] == "K":
                    tileMap[x][y] = (300,300,100,100)

        return tileMap

    def draw(self, tileMap, screen):
        for x in range(4):
            for y in range(4):
                screen.blit(self.tiles, (y * 100, x * 100), tileMap[x][y])
