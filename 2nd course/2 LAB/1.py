import math
class Triangle():
    _a = 0
    _b = 0
    _c = 0
    def __init__(self, _a, _b, _c):
        self._a = _a
        self._b = _b
        self._c = _c
    def square(self):
        if (self.exsist()):
            _p = self.perimenter() / 2
            _ret = 0
            try:
                _ret = math.sqrt(_p * (_p - self._a) * (_p - self._b) * (_p - self._c))
            except ValueError:
                return False
            else:
                return _ret
        else:
            return False
    def perimenter(self):
        if (self.exsist()):
            return self._a + self._b + self._c
        else:
            return False
    def exsist(self):
        _p = (self._a + self._b + self._c) / 2
        try:
            math.sqrt(_p * (_p - self._a) * (_p - self._b) * (_p - self._c))
        except ValueError:
            return False
        else:
            return True

_tr = Triangle(3, 4, 5)
print(_tr.square())
