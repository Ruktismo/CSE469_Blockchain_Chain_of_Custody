
import Block as item
from Block_Chain import BC
from Block import Block
from hashlib import sha256
import pickle

def checkout( item_id):

    for i in BC.datalist:
        if str(i.EvidenceID) == str(item_id):
            if "CHECKEDIN" in i.state:
                i.state = "CHECKEDOUT"

                dataBlock = BC.blockExists(i)
                thing = Block()


                hash = BC.getLatestHash()

                thing.setPreviousHash(hash)
                thing.setCID(dataBlock.getCID())
                thing.setEID(item_id)
                thing.setTimestamp()
                thing.setState("CHECKEDOUT")
                thing.setDataLength(int(dataBlock.getDataLength()))
                thing.setData(dataBlock.getData())

                print(f'Case: {thing.getCID()}')
                print(f'Checked out item: {thing.getEID()}')
                print("Status: " + thing.getState() )
                print(f'\tTime of action: {thing.getTimestamp()}')

                thing.blockToBytes()
                exit(0)


            else:
                print("Error: Cannot check out a checked out item. Must check it in first")
                print("current state: "+ i.state)
                exit(-1)
    exit(-1)


