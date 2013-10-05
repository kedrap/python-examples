from math import sqrt


class Vector2D:
    def __init__(self, x, y=None):
        if isinstance(x, Vector2D):
            self.__x = x.__x
            self.__y = x.__y
        else:
            self.__x = x
            self.__y = y

    def length(self):
        return sqrt((self.__x ** 2 + self.__y ** 2))

    def __add__(self, other):
        return Vector2D(self.__x + other.__x, self.__y + other.__y)

    def __repr__(self):
        return "pos x: {}, y: {}".format(self.__x, self.__y)
        #lenght = property(fget
