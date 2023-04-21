# TODO Johnny
import os
import pickle
import struct
from Block import Block

def removePadding(s):
    s = bytearray(s, 'utf-8')
    s = s.replace(b'\x00', b'')
    s = s.decode('utf-8')
    return s
class Data:
    def __init__(self):
        self.CaseID = 0
        self.EvidenceID = 0
        self.state = 0
        # INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
        # add zeros to respective state to equal 12 characters
   
    def blockToData(self,block):

        self.CaseID = block.getCID()
        # print("CID: "+ str(self.CaseID))
        self.EvidenceID = block.getEID()
        # print("EID: " + str(self.EvidenceID))
        self.state = removePadding(block.getState())
        print("test: "+ removePadding(block.getState()))
        
        
    def toString(self):
        return "Case ID: " + str(self.CaseID) +'\n' + "Evidence ID: " + str(self.EvidenceID) +'\n' + "State: " + str(self.state) 
    
