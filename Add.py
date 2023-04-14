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

# generate random string based on given random data length
def getRandomString(dataLength):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                  for i in range(dataLength))
    return str(res)


def add(case_id, item_ids):
    # Check if CASE ID is UUID
    if not isValidUuid(case_id):
        print("Error: case_id is not a valid UUID. Must input valid UUID")
        exit()

    # Case ID Byte Check Passed, for ea item_id, check BC list if case id && item_id exists
    print("\nCase: " + case_id)
    for j in item_ids:
        # check if item_id[j] is INT
        if isValidInt(item_ids[j]):
            # iter through blockchain. If item already exists, exit. Else add new block to chain
            for i in BC.datalist:
                if i.CaseID == case_id:
                    if i.EvidenceID == item_ids[j]:
                        print("Error: Cannot add an existing item. Must add a new item. ")
                        exit()
                    else:
                        # item_id is unique/new, add new block
                        b = Block()
                        hash = BC.getLatestHash()
                        b.setPreviousHash(hash)
                        b.setTimestamp()

                        # remove hyphens from uuid, store as hexstr
                        b.setCID(uuidToHex(
                            case_id))  # ex: '65cc391d-6568-4dcc-a3f1-86a2f04140f3' stored as '65cc391d65684dcca3f186a2f04140f3'
                        b.setEID(item_ids[j])
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

        # 2. item_id[j] is NOT an INT
        else:
            print("Error: item_id is not an integer. Must input integer")

# add -c 65cc391d65684dcca3f186a2f04140f3 -i 987654321
