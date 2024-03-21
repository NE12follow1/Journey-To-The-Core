class Room():
    def __init__(self,roomID,enemyPresent = False,enemyObject = "",boxPresent = False,isExitRoom = False):
        self.roomID = roomID                   #String determining the type of room it is
        
        if roomID[0] == "1":                   #Boolean determining if the room connects to another room above it
            self.northConnection = True 
        else:
            self.northConnection = False
            
        if roomID[1] == "1":                   #Boolean determining if the room connects to another room to the right of it
            self.eastConnection = True
        else:
            self.eastConnection = False
            
        if roomID[2] == "1":                   #Boolean determining if the room connects to another room below it
            self.southConnection = True 
        else:
            self.southConnection = False
            
        if roomID[3] == "1":                   #Boolean determining if the room connects to another room to the left of it
            self.westConnection = True 
        else:
            self.westConnection = False
            
        self.itemSearched = False                      #Boolean determining if there is still a place to search for an item in the room
        self.enemyPresent = [enemyPresent,enemyObject] #List = [Boolean for the existence of an enemy in the room, Object for the enemy itself]
        self.boxPresent = [boxPresent,False]           #List = [Boolean for the existence of an equipment box in the room, Boolean for whether the box is or isn't open]
        self.isExitRoom = isExitRoom                   #Boolean determining if this room is the exit room
