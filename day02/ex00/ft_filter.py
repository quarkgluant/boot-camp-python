#!/usr/bin/env python3
# -*-coding:utf-8 -*

def ft_filter(function_to_apply, list_of_inputs):
    return [element for element in list_of_inputs if function_to_apply(element)]



if __name__ == '__main__':
    my_numbers = [1,2,3,4,5]

    results = list(filter(lambda x : x > 3, my_numbers))
    ft_results = list(ft_filter(lambda x : x > 3, my_numbers))

    print(results)
    print(ft_results)
    print(results == ft_results)


    my_pets = ['alfred', 'tabitha', 'william', 'arla']

    uppered_pets = list(filter(lambda s : len(s) > 5, my_pets))
    ft_uppered_pets = list(ft_filter(lambda s : len(s) > 5, my_pets))

    print(uppered_pets == ft_uppered_pets)