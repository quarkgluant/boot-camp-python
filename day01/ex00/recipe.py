#!/usr/bin/env python3
# -*-coding:utf-8 -*

class Recipe:
    """class Recipe with name, cooking_lvl, cooking_time, ingredients, description, recipe_type"""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self._name = name
        self._cooking_lvl = cooking_lvl
        self._cooking_time = cooking_time
        self._ingredients = ingredients
        self.description = description
        self._recipe_type = recipe_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise Exception("name cannot be empty")
        self._name = new_name

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, new_level):
        if new_level not in range(1,6):
            raise Exception("cooking_lvl must be beetwen 1 and 5")
        self._cooking_lvl = new_level

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, new_time):
        if new_time < 0:
            raise Exception("cooking_time must be positive")
        self._cooking_time = new_time

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, new_ingredients):
        if not new_ingredients:
            raise Exception("ingredients cannot be empty")
        self._ingredients = new_ingredients

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, new_type):
        if new_type not in ["starter", "lunch", "dessert"]:
            raise Exception("recipe_type must be starter, lunch or dessert")
        self._recipe_type = new_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""
        the recipe {self.name}, of type {self.recipe_type}, is made with {', '.join(self.ingredients)}
        cooking time: {self.cooking_time} with cooking level: {self.cooking_lvl}
        """
        return txt

