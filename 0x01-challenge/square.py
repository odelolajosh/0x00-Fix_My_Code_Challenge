#!/usr/bin/python3
""" Documentation """


class Square():
    """ Documentation """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Documentation """
        if len(args) != 0:
            self.width = self.height = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Documentation """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
