#!/usr/bin/python3
"""define a square class"""


class Square():
    """
    Class that calculates a square area and permiter
    ARGS:
        square = sides of a square
    """
    square = 0

    def __init__(self, *args, **kwargs):
        """ __init__ """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.square * self.square

    def PermiterOfMySquare(self):
        """ permiter of a square """
        return self.square * 4

    def __str__(self):
        """string function of a class"""
        return "{}/{}".format(self.square, self.square)


if __name__ == "__main__":

    s = Square(square=4)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
