#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy as np

class ColorFilter:
    """a tool that can apply a variety of color filters on images.
        For this exercise, the authorized functions and operators are specified for each methods. You
        are not allowed to use anything else."""

    def _dtype_to_int(selfself, array):
        if array.dtype == np.float32:  # Si le résultat n'est pas un tableau d'entiers
            array = (array * 255).astype(np.uint8)
        if array.dtype == np.float64:  # Si le résultat n'est pas un tableau d'entiers
            array = (array * 255 * 255).astype(np.uint16)
        return array

    def _blue_mask(self, array):
        array = self._dtype_to_int(array)
        shape_mask = [array.shape[0], array.shape[1], array.shape[2] - 1]
        return np.zeros(shape_mask, dtype=array.dtype)

    def _shading(self, colors, thresholds):
        val_threshold = 256 // thresholds
        for index, val in enumerate(colors):
            for i in range(thresholds):
                if val_threshold * i <= val < val_threshold * (i + 1):
                    colors[index] &= val_threshold * i
            # if val < 64:
            #     colors[index] &= 64 * (thresholds - 4)
            # elif 64 <= val < 128:
            #     colors[index] &= 64 * (thresholds - 3)
            # elif 128 <= val < 192:
            #     colors[index] &= 64 * (thresholds - 2)
            # elif val >= 192 :
            #     colors[index] = 64 * (thresholds - 1)


    def invert(self, array):
        """Takes a NumPy array of an image as an argument and returns an array with inverted color.
                Authorized function : None
                Authorized operator: -
        """
        array = self._dtype_to_int(array)
        return -array

    def to_blue(self, array):
        """Takes a NumPy array of an image as an argument and returns an array with a blue filter.
                Authorized function : .zeros, .shape
                Authorized operator: None
        """
        array = self._dtype_to_int(array)
        mask = self._blue_mask(array)
        array[:, :, :2] = mask
        return array

    def to_green(self, array):
        """Takes a NumPy array of an image as an argument and returns an array with a green filter.
                Authorized function : None
                Authorized operator: *
        """
        return array[:, :, :] * [0, 1, 0]

    def to_red(self, array):
        """Takes a NumPy array of an image as an argument and returns an array with a red filter.
                Authorized function : None
                Authorized operator: *
        """
        return array[:, :, :] * [1, 0, 0]

    def to_celluloid(self, array, n=4):
        """Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter.
        The celluloid filter must display at least four thresholds of shades. Be careful! You are not
        asked to apply black contour on the object here (you will have to, but later...), you only have to
        work on the shades of your images.
                Authorized function: arange, linspace
        Bonus: add an argument to your method to let the user choose the number of thresholds.
                Authorized function : .vectorize, (.arange?)
                Authorized operator: None
        """
        array = self._dtype_to_int(array)
        # vfunc = np.vectorize(self._shading)
        for ext_array in array:
            for colors in ext_array:
                self._shading(colors, n)
                # vfunc(colors, n)

        return array


    def to_grayscale(self, array, filter="w"):
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
        if filter.startswith("m"):
            # on fait la somme selon l'axe z, donc la somme des 3 nombres RGB:
            arr_sum = np.sum(array, axis=2)
            # arr_sum.shape => (200, 200), donc on transforme cette matrice pour en faire (200, 200, 1):
            arr_resh = np.reshape(arr_sum, (200, 200, 1))
            # ne reste plus qu'à cloner 3 fois la valeur en z, pour avoir une array de (200, 200, 3):
            arr_br = np.broadcast_to(arr_resh, (200, 200, 3))
            # étape finale, on divise par le nombre de couleurs:
            arr_mean = arr_br[:,:,:] / array.shape[2]
            return arr_mean
        elif filter.startswith("w"):
            #  on multiplie les couleurs RGB par les coefficients, puis on somme le tout
            arr_sum = np.sum(array[:, :, :] * [0.299, 0.587, 0.114], axis=2)
            # arr_sum.shape => (200, 200), donc on crée une 3e dim avec arr_sum[:, :, None]
            arr_w = np.tile(arr_sum[:, :, None], (1, 1, 3))
            return arr_w


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
    print(f"type of arr: {arr.dtype}")
    # Loading image of dimensions 200 x 200
    # from ColorFilter import ColorFilter
    cf = ColorFilter()
    invert_arr = cf.invert(arr)
    print("première case de arr:")
    print(arr[ 1, 1, :])
    print("première case de invert_arr:")
    print(invert_arr[ 1, 1, :])
    imp.display(invert_arr)
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_celluloid(arr, 8))
    imp.display(cf.to_celluloid(arr, 2))
    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weigthed'))