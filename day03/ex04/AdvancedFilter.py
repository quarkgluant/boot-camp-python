class AdvancedFilter:
    """
    All methods take in a 3D NumPy array (as in, a tensor of rank 3) and return a modified copy of
    the array.
    The following video should be used as a resource for completing the exercise:
    https://www.youtube.com/watch?v=C_zFhWdM4ic
    BONUS : You can add an optional argument to those methods to choose the kernel size.
    """

    def mean_blur(self, img):
        """This method receives an image, performs a mean blur on it and returns a
        blurred copy. In a mean blur, each pixel becomes the average of its neighboring pixels."""
        pass

    def gaussian_blur(self, img):
        """This method receives an image, performs a gaussian blur on it and returns a blurred copy.
        In a gaussian blur, the weighting of the neighboring pixels is adjusted so that closer pixels
        are more heavily counted in the average."""