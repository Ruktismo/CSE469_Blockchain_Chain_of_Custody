#todo: yumi lamansky
#bchoc checkout -i 987654321


import Block as item

#checking out an evidence item:
#case: [insert case number here]
#checked out item: [987654321]
#  status: CHECKEDOUT
#  time of action: [insert time here]
def checkout(item_id):

    print(f'Case: ')
    print(f'Checked in item: ')
    print(f'\tStatus: CHECKEDOUT')
    print(f'\tTime of action: ')

    pass

#attempting to check out an evidence item twice without checking it in:
#bchoc checkout -i 987654321
#error: cannot check out a checked out item. must check it in first.

#important: the last two lines of the above example ask shell to print the return code of
#most recently run program, meaning the command returned an error code when it exited.
def checkoutTwice(item_id):
