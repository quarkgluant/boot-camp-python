#!/usr/bin/env python3
# -*-coding:utf-8 -*
from sys import exit, argv

def operate(string, size):
    return [word for word in string.split(' ') if len(word) > size]

if __name__ == '__main__':
    if len(argv) == 3:
        print(operate(argv[1], int(argv[2])))
    else:
        print("ERROR")
        exit(1)