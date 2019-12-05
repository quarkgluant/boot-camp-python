#!/usr/bin/env python3
# -*-coding:utf-8 -*

from random import randint

usage = """
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
What's your guess between 1 and 99?
>> """

def guess(number, count, target):

    try:
        to_guess = int(number)
        if to_guess == target:
            res = "Congratulations! You got it on your first try!" if count == 1 else f"You won in {count} attempts!"
            if target == 42:
                res = "The answer to the ultimate question of life, the universe and everything is 42\n" + res
            return res

        elif to_guess < target:
            return "Too low!"
        else:
            return "Too high!"

    except (ValueError, TypeError):
        return 'ERROR'


if __name__ == '__main__':
    count = 1
    essai = input(usage)
    mystery = randint(1, 99)
    while essai != 'exit':
        response = guess(essai, count, mystery)
        print(response)
        if int(essai) == mystery:
            break
        count += 1
        essai = input("What's your guess between 1 and 99?\n>> ")
    print("Good Bye!")