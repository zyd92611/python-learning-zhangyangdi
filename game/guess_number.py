import random

var1 = random.randint(1, 1000)
while True:
    var2 = int(input("Enter a number"))
    if var2 < var1:
        print("The number is too small")
    elif var2 > var1:
        print("The number is too big")
    else:
        print("Bingo")
        break