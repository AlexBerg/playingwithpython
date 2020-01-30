import ecc.curves as curves
import secrets
import ecc.point as point


class Elgamal:
    def __init__(self, curve):
        if not isinstance(curve, curves.Curve):
            raise Exception("curve must be instance of Curve")
        else:
            self.curve = curve
            self.secret = None
            self.public = None

    @property
    def publicKey(self):
        if self.public is None:
            raise Exception("Keys not generated")
        else:
            return (self.curve, self.public)

    def generateKey(self):
        self.secret = secrets.randbelow(self.curve.N - 1)
        self.public = self.curve.getNumberAsCurvePoint(self.secret)
        return self.public

    def encrypt(self, msg, pub, g, n):
        pt = g * msg
        r = secrets.randbelow(n - 1)
        p1 = g * r
        p2 = pt + (pub * r)
        return (p1, p2)

    def decrypt(self, cipher):
        c = cipher[0] * self.secret
        msg = cipher[1] - c
        return msg
