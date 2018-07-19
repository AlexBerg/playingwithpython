from .curve import Curve
import secrets

class Elgamal:
    def __init__(self, curve):
        if not isinstance(curve, Curve):
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

    @classmethod
    def generateKey(self):
        self.secret = secrets.randbelow(self.curve.p - 1)
        self.public = self.curve.G * self.secret
        return True
