from utilities import *

class _Modular(FieldElement):
    NotImplemented

@memoize
def FieldInts(p):
    class FieldInt(FieldElement):
        def __init__(self, n):
            try:
                self.n = int(n) % p
            except Exception:
                raise TypeError('Can not cast %s to int' % (type(n).__name__))
            self.field = FieldInt

        @typecheck
        def __add__(self, other):
            return FieldInt(self.n + other.n)
        @typecheck
        def __sub__(self, other):
            return FieldInt(self.n - other.n)
        @typecheck
        def __mul__(self, other):
            return FieldInt(self.n * other.n)
        @typecheck
        def __truediv__(self, other):
            return self * other.inverse()
        @typecheck
        def __div__(self, other):
            return self * other.inverse()
        def __neg__(self):
            return FieldInt(-self.n)
        @typecheck
        def __eq__(self, other):
            return isinstance(other, FieldInt) and self.n == other.n
        def __abs__(self):
            return abs(self.n)
        def __str__(self):
            return str(self.n)
        def __repr__(self):
            return '%d (mod %d)' % (self.n, self.p)

        @typecheck
        def __divmod__(self, divisor):
            q, r = divmod(self.n, divisor.n)
            return (FieldInt(q), FieldInt(r))

        def inverse(self):
            x, y, d = euclideanAlgorithm(self.n, self.p)
            return FieldInt(x)

    FieldInt.p = p
    FieldInt.__name__ = 'Z/%d' % (p)
    return FieldInt


def euclideanAlgorithm(a, b):
    if abs(b) > abs(a):
        (x, y, d) = euclideanAlgorithm(b, a)
        return (y, x, d)

    if abs(b) == 0:
        return(1, 0, a)

    x1, x2, y1, y2 = 0, 1, 1, 0
    while abs(b) > 0:
        q, r = divmod(a, b)
        x = x2 - q*x1
        y = y2 - q*y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

    return (x2, y2, a)
