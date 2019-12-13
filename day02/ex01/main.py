def what_are_the_vars(*args, **kwargs):
    """Your code"""
    obj = ObjectC()
    for index, element in enumerate(args):
        setattr(obj, f"var_{index}", args[index])
    for key, value in kwargs.items():
        setattr(obj, key, value)
    if len(obj.__dict__) == 0:
        return None
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    # var_0: 7
    # end

    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    # var_0: ft_lol
    # var_1: Hi
    # end

    obj = what_are_the_vars()
    doom_printer(obj)
    # ERROR
    # end

    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    # var_0: 12
    # var_1: Yes
    # var_2: [0, 0, 0]
    # hello: world
    # end

    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    # var_0: 12
    # a: 10
    # var_0: world
    # end
