
# TODO: Anielle
"""
go to blockchain
verify if stuff isn't in use
make blocks
commit to chain error checking - check if bytes r correct length in
"""

import random
import secrets
import string
import uuid
from Block import Block
from Block_Chain import BC


# check if case_id is a valid uuid, works for strings w/ hyphens & no hyphens
def isValidUuid(cid):
    try:
        uuid.UUID(str(cid))
        return True
    except ValueError:
        return False


# check if item_id is a valid 4 byte int
def isValidInt(eid):
    if eid.isdigit():
        return True
    else:
        return False


# remove dashes from uuid
def uuidToHex(u: str) -> str:
    return uuid.UUID(u).hex


# convert int CID to hex string (add dashes again)
# ex. CID=135312414559765810732748806252319031539 -> convert to hex -> 65CC391D65684DCCA3F186A2F04140F3 -> add dashes -> "65cc391d-6568-4dcc-a3f1-86a2f04140f3"
def intToHex(i):
    hex(i)  # convert int to hex
    j = '%x' % i  # remove '0x' & 'L'
    j = uuid.UUID(hex=j)  # add dashes back in
    return j  # returns hex str formatted "########-####-####-####-############"


# generate random string based on given random data length
def getRandomString(dataLength):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                  for i in range(dataLength))
    return str(res)


def add(case_id, item_ids):

    #Test 007 - add before init - should create initial block
    if BC.blockList and BC.blockList[0].getState() == "INITIAL":  # str(len(BC.blockList) != 0), might change condition
        pass
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
        print("Blockchain file not found. Created INITIAL block.")
        b.blockToBytes()  # add into blockchain file, will be printed w/ log
        BC.reload()




    # Check if CASE ID is UUID
    if not isValidUuid(case_id):
        print("Error: case_id is not a valid UUID. Must input valid UUID")
        exit(-1)

    # Case ID Byte Check Passed, for ea item_id, check BC list if case id && item_id exists
    print("Case: " + case_id)
    for j in item_ids:
        # check if j is INT
        #print("Current item_id: " + j)
        if isValidInt(str(j)):  # lol oops, convert input to int
            #print("item_id is VALID")
            # iter through blockchain. If item already exists, exit. Else add new block to chain
            for i in BC.datalist:
                if i.EvidenceID == str(j):
                    print("Error: Cannot add an existing item. Must add a new item. ")
                        #break
                    exit(-1)
                else:
                    # item_id is unique/new, add new block
                    b = Block()
                    hash = BC.getLatestHash()
                    b.setPreviousHash(hash)
                    b.setTimestamp()

                    # set str case_id to int CID
                    #u = uuid.UUID(case_id)
                    #strBytes = str(u.bytes)
                    #n = uuidToHex(case_id)  # remove hyphens from uuid, store as hexstr
                    #intN = int(n, 16)  # convert hexstr to int
                    b.setCID(case_id)  # set int to CID

                    b.setEID(j)  # store item id into block
                    b.setState("000CHECKEDIN")

                    # set data to new block
                    b.setDataLength(random.randint(0, 32))  # set rand length of data (range: [0,32])
                    b.setData(getRandomString(b.getDataLength()))  # gen rand str from data length

                    # get & print block
                    print(f'Added item: {b.getEID()}')
                    print(f'\tStatus: {b.getState()}')
                    print(f'\tTime of action: {b.getTimestamp()}')

                    b.blockToBytes()
                    BC.reload()
        # 2. j is NOT an INT
        else:
            print("Error: item_id is not an integer. Must input integer")

# add -c 65cc391d65684dcca3f186a2f04140f3 -i 987654321
# add -c 65cc391d-6568-4dcc-a3f1-86a2f04140f3 -i 987654321