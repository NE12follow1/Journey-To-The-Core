import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things
from math import trunc      #Used to round numbers down to the nearest whole number
import random               #Used for anything that requires randomness 

class Weapon(pygame.sprite.Sprite):
    def __init__(self, weaponType, weaponIconSpriteSheet, lvl):     #Initialising function that is ran when a new Weapon object is made
        super().__init__()                                          #Takes initialisation information for pygame sprie objects
        self.weaponType = weaponType                                #Defines what type of weapon it is
        self.spriteSheet = pygame.image.load(weaponIconSpriteSheet) #Loads the sprite sheet for the weapon icons
        self.lvl = lvl                                              #Defines the level of the weapon (used for scaling the damage of the weapons)

        #Defines the stats of the shotgun
        if self.weaponType == "Shotgun":
            self.weaponImage = self.spriteSheet.subsurface(Rect(25,25,50,50))   #Defines the shotgun's image on the sprite sheet
            self.ammoConsumption = 1                                            #Defines how much ammo is consumed when the weapon is used
            self.damage = 6 * (3 + trunc(0.3 * (self.lvl - 1)))                 #Defines the damage that the shotgun deals before armour and multipliers
            self.armourBreaking = 0                                             #Defines how much of the monster's armour is broken when used
            self.stunChance = 0.5                                               #Defines the chance to stun the enemy monster when used
            self.reloadTime = 3                                                 #Defines how many turns until the weapon can be fired again

        #Defines the stats of the sniper
        if self.weaponType == "Sniper":
            self.weaponImage = self.spriteSheet.subsurface(Rect(125,25,50,50))
            self.ammoConsumption = 1
            self.damage = 20 + (2 * (self.lvl - 1))
            self.armourBreaking = 0.2
            self.stunChance = 0
            self.reloadTime = 4

        #Defines the stats of the burst rifle
        if self.weaponType == "BurstRifle":
            self.weaponImage = self.spriteSheet.subsurface(Rect(225,25,50,50))
            self.ammoConsumption = 3
            self.damage = 4 + trunc(0.4 * (self.lvl - 1))
            self.armourBreaking = 0
            self.stunChance = 0
            self.reloadTime = 2

        #Defines the stats of the pistol
        if self.weaponType == "Pistol":
            self.weaponImage = self.spriteSheet.subsurface(Rect(25,125,50,50))
            self.ammoConsumption = 5
            self.damage = 1 + trunc(0.1 * (self.lvl - 1))
            self.armourBreaking = 0
            self.stunChance = 0
            self.reloadTime = 1

        #Defines the stats of using the melee weapon
        if self.weaponType == "Melee":
            self.weaponImage = self.spriteSheet.subsurface(Rect(125,125,50,50))
            self.ammoConsumption = 1
            self.damage = 12 + trunc(1.2 * (self.lvl - 1))
            self.armourBreaking = 0.1
            self.stunChance = 0
            self.reloadTime = 0

        self.reload = 0 #Sets the reload to 0 so it can be used on the first turn

    #A function for working out what happens when the weapon is used
    def useWeapon(self, ammoBag):
        #The weapon's ammo is consumed (except if it is the melee weapon
        if self.weaponType != "Melee":
            ammoBag[self.weaponType] -= self.ammoConsumption

        #To check if the monster is stunned from the weapon being used
        num = random.randint(1,100)
        if num <= self.stunChance * 100:
            stunMonster = True
        else:
            stunMonster = False

        #Sets the weapon to its max reload time
        self.reload += self.reloadTime

        #Damage is calculated as the number of bullets fired x the damage of each bullet
        damage = self.ammoConsumption * self.damage

        return ammoBag, stunMonster, damage, self.armourBreaking #Returns all of the values outside of the weapon class that have been changed

    #A procedure to draw the icon onto the screen at a defined position
    def displayIcon(self, x, y, screen, scale):
        if self.reload == 0:
            self.image = self.weaponImage
        elif self.reload == 1:
            self.image = self.spriteSheet.subsurface(Rect(200,100,50,50))
        elif self.reload == 2:
            self.image = self.spriteSheet.subsurface(Rect(250,100,50,50))
        elif self.reload == 3:
            self.image = self.spriteSheet.subsurface(Rect(200,150,50,50))
        elif self.reload == 4:
            self.image = self.spriteSheet.subsurface(Rect(250,150,50,50))

        self.imageSize = (50 * scale, 50 * scale)
        self.image = pygame.transform.scale(self.image, self.imageSize)
        self.location = (x * scale, y * scale)
        screen.blit(self.image, self.location)
            
            
        
