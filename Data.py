# TODO Johnny
import Block
import os
import struct
from Block import byteCounter

class Data:
    def __init__(self):
        self.CaseID = 0
        self.EvedanceID = 0
        self.state = 0
        # INITIAL (for the initial block ONLY), CHECKEDIN, CHECKEDOUT, DISPOSED, DESTROYED, or RELEASED
        # add zeros to respective state to equal 12 characters
        
        
    def blockToData(self, file):
        self.CaseID = 0
        #read file as bytes
        #extract cid
        #extract EID
        #extract state ignoring zeros
        
        
    def toString(self):
        return "Case ID: " + str(self.CaseID) +'\n' + "Evidence ID: " + str(self.EvedanceID) +'\n' + "State: " + str(self.state) 