from Room import * #A separate python file that holds the room class
import random      #Used for anything that requires randomness
import copy        #Used to make copies of lists and arrays that are completely separate from the original 

def NewFloor(floorSize = "large"):
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

    #A list of all the room types that will be copied to another variable to keep track of all the rooms that could be placed in a location
    roomTypes = ["0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"] 

    #Starts loop to place rooms while there are still rooms to place
    while remainingRooms > 0 and len(availableLocations) > 0:
        workingLocation = availableLocations[0] #Places a room at the first listed available location

        possibleRooms = copy.deepcopy(roomTypes) #Copies over the room types to a new variable so it can be manipulated without modifying the full list

        deletedRooms = 0 #Keeps track of how many room types have been deleted from possibleRooms

        for i in range(len(possibleRooms)):

            #Special condition for the first two rooms that are placed between the start and end room
            if roomsPlaced < 4:
                
                #Checks if the exit was placed in a vertical line with the entrance
                if exitRoom[0] == 4:
                    
                    #Makes sure the placed room will have a door above and below it so there is a path from the entrance to the exit no matter how the other rooms are placed
                    if possibleRooms[i - deletedRooms][0] == "0" or possibleRooms[i - deletedRooms][2] == "0": 
                        deleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                        continue         #Skips to the next iteration of the for loop
                        
                #For when the exit is placed in a horizontal line with the entrance
                else:

                    #Makes sure the placed room will have a door to the left and right of it so there is a path from the entrance to the exit no matter how the other rooms are placed
                    if possibleRooms[i - deletedRooms][1] == "0" or possibleRooms[i - deletedRooms][3] == "0":
                        deleteRoomType() #Deletes the room type from the list if it doesn't fit the conditions
                        continue         #Skips to the next iteration of the for loop


def deleteRoomType():
    global possibleRooms, i, deletedRooms #Values used to delete a room type
    possibleRooms.pop(i - deletedRooms)   #Removes the room from the list of possible rooms
    deletedRooms += 1                     #Increases the count of rooms that have been deleted
