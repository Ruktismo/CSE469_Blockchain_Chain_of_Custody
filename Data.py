# TODO Johnny
import Block
import os
import struct

def tupHex(tuple):
    newList = []
    for i in tuple:
        newList.append(hex(i)) 
    return newList

class Data:
    def __init__(self):
        self.CaseID = 0
        self.EvedanceID = 0
        self.state = 0
        # INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
        # -1,                                   0,          2,          3,          4,          5
        #states need to be padded to 12 bytes
    def importData(self, file):
        filesize = os.path.getsize(file)
        with open(file,'rb') as f:
                block = f.read(filesize)
                block = struct.unpack(str(filesize)+"B",block)
        part = block[0:17]
        part = tupHex(part)
        print(part)
d = Data()
d.importData("2023-03-23T001804.594218.raw")