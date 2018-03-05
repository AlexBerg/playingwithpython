class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

        if not curve.pointOnCurve(x, y):
            raise Exception("Point %s is not on the curve %s" % (self, curve))
