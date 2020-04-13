#!/usr/bin/env python3
# -*-coding:utf-8 -*

from sys import exit, argv

MORSE = {
    ' ': '_',
    "'": '.----.',
    '(': '-.--.-',
    ')': '-.--.-',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ':': '---...',
    ';': '-.-.-.',
    '?': '..--..',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--.-'
}


def to_morse(string):
    res = []
    for char in list(string):
        if char.isspace():
            res.append('/')
        elif char.isalnum():
            res.append(MORSE[char.upper()])
        else:
            return 'ERROR'
    return ' '.join(res)


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    else:
        string = " ".join(argv[1:])
        print(to_morse(" ".join(argv[1:])))
