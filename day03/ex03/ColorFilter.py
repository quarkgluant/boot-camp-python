#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy as np

class ColorFilter:
    """a tool that can apply a variety of color filters on images.
        For this exercise, the authorized functions and operators are specified for each methods. You
        are not allowed to use anything else."""

    def invert(array):
        """Takes a NumPy array of an image as an argument and returns an array with inverted color.
                Authorized function : None
                Authorized operator: -
        """
        pass

    def to_blue(array):
        """Takes a NumPy array of an image as an argument and returns an array with a blue filter.
                Authorized function : .zeros, .shape
                Authorized operator: None
        """
        pass

    def to_green(array):
        """Takes a NumPy array of an image as an argument and returns an array with a green filter.
                Authorized function : None
                Authorized operator: *
        """
        pass
    def to_red(array):
        """Takes a NumPy array of an image as an argument and returns an array with a red filter.
                Authorized function : None
                Authorized operator: *
        """
        pass
    def to_celluloid(array):
        """Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter.
        The celluloid filter must display at least four thresholds of shades. Be careful! You are not
        asked to apply black contour on the object here (you will have to, but later...), you only have to
        work on the shades of your images.
                Authorized function: arange, linspace
        Bonus: add an argument to your method to let the user choose the number of thresholds.
                Authorized function : .vectorize, (.arange?)
                Authorized operator: None
        """
        pass

    def to_grayscale(array, filter):
        """Takes a NumPy array of an image as an argument and returns an array in grayscale. The method takes another
        argument to select between two possible grayscale filters. Each filter has specific authorized functions and operators.
            * 'mean' or 'm' : Takes a NumPy array of an image as an argument and returns an array in grayscale created
            from the mean of the RBG channels.
                Authorized function : .sum, .shape, reshape, broadcast_to, (as_type?)
                Authorized operator: /
            * 'weighted' or 'w' : Takes a NumPy array of an image as an argument and returns an array in weighted grayscale.
            This argument should be selected by default if not given.
            The usual weighted grayscale is calculated as : 0.299 * R_channel + 0.587 * G_channel + 0.114 * B_channel.
                Authorized function : .sum, .shape, .tile
                Authorized operator: *
        """
        pass


import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path):
        """opens the .png file specified by the path argument and returns an array
        with the RGB values of the image pixels. It must display a message specifying
        the dimensions of the image (e.g. 340 x 500)."""
        img = mpimg.imread(path)
        # if img.dtype == np.float32:  # Si le résultat n'est pas un tableau d'entiers
        #     img = (img * 255).astype(np.uint8)
        print(f"Loading image of dimensions {img.shape[0:2]}")
        return img

    def display(self, array):
        """takes a NumPy array as an argument and displays the corresponding RGB image."""
        plt.imshow(array)
        plt.show()

if __name__ == '__main__':

    # from ImageProcessor import ImageProcessor
    imp = ImageProcessor()
    arr = imp.load("../ressources/42AI.png")
    # Loading image of dimensions 200 x 200
    # from ColorFilter import ColorFilter
    cf = ColorFilter()
    cf.invert(arr)
    cf.to_green(arr)
    cf.to_red(arr)
    cf.to_blue(arr)
    cf.to_celluloid(arr)
    cf.to_grayscale(arr, 'm')
    cf.to_grayscale(arr, 'weigthed')