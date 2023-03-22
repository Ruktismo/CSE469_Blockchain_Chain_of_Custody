# TODO Johnny
import os
import datetime
import time

def getUnixTime():
   
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000 
    return unix_timestamp

class Block:
    def __init__(self):
        self.PreviousHash = None
        self.Timestamp = None
        self.CID = 0
        self.EID = 0
        self.State = None
        self.DataLen = 0
        self.Data = None
        
    def getPreviousHash(self):
        return self.PreviousHash
    
    def setPreviousHash(self, hash):
        self.PreviousHash = hash

    def getTimestamp(self):
        return self.Timestamp

    def setTimestamp(self, time):
        self.Timestamp = time
    
    def getCID(self):
        return self.CID

    def setCID(self, cid):
        self.CID = cid

    def getEID(self):
        return self.EID

    def setEID(self, eid):
        self.EID = eid
        
    def getState(self):
        return self.State

    def setEID(self, state):
        self.State = state
        
    def getDataLength(self):
        return self.DataLen

    def setDataLength(self, x):
        self.DataLen = x
        
    def getData(self):
        return self.Data

    def setData(self, data):
        self.Data = data
        
class static_block:
    #padding info (length in bytes) for state
    bytelen12 = 12
    #actual state assignment
    stateVar = b'\2'
    
    PreviousHash = "26 19 13 b7 1a 13 30 6d 63 d6 56 12 87 5e ad 13 ed 28 1b 2f 70 f9 c7 13 76 12 47 f4 7a 9f f7 ee "
    
    #function defined at the top, need to change to make 8 byte long float 
    Timestamp = getUnixTime()
    CID = 9269517611667619
    EID = 2179
    
    #force padding of "a"s to the actual state assignment
    State = stateVar.rjust(bytelen12, b'\a')
    #length of following Data
    DataLen = 100
    #Data at length of 100
    Data = "uwF6MJKlWZ6G1JQQuqXRVHAwYIusJQBhhL7KFtrnxnN9xTwhESWbAi6MI09OfyGYUFbp8vUMEJcwCIJInReYggGt9HsS3QzjDc1h"
        
print("Static Block contents: ")
print("Previous hash: " + static_block.PreviousHash)
print("Timestamp: " + str(static_block.Timestamp))
print("CID: " + str(static_block.CID))
print("EID: " + str(static_block.EID))
print("State: " + str(static_block.State))
print("Data Length: " + str(static_block.DataLen))
print("Data: " + static_block.Data)
