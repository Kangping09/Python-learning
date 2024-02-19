# Project two
# let computer guess a random number from our mind

import random

def computer_guess(x):
    low = 1
    high = x       #first, I need to give a range from 1 to x, and let computer to guess;
    feedback = " "   # second, need to expression feedback before in the while loop;
    while feedback != "c":    # if feedback not correctly
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high, bc low = high
        feedback = input(f"Is {guess} too high (H), or too low (L), or correct (C): ").lower()   # feedback is for user;
        # give computer a feedback, does computer guessing too high, too low or corrcet. and .lower means, feedback all
        # lower leeter which are: h,l,c
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1 # this if else function means, the correct guess number should be the last guess number + 1

    print(f"Yay! The computer guessed {guess}, correctly.")

computer_guess(100)