#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy as np
from numpy.lib import stride_tricks

class AdvancedFilter:
    """
    All methods take in a 3D NumPy array (as in, a tensor of rank 3) and return a modified copy of
    the array.
    The following video should be used as a resource for completing the exercise:
    https://www.youtube.com/watch?v=C_zFhWdM4ic
    BONUS : You can add an optional argument to those methods to choose the kernel size.
    """

    def mean_blur(self, img, window_size=3):
        """This method receives an image, performs a mean blur on it and returns a
        blurred copy. In a mean blur, each pixel becomes the average of its neighboring pixels."""

        #  version vectorisée, plus rapide mais très tricky
        #  cf https://realpython.com/numpy-array-programming/
        # Une première étape instructive consiste à visualiser, compte tenu de la taille du patch et de la forme
        # de l 'image, à quoi ressemblerait un tableau de patchs de dimension supérieure. Nous avons un tableau 2D img
        # avec forme (200, 200) et un (10, 10) patch 2D. Cela signifie que notre forme de sortie (avant de prendre
        # la moyenne de chaque tableau 10x10 «intérieur» ) serait:
        shape = (img.shape[0] - window_size + 1, img.shape[1] - window_size + 1, window_size, window_size)
        # shape = (191, 191, 10, 10)
        strides = 2 * img.strides[:2]
        # img.strides = (2400, 12, 4) et strides =  (2400, 12, 2400, 12)
        patches = stride_tricks.as_strided(img, shape=shape, strides=strides)
        veclen = window_size ** 2
        patches.reshape(*patches.shape[:2], veclen).mean(axis=-1).shape
        patches.mean(axis=(-1, -2)).shape
        strided_means = patches.mean(axis=(-1, -2))
        return strided_means

        # window_size = 3
        # version non-vectorisée
        m, n = img.shape
        mm, nn = m - window_size + 1, n - window_size + 1
        patch_means = np.empty((mm, nn))
        for i in range(mm):
            for j in range(nn):
                patch_means[i, j] = img[i: i + window_size, j: j + window_size].mean()
        return patch_means

    def gaussian_blur(self, img):
        """This method receives an image, performs a gaussian blur on it and returns a blurred copy.
        In a gaussian blur, the weighting of the neighboring pixels is adjusted so that closer pixels
        are more heavily counted in the average."""

    def __make_gaussian_window(self, n, sigma=1):
        """
        Creates a square window of size n by n of weights from a gaussian
        of width sigma.
        """
        nn = int((n - 1) / 2)
        a = np.asarray([[x ** 2 + y ** 2 for x in range(-nn, nn + 1)] for y in range(-nn, nn + 1)])
        return np.exp(-a / (2 * sigma ** 2))

    window_sizes = [9, 17, 33, 65]
    # fig, axs = plt.subplots(nrows=3, ncols=len(window_sizes), figsize=(15, 15));

    # mean filter
    # for w, ax in zip(window_sizes, axes[0]):
    #     window = np.ones((w, w))
    #     window /= np.sum(window)
    #     # ax.imshow(convolve_all_colours(im_small, window));
    #     ax.set_title("Mean Filter: window size: {}".format(w));
    #     ax.set_axis_off()

    # fonctions finalement non-utiles

    # def __moving_average(a, n=3):
    #     ret = np.cumsum(a, dtype=float)
    #     ret[n:] = ret[n:] - ret[:-n]
    #     return ret[n - 1:] / n
    #
    # def __running_mean(x, N):
    #     cumsum = np.cumsum(np.insert(x, 0, 0))
    #     return (cumsum[N:] - cumsum[:-N]) / float(N)

if __name__ == '__main__':
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


    # from ImageProcessor import ImageProcessor
    imp = ImageProcessor()
    arr = imp.load("../ressources/42AI.png")
    # Loading image of dimensions 200 x 200
    imp.display(arr)
    filter = AdvancedFilter()
    mean = filter.mean_blur(arr, window_size=10)
    imp.display(mean)