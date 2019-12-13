#!/usr/bin/env python3
# -*-coding:utf-8 -*
from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    res = list_of_inputs[0]
    res = function_to_apply(res, list_of_inputs[1])
    for i in range(2, len(list_of_inputs)):
        res = function_to_apply(res, list_of_inputs[i])

    return res


if __name__ == '__main__':
    my_numbers = [1,2,3,4,5]

    results = reduce(lambda x, y: x * y, my_numbers)
    ft_results = ft_reduce(lambda x, y: x * y, my_numbers)

    print(results)
    print(ft_results)
    print(results == ft_results)

    print(reduce(lambda a, b: a * b, range(1, 11)))
    print(ft_reduce(lambda a, b: a * b, range(1, 11)))