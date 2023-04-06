# TODO Johnny
import datetime
import struct
import os
import pickle

from Block_Chain import *
# INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
# add zeros to respective state to equal 12 characters


#initial get iso time
def getUnixTime():
    presentDate = datetime.datetime.now()
    isoTime = presentDate.isoformat()
    return  isoTime

def byteCounter(f):
    
    return len(struct.pack('f', f))

#converts stored double back to iso format
def getIso8601Timestamp(double_timestamp):
    timestamp = struct.unpack('d', double_timestamp)[0]
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    iso8601_timestamp = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

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
        
    def updateTimestamp(self,x):
        self.Timestamp = x
        
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
    
    #TODO does not return a 8 byte double
    def getDoubleTimestamp(self):
        dt = datetime.datetime.strptime(self.getTimestamp(), '%Y-%m-%dT%H:%M:%S.%f')
        now = datetime.datetime.timestamp(dt)
        now_bytes = struct.pack('d', float(now))
        print("byte verify: " + str(len(now_bytes)))
        return now_bytes
    
            
    def printBlock(self):
        ret ="Static Block contents: --------------------------------------"
        ret += "\nPrevious hash: "+ str(self.PreviousHash)
        ret +=("\nTimestamp: " + str(self.Timestamp))
        ret +=("\nCID: " + str(self.CID))
        ret +=("\nEID: " + str(self.EID))
        ret +=("\nState: " + str(self.State))
        ret +=("\nData Length: " + str(self.DataLen))
        ret +=("\nData: " + str(self.Data))
        ret +=("\n-------------------------------------------------------------")
        return ret
    
    def blockToBytes(self):
        block = []
        packed1 = struct.pack("32s", self.getPreviousHash().encode())
        packed2 = self.getDoubleTimestamp()
        packed3 = struct.pack("16s", str(self.getCID()).encode())
        packed4 = struct.pack("I", self.getEID())
        packed5 = struct.pack("12s", self.getState().encode())
        packed6 = struct.pack("I", self.getDataLength())
        packed7 = struct.pack((str(len(self.getData()))+'s'), self.getData().encode())
        
        block.append(packed1)  
        block.append(packed2) 
        block.append(packed3) 
        block.append(packed4) 
        block.append(packed5) 
        block.append(packed6) 
        block.append(packed7) 
    
        fileName = str(self.getTimestamp()).replace(":", "-")+".raw"
        filePath = os.path.join('./BlockFolder', fileName)
        
        if not os.path.exists('./BlockFolder'):
            os.makedirs('./BlockFolder')
        with open(filePath, "wb") as out:
            out.write(pickle.dumps(block))
            
    def fillFromFile(self, file):
        with open(file,'rb') as f:
            contents = pickle.load(f)
        

        unpacked1 = struct.unpack("32s", contents[0])
        unpacked2 = getIso8601Timestamp(contents[1])
        unpacked3 = struct.unpack("16s", contents[2])
        unpacked4 = struct.unpack("I", contents[3])
        unpacked5 = struct.unpack("12s", contents[4])
        unpacked6 = struct.unpack("I", contents[5])
        
        unpacked1= "".join(str(i) for i in unpacked1)
        unpacked3= "".join(str(i) for i in unpacked3)
        unpacked4= "".join(str(i) for i in unpacked4)
        unpacked5= "".join(str(i) for i in unpacked5)
        unpacked6= "".join(str(i) for i in unpacked6)
        
        
        unpacked7 = struct.unpack(unpacked6+'s', contents[6])
        unpacked7= "".join(str(i) for i in unpacked7)
        
        
        self.setPreviousHash(unpacked1[2:-1])
        self.updateTimestamp(unpacked2)
        self.setCID(unpacked3[2:-1])
        self.setEID(unpacked4)
        self.setState(unpacked5[2:-1].lstrip('0'))
        self.setDataLength(unpacked6)
        self.setData(unpacked7[2:-1])
        
        


# b = Block()
# b.setCID(9269517611667620)
# b.setData("uwF6MJKlWZ6G1JQQuqXRVHAwYIusJQBhhL7KFtrnxnN9xTwhESWbAi6MI09OfyGYUFbp8vUMEJcwCIJInReYggGt9HsS3QzjDc1h")
# b.setEID(2169)
# b.setState("00000INITIAL")
# b.setPreviousHash("261913b71a13306d63d65612875ead13")
# b.setTimestamp()
# b.setDataLength(100)
# b.printBlock()
# print(str(b.getDoubleTimestamp()))

# print(str(getIso8601Timestamp(b.getDoubleTimestamp())))
# b.blockToBytes()
