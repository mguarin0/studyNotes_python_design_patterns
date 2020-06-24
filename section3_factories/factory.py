"""
factories paradigm: factory method

Note a factory method is any method that creates an object
alternative to __init__ with better naming
"""
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # redeclaration won't work
    # def __init__(self, rho, theta):

    # clearly not great because will break open-close principle
    # also `a` and `b` not great
    # shitty god object init
   #def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
   #    if system == CoordinateSystem.CARTESIAN:
   #        self.x = a
   #        self.y = b
   #    elif system == CoordinateSystem.POLAR:
   #        self.x = a * sin(b)
   #        self.y = a * cos(b)

        # steps to add a new system
        # 1. augment CoordinateSystem
        # 2. change init method

    class PointFactory
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * sin(theta), rho * cos(theta))

    factory = PointFactory() # makes PointFactory act in a static fashion effectively a singleton instance

# take out factory methods to a separate class
# separation of concerns
# important issue is discoverability
# add in documentation
# or add it as inner class to `Point``
class PointFactory
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.PointFactory.new_cartesian_point(1, 2)
    # or you can expose factory through the type
    p3 = Point.PointFactory.new_cartesian_point(5, 6)
    p4 = Point.PointFactory.new_cartesian_point(7, 8)
    print(p1, p2, p3, p4)
