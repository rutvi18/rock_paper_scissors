import random

import emoji


player = 0
computer = 0
print("1)", end="")
print(emoji.emojize(":raised_fist:"))
print("2)", end="")
print(emoji.emojize(":raised_hand:"))
print("3)", end="")
print(emoji.emojize(":victory_hand:"))
player = int(input("Pick a number: "))
computer = random.randint(1, 3)
if player < 1 or player > 3:
    print("Invalid input. Please enter a number between 1 and 3.")
else:
    print(f'You chose: {player}')
    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win!")
    else:
        print("You lose!")