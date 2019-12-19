#!/usr/bin/env python3
# -*-coding:utf-8 -*

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path) :
        """opens the .png file specified by the path argument and returns an array
        with the RGB values of the image pixels. It must display a message specifying
        the dimensions of the image (e.g. 340 x 500)."""
        img = mpimg.imread(path)
        if img.dtype == np.float32:  # Si le résultat n'est pas un tableau d'entiers
            img = (img * 255).astype(np.uint8)
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
    print(arr.shape)
    color = arr[0, 0, :]
    print(f"extrait 3x3x3: {arr[:3, :3, :]}")
    print(color)
