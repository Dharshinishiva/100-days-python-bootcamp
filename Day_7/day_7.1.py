#chatgpt code with bug fix
 
import random

lives = 5
words = ["sivakumr", "dharsi", "dhanus"]
chosen = random.choice(words)

placeholder = ""
for position in range(len(chosen)):
    placeholder += "_ "
print(placeholder.strip())

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in chosen and guess not in correct_letters:
        correct_letters.append(guess)

    display = ""
    for letter in chosen:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    print(display.strip())

    if guess not in chosen:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lost. The word was:", chosen)

    if "_" not in display:
        game_over = True
        print("You won!")
