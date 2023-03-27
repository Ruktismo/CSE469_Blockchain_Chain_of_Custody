# TODO Johnny
import os
import struct
import Data
import Block

class BlockChain:   
    def __init__(self):
        self.datalist = [] 
        self.dir = './BlockFolder'
        # Dir of block chain
       
    
    def load_data(self):
        # load in all data from disk and make data classes
        
        for filename in os.listdir(self.dir):
            f = os.path.join(self.dir, filename)
            if os.path.isfile(f):
                print(f)
                temp = f
                #Data() function to extract info
                self.datalist.append(temp)  
        # for d in self.datalist():
        #     print(d)    
        # filesize = os.path.getsize(filepath)
        # with open(filepath,'rb') as f:
        #         block = f.read(filesize)
        #         block = struct.unpack(str(filesize)+"B",block)
        

temp = BlockChain()
temp.load_data()