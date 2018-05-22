class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

        if not curve.pointOnCurve(x, y):
            raise Exception("Point %s is not on the curve %s" % (self, curve))

    def __neg__(self):
        return Point(self.x, -self.y, self.curve)

    def __add__(self, Q):
        if isinstance(Q, IdealPoint):
            return self

        x1, y1, x2, y2 = self.x, self.y, Q.x, Q.y

        if (x1, y1) == (x2, y2):
            if(y1 == 0):
                return IdealPoint(self.curve)

            m = (3 * x1 * x1 + self.curve.a) / (2 * y1)
        else:
            if x1 == x2:
                return IdealPoint(self.curve)

            m = (y2 - y1) / (x2 - x1)

        x3 = m*m - x2 - x1
        y3 = m*(x3 - x1) + y1

        return Point(x3, -y3, self.curve)

    def __sub__(self, Q):
        return self + -Q



class IdealPoint(Point):
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __neg__(self):
        return self

    def __add__(self, Q):
        return Q
