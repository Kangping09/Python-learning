# Rock paper scissors

import random
#   Because this easy game is need random, which means we don't know rock、paper or scissors. so first step is need to add
# import random to lead this program.
def play():
    user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors:\n" )
    # We need to define how to play this game;
    computer = random.choice(['r', 'p', 's'])
    # and let computer know how to play this game with user, and give computer a random fucntion to choose from 'r,s,p'

    if user == computer:
        return "Tie"
    # this is user and computer same so we give the tie.
    elif is_win(user, computer):
        return "You won!"
    else:
        return 'You lost'

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())


# Note: I tried other way to find to code this game. when we play R-P-S in real life, we much have a winer, so when
#computer and player have same situation, we will keep play until have a winer.

'''
    if user == computer:
        return "Tie"
    elif (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return "You Won!"
    else:
        return 'You lost'
'''
# this is part of code I changed, becasue new code more simplify