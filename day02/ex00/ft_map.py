#!/usr/bin/env python3
# -*-coding:utf-8 -*

def ft_map(function_to_apply, list_of_inputs):
    return (function_to_apply(element) for element in list_of_inputs)

if __name__ == '__main__':
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [1,2,3,4,5]

    results = list(map(str.upper, my_strings))
    ft_results = list(ft_map(str.upper, my_strings))

    print(results)
    print(ft_results)
    print(results == ft_results)
    my_pets = ['alfred', 'tabitha', 'william', 'arla']

    uppered_pets = list(map(str.upper, my_pets))
    ft_uppered_pets = list(ft_map(str.upper, my_pets))

    print(uppered_pets == ft_uppered_pets)