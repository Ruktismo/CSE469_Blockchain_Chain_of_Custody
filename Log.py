"""
Log.py
Made By: Andrew Erickson
Last updated: 4/4/23

Displays Info about the blockchain
"""
from Block_Chain import *


def disp_data(blocks):
    for i in range(len(blocks)):
        # convert block state into printable form
        if "INITIAL" in blocks[i].getState():
            block_state = "INITIAL"
        elif "CHECKEDIN" in blocks[i].getState():
            block_state = "CHECKEDIN"
        elif "CHECKEDOUT" in blocks[i].getState():
            block_state = "CHECKEDOUT"
        elif "DISPOSED" in blocks[i].getState():
            block_state = "DISPOSED"
        elif "DESTROYED" in blocks[i].getState():
            block_state = "DESTROYED"
        elif "RELEASED" in blocks[i].getState():
            block_state = "RELEASED"
        else:
            print(f"Unknown block State: {blocks[i].getState()}")
            exit(-7)

        print(f"Case: {blocks[i].getCID()}\n"
              f"Item: {blocks[i].getEID()}\n"
              f"Action: {block_state}\n"
              f"Time: {blocks[i].getTimestamp()}")
        if i < len(blocks) - 1:
            print("\n")  # if not the last piece of data print an extra 2 newlines


def log(is_reversed, num_entries, case_id, item_id):
    """
    Display the blockchain entries giving the oldest first
    Args:
        is_reversed:
            Reverses the order of the block entries to show the most recent entries first.
        num_entries:
            When used with log, shows num_entries number of block entries.
        case_id:
            Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log
            only blocks with the given case_id are returned.
        item_id:
            Specifies the evidence item’s identifier. When used with log  only blocks with the given item_id are returned.
            The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove
            action has been performed on it.
    """
    # TODO get johnny to properly load in all blocks so I can import the Block List
    blocks = BC.blockList  # Copy block list from BlockChain
    p = []
    # flip blocks if reversed
    if is_reversed:
        blocks.reverse()

    # for each block we process
    for i in range(0, (len(blocks) if num_entries == -1 else num_entries)):
        # if not checking case or item
        if case_id == -1 and item_id == -1:
            # print("Checking None")
            p.append(blocks[i])  # just append

        # if checking case but NOT item
        elif case_id != -1 and item_id == -1:
            # print(f"Checking CID\n\t{blocks[i].getCID()}\n\t{case_id}")
            if blocks[i].getCID() == case_id:  # check if case id is what we want
                p.append(blocks[i])  # then add

        # if checking item but NOT case
        elif case_id == -1 and item_id != -1:
            # print(f"Checking EID\n\t{blocks[i].getEID()}\n\t{item_id}")
            if blocks[i].getEID() == item_id:  # check if item id is what we want
                p.append(blocks[i])  # then add

        # if checking both
        else:
            # print("Checking Both")
            if blocks[i].getCID() == case_id and blocks[i].getEID() == item_id:
                p.append(blocks[i])

    # print results
    disp_data(p)
