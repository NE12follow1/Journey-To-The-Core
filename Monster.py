import pygame               #Used for displaying the game
from pygame.locals import * #Used to reduce the need for typing pygame. for certain things
import random               #Used for anything that requires randomness

class Monster(pygame.sprite.Sprite):
    def __init__(self,monsterSpriteSheet, behaviour, floorNum):  #Initialising function that is ran when a new Monster object is made
        super().__init__()                                       #Takes initialisation information for pygame sprie objects
        self.behaviour = behaviour                               #Defines the stats of the monster and how it acts in combat
        self.statMultiplier = floorNum                           #Defines how much the monsters stats get increased by due to the floor 
        self.height = 100                                        #Defines the height of the monster sprite in the sprite sheet
        self.width = 100                                         #Defines the width of the monster sprite in the sprite sheet
        self.x = 150                                             #Defines the x position of the monster on the screen
        self.y = 150                                             #Defines the y position of the monster on the screen
        self.spriteSheet = pygame.image.load(monsterSpriteSheet) #Loads the sprite sheet for the monster
        self.state = [0,0]                                       #Defines which state the monster is in (left,right,up or down)

        #Defines the stats of the cautious monster behaviour type
        if self.behaviour == "cautious":
            self.maxHp = 100 + (20 * ((self.statMultiplier - 1) // 2))      #Defines it's max hp (medium)
            self.speed = 80                                                 #Defines it's speed (fast)
            self.defence = 0.2                                              #Defines it's defence (medium)
            self.healingThreashold = 0.9                                    #Defines the hp it needs to be at to start healing (high)
            self.attackDamage = 10 + (2 * ((self.statMultiplier - 1) // 2)) #Defines the damage it deals on an attack (low)
            self.healing = 0.015                                            #Defines the amount of hp healed when the monster heals (medium)
            self.abilities = ["Attack","Heal","Counter"]                    #Lists the moves the monster has access to
            #A short description of the enemy type
            self.infoCard = "This monster has shown to be very cautious in combat, healing itself from the smallest of scratches" 

        #Defines the stats of the speedy monster behaviour type
        if self.behaviour == "speedy":
            self.maxHp = 100 + (20 * ((self.statMultiplier - 1) // 2))      #Defines it's max hp (medium)
            self.speed = 100                                                #Defines it's speed (very fast)
            self.defence = 0.2                                              #Defines it's defence (medium)
            self.healingThreashold = 0.4                                    #Defines the hp it needs to be at to start healing (medium)
            self.attackDamage = 10 + (2 * ((self.statMultiplier - 1) // 2)) #Defines the damage it deals on an attack (low)
            self.healing = 0.01                                             #Defines the amount of hp healed when the monster heals (low)
            self.abilities = ["Attack","Heal","SpeedUp","Counter"]          #Lists the moves the monster has access to
            #A short description of the enemy type
            self.infoCard = "This monster appears full of adrenaline, becoming erratic when threatened"

        #Defines the stats of the aggressive monster behaviour type
        if self.behaviour == "aggressive":
            self.maxHp = 75 + (15 * ((self.statMultiplier - 1) // 2))       #Defines it's max hp (low)
            self.speed = 60                                                 #Defines it's speed (medium)
            self.defence = 0.1                                              #Defines it's defence (low)
            self.healingThreashold = 0.2                                    #Defines the hp it needs to be at to start healing (low)
            self.attackDamage = 25 + (5 * ((self.statMultiplier - 1) // 2)) #Defines the damage it deals on an attack (high)
            self.healing = 0.02                                             #Defines the amount of hp healed when the monster heals (high)
            self.abilities = ["Attack","Heal","AttackUp","Counter"]         #Lists the moves the monster has access to
            #A short description of the enemy type
            self.infoCard = "This monster deals a lot of damage, showing very little regard for it's own health"

        #Defines the stats of the tank monster behaviour type
        if self.behaviour == "tank":
            self.maxHp = 150 + (30 * ((self.statMultiplier - 1) // 2))      #Defines it's max hp (high)
            self.speed = 35                                                 #Defines it's speed (low)
            self.defence = 0.5                                              #Defines it's defence (high)
            self.healingThreashold = 0.5                                    #Defines the hp it needs to be at to start increasing it's defence (medium)
            self.attackDamage = 20 + (4 * ((self.statMultiplier - 1) // 2)) #Defines the damage it deals on an attack (medium-high)
            self.healing = 0.1                                              #Defines the amount it increases it's defence by on it's turn
            self.abilities = ["Attack","ArmourUp"]                          #Lists the moves the monster has access to
            #A short description of the enemy type
            self.infoCard = "This monster is able to thicken it's armour when threatened and give a hard hit back"

        #Defines the stats of the impressionable monster behaviour type
        if self.behaviour == "impressionable":
            self.maxHp = 100 + (20 * ((self.statMultiplier - 1) // 2))      #Defines it's max hp (medium)
            self.speed = 55                                                 #Defines it's speed (medium)
            self.defence = 0                                                #Defines it's defence (non-existent)
            self.healingThreashold = -1                                     #Defines the hp it needs to be at to start healing (special)
            self.attackDamage = 15 + (3 * ((self.statMultiplier - 1) // 2)) #Defines the damage it deals on an attack (medium)
            self.healing = 1                                                #Defines the amount of hp healed when the monster heals (full)
            self.abilities = ["Attack","Heal","RememberDamage","Counter"]   #Lists the moves the monster has access to
            #A short description of the enemy type
            self.infoCard = "This monster is very intelligent and holds the ability to fully recover it's health if it feels close to death"
            self.rememberedDamage = 0 #Stores the first amount of damage the monster recieves 

        self.currentHp = self.maxHp #Sets the monster's current hp to it's max hp
        self.alive = True           #Determines that the monster is alive
        self.stunned = False        #Determines that the monster is not stunned

    #A function that moves the monster towards the player and returns if it had to move
    def moveToPlayer(self,playerX,playerY):
        #When the player is above the monster
        if playerY + 55 < self.y:
            self.y -= 3        #Moves the monster upwards
            self.state = [0,1] #Sets the monster's state to point up
            self.moved = True  #Defines that the monster has moved
        #When the player is below the monster
        elif playerY > self.y + 100:
            self.y += 3        #Moves the monster downwards
            self.state = [0,0] #Sets the monster's state to point down
            self.moved = True  #Defines that the monster has moved
        #When the player is to the left of the monster
        elif playerX + 45 < self.x:
            self.x -= 3        #Moves the monster left
            self.state = [1,0] #Sets the monster's state to point left
            self.moved = True  #Defines that the monster has moved
        #When the player is to the right of the monster
        elif playerX > self.x + 100:
            self.x += 3        #Moves the monster right
            self.state = [1,1] #Sets the monster's state to point right
            self.moved = True  #Defines that the monster has moved
        #When the player is next to the monster
        else:
            self.moved = False #Defines that the monster has not moved

        return self.moved #Returns if the monster has moved or not

    #A procedure to draw the monster to the screen
    def draw(self,screen,scale):
        #Takes the current state of the monster from the sprite sheet
        self.image = self.spriteSheet.subsurface(Rect(self.state[0] * 100, self.state[1] * 100, self.width, self.height))
        self.imageSize = (self.width * scale, self.height * scale)      #Makes a tuple that determines how large the monster image is supposed to be when scaled up
        self.image = pygame.transform.scale(self.image, self.imageSize) #Scales the monster to the screen
        self.location = (self.x * scale, self.y * scale)                #Makes a tuple that determines the monster's location on the screen
        screen.blit(self.image,self.location)                           #Draws the monster onto the screen at the given location

    #A function that decides which monster will use depending on their behaviour type
    def decideMove(self,playerMove):
        if self.stunned == False:
            self.isAttacking = False #Determines if the monster is attacking this turn (defaults to false)
            #The monster always counter's if the player used a melee attack and the enemy isn't a tank
            if playerMove == "Melee" and self.behaviour != "tank":
                self.counter()
            else:
                #Determines what the impressionable behaviour type does when not countering on it's turn
                if self.behaviour == "impressionable":
                    #Remembers the last attack the player used if it don't have one stored
                    if self.rememberedDamage == 0:
                        self.rememberDamage()
                    #Heals if it is within the remembered attack's amount of health
                    elif self.currentHp < self.healingThreashold * self.maxHp:
                        self.heal()
                    #Attacks if it has a remembered attack and is above that amount of health
                    else:
                        self.attack()

                #Determines what the tank behaviour type does on it's turn
                elif self.behaviour == "tank":
                    #Has a 50/50 chance to increase it's armour or attack if it's under 50% hp and hasn't increased it's armour 5 times already
                    if self.currentHp < self.healingThreashold * self.maxHp and self.speed > 20:
                        num = random.randint(1,10)
                        if num <= 5:
                            self.armourUp()
                        else:
                            self.attack()
                    #Attacks if it has over 50% hp or has increased it's armour 5 times already
                    else:
                        self.attack()

                #Determines what the aggressive behaviour type does on it's turn
                elif self.behaviour == "aggressive":
                    #Heals if it is under the healing threashold 
                    if self.currentHp < self.healingThreashold * self.maxHp:
                        self.heal()
                    else:
                        #Has a 40% chance to increase it's attack and a 60% chance to attack if it isn't going to heal this turn
                        num = random.randint(1,10)
                        if num <= 4:
                            self.attackUp()
                        else:
                            self.attack()

                #Determines what the speedy behaviour type does on it's turn
                elif self.behaviour == "speedy":
                    #Heals if it is under the healing threashold 
                    if self.currentHp < self.healingThreashold * self.maxHp:
                        self.heal()
                    else:
                        #Has a 10% chance to increase it's speed and a 90% chance to attack if it isn't going to heal this turn
                        num = random.randint(1,10)
                        if num <= 1:
                            self.speedUp()
                        else:
                            self.attack()

                elif self.behaviour == "cautious":
                    #Heals if it is under the healing threashold 
                    if self.currentHp < self.healingThreashold * self.maxHp:
                        self.heal()
                    else:
                        #Attacks if it isn't going to heal this turn
                        self.attack()

            #Returns how much damage the monster is dealing this turn, returning 0 if it isn't attacking
            if self.isAttacking == True:
                return self.damage
            else:
                return 0

        else:
            self.stunned = False
            return 0

    #A proccedure to deal damage to the monster, reducing damage taken for the monster's defence
    def takeDamage(self,rawDamage):
        self.currentHp -= int(rawDamage * (1 - self.defence))
        if self.currentHp < 0:
            self.currentHp = 0
        if self.currentHp == 0:
            self.alive = False

    #A proccedure to reduce the monster's armour (e.g from a sniper)
    def reduceArmour(self,armour):
        self.defence -= armour
        self.speed += 3 * (armour / 0.1)
        if self.defence < -0.01:
            self.defence = 0
            self.speed -= 3 * (armour / 0.1)
        elif self.defence == -0.01:
            self.defence = 0

    #A proccedure to deal damage due to the player using a melee attack, but the damage is reduced by 75%
    def counter(self):
        self.isAttacking = True
        self.damage = int(self.attackDamage * 0.75)

    #A procedure to take a value for the damage taken and remember it
    def rememberDamage(self):
        self.rememberedDamage = self.maxHp - self.currentHp
        self.healingThreashold = self.rememberedDamage / self.maxHp

    #A procedure for healing the monster (can't go above it's max health)
    def heal(self):
        self.currentHp += self.maxHp * self.healing
        if self.currentHp > self.maxHp:
            self.currentHp = self.maxHp

    #A procedure for attacking the player
    def attack(self):
        self.isAttacking = True
        self.damage = self.attackDamage

    #A procedure for increasing armour at te cost of speed. Ensures the monster doesn't have 100% damage reduction
    def armourUp(self):
        self.defence += self.healing
        if self.defence >= 1:
            self.defence = 0.99
        self.speed -= 3

    #A procedure for increasing the attack of the monster
    def attackUp(self):
        self.attackDamage = int(self.attackDamage * 1.1)

    #A procedure for increasing the speed of the monster
    def speedUp(self):
        self.speed = int(self.speed * 1.05)
