# TODO Johnny
import datetime
import struct
import os
import pickle

#from Block_Chain import *
# INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
# add zeros to respective state to equal 12 characters


#initial get iso time
def getUnixTime():
    presentDate = datetime.datetime.now()
    isoTime = presentDate.isoformat()
    return  isoTime

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
        
        packed1 = struct.pack("32s", self.getPreviousHash().encode())
        packed2 = self.getDoubleTimestamp()
        packed3 = struct.pack("16s", str(self.getCID()).encode())
        packed4 = struct.pack("I", self.getEID())
        packed5 = struct.pack("12s", self.getState().encode())
        packed6 = struct.pack("I", self.getDataLength())
        packed7 = struct.pack((str(len(self.getData()))+'s'), self.getData().encode())
        
        block = (packed1) + (packed2) + (packed3) + (packed4) + (packed5) + (packed6) + (packed7)

    
        # fileName = "./BC.raw"
        
        
        # with open(fileName, "ab") as out:
        #             out.write(block)
        directory_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')

        directory = os.path.dirname(directory_path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(directory_path):
            with open(directory_path, 'wb') as f:
                f.write(block)
        else:
            with open(directory_path, "ab") as f:
                f.write(block)
            
        f.close()          
            
    def fillFromFile(self):
            
        file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')

        directory = os.path.dirname(file_path)

        if not os.path.exists(directory):
            os.makedirs(directory)


        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.close()
        
        with open(file_path, "rb") as f:
            contents = f.read()
        

        unpacked1 = struct.unpack("32s", contents[0:32])
        unpacked2 = getIso8601Timestamp(contents[32:40])
        unpacked3 = struct.unpack("16s", contents[40:56])
        unpacked4 = struct.unpack("I", contents[56:60])
        unpacked5 = struct.unpack("12s", contents[60:72])
        unpacked6 = struct.unpack("I", contents[72:76])
        
        unpacked1= "".join(str(i) for i in unpacked1)
        unpacked3= "".join(str(i) for i in unpacked3)
        unpacked4= "".join(str(i) for i in unpacked4)
        unpacked5= "".join(str(i) for i in unpacked5)
        unpacked6= "".join(str(i) for i in unpacked6)
        
        countForSeven = int(unpacked6)+76
        unpacked7 = struct.unpack(unpacked6+'s', contents[76:countForSeven])
        unpacked7= "".join(str(i) for i in unpacked7)
        
        
        self.setPreviousHash(unpacked1[2:-1])
        self.updateTimestamp(unpacked2)
        self.setCID(unpacked3[2:-1])
        self.setEID(unpacked4)
        self.setState(unpacked5[2:-1].lstrip('0'))
        self.setDataLength(unpacked6)
        self.setData(unpacked7[2:-1])
        
        


# b = Block()
# b.setCID(9269517612799130)
# b.setData("uwF6MJKlWZqqqqq")
# b.setEID(2133)
# b.setState("000CHECKEDIN")
# b.setPreviousHash("261913b71a13306d63d65612875ead13")
# b.setTimestamp()
# b.setDataLength(15)

# b.blockToBytes()

# b.setCID(9269517612799150)
# b.setData("uwF6MJKlWZ")
# b.setEID(2113)
# b.setState("000CHECKEDIN")
# b.setPreviousHash("261913b71a13306d63d65612875ead13")
# b.setTimestamp()
# b.setDataLength(10)

# b.blockToBytes()