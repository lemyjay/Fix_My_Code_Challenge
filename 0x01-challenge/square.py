#!/usr/bin/python3
'''The module for defining a square class'''


class square():
    '''The square class'''
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        '''For initializing an object of the class'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def PermiterOfMySquare(self):
        '''Calculates and returns the perimeter of a square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''String representation of the object'''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
