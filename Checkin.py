#todo: yumi lamansky
# bchoc checkin -i item_id
#add new checkin entry to chain of custody for given evidence item. checkin actions
#may only be performed on evidence items that have already been added to the blockchain


#checking in an evidence item:
#case: [insert case number here]
#checked out item: [987654321]
#  status: CHECKEDIN
#  time of action: [insert time here]



from Block_Chain import BC
from Block import Block
from hashlib import sha256
from Checkout import checkout
import pickle



def checkin(case_id, item_id):

    # go through the list and make sure its exact thingy, then change state
    for i in BC.datalist:
        if i.CaseID == case_id:
            if i.EvidenceID == item_id:
                if i.State == "CHECKEDOUT":
                    i.State = "CHECKEDIN"
                else:
                    print("Error") #todo; work on later

    # new block thingy to add to the chain
    thing = Block()
    # set the things
    thing.setCID(case_id)
    thing.setEID(item_id)
    thing.setTimestamp()
    thing.setState("CHECKEDIN")

    # print the things from the getters
    print(f'Case: {thing.getCID()}')
    print(f'Checked in item: {thing.getEID()}')
    print(f'\tStatus: {thing.getState()}')
    print(f'\tTime of action: {thing.getTimestamp()}')

    input = pickle.dumps(BC.blockList[-1])
    hash = sha256(input).hexdigest()
    thing.setPreviousHash(hash)

    # add  the thing to the block list
    BC.blockList.append(thing)
    # possibly NIL, remaining block values
    # maaaaybe update block folder #Johnny job???

    # now do the thing

checkout(9269517611667620, 2169)
checkin(9269517611667620, 2169)
#
# Case ID: 9269517611667620
# Evidence ID: 2169
# State: INITIAL

