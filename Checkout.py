#todo: yumi lamansky
#bchoc checkout -i 987654321


import Block as item

#checking out an evidence item:
#case: [insert case number here]
#checked out item: [987654321]
#  status: CHECKEDOUT
#  time of action: [insert time here]

from Block_Chain import BC
from Block import Block
from hashlib import sha256
import pickle

def checkout( item_id):

    #go through the list and make sure its exact thingy, then change state
    for i in BC.datalist:
        if str(i.EvidenceID) == str(item_id):
            if i.state == "CHECKEDIN":
                i.state = "CHECKEDOUT"

                # this takes your data obj "i" and returns the block obj that matches it
                # this is mainly for filling the data and data length for writing to bytes
                dataBlock = BC.blockExists(i)
                thing = Block()

                # set the things
                hash = BC.getLatestHash()

                thing.setPreviousHash(hash)
                thing.setCID(dataBlock.getCID())
                thing.setEID(item_id)
                thing.setTimestamp()
                thing.setState("CHECKEDOUT")
                thing.setDataLength(int(dataBlock.getDataLength()))
                thing.setData(dataBlock.getData())

                # print the things from the getters
                print(f'Case: {thing.getCID()}')
                print(f'Checked out item: {thing.getEID()}')
                print(f'\tStatus: {thing.getState()}')
                print(f'\tTime of action: {thing.getTimestamp()}')

                # add  the thing to the file and update lists with reload
                thing.blockToBytes()
                # BC.reload()

            else:
                print("Error: Cannot check out a checked out item. Must check it in first")
                print("current state: "+ i.state)
                exit(-1)


    # #new block thingy to add to the chain
    # blox = Block()
    # #set the things
    # blox.setCID(case_id)
    # blox.setEID(item_id)
    # blox.setTimestamp()
    # blox.setState("CHECKEDOUT")
    # #possibly NIL, remaining block values
    #
    # #print the things from the getters
    # print(f'Case: {blox.getCID()}')
    # print(f'Checked out item: {blox.getEID()}')
    # print(f'\tStatus: {blox.getState()}')
    # print(f'\tTime of action: {blox.getTimestamp()}')
    #
    #
    # input = pickle.dumps(BC.blockList[-1])
    # hash = sha256(input).hexdigest()
    # blox.setPreviousHash(hash)
    #
    # #add  the thing to the block list
    # blox.blockToBytes()
    # BC.reload()



#now do the thing
#checkout(9269517611667620, 2169)
#
# Case ID: 9269517611667620
# Evidence ID: 2169
# State: INITIAL
#attempting to check out an evidence item twice without checking it in:
#bchoc checkout -i 987654321
#error: cannot check out a checked out item. must check it in first.

#important: the last two lines of the above example ask shell to print the return code of
#most recently run program, meaning the command returned an error code when it exited.

