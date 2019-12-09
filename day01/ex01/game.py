class GotCharacter:
    """class for characters of Games Of Throne
    attributes: first_name, is_alive=True
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people.
    attributes: family_name, house_words
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

# python
# >>> from game import GotCharacter, Stark
# >>> arya = Stark("Arya")
# >>> print(arya.__dict__)
# {'first_name': 'Arya', 'is_alive': True, 'family_name': 'Stark', 'house_words': 'Winter is Coming'}
# >>> aray.print_house_words
# >>> arya.print_house_words()
# Winter is Coming
# >>> arya.die()
# >>> print(arya.is_alive)
# >>> False

