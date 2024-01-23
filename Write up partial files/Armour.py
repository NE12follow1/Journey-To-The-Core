class Armour:
    def __init__(self,pref1,pref2):
        rollArmour(pref1,pref2)#Randomises the stats on the armour once it has been initialised
        
    def rollArmour(pref1,pref2):
        #Randomly chooses one of the 4 armour slots for the armour to be
        slotNum = random.randint(1,4)
        if slotNum == 1:
            self.slot = "Helmet"
        elif slotNum == 2:
            self.slot = "Chestplate"
        elif slotNum == 3:
            self.slot = "Gauntlets"
        else:
            self.slot = "Leggings"

        #Initialises the stat attributes
        self.speed = 0
        self.health = 0
        self.armour = 0
        self.damage = 0
        self.criticalDamage = 0
        self.criticalChance = 0

        #Determines how many points there are to be distributed among the stats
        num1 = random.randint(1,7)
        if num1 > 3:
            self.points = random.randint(60,80)#4/7 times it gets the most highest range for points
        elif num1 > 1:
            self.points = random.randint(40,60)#2/7 times it gets the second highest range for points
        else:
            self.points = random.randint(30,40)#1/7 times it gets the lowest range of points

        #Takes 12 points away to give each stat 2 at the end of the proccess and splits the remaining points between group 1 and group 2
        distribution = self.points - 12
        group1 = distribution // 2
        group2 = distribution - group1
        
        #Distributes points for group 1

        #Selects a stat from group 1 to get most of group 1's points
        num1 = random.randint(1,4)
        #The preferred stat has a 1/2 chance of being the main stat for that group, the other 2 have an equal 1/4 chance each
        if num1 == 4:
            group1Main = pref1
        else:
            group1Main = num1

        #Gives the main stat between 50% and 75% of the points for group 1
        if group1Main == 1:
            self.speed = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.speed
        if group1Main == 2:
            self.health = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.health
        if group1Main == 3:
            self.armour = random.randint(group1 // 2,(group1 // 4) * 3)
            group1 -= self.armour

        #Chooses which stat will get the remaining points for group 1. This first one is for when the preffered stat was 
        #chosen as the main stat, giving the remaining 2 stats in the group a 1/2 chance of being chosen
        if group1Main == pref1:
            group1Second = random.randint(1,2)
            if pref1 == 1:
                group1Second += 1
            elif pref1 == 2:
                if group1Second == 2:
                    group1Second += 1
            else:
                pass
        #This second version of the secondary stat selector is for when the preffered stat wasn't chosen as the main stat, 
        #giving the preffered stat a 2/3 chance of being the secondary stat, and the other stat being chosen only 1/3 times
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
              
        #Gives the secondary stat the remaining points for group 1
        if group1Second == 1:
            self.speed = group1
        if group1Second == 2:
            self.health = group1
        if group1Second == 3:
            self.armour = group1
          
        #Each stat in group 1 is given the 2 points given to every stat on the armour
        self.speed += 2
        self.health += 2
        self.armour += 2
    
    
        #Distributes points for group 2. This is the same code as for group 1 but with changes to the attribute names.

        #Selects a stat from group 2 to get most of group 2's points
        num1 = random.randint(1,4)
        #The preferred stat has a 1/2 chance of being the main stat for that group, the other 2 have an equal 1/4 chance each
        if num1 == 4:
            group2Main = pref2
        else:
            group2Main = num1

        #Gives the main stat between 50% and 75% of the points for group 2
        if group2Main == 1:
            self.damage = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.damage
        if group2Main == 2:
            self.criticalDamage = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.criticalDamage
        if group2Main == 3:
            self.criticalChance = random.randint(group2 // 2,(group2 // 4) * 3)
            group2 -= self.criticalChance

        #Chooses which stat will get the remaining points for group 2. This first one is for when the preffered stat was 
        #chosen as the main stat, giving the remaining 2 stats in the group a 1/2 chance of being chosen
        if group2Main == pref2:
            group2Second = random.randint(1,2)
            if pref2 == 1:
                group2Second += 1
            elif pref2 == 2:
                if group2Second == 2:
                    group2Second += 1
            else:
                pass
        #This second version of the secondary stat selector is for when the preffered stat wasn't chosen as the main stat, 
        #giving the preffered stat a 2/3 chance of being the secondary stat, and the other stat being chosen only 1/3 times
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

        #Gives the secondary stat the remaining points for group 2
        if group2Second == 1:
            self.damage = group2
        if group2Second == 2:
            self.criticalDamage = group2
        if group2Second == 3:
            self.criticalChance = group2

        #Each stat in group 2 is given the 2 points given to every stat on the armour
        self.damage += 2
        self.criticalDamage += 2
        self.criticalChance += 2
