import pygame               #Used for displaying the game
import random               #Used for anything that requires randomness
from settings import *      #A separate python file that holds many constants to do with pygame

class Armour:
    def __init__(self,slot,points,sp,hp,ar,dm,cd,cc):
        self.armourSlot = slot
        self.points     = points
        self.speed      = sp
        self.health     = hp
        self.armour     = ar
        self.damage     = dm
        self.critDamage = cd
        self.critChance = cc

def rollArmour(pref1,pref2):
    slotNum = random.randint(1,4)
    if slotNum == 1:
        slot = "Helmet"
    elif slotNum == 2:
        slot = "Chestplate"
    elif slotNum == 3:
        slot = "Gauntlets"
    else:
        slot = "Leggings"
    
    sp = 0
    hp = 0
    ar = 0
    dm = 0
    cd = 0
    cc = 0

    num1 = random.randint(1,7)
    if num1 > 3:
        points = random.randint(60,80)
    elif num1 > 1:
        points = random.randint(40,60)
    else:
        points = random.randint(30,40)

    distribution = points - 12
    group1 = distribution // 2
    group2 = distribution - group1
    
    #Distributes points for group 1   
    num1 = random.randint(1,4)
    if num1 == 4:
        group1Main = pref1
    else:
        group1Main = num1

    if group1Main == 1:
        sp = random.randint(group1 // 2,(group1 // 4) * 3)
        group1 -= sp
    if group1Main == 2:
        hp = random.randint(group1 // 2,(group1 // 4) * 3)
        group1 -= hp
    if group1Main == 3:
        ar = random.randint(group1 // 2,(group1 // 4) * 3)
        group1 -= ar

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
        sp = group1
    if group1Second == 2:
        hp = group1
    if group1Second == 3:
        ar = group1

    sp += 2
    hp += 2
    ar += 2


    #Distributes points for group 2
    num1 = random.randint(1,4)
    if num1 == 4:
        group2Main = pref2
    else:
        group2Main = num1

    if group2Main == 1:
        dm = random.randint(group2 // 2,(group2 // 4) * 3)
        group2 -= dm
    if group2Main == 2:
        cd = random.randint(group2 // 2,(group2 // 4) * 3)
        group2 -= cd
    if group2Main == 3:
        cc = random.randint(group2 // 2,(group2 // 4) * 3)
        group2 -= cc

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
        dm = group2
    if group2Second == 2:
        cd = group2
    if group2Second == 3:
        cc = group2

    dm += 2
    cd += 2
    cc += 2

    return Armour(slot,points,sp,hp,ar,dm,cd,cc)

#Initialises the pygame library
pygame.init()

screen = pygame.display.set_mode((0,0),FULLSCREEN)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    pygame.clock.tick(fps)
