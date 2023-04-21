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
        # Check that this blocks previous hash is not present on the chain
        for b in range(i-1, 0, -1):
            if BC.blockList[b].getPreviousHash() == BC.blockList[i].getPreviousHash():
                print(f"Two Blocks can not have the same parent\n"
                      f"First OC {b}: {BC.blockList[b].getPreviousHash()}\n"
                      f"dup OC {i}: {BC.blockList[i].getPreviousHash()}")
                exit(-3)

        # check that state is a valid state
        curr_state = BC.blockList[i].getState()
        print(curr_state)
        if "INITIAL" in curr_state or "CHECKEDIN" in curr_state or "CHECKEDOUT" in curr_state or \
           "DISPOSED" in curr_state or "DESTROYED" in curr_state or "RELEASED" in curr_state:
            pass
        else:
            print(f"State: {curr_state} is not a valid state")
            exit(-3)

        # check datas to see if state change is valid
        if BC.blockList[i].getEID() in datas:
            """
            Current state -> Valid state(s)
            I -> None
            CI -> any except CI
            CO -> CI
            DI, DE, RE -> None
            """
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

