from math import sqrt


class Vector2d:
    def __init__(self, x, y=None):
        #if isinstance(x, Vector2d):
        if y == None:
            print('aa')
            self.x = x.x
            self.y = x.y
        else:
            print('bb')
            self.x = x
            self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'x=' + str(self.x) + ', y=' + str(self.y)

    def __lenght(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    lenght = property(fget=__lenght)


v1 = Vector2d(1, 1)
v2 = Vector2d(2, 2)
v3 = v1 + v2

print(v1.lenght)
print(v2.lenght)
print(v3.lenght)
print(v1 + v2)

v4 = Vector2d(v3)
