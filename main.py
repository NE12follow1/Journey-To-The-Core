import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds many constants to do with pygame

class Armour:
    def __init__(self,pref1,pref2):
        rollArmour(pref1,pref2)
        
    def rollArmour(pref1,pref2):
        slotNum = random.randint(1,4)
        if slotNum == 1:
            self.slot = "Helmet"
        elif slotNum == 2:
            self.slot = "Chestplate"
        elif slotNum == 3:
            self.slot = "Gauntlets"
        else:
            self.slot = "Leggings"
        
        self.speed = 0
        self.health = 0
        self.armour = 0
        self.damage = 0
        self.criticalDamage = 0
        self.criticalChance = 0
    
        num1 = random.randint(1,7)
        if num1 > 3:
            self.points = random.randint(60,80)
        elif num1 > 1:
            self.points = random.randint(40,60)
        else:
            self.points = random.randint(30,40)
    
        distribution = self.points - 12
        group1 = distribution // 2
        group2 = distribution - group1
        
        #Distributes points for group 1   
        num1 = random.randint(1,4)
        if num1 == 4:
            group1Main = pref1
        else:
            group1Main = num1
    
        if group1Main == 1:
            self.speed = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.speed
        if group1Main == 2:
            self.health = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.health
        if group1Main == 3:
            self.armour = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.armour
    
        if group1Main == pref1:
            group1Second = random.randint(1,2)
            if pref1 == 1:
                group1Second += 1
            elif pref1 == 2:
                if group1Second == 2:
                    group1Second += 1
            else:
                pass
        else:
            group1Second = random.randint(1,3)
            if group1Second == 3:
                group1Second = pref1
            elif group1Main == 1:
                group1Second += 1
            elif group1Main == 2:
                if group1Second == 2:
                    group1Second += 1
            else:
                pass
    
        if group1Second == 1:
            self.speed = group1
        if group1Second == 2:
            self.health = group1
        if group1Second == 3:
            self.armour = group1
    
        self.speed += 2
        self.health += 2
        self.armour += 2
    
    
        #Distributes points for group 2
        num1 = random.randint(1,4)
        if num1 == 4:
            group2Main = pref2
        else:
            group2Main = num1
    
        if group2Main == 1:
            self.damage = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.damage
        if group2Main == 2:
            self.criticalDamage = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.criticalDamage
        if group2Main == 3:
            self.criticalChance = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.criticalChance
    
        if group2Main == pref2:
            group2Second = random.randint(1,2)
            if pref2 == 1:
                group2Second += 1
            elif pref2 == 2:
                if group2Second == 2:
                    group2Second += 1
            else:
                pass
        else:
            group2Second = random.randint(1,3)
            if group2Second == 3:
                group2Second = pref1
            elif group2Main == 1:
                group2Second += 1
            elif group2Main == 2:
                if group2Second == 2:
                    group2Second += 1
            else:
                pass
    
        if group2Second == 1:
            self.damage = group2
        if group2Second == 2:
            self.criticalDamage = group2
        if group2Second == 3:
            self.criticalChance = group2
    
        self.damage += 2
        self.criticalDamage += 2
        self.criticalChance += 2

#Initialises the pygame library
pygame.init()

screen = pygame.display.set_mode((0,0),FULLSCREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    pygame.clock.tick(fps)
