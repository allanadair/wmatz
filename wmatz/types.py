import math


class WeightedPointZ(object):
    def __init__(self, x, y, z, weight=1.0):
        """
        Point primitive.

        :param x: X coordinate of point
        :type x: float or integer
        :param y: Y coordinate of point
        :type y: float or integer
        :param z: Z coordinate of point
        :type z: float or integer
        :param weight: Weight measurement of the point
        :type weight: float or integer
        """
        self._x = x
        self._y = y
        self._z = z
        self._w = weight

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def distance(self, other):
        """
        Calculates the distance between the instantiated point and one other.

        :param other: Another point
        :type other: WeightedPointZ
        """
        return math.sqrt((other.x - self.x) ** 2 +
                         (other.y - self.y) ** 2 +
                         (other.z - self.z) ** 2)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def weight(self):
        return self._w
