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

        self.CaseID = block.getCID()
        # print("CID: "+ str(self.CaseID))
        self.EvidenceID = block.getEID()
        # print("EID: " + str(self.EvidenceID))
        self.state = block.getState().replace("\x00","")
        print("type of new data obj: "+type(block.getState()))
        
    def toString(self):
        return "Case ID: " + str(self.CaseID) +'\n' + "Evidence ID: " + str(self.EvidenceID) +'\n' + "State: " + str(self.state) 
    
