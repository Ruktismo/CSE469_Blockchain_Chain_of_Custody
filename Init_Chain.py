# TO DO: Anielle

import Data
from Data import Data
import Block
from Block import Block


def init_chain():
    # check if blockchain file exists
    # 1. if filename.raw exists, print
    print("Blockchain file found with INITIAL block.")

    # 2. else, create initial block
    i = Block()  # create initial block obj
    d = Data()  # create initial data obj
    i.setData(d)  # set data in initial block
    # add into blockchain file
    print("Blockchain file not found. Created INITIAL block.")
    pass
