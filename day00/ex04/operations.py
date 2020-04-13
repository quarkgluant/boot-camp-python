#!/usr/bin/env python3
# -*-coding:utf-8 -*
from sys import exit, argv


def operate(first_arg, second_arg):
    try:
        first_arg += 0
        second_arg += 0
        arg_1, arg_2 = int(first_arg), int(second_arg)
    except (ValueError, TypeError):
        return """
            InputError: only numbers
            Usage: python operations.py
            Example:
                python operations.py 10 3        
            """
    try:
        return f"""
        Sum:        {arg_1 + arg_2}
        Difference: {arg_1 - arg_2}
        Product:    {arg_1 * arg_2}
        Quotient:   {arg_1 / arg_2}
        Remainder:  {arg_1 % arg_2}
        """
    except ZeroDivisionError:
        return f"""
        Sum:        {arg_1 + arg_2}
        Difference: {arg_1 - arg_2}
        Product:    {arg_1 * arg_2}
        Quotient:   ERROR (div by zero)
        Remainder:  ERROR (modulo by zero)
        """


if __name__ == '__main__':
    if len(argv) < 3:
        print("""Usage: python operations.py
                Example:
                    python operations.py 10 3""")
        exit(1)
    elif len(argv) == 3:
        print(operate(argv[1], argv[2]))

    elif len(argv) > 3:
        print("""InputError: too many arguments
                Usage: python operations.py
                Example:
                    python operations.py 10 3""")
        exit(1)
