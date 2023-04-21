# TODO Johnny
import os
import Data
from Data import *
from Block import Block
from Block import getIso8601Timestamp
from hashlib import sha256
import uuid
class BlockChain:   
    def __init__(self):
        self.datalist = [] 
        self.blockList = []
        self.load_data()
       
    def dataExists(self, newData):
        for d in self.datalist:
            if d.CaseID == newData.CaseID and d.EvidenceID == newData.EvidenceID:
                return d
        return False
    
    def blockExists(self, newData):
        for d in self.blockList:
            if d.CID == newData.CaseID and d.EID == newData.EvidenceID:
                return d
        return False
    
    def getLatestHash(self):
        print(str(len(self.blockList)))
        input = pickle.dumps(self.blockList[-1])
        hash = sha256(input).digest()
        return hash
    
    def reload(self):
        self.blockList.clear()
        self.datalist.clear()
        self.load_data()
        
    def load_data(self):
        byteCount = 90
        
        
        file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')

        if not os.path.exists(file_path):
            return # No BC to load. Leave BC structure empty.

        
        with open(file_path, "rb") as f:
            contents = f.read()
            file_size = os.path.getsize(file_path)
        
        
        initBlock = Block()
        initBlock.fillFromFile()
        initData = Data()
        initData.blockToData(initBlock)
        
        self.datalist.append(initData) 
        self.blockList.append(initBlock)
        
        while byteCount < int(file_size) and int(file_size) != 0:
            
            if(file_size == 90):
                break
            temp = Data()
            newBlock = Block()

            unpacked1 = struct.unpack("32s", contents[byteCount:byteCount+32])
            byteCount += 32
            unpacked2 = getIso8601Timestamp(contents[byteCount:byteCount +8])
            byteCount += 8
            unpacked3 = struct.unpack("16s", contents[byteCount:byteCount +16])[0]
            cid_uuid = uuid.UUID(bytes=unpacked3)

            unpacked3 = str(cid_uuid)
            print(unpacked3)
            
            byteCount += 16
            unpacked4 = struct.unpack("I", contents[byteCount:byteCount +4])
            byteCount += 4
            unpacked5 = struct.unpack("12s", contents[byteCount:byteCount +12])
            byteCount += 12
            unpacked6 = struct.unpack("I", contents[byteCount:byteCount +4])
            byteCount += 4
            
            unpacked1= "".join(str(i) for i in unpacked1)
            unpacked3= "".join(str(i) for i in unpacked3)
            unpacked4= "".join(str(i) for i in unpacked4)
            unpacked5= "".join(str(i) for i in unpacked5)
            unpacked6= "".join(str(i) for i in unpacked6)
            
            countForSeven = int(unpacked6)+byteCount
            unpacked7 = struct.unpack(unpacked6+'s', contents[byteCount:countForSeven])
            byteCount += int(unpacked6)
            unpacked7= "".join(str(i) for i in unpacked7)
            
            
            newBlock.setPreviousHash(unpacked1[2:-1])
            newBlock.updateTimestamp(unpacked2)
            newBlock.setCID(unpacked3[2:-1])
            newBlock.setEID(unpacked4)
            newBlock.setState(unpacked5[2:-1])
            newBlock.setDataLength(unpacked6)
            newBlock.setData(unpacked7[2:-1])
            
            
            temp.blockToData(newBlock)
            self.blockList.append(newBlock)

            x = self.dataExists(temp)
            if x == False:
                self.datalist.append(temp)  
            else:
                x.state = temp.state
                
    def printBC(self):
        print("\nBlock list count: "+str(len(self.datalist)))
        print("datalist contents: ")
        for i in self.datalist:
            print(i.toString()+'\n')
        print("\nBlock list count: "+str(len(self.blockList)))
        print("\nBlock list contents: ")
        for obj in self.blockList:
            print(obj.printBlock())   
        

BC = BlockChain()  # Friendly name for us to import
# BC.printBC()