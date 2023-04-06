import sys

from Add import add
from Checkout import checkout
from Checkin import checkin
from Log import log
from Remove import remove
from Init_Chain import init_chain
from Verify_Chain import verify_chain


"""
Main will deal with all setup and arg parsing.
Once it has the cmd and all args needed it will pass off to the corresponding function.
"""
def main():
    # TODO put any setup that needs to be done here. ie. load blockchain from disk
    # TODO Johnny
    # File names will be the time ISO

    """
    Argument Types:
        bchoc add -c case_id -i item_id [-i item_id ...]cv
        bchoc checkout -i item_id
        bchoc checkin -i item_id
        bchoc log [-r] [-n num_entries] [-c case_id] [-i item_id]
        bchoc remove -i item_id -y reason [-o owner]
        bchoc init
        bchoc verify
    """
    if len(sys.argv) < 2:
        print("ERROR: please give a command")
        exit(-1)

    if sys.argv[1] is "add":
        if len(sys.argv) < 6 or (len(sys.argv) % 2 != 0):
            print("ERROR: Incorrect number of args\n Proprer format: bchoc add -c case_id -i item_id [-i item_id ...]")
            exit(-1)
        case_id = sys.argv[3]
        item_ids = []
        for i in range(4, len(sys.argv)):
            if sys.argv[i] is "-i":
                item_ids.append(sys.argv[i+1])
        add(case_id, item_ids)

    if sys.argv[1] is "checkout":
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc checkout -i item_id")
            exit(-1)
        checkout(sys.argv[3])

    if sys.argv[1] is "checkin":
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of args\n Proprer format: bchoc checkin -i item_id")
            exit(-1)
        checkin(sys.argv[3])

    if sys.argv[1] is "log":
        is_reversed = False
        num_entries = -1
        case_id = -1
        item_id = -1
        for i in range(2, len(sys.argv)):
            if '-r' in sys.argv[i]:
                is_reversed = True
            if '-n' in sys.argv[i]:
                num_entries = sys.argv[i+1]
            if '-c' in sys.argv:
                case_id = sys.argv[i+1]
            if '-i' in sys.argv:
                item_id = sys.argv[i+1]
        log(is_reversed, num_entries, case_id, item_id)

    if sys.argv[1] is "remove":
        if len(sys.argv) != 6 or len(sys.argv) != 8:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc remove -i item_id -y reason [-o owner]")
            exit(-1)
        owner = None
        if len(sys.argv) == 8:
            owner = sys.argv[7]
        remove(sys.argv[3], sys.argv[5], owner)

    if sys.argv[1] is "init":
        if len(sys.argv) != 2:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc init")
            exit(-1)
        init_chain()

    if sys.argv[1] is "verify":
        if len(sys.argv) != 2:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc verify")
            exit(-1)
        verify_chain()

    # if none of the args hit then exit with error
    print("ERROR: Unknown command\n")
    exit(-1)


if __name__ == "__main__":
    main()
