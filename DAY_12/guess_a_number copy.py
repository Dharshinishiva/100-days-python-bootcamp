print("---------------WELCOME TO THE GUESS A NUMBER GAME---------------")

import random

guess_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 29, 20]
guessed_number = random.choice(guess_number)


def guess(chance):
    print(f"you got {chance} chances to find the number!!!")

    chance = chance
    while chance > 0:
        number = int(input("enter a number between 1 to 20:  "))
        if number == guessed_number:
            print("\n")
            print("yes!! You Won. You guessed it right.")
            return
        elif number > guessed_number:
            print("too high!!!")

        else:
            print("too low!!!")

        chance -= 1
        print("Number of chances left:", chance)

    else:
        print("\n")
        print("You Lost the game. Play again")


game = False

while not game:
    print("\n")
    print("If you want to exit the game, type exit.")
    hard_or_easy = input("Type the level- Easy or Hard: ").lower()
    if hard_or_easy == "easy":
        guess(10)

    elif hard_or_easy == "hard":
        guess(5)
    elif hard_or_easy == "exit":
        print("bye")
        game = True

    else:
        print("invalid input !!")
