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
        
    def blockToData(self):
        self.CaseID = 0
