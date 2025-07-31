print("-------------WELCOME TO HIGHER LOWER GAME -------------")

data = [
    {"name": "Virat Kohli", "instagram_followers": 270_853_161},
    {"name": "Sachin Tendulkar", "instagram_followers": 50_314_369},
    {"name": "MS Dhoni", "instagram_followers": 49_657_277},
    {"name": "Rohit Sharma", "instagram_followers": 42_800_948},
    {"name": "Hardik Pandya", "instagram_followers": 39_265_762},
    {"name": "Suresh Raina", "instagram_followers": 27_615_285},
    {"name": "AB de Villiers", "instagram_followers": 26_421_664},
    {"name": "KL Rahul", "instagram_followers": 21_993_783},
    {"name": "Yuvraj Singh", "instagram_followers": 20_526_202},
    {"name": "Shikhar Dhawan", "instagram_followers": 17_400_000},
    # 10 more powerful Indian names
    {"name": "Jasprit Bumrah", "instagram_followers": 17_900_000},
    {"name": "Suryakumar Yadav", "instagram_followers": 16_600_000},
    {"name": "Mohammed Shami", "instagram_followers": 15_400_000},
    {"name": "Shubman Gill", "instagram_followers": 14_900_000},
    {"name": "Rishabh Pant", "instagram_followers": 13_600_000},
    {"name": "Shreyas Iyer", "instagram_followers": 11_500_000},
    {"name": "Yuzvendra Chahal", "instagram_followers": 10_500_000},
    {"name": "Ishan Kishan", "instagram_followers": 8_000_000},
    {"name": "Ajinkya Rahane", "instagram_followers": 5_400_000},
    {"name": "Ruturaj Gaikwad", "instagram_followers": 5_000_000},
    # International stars
    {"name": "Babar Azam", "instagram_followers": 6_000_000},
    {"name": "David Warner", "instagram_followers": 11_000_000},
    {"name": "Ben Stokes", "instagram_followers": 3_000_000},
    {"name": "Kane Williamson", "instagram_followers": 3_000_000},
    {"name": "Faf du Plessis", "instagram_followers": 5_000_000},
    {"name": "Chris Gayle", "instagram_followers": 3_800_000},
    {"name": "Virender Sehwag", "instagram_followers": 6_600_000},
    {"name": "Steve Smith", "instagram_followers": 1_900_000},
    {"name": "Glenn Maxwell", "instagram_followers": 3_900_000},
]

import random


def format_data(random_cricket):
    account_name = random_cricket["name"]
    return f"account_name: {account_name}"


def check_answer(user_guess, first_account, second_account):
    if first_account > second_account:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game = True
random_cricket_2 = random.choice(data)

while game:

    random_cricket_1 = random_cricket_2
    random_cricket_2 = random.choice(data)
    if random_cricket_1 == random_cricket_2:
        random_cricket_2 = random.choice(data)

    print(f"compare A: {format_data(random_cricket_1)}")
    print(f"against B: {format_data(random_cricket_2)}")

    guess = input("who has more followers ?? type 'A' or type 'B':  ").lower()

    print("\n" * 30)

    account_value_1 = random_cricket_1["instagram_followers"]
    account_value_2 = random_cricket_2["instagram_followers"]

    is_correct = check_answer(guess, account_value_1, account_value_2)
    print("is_correct", is_correct)
    if is_correct:
        score += 1
        print("yes!! you are right and your current score is  ", score)

    else:
        print("sorry!! you are wrong. Final score:  ", score)
        game = False
