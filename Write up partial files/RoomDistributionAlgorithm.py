from Room import * #A separate python file that holds the room class
import random      #Used for anything that requires randomness

def NewFloor(floorSize = "large"):

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

    #Creates the 2D array that the floor layout and all the room objects will be stored inside
    currentFloorLayout = [[1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1]]
