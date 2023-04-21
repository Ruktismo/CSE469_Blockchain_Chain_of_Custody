#todo: yumi lamansky


from Block_Chain import BC
from Block import Block


def checkin( item_id):

    for i in BC.datalist:
        if str(i.EvidenceID) == str(item_id):
            if "CHECKEDOUT" in i.state:
                i.state = "CHECKEDIN"
                
                dataBlock = BC.blockExists(i)
                thing = Block()
                
                hash = BC.getLatestHash()
                
                thing.setPreviousHash(hash)
                thing.setCID(dataBlock.getCID())
                thing.setEID(int(item_id))
                thing.setTimestamp()
                thing.setState("CHECKEDIN")
                thing.setDataLength(int(dataBlock.getDataLength()))
                thing.setData(dataBlock.getData())

                print(f'Case: {thing.getCID()}')
                print(f'Checked in item: {thing.getEID()}')
                print(f'\tStatus: {thing.getState()}')
                print(f'\tTime of action: {thing.getTimestamp()}')
                
                thing.blockToBytes()
                exit(0)
                
                
            else:
                print("Error: cannot check in what is not checked out") 
                print("current state: "+ i.state)
                exit(-1)
    exit(-1)
            
    
