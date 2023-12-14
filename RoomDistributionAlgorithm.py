from Room import *
import random

def NewFloor(floorSize = "large"):
    #Defines where and what the entrance room is
    entranceRoom = [4,4]
    entranceRoomObject = Room("1111")

    #Handles the 3 different floor sizes and what each means to the total number of rooms
    if floorSize.lower() == "small":
        totalRooms = 15
    elif floorSize.lower() == "medium":
        totalRooms = 20
    else:
        totalRooms = 25

    #Randomly chooses one of the 4 sides of the max floor size to be the exit room
    exitRoomType = random.randint(1,4)
    #Defines where and what the exit room is due to which side was chosen
    if exitRoomType == 1:
        exitRoom = [4,1]
        exitRoomObject = Room("0010")
    elif exitRoomType == 2:
        exitRoom = [7,4]
        exitRoomObject = Room("0001")
    elif exitRoomType == 3:
        exitRoom = [4,7]
        exitRoomObject = Room("1000")
    else:
        exitRoom = [1,4]
        exitRoomObject = Room("0100")

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

    roomsPlaced = 2

    roomTypes = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

    while remainingRooms > 0:
        workingLocation = availableLocations[0]
        possibleRooms = roomTypes

        deletedRooms = 0
        for i in range(len(possibleRooms)):
            
            roomDeleted = False

            if roomsPlaced < 4:
                if exitRoom[0] == 4:
                    if possibleRooms[i - deletedRooms][0] == "0" or possibleRooms[i - deletedRooms][2] == "0":
                        possibleRooms.pop(i - deletedRooms)
                        deletedRooms += 1
                        roomDeleted = True
                else:
                    if possibleRooms[i - deletedRooms][1] == "0" or possibleRooms[i - deletedRooms][3] == "0":
                        possibleRooms.pop(i - deletedRooms)
                        deletedRooms += 1
                        roomDeleted = True

            doorsToSpace = 0
            
            if currentFloorLayout[workingLocation[0]][workingLocation[0] - 1] == 1 and roomDeleted == False:
                if possibleRooms[i - deletedRooms][0] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
            elif currentFloorLayout[workingLocation[0]][workingLocation[0] - 1] == 0 and possibleRooms[i - deletedRooms][0] == "0" and roomDeleted == False:
                doorsToSpace += 1

            elif currentFloorLayout[workingLocation[0]][workingLocation[0] - 1] == 0 and possibleRooms[i - deletedRooms][0] == "1" and roomDeleted == False:
                pass
            
            elif roomDeleted == False:
                if currentFloorLayout[workingLocation[0]][workingLocation[0] - 1].southConnection == True and possibleRooms[i - deletedRooms][0] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
                elif currentFloorLayout[workingLocation[0]][workingLocation[0] - 1].southConnection == False and possibleRooms[i - deletedRooms][0] == "1":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True

            if currentFloorLayout[workingLocation[0] + 1][workingLocation[0]] == 1 and roomDeleted == False:
                if possibleRooms[i - deletedRooms][1] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
            elif currentFloorLayout[workingLocation[0] + 1][workingLocation[0]] == 0 and possibleRooms[i - deletedRooms][1] == "0" and roomDeleted == False:
                doorsToSpace += 1

            elif currentFloorLayout[workingLocation[0] + 1][workingLocation[0]] == 0 and possibleRooms[i - deletedRooms][1] == "1" and roomDeleted == False:
                pass
            
            elif roomDeleted == False:
                if currentFloorLayout[workingLocation[0] + 1][workingLocation[0]].westConnection == True and possibleRooms[i - deletedRooms][1] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
                elif currentFloorLayout[workingLocation[0] + 1][workingLocation[0]].westConnection == False and possibleRooms[i - deletedRooms][1] == "1":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True

            if currentFloorLayout[workingLocation[0]][workingLocation[0] + 1] == 1 and roomDeleted == False:
                if possibleRooms[i - deletedRooms][2] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
            elif currentFloorLayout[workingLocation[0]][workingLocation[0] + 1] == 0 and possibleRooms[i - deletedRooms][2] == "0" and roomDeleted == False:
                doorsToSpace += 1

            elif currentFloorLayout[workingLocation[0]][workingLocation[0] + 1] == 0 and possibleRooms[i - deletedRooms][2] == "1" and roomDeleted == False:
                pass
            
            elif roomDeleted == False:
                if currentFloorLayout[workingLocation[0]][workingLocation[0] + 1].northConnection == True and possibleRooms[i - deletedRooms][2] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
                elif currentFloorLayout[workingLocation[0]][workingLocation[0] + 1].northConnection == False and possibleRooms[i - deletedRooms][2] == "1":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True

            if currentFloorLayout[workingLocation[0] - 1][workingLocation[0]] == 1 and roomDeleted == False:
                if possibleRooms[i - deletedRooms][3] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
            elif currentFloorLayout[workingLocation[0] - 1][workingLocation[0]] == 0 and possibleRooms[i - deletedRooms][3] == "0" and roomDeleted == False:
                doorsToSpace += 1

            elif currentFloorLayout[workingLocation[0] - 1][workingLocation[0]] == 0 and possibleRooms[i - deletedRooms][3] == "1" and roomDeleted == False:
                pass
            
            elif roomDeleted == False:
                if currentFloorLayout[workingLocation[0] - 1][workingLocation[0]].northConnection == True and possibleRooms[i - deletedRooms][3] == "0":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True
                    
                elif currentFloorLayout[workingLocation[0] - 1][workingLocation[0]].northConnection == False and possibleRooms[i - deletedRooms][3] == "1":
                    possibleRooms.pop(i - deletedRooms)
                    deletedRooms += 1
                    roomDeleted = True

            if roomDeleted == False:
                if len(availableLocations) + 3 > remainingRooms:
                    if doorsToSpace >= 3:
                        possibleRooms.pop(i - deletedRooms)
                        deletedRooms += 1
                        roomDeleted = True

                elif len(availableLocations) + 2 > remainingRooms:
                    if doorsToSpace >= 2:
                        possibleRooms.pop(i - deletedRooms)
                        deletedRooms += 1
                        roomDeleted = True

                elif len(availableLocations) + 1 > remainingRooms:
                    if doorsToSpace >= 1:
                        possibleRooms.pop(i - deletedRooms)
                        deletedRooms += 1
                        roomDeleted = True

        chosenRoomType = random.choice(possibleRooms)

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
            if newPossibleLocations[i] in availableLocations:
                pass
            else:
                availableLocations.append(newPossibleLocations[i])

        newRoom = Room(chosenRoomType)

        currentFloorLayout[workingLocation[0]][workingLocation[1]] = newRoom

        for i in range(len(availableLocations)):
            if availableLocations[i] == workingLocation:
                availableLocations.pop(i)
                break

        roomsPlaced += 1
        remainingRooms -= 1
        
    #Returns the finished 2D array of the floor layout and room objects
    return currentFloorLayout
    
currentFloorLayout = NewFloor("large")
