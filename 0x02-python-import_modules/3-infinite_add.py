#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    result = 0
    n = len(argv)

    for i in range(1, n):
        result += int(argv[i])
    print(result)
