#!/usr/bin/python3
""" Documentation """

class square():
    """ Documentation """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ Documentation """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())i
