#!/usr/bin/env python3
# -*-coding:utf-8 -*

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

print('les clés majeurs')
print(cookbook.keys())
print('toutes les clés')
for name, recipe in cookbook.items():
    print(name)
    for key, _ in recipe.items():
        print(key)

print('les valeurs majeures')
print(cookbook.values())
print('toutes les valeurs')
for name, recipe in cookbook.items():
    for _, val in recipe.items():
        print(val)

print('tout')
print(cookbook.items())
for name, recipe in cookbook.items():
    print(name)
    for key, val in recipe.items():
        print(key, val)

def print_recipe(name):
    print(f"""
    Recipe for {name}:
    Ingredients list: {cookbook[name]['ingredients']}
    To be eaten for {cookbook[name]['meal']}.
    Takes {cookbook[name]['prep_time']} minutes of cooking.
    """)

def delete_recipe(name):
    del cookbook[name]

def add_recipe(name, ingredients, meal, prep_time):
    # cookbook[name]['ingredients'] = ingredients
    # cookbook[name]['meal'] = meal
    # cookbook[name]['prep_time'] = prep_time
    cookbook[name] = dict(ingredients=ingredients, meal=meal, prep_time=prep_time)

def print_all():
    for name in cookbook:
        print_recipe(name)

usage = """
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
"""

def menu():
    print(usage)
    choice = input()
    while choice != '5':

        if choice == '1':
            recipe = input("Please enter the recipe's name, an array of ingredients, the type of meal and the preparation time:")
            add_recipe(recipe)
        elif choice == '2':
            name = input("Please enter the recipe's name to delete:")
            delete_recipe(name)
        elif choice == '3':
            recipe = input("Please enter the recipe's name to print:")
            print_recipe(recipe)
        elif choice == '4':
            print_all()
        else:
            print("""
            This option does not exist, please type the corresponding number.
            To exit, enter 5.
            """)
        choice = input(usage)

    print("Cookbook closed.")
    exit(0)

if __name__ == '__main__':
    menu()