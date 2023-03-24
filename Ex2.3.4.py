class Pixel:
    """
    A class that represents a pixel with its necessary values.
    :param x: The x value of the pixel. Default is 0.
    :type x: int
    :param y: The y value of the pixel. Default is 0.
    :type y: int
    :param r: The red color value of the pixel. Default is 0.
    :type r: int
    :param g: The green color value of the pixel. Default is 0.
    :type g: int
    :param b: The blue color value of the pixel. Default is 0.
    :type b: int
    :ivar _x: The x value of the current pixel
    :ivar _y: The y value of the current pixel
    :ivar _red: The red color value of the current pixel
    :ivar _green: The green color value of the current pixel
    :ivar _blue: The blue color value of the current pixel
    """
    def __init__(self, x: int = 0, y: int = 0,
                 r: int = 0, g: int = 0, b: int = 0):
        self._x, self._y = x, y
        self._red, self._green, self._blue = r, g, b

    def set_coords(self, x: int, y: int) -> None:
        """
        Re-sets the coordinates of the pixel
        :param x: The new x value
        :type x: int
        :param y: The new y value
        :type y: int
        :return: None
        """
        self._x = x
        self._y = y

    def set_grayscale(self) -> None:
        """
        Sets each color of the pixel to the average of all 3
        """
        average = (self._red + self._green + self._blue) // 3
        self._red = self._green = self._blue = average

    def print_pixel_info(self) -> None:
        """
        Used as the __str__ method for the pixel, but prints instead of returning a string
        """
        color = (self._red, self._green, self._blue)
        pixel_properties = f"X: {self._x}, Y: {self._y}, Color: {color}"

        if self._green == 0 and self._blue == 0 and self._red != 0:
            pixel_properties += " Red"
        elif self._red == 0 and self._blue == 0 and self._green != 0:
            pixel_properties += " Green"
        elif self._red == 0 and self._green == 0 and self._blue != 0:
            pixel_properties += " Blue"

        print(pixel_properties)


def main():
    new_pix = Pixel(5, 6, 250)
    new_pix.print_pixel_info()
    new_pix.set_grayscale()
    new_pix.print_pixel_info()


if __name__ == '__main__':
    main()
