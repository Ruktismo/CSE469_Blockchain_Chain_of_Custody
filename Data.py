# TODO Johnny
import os
import pickle
import struct
from Block import Block
class Data:
    def __init__(self):
        self.CaseID = 0
        self.EvidenceID = 0
        self.state = 0
        # INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
        # add zeros to respective state to equal 12 characters
   
    def blockToData(self,block):
        # with open("BC.raw",'rb') as f:
        #     contents = f.read()
        
        # unpacked3 = struct.unpack("16s", contents[40:56])
        # unpacked4 = struct.unpack("I", contents[56:60])
        # unpacked5 = struct.unpack("12s", contents[60:72])
        
        # unpacked3= "".join(str(i) for i in unpacked3)
        # unpacked4= "".join(str(i) for i in unpacked4)
        # unpacked5= "".join(str(i) for i in unpacked5)
        
        # self.CaseID = unpacked3[2:-1]
        # # print("CID: "+ str(self.CaseID))
        # self.EvidenceID = unpacked4
        # # print("EID: " + str(self.EvidenceID))
        # self.state = unpacked5[2:-1].lstrip('0')
        # print("state: " + str(self.state))
        self.CaseID = block.getCID()
        # print("CID: "+ str(self.CaseID))
        self.EvidenceID = block.getEID()
        # print("EID: " + str(self.EvidenceID))
        self.state = block.getState().lstrip("0")
        
    def toString(self):
        return "Case ID: " + str(self.CaseID) +'\n' + "Evidence ID: " + str(self.EvidenceID) +'\n' + "State: " + str(self.state) 
    
