import sys


"""
Main will deal with all setup and arg parsing.
Once it has the cmd and all args needed it will pass off to the corresponding function.
"""
def main():
    # TODO put any setup that needs to be done here. ie. load blockchain from disk
    """
    Argument Types:
        bchoc add -c case_id -i item_id [-i item_id ...]
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

    if sys.argv[1] is "checkout":
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc checkout -i item_id")
            exit(-1)

    if sys.argv[1] is "checkin":
        if len(sys.argv) != 4:
            print("ERROR: Incorrect number of args\n Proprer format: bchoc checkin -i item_id")
            exit(-1)

    if sys.argv[1] is "log":
        is_reversed = False
        if '-r' in sys.argv:
            is_reversed = True
        if '-n' in sys.argv:
            pass
        if '-c' in sys.argv:
            pass
        if '-i' in sys.argv:
            pass

    if sys.argv[1] is "remove":
        if len(sys.argv) != 6 or len(sys.argv) != 8:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc remove -i item_id -y reason [-o owner]")
            exit(-1)

    if sys.argv[1] is "init":
        if len(sys.argv) != 2:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc init")
            exit(-1)

    if sys.argv[1] is "verify":
        if len(sys.argv) != 2:
            print("ERROR: Incorrect number of args\n Proprer format:  bchoc verify")
            exit(-1)

    # if none of the args hit then exit with error
    print("ERROR: Unknown command\n")
    exit(-1)


if __name__ == "__main__":
    main()
