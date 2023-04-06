# TO DO: Anielle
"""
go to blockchain
verify if stuff isn't in use
make blocks
commit to chain error checking - check if bytes r correct length in
"""
import Block
from Block import Block


def add(case_id, item_ids):
    # go to blockchain file
    # check if case_id block isn't checked out?

    # if case_id isn't in use, error checking
    i = 0  # iter thru item ids
    # for ea item_ids, create block and add to file #need to look over again lol
    b = Block()
    b.setCID(case_id)
    b.setData("")
    #b.setEID(item_ids[i]) #what to set to?
    b.setState("000CHECKEDIN")
    b.setPreviousHash("")
    b.setTimestamp()
    b.setDataLength(100)

    # print confirmation block is added
    print("Case: " + case_id)
    #print("Case: " + item_ids[i])
    pass
