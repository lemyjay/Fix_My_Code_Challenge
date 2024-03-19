#!/usr/bin/python3
'''The module for defining a square class'''


class Square:
    '''The square class'''

    def __init__(self, width=0, height=0):
        '''For initializing an object of the class'''
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def permiter_of_square(self):
        '''Calculates and returns the perimeter of a square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''String representation of the object'''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_square())
