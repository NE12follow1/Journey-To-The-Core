import pygame #Used for displaying the game

#A class to make tile maps for the rooms and draw them on the screen
class TileMap(pygame.sprite.Sprite):
    def __init__(self, roomSpriteSheet, tileMap, scale):                       #Initialising function that is ran when a new TileMap object is made
        super().__init__()                                                     #Takes initialisation information for pygame sprie objects
        self.file = open(tileMap, mode = "r")                                  #Opens the .txt file that maps out the tile locations for the room being displayed on the screen
        self.tiles = pygame.image.load(roomSpriteSheet)                        #Loads the sprite sheet image that is used to make the rooms
        self.tileSize = 100 * scale                                            #Defines the size of each square tile in each direction
        self.spriteSheetSize = (6 * tileSize, 4 * tileSize)                    #Defines the size of the sprite sheet with the tiles on it
        self.tiles = pygame.transform.scale(self.tiles, self.spriteSheetSize)  #Scales the sprite sheet up or down to the user's needs

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
