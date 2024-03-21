import pygame                           #Used for displaying the game
import random                           #Used for anything that requires randomness
from pygame.locals import *             #Used to reduce the need for typing pygame. for certain things 
from Settings import *                  #A separate python file that holds many constants to do with pygame
from RoomDistributionAlgorithm import * #A separate python file that creates the floor layout
from Dwarf import *                     #A separate python file that handles the visuals of the player character and how they move around
from TileMap import *                   #A separate python file that is used to make a tile map for the screen and draws it to the screen
from MiniMap import *                   #A separate python file that is used to make the mini-map for the game and draws it to the screen
from Map import *                       #A separate python file that is used to make the map screen for the game and display it once the user presses the right button
from CombatEncounter import *           #A separate python file that is used to display the combat encounters

#Initialises the pygame library and the clock used to determine the fps (frames per second) of the game
pygame.init()
clock = pygame.time.Clock()

#Creates a pygame screen abd gives it a caption
screen = pygame.display.set_mode((400 * scale,400 * scale))
pygame.display.set_caption("Journey To The Core")

running = True #Used to determine if the user has quit the program or not
count = 0      #Used to stall the dwarf's animation

floorNum = 1                                                        #Determines the current floor's number (for monster scaling)
possibleBehaviours = ["cautious"]                                   #Determines which possible monster behaviour types are on the floor

currentFloorLayout = NewFloor("Large",floorNum,possibleBehaviours)  #Creates a 2D array room layout using the imported module
currentRoomLocation = [4,4]                                         #Determines which room in the floor the player is in, which always starts as the middle
dwarf = Dwarf("Assets/SpriteSheet.png")                             #Initialises the dwarf object

currentRoomObject = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]]                                            #Gets the room object of the room the player is currently in
currentRoomMap = TileMap("Assets/TileSpriteSheet.png","RoomMaps/{}.txt".format(currentRoomObject.roomID),scale,currentRoomObject) #Makes a tile map object of the type of room the player is currently in
currentRoomMap.loadTileMap(currentRoomObject.isExitRoom)                                                                          #Makes the tile map for the tile map object

miniMap = MiniMap("Assets/MiscellaneousGraphics.png")       #Makes the mini-map object  
miniMap.loadMiniMap(currentFloorLayout,currentRoomLocation) #Makes the mini-map from the player's current location and the floor layout

mapScreen = Map("Assets/MiscellaneousGraphics.png")       #Makes the map object
mapScreen.loadMap(currentFloorLayout,currentRoomLocation) #Makes the map from the player's current location and the floor layout

reloadCombatStage = True #Determines if the combat stage needs to be reloaded due to part of it changing

inCombat = False    #Determines if the player is in a combat encounter, or is exploring the floor
playerTm = 0        #A counter for the turn meter of the player
monsterTm = 0       #A counter for the turn meter of the monster
playerTurn = False  #Used in combat to determine if it is the player's turn or not
monsterTurn = False #Used in combat to determine if it is the monster's turn or not
weaponChoice = 0    #Determines the player's choice of weapon, 0 being no weapon selected
playerMove = ""     #Determines the name of the weapon used by the player

#Starts the main game loop
while running:

    #Checks for user input
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            
            #Checks if the user presses the escape key to quit the game
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()

            #Checks if the user presses the m key to open the map
            if event.key == K_m and inCombat == False:
                running = mapScreen.displayMap(screen, scale)

            #Checks if the player has selected a weapon while it's their turn
            if event.key == K_1 and dwarf.weapons[1].reload == 0 and weaponChoice == 0 and playerTurn == True:
                weaponChoice = 1
            elif event.key == K_2 and dwarf.weapons[2].reload == 0 and weaponChoice == 0 and playerTurn == True:
                weaponChoice = 2
            elif event.key == K_3 and dwarf.weapons[3].reload == 0 and weaponChoice == 0 and playerTurn == True:
                weaponChoice = 3
            elif event.key == K_4 and dwarf.weapons[4].reload == 0 and weaponChoice == 0 and playerTurn == True:
                weaponChoice = 4

        #Checks if the user has pressed the x button to close the game
        if event.type == QUIT:
            running = False
            pygame.quit()

    #Runs if the player is not in combat and the game isn't over
    if inCombat == False and running == True:
        #Increases count by 1 
        count += 1
        #Resets count once it reaches a value of 8
        if count == 8:
            count = 0

        #Fills in the screen with black 
        screen.fill((0,0,0))

        reloadRoom = False #Determines if the room's image needs to be loaded again due to something changing in it

        #Moves the character to the next room if they go through the door to that room
        if dwarf.x <= 0:
            currentRoomLocation[0] -= 1
            dwarf.x = 400 - dwarf.width - 20
            reloadRoom = True

        if dwarf.x + dwarf.width >= 400:
            currentRoomLocation[0] += 1
            dwarf.x = 0 + 20
            reloadRoom = True

        if dwarf.y <= 0:
            currentRoomLocation[1] -= 1
            dwarf.y = 400 - dwarf.height - 20
            reloadRoom = True

        if dwarf.y + dwarf.height >= 400:
            currentRoomLocation[1] += 1
            dwarf.y = 0 + 20
            reloadRoom = True

        #Loads the new floor if the the dwarf goes over the exit hole
        if currentRoomObject.isExitRoom == True and dwarf.x >= 148 and dwarf.x <= 252 - dwarf.width and dwarf.y <= 227 - dwarf.height and dwarf.y >= 173 - dwarf.height:
            floorNum += 1 #Updates the number of the current floor (used for monster scaling)
            #The types of monster behaviours that appear on each floor change every 5 floors to make the strategies more complex
            if floorNum == 2:
                possibleBehaviours.append("speedy")
            elif floorNum == 3:
                possibleBehaviours.append("aggressive")
            elif floorNum == 4:
                possibleBehaviours.append("tank")
            elif floorNum == 5:
                possibleBehaviours.append("impressionable")
            elif floorNum == 6:
                possibleBehaviours.pop(0)
                
            currentFloorLayout = NewFloor("Large",floorNum,possibleBehaviours) #Creates a new floor layout
            currentRoomLocation = [4,4]                                        #Sets the player back to the entrance room
            dwarf.x = 200 - int(dwarf.width / 2)                               #Sets the player to the centre of the room
            dwarf.y = 200 - int(dwarf.height / 2)                              #Sets the player to the centre of the room
            reloadRoom = True                                                  #Tells the program to reload the current room to be the new entrance room

        if reloadRoom == True:
            currentRoomObject = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]]                                            #Gets the room object of the room the player is currently in
            currentRoomMap = TileMap("Assets/TileSpriteSheet.png","RoomMaps/{}.txt".format(currentRoomObject.roomID),scale,currentRoomObject) #Makes a tile map object of the type of room the player is currently in
            currentRoomMap.loadTileMap(currentRoomObject.isExitRoom)                                                                          #Makes the tile map for the tile map object

            miniMap = MiniMap("Assets/MiscellaneousGraphics.png")       #Makes the mini-map object  
            miniMap.loadMiniMap(currentFloorLayout,currentRoomLocation) #Makes the mini-map from the player's current location and the floor layout

            mapScreen = Map("Assets/MiscellaneousGraphics.png")       #Makes the map object
            mapScreen.loadMap(currentFloorLayout,currentRoomLocation) #Makes the map from the player's current location and the floor layout

            enemyMoved = True #Lets any monster inside the new room move
            inCombat = False  #Stops any combat encounter if there was one going on

        currentRoomMap.draw(screen) #Draws the room to the screen

        #When the player walks into a room with a monster in it
        if currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[0] == True and inCombat == False:
            #Sets the dwarf to it's idle animation
            if dwarf.state < 4:
                dwarf.state += 4
            currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[1].draw(screen,scale) #Draws the monster to the screen
            #Moves the monster towards the player until it reaches the player
            if enemyMoved != False:
                enemyMoved = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[1].moveToPlayer(dwarf.x,dwarf.y)
            else:
                inCombat = True         #Tells the program the player is now in a combat encounter
                monsterLoaded = False   #Used to tell the program to load the monster in the current room

        else:
            dwarf.updatePosition(currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].roomID) #Updates the position of the dwarf character on the screen
            
        dwarf.draw(screen,count,scale) #Draws the dwarf character onto the screen

        miniMap.draw(screen,scale) #Draws the mini-map onto the screen

    #If the player is in combat and the game is still running
    elif running == True:

        #If there is no monster loaded, take the one in the current room
        if monsterLoaded == False:
            monster = currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[1]
            monsterLoaded = True
            print(monster.behaviour,"\n"+monster.infoCard)

        #Runns if bothe the player and monster is still alive
        if dwarf.alive == True and monster.alive == True:

            #Reloads the combat stage if something has changed
            if reloadCombatStage == True:
                combatStage = CombatStage("Assets/CombatStage.png", "Assets/MiscellaneousGraphics.png", "Assets/EnemySpriteSheet.png", "Assets/SpriteSheet.png", "Assets/AmmoNumbers.png", dwarf, monster)
                combatStageImage = combatStage.loadCombatStage(scale)
                reloadCombatStage = False
                screen.blit(combatStageImage,(0,0))

            #Runs to determine whether the player or monster has the next turn
            if playerTurn == False and monsterTurn == False:
                playerTm += dwarf.speed
                monsterTm += monster.speed
                totalTmNeeded = dwarf.speed * monster.speed
                if totalTmNeeded % 10 == 0:
                    totalTmNeeded = totalTmNeeded / 10

                if monsterTm >= totalTmNeeded:
                    if monster.stunned == True:
                        monster.stunned = False
                        monsterTm = 0
                    else:
                        monsterTurn = True
                        monsterTm = 0

                elif playerTm >= totalTmNeeded:
                    playerTurn = True
                    playerTm = 0
                    weaponChoice = 0
                    playerMove = ""
                    for i in range(4):
                        dwarf.weapons[i + 1].reload -= 1
                        if dwarf.weapons[i + 1].reload < 0:
                            dwarf.weapons[i + 1].reload = 0
                    reloadCombatStage = True

            elif monsterTurn == True:
                monsterDamage = monster.decideMove(playerMove)
                dwarf.takeDamage(monsterDamage)
                monsterTurn = False
                reloadCombatStage = True

            elif playerTurn == True:
                if weaponChoice != 0:
                    playerDamage, stunMonster, playerMove, armourBreaking = dwarf.attack(weaponChoice)
                    if stunMonster == True:
                        monster.stunned = True
                    if playerMove == "Melee":
                        monsterDamage = monster.decideMove(playerMove)
                        dwarf.takeDamage(monsterDamage)
                    if armourBreaking != 0:
                        monster.reduceArmour(armourBreaking)
                    monster.takeDamage(playerDamage)
                    playerTurn = False
                    reloadCombatStage = True
                    
        elif monster.alive == False:
            currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[0] = False
            currentFloorLayout[currentRoomLocation[0]][currentRoomLocation[1]].enemyPresent[1] = ""
            inCombat = False
            dwarf.currentHp += dwarf.maxHp * 0.5
            if dwarf.currentHp > dwarf.maxHp:
                dwarf.currentHp = dwarf.maxHp

            weaponNames = ["Shotgun","Sniper","BurstRifle","Pistol"]
            ammoRecovRates = [0.5,0.5,0.5,0.5]
            for i in range(4):
                dwarf.ammoBag[weaponNames[i]] += int(dwarf.ammoMax[weaponNames[i]] * ammoRecovRates[i])
                if dwarf.ammoBag[weaponNames[i]] > dwarf.ammoMax[weaponNames[i]]:
                    dwarf.ammoBag[weaponNames[i]] = dwarf.ammoMax[weaponNames[i]]

            for i in range(4):
                if dwarf.weapons[i + 1].weaponType == "Melee":
                    if i == 0:
                        dwarf.weapons[i + 1] = Weapon("Shotgun",dwarf.weaponSpriteSheet,dwarf.lvl)
                    if i == 1:
                        dwarf.weapons[i + 1] = Weapon("Sniper",dwarf.weaponSpriteSheet,dwarf.lvl)
                    if i == 2:
                        dwarf.weapons[i + 1] = Weapon("BurstRifle",dwarf.weaponSpriteSheet,dwarf.lvl)
                    if i == 3:
                        dwarf.weapons[i + 1] = Weapon("Pistol",dwarf.weaponSpriteSheet,dwarf.lvl)
                        
            for i in range(4):
                dwarf.weapons[i + 1].reload = 0

        else:
            running = False
            pygame.quit()

    if running == True:
        #Updates the screen's graphics
        pygame.display.update() 

        #Used to set the game to the fps found in the settings file
        clock.tick(fps)
