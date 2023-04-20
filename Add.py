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

# generate random string based on given random data length
def getRandomString(dataLength):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                  for i in range(dataLength))
    return str(res)

def add(case_id, item_ids):
    # if case_id is UUID format
    if not uuid.UUID(str(case_id)):
        print("Error: case_id is not a valid UUID. Must input valid UUID")
        exit(-1)

    # empty inputs
    if case_id is None: exit(-1)
    for j in item_ids:
        if j is None: exit(-1)

    # init_chain if no initial block
    file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')
    if not os.path.exists(file_path):
        init_chain()

    # [CHECKS PASSED] case_id is valid. no empty inputs. initial block exists.
    print("Case: " + case_id)
    # for ea item_id
    for j in item_ids:
        # if item_id is INT
        if not str(j).isdigit():
            print("Error: item_id is not an integer. Must input integer")
            exit(-1)

        # if item_id a duplicate
        for i in BC.datalist:
            if i.EvidenceID == str(j):
                print("Error: Cannot add an existing item. Must add a new item. ")
                exit(-1)
            else:
                pass

        # [CHECKS PASSED] item_id is INT & unique. Add new block.
        b = Block()
        hash = BC.getLatestHash()
        b.setPreviousHash(hash)
        b.setTimestamp()

        b.setCID(str(case_id)) # set str case_id
        b.setEID(int(j))  # store item id into block
        b.setState("CHECKEDIN000")

        # set data to new block
        b.setDataLength(random.randint(0, 32))  # set rand length of data (range: [0,32])
        b.setData(getRandomString(b.getDataLength()))  # gen rand str from data length

        # get & print block
        print(f'CID check: {b.getCID()}')
        print(f'Added item: {b.getEID()}')
        print(f'\tStatus: {b.getState()}')
        print(f'\tTime of action: {b.getTimestamp()}')

        b.blockToBytes()
        # BC.reload()

# add -c 65cc391d65684dcca3f186a2f04140f3 -i 987654321
# add -c 65cc391d-6568-4dcc-a3f1-86a2f04140f3 -i 987654321
