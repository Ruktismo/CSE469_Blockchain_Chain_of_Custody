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


def checkin( item_id):

    # go through the list and make sure its exact thingy, then change state
    for i in BC.datalist:
            if str(i.EvidenceID) == str(item_id):
                if i.state == "CHECKEDOUT":
                    i.state = "CHECKEDIN"
                    
                    #this takes your data obj "i" and returns the block obj that matches it
                    # this is mainly for filling the data and data length for writing to bytes
                    dataBlock = BC.blockExists(i)
                    thing = Block()
                    
                    
                    # set the things
                    hash = BC.getLatestHash()
                    
                    thing.setPreviousHash(hash)
                    thing.setCID(case_id)
                    thing.setEID(item_id)
                    thing.setTimestamp()
                    thing.setState("000CHECKEDIN")
                    thing.setDataLength(int(dataBlock.getDataLength()))
                    thing.setData(dataBlock.getData())
                    
                    # print the things from the getters
                    print(f'Case: {thing.getCID()}')
                    print(f'Checked in item: {thing.getEID()}')
                    print(f'\tStatus: {thing.getState()}')
                    print(f'\tTime of action: {thing.getTimestamp()}')

                    

                    # add  the thing to the file and update lists with reload
                    thing.blockToBytes()
                    # BC.reload()
                    
                    
                else:
                    print("Error: cannot check in what is not checked out") #todo; work on later

            
    
    

    # now do the thing

# checkin(9269517611799130, 2123)
# BC.printBC()
# checkin(9269517611799130, 2123)

