from art import logo
import os

# os.system("cls")

bids = {}
any_bid = True
print(logo)

print("Welcome to the secret auction program.")
while any_bid:
    name = input("What is your name?: ")
    bid = int(input("What's you bid?: $"))
    bids[name] = bid

    def check(bidding_record):
        top_bid = 0
        winner = ""
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder] 
            if bid_amount > top_bid:
                top_bid = bid_amount 
                winner = bidder
        print(f"The winner is {winner} with a bid of ${top_bid}")

    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == "no":
        any_bid = False    
        check(bids)
    elif answer == "yes":
        os.system("cls")