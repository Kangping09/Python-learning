# Question: use "for loop" and '*' run_out this graphic:(not include "#  ")
#  ****** //////////// ******
#  *****  //////////\\  *****
#  ****   ////////\\\\   ****
#  ***    //////\\\\\\    ***
#  **     ////\\\\\\\\     **
#  *      //\\\\\\\\\\      *
#         \\\\\\\\\\\\

def main():
    for i in range(6,0,-1):
        print("*" * i + " " * (7-i) + "//" * i, end = "")
        print("\\\\" * (6 - i) + " " * (7 - i) + "*" * i)
    print(" " * 7 + "\\\\" * 6 )

main()

#Coding notes:
#       For this question, for loop is the most important test point. But how to use 'for i in range( )'
# is the key. Remember that have three different range:
#           1. range(max): which means from "0 to max", and not include "max". for example: range(5) ---> 0,1,2,3,4
#           2. range(min, max): which means from "min to max", and not include "max". for example: range(1,4)--> 1,2,3
#   *****   3. range(min, max,step): from "min to max, and every time increase 'step'". And step can be negative
#                    for example_1: range(1,20,3) ----> 1,4,7,10,13,16,19
#                    for example_2: range(20,1,-3) ---> 20, 17,14,11,8,5,2


