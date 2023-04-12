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

def checkout(case_id, item_id):

    #go through the list and make sure its exact thingy, then change state
    for i in BC.datalist:
        if i.CaseID == case_id:
            if i.EvidenceID == item_id:
                if i.State != "CHECKEDOUT":
                    i.State = "CHECKEDOUT"
                else:
                    print("Error: Cannot check out a checked out item. Must check it in first")


    #new block thingy to add to the chain
    blox = Block()
    #set the things
    blox.setCID(case_id)
    blox.setEID(item_id)
    blox.setTimestamp()
    blox.setState("CHECKEDOUT")

    #print the things from the getters
    print(f'Case: {blox.getCID()}')
    print(f'Checked out item: {blox.getEID()}')
    print(f'\tStatus: {blox.getState()}')
    print(f'\tTime of action: {blox.getTimestamp()}')


    input = pickle.dumps(BC.blockList[-1])
    hash = sha256(input).hexdigest()
    blox.setPreviousHash(hash)

    #add  the thing to the block list
    BC.blockList.append(blox)
    #possibly NIL, remaining block values
    #maaaaybe update block folder #Johnny job???



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

