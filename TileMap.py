import pygame

class TileMap(pygame.sprite.Sprite):
    def __init__(self, roomSpriteSheet, tileMap, scale):
        super().__init__()
        self.file = open(tileMap, mode = "r")
        self.tilesSize = (600 * scale, 400 * scale)
        self.tiles = pygame.image.load(roomSpriteSheet)
        self.tiles = pygame.transform.scale(self.tiles, self.tilesSize)

    def loadTileMap(self,scale):
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
                    tileMap[x][y] = (0 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "1":
                    tileMap[x][y] = (100 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "2":
                    tileMap[x][y] = (200 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "3":
                    tileMap[x][y] = (300 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "4":
                    tileMap[x][y] = (400 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "5":
                    tileMap[x][y] = (500 * scale,0 * scale,100 * scale,100 * scale)
                if line[y] == "6":
                    tileMap[x][y] = (0 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "7":
                    tileMap[x][y] = (100 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "8":
                    tileMap[x][y] = (200 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "9":
                    tileMap[x][y] = (300 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "A":
                    tileMap[x][y] = (400 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "B":
                    tileMap[x][y] = (500 * scale,100 * scale,100 * scale,100 * scale)
                if line[y] == "C":
                    tileMap[x][y] = (0 * scale,200 * scale,100 * scale,100 * scale)
                if line[y] == "D":
                    tileMap[x][y] = (100 * scale,200 * scale,100 * scale,100 * scale)
                if line[y] == "E":
                    tileMap[x][y] = (200 * scale,200 * scale,100 * scale,100 * scale)
                if line[y] == "F":
                    tileMap[x][y] = (300 * scale,200 * scale,100 * scale,100 * scale)
                if line[y] == "G":
                    tileMap[x][y] = (400 * scale,200 * scale,100 * scale,100 * scale)
                if line[y] == "H":
                    tileMap[x][y] = (0 * scale,300 * scale,100 * scale,100 * scale)
                if line[y] == "I":
                    tileMap[x][y] = (100 * scale,300 * scale,100 * scale,100 * scale)
                if line[y] == "J":
                    tileMap[x][y] = (200 * scale,300 * scale,100 * scale,100 * scale)
                if line[y] == "K":
                    tileMap[x][y] = (300 * scale,300 * scale,100 * scale,100 * scale)

        return tileMap

    def draw(self, tileMap, screen, scale):
        for x in range(4):
            for y in range(4):
                self.location = (y * 100 * scale, x * 100 * scale)
                screen.blit(self.tiles, self.location, tileMap[x][y])
