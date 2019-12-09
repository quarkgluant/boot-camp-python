class Vector:
    def __init__(self, values):
        if type(values) is int:
            self.values = [float(number) for number in range(0, values)]
        elif type(values) is tuple:
            self.values = [float(number) for number in range(values[0], values[1])]
        elif type(values) is list:
            self.values = values
        else:
            raise TypeError("You must put an integer, or a range or a list of numeric values")

        self.length = len(self.values)

    def __add__(self, other):
        if type(other) is Vector:
            if self.length == other.length:
                return Vector([sum(value) for value in zip(self.values, other.values)])
            else:
                raise TypeError("The vectors must have same size")
        elif type(other) is int or type(other) is float:
            return Vector([value + other for value in self.values])
        else:
            raise TypeError("You can add/substract to a vector only another vector or a scalar")

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Vector([-value for value in self.values])

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -(self - other)

    def __mul__(self, other):
        if type(other) is Vector:
            if self.length == other.length:
                return sum([value[0] * value[1] for value in zip(self.values, other.values)])
            else:
                raise TypeError("The vectors must have same size")
        elif type(other) is int or type(other) is float:
            return Vector([value * other for value in self.values])
        else:
            raise TypeError("You can multiply a vector by only another vector or a scalar")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            if other is not 0:
                return Vector([value / other for value in self.values])
            else:
                raise ZeroDivisionError
        else:
            raise TypeError("You can divide a vector by only a scalar")

    def __rtruediv__(self, other):
        if type(other) is int or type(other) is float:
            if any(self.values):
                return Vector([other / value for value in self.values])
            else:
                raise ZeroDivisionError
        else:
            raise TypeError("You can divide a scalar by only a vector")
