import random

lives = 5
words=["sivakumr", "dharsi", "dhanus"]
chosen = random.choice(words)
chosen_word = len(chosen)

placeholder=""
for position in range (0, chosen_word):
    placeholder += "_ "
print(placeholder)

game_over = False
crtt_letter=[]

while not game_over:
    guess = input("guess a letter:").lower()

    display=""

    for letter in chosen:
        if letter==guess:
            display+= letter
            crtt_letter.append(guess)
        elif letter in crtt_letter:
            display+=letter
        else:
            display+="_ "
            
    print(display)

    if guess not in chosen:
        lives-=1
        if lives == 0:
            game_over = True
            print ("you lost")

    if "_" not in display:
       game_over = True
       print("you won.")   





