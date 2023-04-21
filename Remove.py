# TODO: Anielle
import uuid
from Block_Chain import BC
from Block import Block


# convert int to hex
def intToHex(i):
    hex(i)  # convert int to hex
    j = '%x' % i  # remove '0x' & 'L'
    j = uuid.UUID(hex=j)  # add dashes back in
    return j  # returns hex str formatted "########-####-####-####-############"

def remove(item_id, reason, owner):
    #check if item_id exists
    # go through the list to check if item_id exists
    print("in Remove()")
    for i in BC.datalist:
        if i.EvidenceID == item_id:
            print(i.EvidenceID)
            print(item_id)
            print(reason)
            if i.state == "CHECKEDOUT":
                print("Error: Cannot remove a checked out item. Must check it in first")
                exit(-1)
            elif i.state == "INITIAL":
                print("Error: Cannot remove an initial block.")  # possible to remove initial block?
                exit(-1)
            elif i.state == "DISPOSED" or i.state == "DESTROYED" or i.state == "RELEASED":
                print("Error: Cannot remove an already disposed/destroyed/released item")
                exit(-1)
            elif reason != "DISPOSED" and reason != "DESTROYED" and reason != "RELEASED":
                print("Error: Not a valid reason. Must be 'DISPOSED', 'DESTROYED', or 'RELEASED")
                exit(-1)
            else:
                print("removing block!")
                # Remove block

                dataBlock = BC.blockExists(i)
                b = Block()

                hash = BC.getLatestHash()
                b.setPreviousHash(hash)
                b.setTimestamp()
                print(dataBlock.getCID())
                #b.setCID(str(i.getCID())) #convert bytes to 16byte string
                b.setCID(dataBlock.getCID())
                b.setEID(int(item_id))

                # state needs to be 12 char in length
                if reason == "DISPOSED":
                    b.setState("DISPOSED")
                elif reason == "DESTROYED":
                    b.setState("DESTROYED")
                else:
                    b.setState("RELEASED")

                # set data & data length from existing block's
                b.setDataLength(0)
                b.setData('')

                #n = b.getCID()  # get int CID
                #UUIDstr = intToHex(n)  # convert int CID to UUID str (w dashes)
                print(f'Case: {b.getCID()}')  # print UUID str
                print(f'Removed item: {b.getEID()}')
                print(f'\tStatus: {b.getState()}')
                if (b.getState() == "RELEASED"):
                    print(f'\tOwner info: {owner}')
                print(f'\tTime of action: {b.getTimestamp()}')

                b.blockToBytes()
                exit(0)
                #BC.reload()
    exit(-1)

# remove -i 987654321 -y RELEASED -o "John Doe, 123 Cherry Ln, Pleasant, AZ 84848, 480-XXX-4321"