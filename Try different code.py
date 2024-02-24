import random
def play():
    while True:
        computer = random.choice(['r', 'p', 's'])
        user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors:\n")

        if user == computer:
            print("It's a tie! Try again.")
            continue

        if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
            print("You Won!")
        else:
            print("You lost!")

        print("Computer chose:", computer)
        break

play()

#    In this code, i just use while loop to find a real winner which means code will not stop when user equal computer
#and in this code, there are two funny point, one is when 'user == computer', use contiue to keep loop, and let user
#try again. And at end of the code just use 'break' which can stop this loop continue.


