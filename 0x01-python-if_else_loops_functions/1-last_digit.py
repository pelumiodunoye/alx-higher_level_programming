#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def lastdigit(number):
    if number > 0:
        return(number % 10)
    else:
        number *= -1
        number %= 10
        return(-1 * number)

num = lastdigit(number)
if num > 5:
    print(f"Last digit of {number} is {num} and is reater than 5")
elif num == 0:
    print(f"Last  digit of {number} is {num} and is 0")
else:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
