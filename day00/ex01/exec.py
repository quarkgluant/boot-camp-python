#!/usr/bin/env python3
# -*-coding:utf-8 -*
from sys import exit, argv

def change(str):
    return str[::-1].swapcase()

if __name__ == '__main__':
    if len(argv) == 1:
        exit(1)
    elif len(argv) == 2:
        print(change(argv[1]))
    else:
        print(' '.join([change(str) for str in argv[-1:0:-1]]))