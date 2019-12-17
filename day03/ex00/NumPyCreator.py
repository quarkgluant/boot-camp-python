#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy
from numpy import asarray, full, random, identity


class NumPyCreator:
    def from_list(self, lst, dtype=None):
        """takes in a list and returns its corresponding NumPy array."""
        return asarray(lst, dtype=dtype, order=None)

    def from_tuple(self, tpl, dtype=None):
        """takes in a tuple and returns its corresponding NumPy array."""
        return asarray(tpl, dtype=dtype, order=None)

    def from_iterable(self, itr, dtype=None):
        """takes in an iterable and returns an array which contains all  of its elements."""
        return asarray(list(itr), dtype=dtype, order=None)

    def from_shape(self, shape, value=0, dtype=None):
        """returns an array filled with the same value. The first argument is a tuple which specifies the shape of the
        array, and the second argument specifies the value of  all the elements.This value must be 0 by default."""
        return full(shape, value, dtype=dtype)

    def random(self, shape):
        """returns an array filled with random values. It takes as an argument a tuple which specifies the shape of the array."""
        return random.rand(*shape)

    def identity(self, n, dtype=None):
        """returns an array representing the identity matrix of size n."""
        return identity(n, dtype=dtype)

if __name__ == '__main__':
    # from NumPyCreator import NumPyCreator
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    # array([[1, 2, 3],
    #        [6, 3, 4]])
    print(npc.from_tuple(("a", "b", "c")))
    # array(['a', 'b', 'c'])
    print(npc.from_iterable(range(5)))
    # array([0, 1, 2, 3, 4])
    shape = (3, 5)
    print(npc.from_shape(shape))
    # array([[0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0]])
    print(npc.random(shape))
    # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768],
    #        [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
    #        [0.79585328, 0.00660962, 0.92910958, 0.9905421, 0.05244791]])
    print(npc.identity(4))
    # array([[1., 0., 0., 0.],
    #        [0., 1., 0., 0.],
    #        [0., 0., 1., 0.],
    #        [0., 0., 0., 1.]])