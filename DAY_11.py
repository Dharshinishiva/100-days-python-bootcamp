#BLACKJACK PROJECT 

import random

def deal_card():  #each time we call this function, it takes a random number from the list below
    cards = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 , 10]
    card = random.choice(cards)
    return card

def calculator_score(cards):  #check whether it is blackjack and returns 0 bcoz its special code
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    
     # if the point is going to exceed 21 and if 11 is in it this code coverts 11 into 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return(sum(cards))

def compare(user_score, computer_score ):
    if user_score == computer_score:
        print("draw")
    elif user_score == 0:
        print ("win ! with a blackjack")
    elif computer_score == 0:
        print ("lose ! the opponent has blackjack")
    elif user_score > 21:
        print ("you lose because u exceed")
    elif computer_score > 21:
        print ("you win ! because opponent exceed")
    elif user_score > computer_score:
        print("you win !!!")
    else:
        print("opponent wins !!!")

def game():
    user_card = []
    computer_card = []
    computer_score = -1 #initialing the score
    user_score = -1
    is_game_over = False

    for _ in range (2):       # underscore is used because it take has a placeholder
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over :
        user_score = calculator_score(user_card)
        computer_score = calculator_score(computer_card)

        print(f"user card: {user_card} and users current score {user_score}")
        print(f"computer first card: {computer_card[0]}")

        if user_score == 0 or computer_card == 0 or user_score > 21:
            is_game_over = True
        else:
            user_response = input("type yes to to retrive another card and type no to end the game  ")
            if user_response == "yes":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculator_score(computer_card)

    print(f"the final card: {user_card} and your final score is {user_score}")
    print(f"the computer's final card: {computer_card} and computer's final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("hi there !!! if you want to play the game type y or else type n :  ") == "y":
    print("\n"*20)
    game()
