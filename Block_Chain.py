# TODO Johnny
import os
import struct
import Data
from Data import Data

class BlockChain:   
    def __init__(self):
        self.datalist = [] 
        self.dir = './BlockFolder'
        # Dir of block chain
       
    
    def load_data(self):
        # load in all data from disk and make data classes
        temp = Data()
        for filename in os.listdir(self.dir):
            f = os.path.join(self.dir, filename)
            if os.path.isfile(f):
                # print(f)
                temp = Data()
                #TODO finish blockToData()
                temp.blockToData(f)
                self.datalist.append(temp)  
                
        #show datalist content for shits and gigs
        for i in self.datalist:
            print(i.toString()+'\n')
        

# x = BlockChain()
# x.load_data()
