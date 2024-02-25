# A daily question think and notes

# Question is: find 3 mistakes from code.
'''
def main():
    a = 90
    b = 42
    minimum(a, b)
    if smaller == a      # 1. Not define 'smaller' here. should add a define before 'samller = minimum(a,b)'
                         # 2. Missing ':' here, should be ' if smaller == a:'
        print(" a is the smallest!")
def minimum(a, b):
    smaller = 0
    if a < b:
        smaller = a
    else a => b:         # 3. there is no need to add anything after 'else', should be ' else:'
        smaller = b
    return smaller

main()
'''

# I give a right answer here, and also add some notes.

def main():
    a = 90
    b = 42
    minimum(a, b)
    result = minimum(a,b)    #  We need define 'result = minimun(a,b)', which means let "result" equal to minimum, which
                             #also can let return smaller know to result.
    if result == a:
        print(" a is the smallest!")
    else:                    # for here, I add two line codes for more details. Becasue for the orginal question we
                             #already know hta a<b, and a = 7, b =42. But if a > b, will have 'None' for final.
        print(" b is not the smallest!")
def minimum(a, b):
    smaller = 0              # this line also means that we need to define a variable first. but for this question
                             #it is ok if no 'samller = 0', no any issue.
    if a < b:
        smaller = a
    else:
        smaller = b
    return smaller
main()
