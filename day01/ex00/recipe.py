def controler_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""

        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""

            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal " \
                                "au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type " \
                                    "{1}".format(i, a_args[i]))

            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type " \
                                    "précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type" \
                                    "{1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)

        return fonction_modifiee

    return decorateur


@controler_types(int, int)
def intervalle(base_inf, base_sup):
    print("Intervalle de {0} à {1}".format(base_inf, base_sup))
   
intervalle(1, 8)
# Intervalle de 1 à 8
intervalle(5, "oups!")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 24, in fonction_modifiee
# TypeError: l'argument 1 n'est pas du type <class 'int'>

def Recipe():
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
        the recipe {name()}, of type {recipe_type()}, is made with {', '.join(ingredients())}
        cooking time: {cooking_time()} with cooking level: {cooking_lvl()}
        """
        return txt

