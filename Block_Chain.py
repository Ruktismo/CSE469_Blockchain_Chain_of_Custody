# TODO Johnny
import os
import Data
from Data import *
from Block import Block

class BlockChain:   
    def __init__(self):
        self.datalist = [] 
        self.blockList = []
        self.dir = './BlockFolder'
        self.load_data()
        # Dir of block chain
       
    def dataExists(self, newData):
        for d in self.datalist:
            if d.CaseID == newData.CaseID and d.EvidenceID == newData.EvidenceID:
                return d
        return False
    
    def load_data(self):
        # load in all data from disk and make data classes
        temp = Data()
        for filename in os.listdir(self.dir):
            f = os.path.join(self.dir, filename)
            if os.path.isfile(f):
                
                temp = Data()
                newBlock = Block()
                
                temp.blockToData(f)
                newBlock.fillFromFile(f)
                
                self.blockList.append(newBlock)
                # newBlock.printBlock()
                x = self.dataExists(temp)
                if x == False:
                    self.datalist.append(temp)  
                else:
                    x.state = temp.state
                
        # show datalist content 
        print("\nBlock list count: "+str(len(self.datalist)))
        print("datalist contents: ")
        for i in self.datalist:
            print(i.toString()+'\n')
        print("\nBlock list count: "+str(len(self.blockList)))
        print("\nBlock list contents: ")
        for obj in self.blockList:
            print(obj.printBlock())
        

x = BlockChain()

