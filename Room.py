class Room():
    def __init__(self,roomID):
        self.roomID = roomID                   #String
        
        if roomID[0] == "1":                          #Boolean
            self.northConnection = True 
        else:
            self.northConnection = False
            
        if roomID[1] == "1":                          #Boolean
            self.eastConnection = True
        else:
            self.eastConnection = False
            
        if roomID[2] == "1":                          #Boolean
            self.southConnection = True 
        else:
            self.southConnection = False
            
        if roomID[3] == "1":                          #Boolean
            self.westConnection = True 
        else:
            self.westConnection = False
            
        self.timesItemSearched = 0             #Integer from 0 - 3
        self.enemyPresent = [False,""]         #List = [Boolean,Object]
        self.boxPresent = [False,False]        #List = [Boolean,Boolean]
