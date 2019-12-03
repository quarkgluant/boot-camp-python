#!/usr/bin/env python3
# -*-coding:utf-8 -*
from sys import stdin

def text_analyzer(text=''):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    :param text: text to analyse or stdin by default
    :return: numbers of spaces, punctuation marks, upper and lower letters
    """
    nb_chars = spaces = upper_letters = lower_letters = punctuations = 0

    if len(text) > 0:
        text = text
    else:
        print("What is the text to analyse?")
        text = stdin.read()

    space = text.count(' ')
    for char in text:
        nb_chars += 1
        if char.islower():
            lower_letters += 1
        elif char.isupper():
            upper_letters += 1
        elif char in [";", ":", ".", "!", "?", ",", "-", "'"]:
            punctuations += 1
        elif char.isspace():
            spaces += 1

    print(f"This text contains {nb_chars} characters:")
    print(f"- {upper_letters} upper letters")
    print(f"- {lower_letters} lower letters")
    print(f"- {punctuations} punctuation marks")
    print(f"- {spaces} spaces")
    print(f"- {space} spaces")