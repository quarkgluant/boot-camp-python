#!/usr/bin/env python3
# -*-coding:utf-8 -*

from book import Book
from recipe import Recipe


cookbook = {
    'sandwich': {
        'ingredients': [ 'ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': [ 'flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': [ 'avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    }
}

sandwich = Recipe('sandwich', 1, 10, [ 'ham', 'bread', 'cheese', 'tomatoes'], 'THE sandwich', 'lunch')
# sandwich.name, sandwich.cooking_lvl, sandwich.cooking_time, sandwich.ingredients, sandwich.description, sandwich.recipe_type = 'sandwich', 1, 10, [ 'ham', 'bread', 'cheese', 'tomatoes'], 'THE sandwich', 'lunch'
print(sandwich)

cake = Recipe('cake', 2, 60, [ 'flour', 'sugar', 'eggs'], 'The marvelous cake', 'dessert')
print(cake)

salad = Recipe('salad', 1, 15, [ 'avocado', 'arugula', 'tomatoes', 'spinach'], 'THE salad', 'starter')

my_null_book = Book('null book', dict(starter=[salad], lunch=[sandwich], dessert=[cake]))

print(my_null_book)

