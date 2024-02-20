# Practice_1
def main_1():
    print("+" + "-" * 9 + "+")
    for i in range(1,5):
        print("|" + " " * (5-i) + "/" * (i - 1) + "*" + "\\" * (i - 1) + " " * (5-i) + "|")
    for j in range(3,-1,-1):
        print("|" + " " * (4 - j) + "\\" * j + "*" + "/" * j + " " * (4 - j) + "|")
    print("+" + "-" * 9 + "+")

    for j in range(3,-1,-1):
        print("|" + " " * (4 - j) + "\\" * j + "*" + "/" * j + " " * (4 - j) + "|")
    for i in range(1, 5):
        print("|" + " " * (5 - i) + "/" * (i - 1) + "*" + "\\" * (i - 1) + " " * (5 - i) + "|")
    print("+" + "-" * 9 + "+")

main_1()

print( )
print( )
print( )

# Practice_2
def main_2():
    print("|" + '"' * 10 + "|")
    for i in range(4,0,-1):
        print(" " * (5 - i) + "\\" + "::" * i + "/")
    print(" " * 5 + "|" * 2)
    for j in range(1,5):
        print(" " * (5 - j) + "/" + "::" * j + "\\")
    print("|" + '"' * 10 + "|")

main_2()

print( )
print( )
print( )
# Practice_3
def main_3():
    for i in range(1,6):
        print(" " * (6 - i) + "/" * i + "*" * 2 + "\\" * i)
    print("+" + "=*" * 6 + "+")
    for j in range(1,4):
        print("|" + "." * (-j + 3) + "/\\" * j + "." * (-j + 3) * 2 + "/\\" * j + "." * (-j + 3) + "|")
    for n in range(3,0,-1):
        print("|" + "." * (3 - n) +"\\/" * n + "." * (3 - n) + "." * (3 - n) +"\\/" * n + "." * (3 - n) + "|")
    print("+" + "=*" * 6 + "+")
    for n in range(3,0,-1):
        print("|" + "." * (3 - n) +"\\/" * n + "." * (3 - n) + "." * (3 - n) +"\\/" * n + "." * (3 - n) + "|")
    for j in range(1, 4):
        print("|" + "." * (-j + 3) + "/\\" * j + "." * (-j + 3) * 2 + "/\\" * j + "." * (-j + 3) + "|")
    print("+" + "=*" * 6 + "+")
    for i in range(1, 6):
        print(" " * (6 - i) + "/" * i + "*" * 2 + "\\" * i)

main_3()
