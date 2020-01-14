#!/usr/bin/env python3
# -*-coding:utf-8 -*

import numpy as np

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
        for x in range (1, img.shape[0]):
            for y in range(1, img.shape[1]):
                pass

    def gaussian_blur(self, img):
        """This method receives an image, performs a gaussian blur on it and returns a blurred copy.
        In a gaussian blur, the weighting of the neighboring pixels is adjusted so that closer pixels
        are more heavily counted in the average."""

    def _make_gaussian_window(self, n, sigma=1):
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
    for w, ax in zip(window_sizes, axs[0]):
        window = np.ones((w, w))
        window /= np.sum(window)
        # ax.imshow(convolve_all_colours(im_small, window));
        ax.set_title("Mean Filter: window size: {}".format(w));
        ax.set_axis_off()

    def _moving_average(a, n=3):
        ret = np.cumsum(a, dtype=float)
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n - 1:] / n
