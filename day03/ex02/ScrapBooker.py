#!/usr/bin/env python3
# -*-coding:utf-8 -*

from numpy import asarray, full, random, identity

class ScrapBooker:
    """In this exercise, when specifying positions or dimensions, we will assume that the first coordinate is counted
        along the vertical axis starting from the TOP, and that the second coordinate is counted along the horizontal axis starting
        from the left.Indexing starts from 0."""

    def crop(self, array, dimensions, position):
        """crop the image as a rectangle with the given dimensions(meaning, the new height and width for the image),
        whose top left corner is given by the position argument.The position should be(0, 0) by default.You have to
        consider it an error( and handle said error) if dimensions is larger than the current image size."""
        pass

    def thin(self, array, n, axis):
        """delete ever n-th pixel row along the specified axis(0 vertical, 1 horizontal), example below."""
        pass

    def juxtapose(self, array, n, axis):
        """juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal)."""
        pass

    def mosaic(self, array, dimensions):
        """make a grid with multiple copies of the array.The dimensions argument specifies the dimensions(meaning the
        height and width) of the grid (e.g. 2x3)."""
        pass

