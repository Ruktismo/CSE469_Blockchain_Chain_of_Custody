"""
Verify_Chain.py
Made By: Andrew Erickson
Last updated: 4/4/23


"""
from Block_Chain import *

def disp_error():
    pass


def verify_chain():
    # TODO get johnny to properly load in all blocks / data so I can import the Block and Data List
    blocks = []
    datas = []  # make datas a dic of itemID: Data?
    transactions_count = 0
    found_error = False

    previous_hash = None

    for block in blocks:
        # check that this block's previous hash is the hash of the last block
        if previous_hash is not block.getPreviousHash():
            found_error = True
            # Add error info for printing

        # check through datas to see if
        #       the state change is valid
        # check through blocks to see if
        #       any block has the same parent hash as this block

        # TODO find way to check "Block contents do not match block checksum."

        transactions_count += 1

    if found_error:
        disp_error()

