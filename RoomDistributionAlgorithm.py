from Room import *      #A separate python file that holds the room class
import random           #Used for anything that requires randomness
import copy             #Used to make copies of lists and arrays that are completely separate from the original
from Monster import *   #Used to create monster objects that are added to the rooms

def NewFloor(floorSize = "large",floorNum = 1,possibleBehaviours = ["cautious"]):
    global possibleRooms, i, deletedRooms #Values used to delete a room type

    #Handles the 8 different floor sizes and what each means to the total number of rooms
    if floorSize.lower() == "xsmall":
        totalRooms = 10
    elif floorSize.lower() == "small":
        totalRooms = 15
    elif floorSize.lower() == "medium":
        totalRooms = 20
    elif floorSize.lower() == "large":
        totalRooms = 25
    elif floorSize.lower() == "xlarge":
        totalRooms = 30
    elif floorSize.lower() == "2xlarge":
        totalRooms = 35
    elif floorSize.lower() == "3xlarge":
        totalRooms = 40
    elif floorSize.lower() == "4xlarge":
        totalRooms = 45

    #Defines where and what the entrance room is
    entranceRoom = [4,4]
    entranceRoomObject = Room("1111")

    #Randomly chooses one of the 4 sides of the max floor size to be the exit room
    exitRoomType = random.randint(1,4)
    #Defines where and what the exit room is due to which side was chosen
    if exitRoomType == 1:
        exitRoom = [4,1]
        exitRoomObject = Room("0010",isExitRoom = True)
    elif exitRoomType == 2:
        exitRoom = [7,4]
        exitRoomObject = Room("0001",isExitRoom = True)
    elif exitRoomType == 3:
        exitRoom = [4,7]
        exitRoomObject = Room("1000",isExitRoom = True)
    else:
        exitRoom = [1,4]
        exitRoomObject = Room("0100",isExitRoom = True)

    #Creates the 2D array that the floor layout and all the room objects will be stored inside
    currentFloorLayout = [[1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1]]
    currentFloorLayout[entranceRoom[0]][entranceRoom[1]] = entranceRoomObject #Adds the entrance room object to its position in the 2D array
    currentFloorLayout[exitRoom[0]][exitRoom[1]] = exitRoomObject             #Adds the exit room object to its position in the 2D array

    remainingRooms = totalRooms - 2 #Determines how many rooms are left to be placed. At the start it is the total rooms (determined by the floor size) take away the entrance and exit

    availableLocations = [] #Creates a list to keep track of all the places that have a door leading to them, but aren't yet a room
 
    if exitRoom[0] == 4:
        #Adds the location that the exit room points to to the list of available room locations 
        availableLocations.append([exitRoom[0],exitRoom[1] + int((4 - exitRoom[1]) / 3)])
        
        #Adds the locations that the entrance room points to to the list of available room locations
        availableLocations.append([exitRoom[0],exitRoom[1] + 2 * int((4 - exitRoom[1]) / 3)])
        availableLocations.append([exitRoom[0] - 1,exitRoom[1] + 3 * int((4 - exitRoom[1]) / 3)])
        availableLocations.append([exitRoom[0] + 1,exitRoom[1] + 3 * int((4 - exitRoom[1]) / 3)])
        availableLocations.append([exitRoom[0],exitRoom[1] + 4 * int((4 - exitRoom[1]) / 3)])
        
    else:
        #Adds the location that the exit room points to to the list of available room locations 
        availableLocations.append([exitRoom[0] + int((4 - exitRoom[0]) / 3),exitRoom[1]])

        #Adds the locations that the entrance room points to to the list of available room locations
        availableLocations.append([exitRoom[0] + 2 * int((4 - exitRoom[0]) / 3),exitRoom[1]])
        availableLocations.append([exitRoom[0] + 3 * int((4 - exitRoom[0]) / 3),exitRoom[1] - 1])
        availableLocations.append([exitRoom[0] + 3 * int((4 - exitRoom[0]) / 3),exitRoom[1] + 1])
        availableLocations.append([exitRoom[0] + 4 * int((4 - exitRoom[0]) / 3),exitRoom[1]])

    #A list of all the room types that will be copied to another variable to keep track of all the rooms that could be placed in a location
    roomTypes = ["0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"] 

    #Starts loop to place rooms while there are still rooms to place
    while remainingRooms > 0 and len(availableLocations) > 0:
        workingLocation = availableLocations[0] #Places a room at the first listed available location

        possibleRooms = copy.deepcopy(roomTypes) #Copies over the room types to a new variable so it can be manipulated without modifying the full list

        deletedRooms = 0 #Keeps track of how many room types have been deleted from possibleRooms

        for i in range(len(possibleRooms)):

            #Special condition for the first two rooms that are placed between the start and end room
            if remainingRooms > totalRooms - 4:
                
                #Checks if the exit was placed in a vertical line with the entrance
                if exitRoom[0] == 4:
                    
                    #Makes sure the placed room will have a door above and below it so there is a path from the entrance to the exit no matter how the other rooms are placed
                    if possibleRooms[i - deletedRooms][0] == "0" or possibleRooms[i - deletedRooms][2] == "0": 
                        DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                        continue         #Skips to the next iteration of the for loop
                        
                #For when the exit is placed in a horizontal line with the entrance
                else:

                    #Makes sure the placed room will have a door to the left and right of it so there is a path from the entrance to the exit no matter how the other rooms are placed
                    if possibleRooms[i - deletedRooms][1] == "0" or possibleRooms[i - deletedRooms][3] == "0":
                        DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                        continue         #Skips to the next iteration of the for loop

            doorsToSpace = 0 #Starts to count how many doors of the current room type being checked will lead to

            #Checks the room type doesnt have a door pointing north into the edge of the floor
            if currentFloorLayout[workingLocation[0]][workingLocation[1] - 1] == 1 and possibleRooms[i - deletedRooms][0] == "1":
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue

            #Checks if the room type has a door pointing north into an empty space
            elif currentFloorLayout[workingLocation[0]][workingLocation[1] - 1] == 0 and possibleRooms[i - deletedRooms][0] == "1":
                doorsToSpace += 1 #Increases the counted number of doors pointing towards an empty space
                
            #Checks if there is a room to the north of the current one
            elif currentFloorLayout[workingLocation[0]][workingLocation[1] - 1] != 1 and currentFloorLayout[workingLocation[0]][workingLocation[1] - 1] != 0:
                #Checks that the room type has a door towards the north if the room to the north has a door towards the south 
                if currentFloorLayout[workingLocation[0]][workingLocation[1] - 1].southConnection == True and possibleRooms[i - deletedRooms][0] == "0":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

                #Checks that the room type doesn't have a door to the north if the room to the north hasn't got a door to the south
                elif currentFloorLayout[workingLocation[0]][workingLocation[1] - 1].southConnection == False and possibleRooms[i - deletedRooms][0] == "1":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

                
            #Checks the room type doesnt have a door pointing east into the edge of the floor
            if currentFloorLayout[workingLocation[0] + 1][workingLocation[1]] == 1 and possibleRooms[i - deletedRooms][1] == "1":
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue

            #Checks if the room type has a door pointing east into an empty space    
            elif currentFloorLayout[workingLocation[0] + 1][workingLocation[1]] == 0 and possibleRooms[i - deletedRooms][1] == "1":
                doorsToSpace += 1 #Increases the counted number of doors pointing towards an empty space

            #Checks if there is a room to the east of the current one
            elif currentFloorLayout[workingLocation[0] + 1][workingLocation[1]] != 1 and currentFloorLayout[workingLocation[0] + 1][workingLocation[1]] != 0:
                #Checks that the room type has a door towards the east if the room to the east has a door towards the west
                if currentFloorLayout[workingLocation[0] + 1][workingLocation[1]].westConnection == True and possibleRooms[i - deletedRooms][1] == "0":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

                #Checks that the room type doesn't have a door to the east if the room to the east hasn't got a door to the west
                elif currentFloorLayout[workingLocation[0] + 1][workingLocation[1]].westConnection == False and possibleRooms[i - deletedRooms][1] == "1":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue


            #Checks the room type doesnt have a door pointing south into the edge of the floor
            if currentFloorLayout[workingLocation[0]][workingLocation[1] + 1] == 1 and possibleRooms[i - deletedRooms][2] == "1":
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue
                
            #Checks if the room type has a door pointing south into an empty space    
            elif currentFloorLayout[workingLocation[0]][workingLocation[1] + 1] == 0 and possibleRooms[i - deletedRooms][2] == "1":
                doorsToSpace += 1 #Increases the counted number of doors pointing towards an empty space

            #Checks if there is a room to the south of the current one
            elif currentFloorLayout[workingLocation[0]][workingLocation[1] + 1] != 1 and currentFloorLayout[workingLocation[0]][workingLocation[1] + 1] != 0:
                #Checks that the room type has a door towards the south if the room to the south has a door towards the north 
                if currentFloorLayout[workingLocation[0]][workingLocation[1] + 1].northConnection == True and possibleRooms[i - deletedRooms][2] == "0":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

                #Checks that the room type doesn't have a door to the south if the room to the south hasn't got a door to the north    
                elif currentFloorLayout[workingLocation[0]][workingLocation[1] + 1].northConnection == False and possibleRooms[i - deletedRooms][2] == "1":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

            
            #Checks the room type doesnt have a door pointing west into the edge of the floor
            if currentFloorLayout[workingLocation[0] - 1][workingLocation[1]] == 1 and possibleRooms[i - deletedRooms][3] == "1":
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue
                
            #Checks if the room type has a door pointing west into an empty space    
            elif currentFloorLayout[workingLocation[0] - 1][workingLocation[1]] == 0 and possibleRooms[i - deletedRooms][3] == "1":
                doorsToSpace += 1 #Increases the counted number of doors pointing towards an empty space

            #Checks if there is a west to the west of the current one
            elif currentFloorLayout[workingLocation[0] - 1][workingLocation[1]] != 1 and currentFloorLayout[workingLocation[0] - 1][workingLocation[1]] != 0:
                #Checks that the room type has a door towards the west if the room to the west has a door towards the east 
                if currentFloorLayout[workingLocation[0] - 1][workingLocation[1]].eastConnection == True and possibleRooms[i - deletedRooms][3] == "0":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue

                #Checks that the room type doesn't have a door towards the west if the room to the west hasn't got a door towards the east
                elif currentFloorLayout[workingLocation[0] - 1][workingLocation[1]].eastConnection == False and possibleRooms[i - deletedRooms][3] == "1":
                    DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                    continue


            if len(availableLocations) + 3 > remainingRooms and doorsToSpace >= 3:
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue

            elif len(availableLocations) + 2 > remainingRooms and doorsToSpace >= 2:
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue

            elif len(availableLocations) + 1 > remainingRooms and doorsToSpace >= 1:
                DeleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                continue

        chosenRoomType = random.choice(possibleRooms) #Randomly chooses a room type from the list of possible room types

        newPossibleLocations = []
        
        if chosenRoomType[0] == "1" and currentFloorLayout[workingLocation[0]][workingLocation[1] - 1] == 0:
            newPossibleLocations.append([workingLocation[0],workingLocation[1] - 1])

        if chosenRoomType[1] == "1" and currentFloorLayout[workingLocation[0] + 1][workingLocation[1]] == 0:
            newPossibleLocations.append([workingLocation[0] + 1,workingLocation[1]])

        if chosenRoomType[2] == "1" and currentFloorLayout[workingLocation[0]][workingLocation[1] + 1] == 0:
            newPossibleLocations.append([workingLocation[0],workingLocation[1] + 1])

        if chosenRoomType[3] == "1" and currentFloorLayout[workingLocation[0] - 1][workingLocation[1]] == 0:
            newPossibleLocations.append([workingLocation[0] - 1,workingLocation[1]])
            
        for i in range(len(newPossibleLocations)):
            if newPossibleLocations[i] not in availableLocations:
                availableLocations.append(newPossibleLocations[i])

        #Places a monster in the room next to the exit room
        if remainingRooms == totalRooms - 2:
            enemyPresent = True
            behaviour = random.choice(possibleBehaviours)
            enemyObject = Monster("Assets/EnemySpriteSheet.png",behaviour,floorNum)

        #All other rooms have no monster or box
        else:
            enemyPresent = False
            enemyObject = ""
        
        newRoom = Room(chosenRoomType,enemyPresent,enemyObject) #The room object is created

        currentFloorLayout[workingLocation[0]][workingLocation[1]] = newRoom #The room is added to the floor at the location

        #Removes the room's location from the list of available locations
        for i in range(len(availableLocations)):
            if availableLocations[i] == workingLocation:
                availableLocations.pop(i)
                break

        remainingRooms -= 1 #A room has been placed, so there is one less left to place

    #Counts how many rooms are on the floor
    totalRooms = 0
    for y in range(9):
        for x in range(9):
            if currentFloorLayout[x][y] != 0 and currentFloorLayout[x][y] != 1:
                totalRooms += 1

    #Calculates how many monsters and boxes need to be added to the floor
    enemiesToPlace = ((totalRooms / 5) * 2) - 1
    boxesToPlace = (totalRooms / 5) * 2

    #Runs while there are monsters or boxes left to place, and there are rooms without either left
    while (enemiesToPlace != 0 or boxesToPlace != 0) and totalRooms != 0:
        
        location = [random.randint(1,7),random.randint(1,7)] #Selects a random location on the floor

        #If the location is a room object
        if currentFloorLayout[location[0]][location[1]] != 0 and currentFloorLayout[location[0]][location[1]] != 1:
            #If there are both monsters and boxes left to be placed
            if enemiesToPlace > 0 and boxesToPlace > 0:
                #If the room is not the entrance or exit and doesn't have a box or monster in it already
                if location != exitRoom and location != entranceRoom and currentFloorLayout[location[0]][location[1]].enemyPresent[0] == False and currentFloorLayout[location[0]][location[1]].boxPresent[0] == False:

                    typeToPlace = random.randint(1,2) #Randomly selects a box or monster to be placed

                    #Places a box in the room
                    if typeToPlace == 1:
                        currentFloorLayout[location[0]][location[1]].boxPresent[0] = True
                        boxesToPlace -= 1

                    #Places a monster in the room
                    else:
                        currentFloorLayout[location[0]][location[1]].enemyPresent[0] = True
                        behaviour = random.choice(possibleBehaviours)
                        enemyObject = Monster("Assets/EnemySpriteSheet.png",behaviour,floorNum)
                        currentFloorLayout[location[0]][location[1]].enemyPresent = [True,enemyObject]
                        enemiesToPlace -= 1

            #If there are only boxes left to be placed
            elif enemiesToPlace == 0:
                #If the room is not the entrance or exit and doesn't have a box or monster in it already
                if location != exitRoom and location != entranceRoom and currentFloorLayout[location[0]][location[1]].enemyPresent[0] == False and currentFloorLayout[location[0]][location[1]].boxPresent[0] == False:        
                    #Places a box in the room
                    currentFloorLayout[location[0]][location[1]].boxPresent[0] = True
                    boxesToPlace -= 1

            #If there are only monsters left to be placed
            else:
                #If the room is not the entrance or exit and doesn't have a box or monster in it already
                if location != exitRoom and location != entranceRoom and currentFloorLayout[location[0]][location[1]].enemyPresent[0] == False and currentFloorLayout[location[0]][location[1]].boxPresent[0] == False:
                    #Places a monster in the room
                    currentFloorLayout[location[0]][location[1]].enemyPresent[0] = True
                    behaviour = random.choice(possibleBehaviours)
                    enemyObject = Monster("Assets/EnemySpriteSheet.png",behaviour,floorNum)
                    currentFloorLayout[location[0]][location[1]].enemyPresent = [True,enemyObject]
                    enemiesToPlace -= 1

            totalRooms -= 1 #Since a box or monster has been placed, the number of rooms left that can have something placed in them goes down by 1
    
    #Returns the finished 2D array of the floor layout and room objects
    return currentFloorLayout

def ShowFloorLayout(currentFloorLayout):

    #A larger 2D array used for the graphical version of the floor layout
    graphicalFloorLayout = [["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]

    #Checks every value in the floor layout
    for y in range(8):
        for x in range(8):
            #Checks if the current value is a room object
            if currentFloorLayout[x][y] != 0 and currentFloorLayout[x][y] != 1:
                #Replaces the room objects with a + symbol
                graphicalFloorLayout[((x - 1) * 2) + 1][((y - 1) * 2) + 1] = "+"
                #Shows if there is a door to the east of the room
                if currentFloorLayout[x][y].eastConnection == True:
                    graphicalFloorLayout[((x - 1) * 2) + 2][((y - 1) * 2) + 1] = "-"
                #Shows if there is a door to the west of the room
                if currentFloorLayout[x][y].westConnection == True:
                    graphicalFloorLayout[((x - 1) * 2)][((y - 1) * 2) + 1] = "-"
                #Shows if there is a door to the south of the room
                if currentFloorLayout[x][y].southConnection == True:
                    graphicalFloorLayout[((x - 1) * 2) + 1][((y - 1) * 2) + 2] = "|"
                #Shows if there is a door to the north of the room
                if currentFloorLayout[x][y].northConnection == True:
                    graphicalFloorLayout[((x - 1) * 2) + 1][((y - 1) * 2)] = "|"

    #Prints the 2D array to the python shell
    for y in range (15):
        line = ""
        for x in range (15):
            line += str(graphicalFloorLayout[x][y]) + " "
        print(line)

def DeleteRoomType():
    global possibleRooms, i, deletedRooms #Values used to delete a room type
    possibleRooms.pop(i - deletedRooms)   #Removes the room from the list of possible rooms
    deletedRooms += 1                     #Increases the count of rooms that have been deleted
