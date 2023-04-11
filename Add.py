# TODO: Anielle
"""
go to blockchain
verify if stuff isn't in use
make blocks
commit to chain error checking - check if bytes r correct length in
"""
import Block
from Block import Block
from Data import Data
from Block_Chain import BC


def add(case_id, item_ids):
    #print("\nCase: " + case_id)

    # 1. check if case_id is checked out

    # 2. if not checked out, check if ea item_id is duplicate, if duplicate throw error
    # for ea item_id
    #if BC.dataExists(BC, newData):
        #print("\nItem already exists for this case file")

    #else:
        # if case_id isn't in use, error checking
        # for ea item_ids (i=0), create block and add to file
        # b = Block()
        # b.setCID(case_id)
        # b.setData("")
        # b.setEID(item_ids[i])
        # b.setState("000CHECKEDIN")
        # b.setPreviousHash("")
        # b.setTimestamp()
        # b.setDataLength(100)

        # confirmation block is added
        #print("\nAdded item: " + item_ids[i])  # Added item: 987654321
        #print("\nStatus: CHECKED IN")  # reformat
        #print("\nTime of action: ")  # Time of action: 2022-01-22T03:13:07.820445Z
        pass
