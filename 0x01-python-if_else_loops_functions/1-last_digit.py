#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
if num > 5:
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
if num == 0:
    print(f"Last digit of {number:d} is {num:d} and is 0")
if 6 > num != 0:
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
