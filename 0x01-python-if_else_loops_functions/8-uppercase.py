#!/usr/bin/python3
# uppercase - prints a string in uppercase
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - (ord('a') - ord('A')))
        print("{:s}".format(i), end='')
    print()
