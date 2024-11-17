# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

data = {}
continue_bidding = True
while continue_bidding:
    name = input("Type your name ")
    price = input("Type your bid $ ")
    new_bid = input("Does someone else need to bid? (Yes/no ")
    print("\n" * 200)
    data[name] = price
    if new_bid.lower() == "no":
        continue_bidding = False

for key in data:
        highest_bid = 0
        winner = ""
        bid_amount = int(data[key])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
print(f"{key} has won with the highest bid of {highest_bid}")
