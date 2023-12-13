from Room import *
import random

def NewFloor(floorSize):
    entranceRoom = [4,4]
    entranceRoomObject = Room("1111")
    
    num1 = random.randint(1,4)
    if num1 == 1:
        exitRoom = [4,1]
        exitRoomObject = Room("0010")
    elif num1 == 2:
        exitRoom = [7,4]
        exitRoomObject = Room("0001")
    elif num1 == 3:
        exitRoom = [4,7]
        exitRoomObject = Room("1000")
    else:
        exitRoom = [1,4]
        exitRoomObject = Room("0100")

    print(exitRoom)
    
    currentFloorLayout = [[1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1]]
    currentFloorLayout[entranceRoom[0]][entranceRoom[1]] = entranceRoomObject
    currentFloorLayout[exitRoom[0]][exitRoom[1]] = exitRoomObject

    return currentFloorLayout
    
