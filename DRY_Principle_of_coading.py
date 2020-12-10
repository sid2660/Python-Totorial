# DRY (Don`t Repeat Yourself)
# Update numberguessing game


import random
winning_number = random.randint(1,100)
guess = 1
user_input = int(input("Guess a number = "))
game_over = False
while not game_over:
    if user_input == winning_number:
        print(f"YOU WIN !!!!, and you guess this number in {guess} time")
        game_over = True
    else:
        if user_input< winning_number:
            print("TOO LOW !!!")
            guess += 1
        # user_input = int(input("Guess this number again : "))
            #  Remove his line and update
        elif user_input>winning_number:
            print("TOO HIGH !!")
        guess += 1
        user_input = int(input("Guess this number again : "))