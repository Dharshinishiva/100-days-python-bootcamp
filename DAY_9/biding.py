#auction

def find_highest_bind(bidding_dictionary):
     winner = ""
     highest_bind = 0

     max(bidding_dictionary)

     for bidder in bidding_dictionary:
       bidding_amount = bidding_dictionary[bidder]
       if bidding_amount > highest_bind:
            highest_bind = bidding_amount
            winner = bidder 
            
     print(f"the winner is {winner} and the winning amount is {highest_bind}")

         
bid = {}
continue_biding = True
while continue_biding:
    name = input("enter your name:")
    price = int(input("enter your amount:"))
    bid[name]=price
    should_coutinue= input("you want to continue type yes else type no: ").lower()
    if should_coutinue == "no":
        continue_biding = False
        find_highest_bind(bid)

    else:
        should_coutinue == "yes"
        print("\n" * 20)
        
        
        
 


