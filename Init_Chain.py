# TODO: Anielle
# reformat previous hash and cid for printing?
# examples: 2023-04-10T22-21-33.581201.raw and 2023-04-10T22-23-55.495321.raw

import Block
from Block import Block
from Block_Chain import BC
import os


def init_chain():
    
    file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')

    directory = os.path.dirname(file_path)
        
    if not os.path.exists(directory):
        os.makedirs(directory)

        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.close()
                b = Block()
                
        b.setCID(None)  # or b.setCID(None)? reformat for printing, null
        b.setData("Initial block")
        b.setEID(None)
        b.setState("00000INITIAL")
        b.setPreviousHash(None)  # or b.setPreviousHash("None")? reformat for printing
        b.setTimestamp()
        b.setDataLength(14)
        b.setData("Initial block ")  # 14 length string
        print("Blockchain file not found. Created INITIAL block.")
        b.initToBytes()  # add into blockchain file, will be printed w/ log
        BC.reload()
        
        

    else:

        print("Blockchain file found with INITIAL block.")
        exit(1)
                


# init_chain()
