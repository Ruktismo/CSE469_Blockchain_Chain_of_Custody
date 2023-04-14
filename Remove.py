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
    # go through the list to check if item_id exists
    for i in BC.datalist:
        if i.EvidenceID == item_id:
            if i.State == "CHECKEDOUT":
                print("Error: Cannot remove a checked out item. Must check it in first")
                exit()
            elif i.State == "INITIAL":
                print("Error: Cannot remove an initial block.")  # possible to remove initial block?
                exit()
            elif i.State == "DISPOSED" or i.State == "DESTROYED" or i.State == "RELEASED":
                print("Error: Cannot remove an already disposed/destroyed/released item")
                exit()
            elif reason != "DISPOSED" or reason != "DESTROYED" or reason != "RELEASED":
                print("Error: Not a valid reason. Must be 'DISPOSED', 'DESTROYED', or 'RELEASED")
                exit()
            else:
                # Remove block
                dataBlock = BC.blockExists(i)  # for setting data
                b = Block()

                hash = BC.getLatestHash()
                b.setPreviousHash(hash)
                b.setTimestamp()
                b.setCID(i.CID)
                b.setEID(item_id)

                # state needs to be 12 char in length
                if reason == "DISPOSED":
                    b.setState("0000DISPOSED")
                elif reason == "DESTROYED":
                    b.setState("000DESTROYED")
                else:
                    b.setState("0000RELEASED")

                # set data & data length from existing block's
                b.setDataLength(int(dataBlock.getDataLength()))
                b.setData(dataBlock.getData())

                # print(f'Case: {b.getCID()}')

                n = b.getCID()  # get int CID
                UUIDstr = intToHex(n)  # convert int CID to UUID str (w dashes)
                print(f'Case: {UUIDstr}')  # print UUID str
                print(f'Removed item: {b.getEID()}')
                print(f'\tStatus: {b.getState()}')
                if (b.getState() == "RELEASED"):
                    print(f'\tOwner info: {owner}')
                print(f'\tTime of action: {b.getTimestamp()}')

                b.blockToBytes()
                BC.reload()

# remove -i 987654321 -y RELEASED -o "John Doe, 123 Cherry Ln, Pleasant, AZ 84848, 480-XXX-4321"
