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
import os
from Block import Block
from Block_Chain import BC
from Init_Chain import init_chain


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


# generate random string based on given random data length
def getRandomString(dataLength):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                  for i in range(dataLength))
    return str(res)


def add(case_id, item_ids):
    # init_chain if no initial block
    file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')
    directory = os.path.dirname(file_path)
    if not os.path.exists(file_path):
        #print("Directory isnt there, initializing chain")
        init_chain()
        add(case_id, item_ids)
    else:
        # Check if CASE ID is UUID
        if not isValidUuid(case_id):
            print("Error: case_id is not a valid UUID. Must input valid UUID")
            exit(-1)
        # Case ID Byte Check Passed, for ea item_id, check BC list if case id && item_id exists
        print("Case: " + case_id)
        for j in item_ids:
            # check if j is INT
            # print("Current item_id: " + j)
            if isValidInt(str(j)):  # lol oops, convert input to int
                # print("item_id is VALID")
                # iter through blockchain. If item already exists, exit. Else add new block to chain
                for i in BC.datalist:
                    if i.EvidenceID == int(j):
                        print("Error: Cannot add an existing item. Must add a new item. ")
                        # break
                        exit(-1)
                    else:
                        # item_id is unique/new, add new block
                        b = Block()
                        #hash = BC.getLatestHash()
                        #b.setPreviousHash(hash)
                        #testing only for block 1
                        b.setPreviousHash(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                        b.setTimestamp()


                        # set str case_id
                        #issue, fix setCID()
                        b.setCID(case_id)  # set int to CID
                        b.setEID(int(j))  # store item id into block
                        b.setState("CHECKEDIN000")

                        # set data to new block
                        #b.setDataLength(random.randint(0, 32))  # set rand length of data (range: [0,32])
                        #b.setData(getRandomString(b.getDataLength()))  # gen rand str from data length
                        # testing only for block 1
                        b.setDataLength(0)  # set rand length of data (range: [0,32])
                        b.setData(getRandomString(b.getDataLength()))  # gen rand str from data length


                        # get & print block
                        print(f'Added item: {b.getEID()}')
                        print(f'\tStatus: {b.getState()}')
                        print(f'\tTime of action: {b.getTimestamp()}')

                        b.blockToBytes()
                        #BC.reload()
            # 2. j is NOT an INT
            else:
                print("Error: item_id is not an integer. Must input integer")

# add -c 65cc391d65684dcca3f186a2f04140f3 -i 987654321
# add -c 65cc391d-6568-4dcc-a3f1-86a2f04140f3 -i 987654321
