#!/usr/bin/env python3
# -*-coding:utf-8 -*
from sys import exit, argv


def oddity(string):
    number = int(string)
    if number == 0:
        return "I'm Zero."
    elif number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if __name__ == '__main__':
    if len(argv) == 1:
        exit(1)
    elif len(argv) == 2 and argv[1].isdigit():
        print(oddity(argv[1]))
    else:
        print('ERROR')
