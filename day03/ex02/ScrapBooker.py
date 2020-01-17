#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy as np

class ScrapBooker:
    """All methods take in a NumPy array and return a new modified one.
        We are assuming that all inputs are correct, ie, you don't have to protect your functions
        against input errors.
        In this exercise, when specifying positions or dimensions, we will assume that the first coordinate is counted
        along the vertical axis starting from the TOP, and that the second coordinate is counted along the horizontal axis starting
        from the left.Indexing starts from 0."""

    def crop(self, array, dimensions, position=(0,0)):
        """crop the image as a rectangle with the given dimensions(meaning, the new height and width for the image),
        whose top left corner is given by the position argument.The position should be(0, 0) by default.You have to
        consider it an error( and handle said error) if dimensions is larger than the current image size."""
        if array.shape[0] < position[0] + dimensions[0] or array.shape[1] < position[1] + dimensions[1]:
            raise BaseException(f"the positions {position} + dimensions {dimensions} are greater than the image's dim {array.shape[0:2]}")
        return array[position[0]:dimensions[0], position[1]:dimensions[1]]

    def thin(self, array, n, axis):
        """delete ever n-th pixel row along the specified axis(0 vertical, 1 horizontal), example below."""
        return np.delete(array, [num for num in range(array.shape[axis]) if num % n == 0 and num > 0], axis)


    def juxtapose(self, array, n, axis=0):
        """juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal)."""
        # return np.stack([array for _ in range(n)], axis=axis)
        if axis == 1:
            return np.hstack([array for _ in range(n)])
        elif axis == 0:
            return np.vstack([array for _ in range(n)])

    def mosaic(self, array, dimensions):
        """make a grid with multiple copies of the array.The dimensions argument specifies the dimensions(meaning the
        height and width) of the grid (e.g. 2x3)."""
        result =  self.juxtapose(array, dimensions[0], axis=0)
        return self.juxtapose(result, dimensions[1], axis=1)


import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path) :
        """opens the .png file specified by the path argument and returns an array
        with the RGB values of the image pixels. It must display a message specifying
        the dimensions of the image (e.g. 340 x 500)."""
        img = mpimg.imread(path)
        # if img.dtype == np.float32:  # Si le résultat n'est pas un tableau d'entiers
        #     img = (img * 255).astype(np.uint8)
        print(f"Loading image of dimensions {img.shape[0:2]}")
        return img

    def display(self, array) :
        """takes a NumPy array as an argument and displays the corresponding RGB image."""
        plt.imshow(array)
        plt.show()

if __name__ == '__main__':
    # from ImageProcessor import ImageProcessor
    imp = ImageProcessor()
    arr = imp.load("../ressources/42AI.png")
    # Loading image of dimensions 200 x 200
    imp.display(arr)
    print(arr)
    sb = ScrapBooker()
    imp.display(sb.crop(arr, (100, 100), position=(50, 50)))
    # imp.display(sb.crop(arr, (200, 200)))
    # try:
    #     imp.display(sb.crop(arr, (150, 150), position=(60, 50)))
    # except BaseException:
    #     print("Error")

    three_times = sb.juxtapose(arr, 3)
    print(f"shape of juxtapose: {three_times.shape}")
    imp.display(three_times)
    mosaic = sb.mosaic(arr, (3,2))
    imp.display(mosaic)

