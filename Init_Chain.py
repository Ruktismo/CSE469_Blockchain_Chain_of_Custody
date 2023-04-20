# TODO: Anielle
# reformat previous hash and cid for printing?
# examples: 2023-04-10T22-21-33.581201.raw and 2023-04-10T22-23-55.495321.raw

import Block
from Block import Block
from Block_Chain import BC
import os


def init_chain():
    
    file_path = os.getenv('BCHOC_FILE_PATH', './BlockFolder/BC.raw')
    print(file_path)
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
                os.makedirs(directory)
                
    if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.close()
                b = Block()   
                 
            
                
                        
                b.setCID(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')  # or b.setCID(None)? reformat for printing, null
                b.setData("Initial block")
                b.setEID(b'\x00\x00\x00\x00')
                b.setState("INITIAL")
                b.setPreviousHash(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')  # or b.setPreviousHash("None")? reformat for printing
                b.setTimestamp()
                b.setDataLength(14)
                b.setData("Initial block")  # 14 length string
                print("Blockchain file not found. Created INITIAL block.")
                b.initToBytes()  # add into blockchain file, will be printed w/ log
                BC.reload()
        
        

    else:

        print("Blockchain file found with INITIAL block.")
        file_size = os.path.getsize(file_path)
        # print(str(file_size))
        if(file_size < 90):
            exit(-1)
        
        BC.reload()
        # print("BC len: "+str(len(BC.blockList)))
        # BC.printBC()
        exit(0)
                


init_chain()
