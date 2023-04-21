"""
Verify_Chain.py
Made By: Andrew Erickson
Last updated: 4/4/23


"""
import struct
from hashlib import sha256

from Block_Chain import BC
from Data import Data

# This should be in the Block class, but I don't want to nag johnny
# And I may be the only one who needs it
def getBlockHash(Block):
    try:
        packed1 = struct.pack("32s", Block.getPreviousHash().encode())
        packed2 = Block.getDoubleTimestamp()
        packed3 = struct.pack("16s", str(Block.getCID()).encode())
        packed4 = struct.pack("I", int(Block.getEID()))
        packed5 = struct.pack("12s", Block.getState().encode())
        packed6 = struct.pack("I", int(Block.getDataLength()))
        packed7 = struct.pack((str(len(Block.getData())) + 's'), Block.getData().encode())

        blockBytes = packed1 + packed2 + packed3 + packed4 + packed5 + packed6 + packed7
    except Exception as e:
        print("Error doing checksum in verify, bad block")
        print(e)
        exit(-6)
    return sha256(blockBytes).digest()

def verify_chain():
    datas = {}  # make datas a dic of itemID: Data?
    print(f"Transactions in blockchain: {len(BC.blockList)}")

    for i in range(len(BC.blockList)):
        # Check that this blocks previous hash is the hash of the last block
        # but skip the init block since it has no parent
        """
        if i > 0 and BC.blockList[i].getPreviousHash() != getBlockHash(BC.blockList[i-1]):
            print(f"Hash error at block {i}")
            exit(-1)
        """
        # check datas to see if state change is valid
        if BC.blockList[i].getEID() in datas:
            """
            Current state -> Valid state(s)
            I -> None
            CI -> any except CI
            CO -> CI
            DI, DE, RE -> None
            """
            # TODO check if state change is valid
            if "INITIAL" in BC.blockList[i].getState():
                print("Can't have more than one Init block")
                exit(-3)
            if "CHECKEDIN" in datas[BC.blockList[i].getEID()].state and "CHECKEDIN" in BC.blockList[i].getState():
                print("Can't check in item that is already in")
                exit(-3)
            if "CHECKEDOUT" in datas[BC.blockList[i].getEID()].state and "CHECKEDIN" not in BC.blockList[i].getState():
                print("Can't preform action on item that is already out")
                exit(-3)
            if "DISPOSED" in datas[BC.blockList[i].getEID()].state or \
                    "DESTROYED" in datas[BC.blockList[i].getEID()].state or \
                    "RELEASED" in datas[BC.blockList[i].getEID()].state:
                print("Can't preform action on item that has been removed")
                exit(-3)
            # if valid then update state
            datas[BC.blockList[i].getEID()].state = BC.blockList[i].getState()
        else:
            # add data obj to datas
            newD = Data()
            newD.CaseID = BC.blockList[i].getCID()
            newD.EvidenceID = BC.blockList[i].getEID()
            newD.state = BC.blockList[i].getState()
            if "CHECKEDIN" in newD.state or "INITIAL" in newD.state:
                pass  # valid for new evidence
            else:
                print(f"New evidence {i} added with invalid state\n"
                      f"\tCID: {BC.blockList[i].getCID()}\n"
                      f"\tEID: {BC.blockList[i].getEID()}\n"
                      f"\tState: {BC.blockList[i].getState()}")
                exit(-3)

            datas[BC.blockList[i].getEID()] = newD

    # if we reach here then no errors where found
    print("State of blockchain: CLEAN")

