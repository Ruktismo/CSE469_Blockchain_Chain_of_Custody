<h1>Blockchain Chain of Custody</h1>

Group #25  
Group Members:  
Andrew Erickson  
Johnny Navarro  
Anielle Mari David  
Yumi Lamansky  

<h1> Description </h1>
The program demonstrates a blockchain chain of custody form.  
Users can input the follow commands:  
<li> Add: `bchoc add -c case_id -i item_id [-i item_id ...]` Add a new evidence object into the blockchain. The state will be CHECKEDIN and the item_id must be unique. </li>
<li> Checkout: `bchoc checkout -i item_id` Add a new checkout entry into the blockchain based on the evidence item. A block may only be checked out if it has been added to the blockchain.</li>
<li>Checkin: `bchoc checkin -i item_id` Add a new checkin entry into the blockchain based on the evidence item. A block may only be checked in if it has been added to the blockchain. </li>
<li>Log: `bchoc log [-r] [-n num_entries] [-c case_id] [-i item_id]` Displays the entries of the blockchain from oldest to newest by default</li>
<li>Remove: `bchoc remove -i item_id -y reason [-o owner]` Prevents further action from being done to the specified block. The block must first be CHECKEDIN. </li>
<li>Init: `./bchoc init` Starts up and checks for the initial block in the blockchain. </li>
<li>Verify: `./bchoc verify` Parse the blockchain and validate all of its entries.</li>

<h1> Submitting Files </h1>
Add.py
bchoc
Block.py
Block_Chain.py
Checkin.py
Checkout.py
Data.py
Init_Chain.py
Log.py
Main.py
makefile
README.md
Remove.py
Verify_Chain.py
