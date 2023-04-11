# TODO: Anielle
# reformat previous hash and cid for printing?
# examples: 2023-04-10T22-21-33.581201.raw and 2023-04-10T22-23-55.495321.raw

import Block
from Block import Block
from Block_Chain import BC

def init_chain():
    # 1. check if at least one blockchain .raw file exists
    if BC.blockList != None:  # str(len(BC.blockList) != 0), might change condition
        print("Blockchain file found with INITIAL block.")

    # 2. else, create initial block
    else:
        b = Block()
        b.setCID(0)  # or b.setCID(None)? reformat for printing, null
        b.setData("Initial block")
        b.setEID(0)
        b.setState("00000INITIAL")
        b.setPreviousHash("0000000000000000000000000000None")  # or b.setPreviousHash("None")? reformat for printing
        b.setTimestamp()
        b.setDataLength(14)
        b.setData("Initial block ")  # 14 length string
        b.blockToBytes()  # add into blockchain file, will be printed w/ log
        print("Blockchain file not found. Created INITIAL block.")
    # pass
