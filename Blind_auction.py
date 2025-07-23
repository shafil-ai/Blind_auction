logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def higest_bid_record(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Highest bidder is {winner} with a bid of ${highest_bid}")


bids={}
continue_bidding = True
while continue_bidding:
    name = input("Whats your name?")
    price = int(input("Whats your bid? $:"))
    bids[name] = price
    should_continue = input("Is there any other bidder? Type 'Yes' or 'No'\n ")
    if should_continue == "no".lower():
        continue_bidding = False
        higest_bid_record(bids)
    elif should_continue == "yes".lower():
        print("\n" * 20)


