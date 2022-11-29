#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if (c > 64 and c < 90):
            print("{}".format(chr(c)))
