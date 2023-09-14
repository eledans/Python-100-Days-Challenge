answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if answer == "no":
        any_bid = False
        print(f"The winner is {win_bid} with a bid of ${top_bid}")