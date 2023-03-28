# TODO Johnny
import datetime
import struct
import os
# INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
# add zeros to respective state to equal 12 characters


#initial get iso time
def getUnixTime():
    presentDate = datetime.datetime.now()
    isoTime = presentDate.isoformat()
    return  isoTime

def byteCounter(str):
    return len(str.encode("utf-8"))

#converts stored double back to iso format
def getIso8601Timestamp(double_timestamp):
    unix_timestamp = struct.unpack('d', double_timestamp)[0] / 1000
    dt = datetime.datetime.fromtimestamp(unix_timestamp)
    iso8601_timestamp = dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return iso8601_timestamp

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

    #auto grabs current unix time, no params needed
    def setTimestamp(self):
        self.Timestamp = getUnixTime()
    
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

    def setState(self, state):
        self.State = state
        
    def getDataLength(self):
        return self.DataLen

    #TODO pack x into a 4 byte int
    def setDataLength(self, x):
        self.DataLen = x
        
    def getData(self):
        return self.Data

    def setData(self, data):
        self.Data = data
    
    #TODO does not return a 4 byte double
    def getDoubleTimestamp(self):
        dt = datetime.datetime.strptime(self.getTimestamp(), '%Y-%m-%dT%H:%M:%S.%f')
        unix_timestamp = datetime.datetime.timestamp(dt) * 1000
        double_timestamp = struct.pack('d', unix_timestamp)
        # print(byteCounter(str(double_timestamp)))
        return double_timestamp
    

        
    #TODO need to work on formatting this
    def blockToBytes(self):

        # block = bytes((str(self.getPreviousHash())),'utf-8')
        
        # # print("***"+ self.getTimestamp())
        # # y = self.getDoubleTimestamp()
        # # print("***"+str(y))
        # # print("***"+str(getIso8601Timestamp(y)))
        
        # #TODO need to make time a nicer hex
        # block += bytes(str(self.getDoubleTimestamp()),'utf-8')
        # block += bytes(hex(self.getCID())[2:],'utf-8')
        # block += bytes(hex(self.getEID())[2:],'utf-8')
        
        # state = self.getState().encode('utf-8')
        # block += bytes(state.hex(),'utf-8')
        
        # block += bytes(hex(self.getDataLength())[2:],'utf-8')
        # s = self.getData().encode('utf-8')
        # block += bytes(s.hex(),'utf-8')

        block = self.getPreviousHash()
        block += str(self.getDoubleTimestamp())
        block += str(self.getCID())
        block += str(self.getEID())
        block += str(self.getState())
        block += str(self.getDataLength())
        block += str(self.getData())
        fileName = str(self.getTimestamp()).replace(":", "-")+".raw"
       # print(fileName)
       #TODO should turn "block" into hex or something but file is written as bytes
        filePath = os.path.join('./BlockFolder', fileName)
        if not os.path.exists('./BlockFolder'):
            os.makedirs('./BlockFolder')
        out = open(filePath, "wb")
        out.write(bytes(block, 'utf-8'))
        
    def blockByteCounter(self):
        print("Block byte counts: --------------------------------------")
        print("Previous hash: " + str(byteCounter(self.PreviousHash))  )
        print("Timestamp: " + str(byteCounter(str(self.getDoubleTimestamp()))))
        print("CID: " + str(byteCounter(str(self.CID))) )
        print("EID: " + str(byteCounter(str(self.EID))))
        print("State: " + str(byteCounter(str(self.State))))
        print("Data Length: " + str(byteCounter(str(self.DataLen))))
        print("Data: " + str(byteCounter(self.Data)))
    print("-------------------------------------------------------------")
        
    def printBlock(self):
        print("Static Block contents: --------------------------------------")
        print("Previous hash: " + self.PreviousHash)
        print("Timestamp: " + str(self.Timestamp))
        print("CID: " + str(self.CID))
        print("EID: " + str(self.EID))
        print("State: " + str(self.State))
        print("Data Length: " + str(self.DataLen))
        print("Data: " + self.Data)
        print("-------------------------------------------------------------")
        
# class static_block:
#     #padding info (length in bytes) for state
#     bytelen12 = 12
#     #actual state assignment
#     stateVar = b'\2'
    
#     PreviousHash = "26 19 13 b7 1a 13 30 6d 63 d6 56 12 87 5e ad 13 ed 28 1b 2f 70 f9 c7 13 76 12 47 f4 7a 9f f7 ee "
    
#     #function defined at the top, need to change to make 8 byte long float 
#     Timestamp = getUnixTime()
#     CID = 9269517611667619
#     EID = 2179
    
#     #force padding of "a"s to the actual state assignment
#     State = stateVar.rjust(bytelen12, b'\a')
#     #length of following Data
#     DataLen = 100
#     #Data at length of 100
#     Data = "uwF6MJKlWZ6G1JQQuqXRVHAwYIusJQBhhL7KFtrnxnN9xTwhESWbAi6MI09OfyGYUFbp8vUMEJcwCIJInReYggGt9HsS3QzjDc1h"
        
# print("Static Block contents: ")
# print("Previous hash: " + static_block.PreviousHash)
# print("Timestamp: " + str(static_block.Timestamp))
# print("CID: " + str(static_block.CID))
# print("EID: " + str(static_block.EID))
# print("State: " + str(static_block.State))
# print("Data Length: " + str(static_block.DataLen))
# print("Data: " + static_block.Data)

b = Block()
b.setCID(9269517611667619)
b.setData("uwF6MJKlWZ6G1JQQuqXRVHAwYIusJQBhhL7KFtrnxnN9xTwhESWbAi6MI09OfyGYUFbp8vUMEJcwCIJInReYggGt9HsS3QzjDc1h")
b.setEID(2179)
b.setState("000CHECKEDIN")
b.setPreviousHash("261913b71a13306d63d65612875ead13")
b.setTimestamp()
b.setDataLength(100)
b.printBlock()

# b.blockToBytes()
b.blockByteCounter()