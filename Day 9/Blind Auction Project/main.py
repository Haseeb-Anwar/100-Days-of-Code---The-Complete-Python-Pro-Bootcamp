# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print (art.logo)

dic={}
nxt ="Y"

while nxt =="Y":

    name = input("Please enter your name:")
    bid = int(input("Enter your bid: $"))
    dic[name] = bid
    nxt = input("Any other person in the room?: Y/N ")
    print("\n"*50)





name, amount = max(dic.items(), key=lambda x: x[1])
print(f"Name: {name}, Amount: {amount}")



