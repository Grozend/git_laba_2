import math


class Circle:
    _rad = None

    def set_rad(self, rad):
        self._rad = rad

    def s_circle(self):
        return math.pi * (self._rad ** 2)

    def l_circle(self):
        return 2 * math.pi * self._rad


circle = Circle()

circle.set_rad(12)

print(circle.s_circle())
print(circle.l_circle())