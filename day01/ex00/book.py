import datetime

def Book():
    def __init__(self, name, last_update, creation_date, recipe_list):
        self._name = name
        self._last_update = last_update
        self._creation_date = creation_date
        self._recipe_list = recipe_list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise Exception("name cannot be empty")
        self._name = new_name

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, new_time):
        if type(new_time) is not datetime:
            raise Exception("last update must be of type datetime")
        self._last_update = new_time

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, new_time):
        if new_time < 0:
            raise Exception("creation_date must be of type datetime")
        self._creation_date = new_time

    @property
    def recipe_list(self):
        return self._recipe_list

    @recipe_list.setter
    def recipe_list(self, new_list):
        if new_list.keys not in ["starter", "lunch", "dessert"]:
            raise Exception("recipe_list must be starter, lunch or dessert")
        self._recipe_list = new_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""
        the recipe {name()}, with {recipe_list()}, is made at {creation_date()}
        and updated at {last_update()}
        """
        return txt

