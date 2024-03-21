import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things

class CombatStage(pygame.sprite.Sprite):
    
    #Initialising function that is ran when a new combat stage object is made
    def __init__(self, combatStageSpriteSheet, miscellaneousGraphics, enemySpriteSheet, dwarfSpriteSheet, numberSpriteSheet, dwarf, monster):
        super().__init__()                                                  #Takes initialisation information for pygame sprie objects
        self.dwarfObject = dwarf                                            #Holds the dwarf object for later use
        self.monsterObject = monster                                        #Holds the monster object for later use
        self.combatStageImage = pygame.image.load(combatStageSpriteSheet)   #Loads the sprite sheet with the combat stage image on it
        self.healthBarSpriteSheet = pygame.image.load(miscellaneousGraphics)#Loads the sprite sheet with the health bar on it
        self.monsterSpriteSheet = pygame.image.load(enemySpriteSheet)       #Loads the sprite sheet with the monster on it
        self.dwarfSpriteSheet = pygame.image.load(dwarfSpriteSheet)         #Loads the sprite sheet with the dwarf on it
        self.numberSpriteSheet = pygame.image.load(numberSpriteSheet)       #Loads the sprite sheet with numbers used for the ammo on it

    def loadCombatStage(self, scale):
        #Creates the image of the encounter and adds the background stage
        self.image = pygame.Surface((400 * scale,400 * scale))
        self.imageSize = (400 * scale, 400 * scale)
        self.combatStageImage = pygame.transform.scale(self.combatStageImage,self.imageSize)
        self.image.blit(self.combatStageImage,(0,0))

        #Draws the dwarf's empty health bar
        self.emptyHealthBar = self.healthBarSpriteSheet.subsurface(Rect(0,60,120,20))
        self.dwarfHpBarLocation = (39 * scale, 224 * scale)
        self.imageSize = (120 * scale, 20 * scale)
        self.emptyHealthBar = pygame.transform.scale(self.emptyHealthBar, self.imageSize)
        self.image.blit(self.emptyHealthBar, self.dwarfHpBarLocation)

        #Draws the monster's empty health bar
        self.monsterHpBarLocation = (258 * scale, 224 * scale)
        self.image.blit(self.emptyHealthBar, self.monsterHpBarLocation)

        #Draws the dwarf's current health bar
        dwarfHpPercent = self.dwarfObject.currentHp / self.dwarfObject.maxHp
        self.dwarfHealthBar = self.healthBarSpriteSheet.subsurface(Rect(2,82,116 * dwarfHpPercent,16))
        self.imageSize = (116 * dwarfHpPercent * scale, 16 * scale)
        self.dwarfHealthBar = pygame.transform.scale(self.dwarfHealthBar, self.imageSize)
        self.dwarfHealthBarLocation = (41 * scale, 226 * scale)
        self.image.blit(self.dwarfHealthBar, self.dwarfHealthBarLocation)

        #Draws the monster's current health bar
        monsterHpPercent = self.monsterObject.currentHp / self.monsterObject.maxHp
        self.monsterHealthBar = self.healthBarSpriteSheet.subsurface(Rect(2,82,116 * monsterHpPercent,16))
        self.imageSize = (116 * monsterHpPercent * scale, 16 * scale)
        self.monsterHealthBar = pygame.transform.scale(self.monsterHealthBar, self.imageSize)
        self.monsterHealthBarLocation = (260 * scale, 226 * scale)
        self.image.blit(self.monsterHealthBar, self.monsterHealthBarLocation)

        #Draws the dwarf onto the image
        self.dwarfImage = self.dwarfSpriteSheet.subsurface(Rect(0,0,45,55))
        self.imageSize = (45 * scale, 55 * scale)
        self.dwarfImage = pygame.transform.scale(self.dwarfImage, self.imageSize)
        self.dwarfLocation = (76 * scale, 123 * scale)
        self.image.blit(self.dwarfImage, self.dwarfLocation)

        #Draws the monster onto the image
        self.monsterImage = self.monsterSpriteSheet.subsurface(Rect(0,0,100,100))
        self.imageSize = (100 * scale, 100 * scale)
        self.monsterImage = pygame.transform.scale(self.monsterImage, self.imageSize)
        self.monsterLocation = (268 * scale, 42 * scale)
        self.image.blit(self.monsterImage, self.monsterLocation)

        #Draws the dwarf's weapon's icons onto the image
        self.dwarfObject.weapons[1].displayIcon(30,330,self.image,scale)
        self.dwarfObject.weapons[2].displayIcon(130,330,self.image,scale)
        self.dwarfObject.weapons[3].displayIcon(230,330,self.image,scale)
        self.dwarfObject.weapons[4].displayIcon(330,330,self.image,scale)

        #Adds the ammo for each weapon next to the weapon's icon
        for i in range(4):
            #Takes the ammo number and finds out how many digits it is
            currentAmmoType = self.dwarfObject.weapons[i + 1].weaponType
            currentAmmoAmount = str(self.dwarfObject.ammoBag[currentAmmoType])
            currentAmmoDigits = len(currentAmmoAmount)
            #Runs if the weapon isn't the melee weapon
            if currentAmmoAmount != "∞":
                #Creates an image of the ammo number
                self.ammoImage = pygame.Surface((6 * currentAmmoDigits * scale, 10 * scale))
                self.backgroundImage = self.numberSpriteSheet.subsurface(Rect(0, 10, 6 * currentAmmoDigits, 10))
                self.imageSize = (6 * currentAmmoDigits * scale, 10 * scale)
                self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.imageSize)
                self.ammoImage.blit(self.backgroundImage, (0, 0))
                #Adds each digit in the ammo number to the image of the ammo number
                for j in range(currentAmmoDigits):
                    self.numberImage = self.numberSpriteSheet.subsurface(Rect(int(currentAmmoAmount[j]) * 7, 0, 6, 10))
                    self.imageSize = (6 * scale, 10 * scale)
                    self.numberImage = pygame.transform.scale(self.numberImage, self.imageSize)
                    self.ammoImage.blit(self.numberImage, (6 * scale * j, 0))

                #Changes where the ammo image is on the screen depending on the number of digits in the ammo number
                if currentAmmoDigits == 1:
                    self.ammoLocation = ((12 + i * 100) * scale, 365 * scale)

                elif currentAmmoDigits == 2:
                    self.ammoLocation = ((9 + i * 100) * scale, 365 * scale)

                else:
                    self.ammoLocation = ((6 + i * 100) * scale, 365 * scale)

            #Creates an image of the infinite symbol and determines where it needs to be placed on the combat stage image
            else:
                self.ammoImage = pygame.Surface((14 * scale, 10 * scale))
                self.backgroundImage = self.numberSpriteSheet.subsurface(Rect(0, 10, 14, 10))
                self.imageSize = (14 * scale, 10 * scale)
                self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.imageSize)
                self.ammoImage.blit(self.backgroundImage, (0, 0))
                
                self.symbolImage = self.numberSpriteSheet.subsurface(Rect(70, 0, 14, 10))
                self.imageSize = (14 * scale, 10 * scale)
                self.symbolImage = pygame.transform.scale(self.symbolImage, self.imageSize)
                self.ammoImage.blit(self.symbolImage, (0, 0))
                self.ammoLocation = ((8 + i * 100) * scale, 365 * scale)
                                    
            self.image.blit(self.ammoImage, self.ammoLocation) #Draws the ammo image onto the combat stage image

        return self.image #Returns the image of the combat encounter
