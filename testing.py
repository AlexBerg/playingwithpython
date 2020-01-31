from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod
from ecc.innercircle import InnerCircle
from ecc.utilities import multiplePointTuple
import unittest
from collections import namedtuple

class Test(unittest.TestCase):
    def test_elgamal(self):
        el = Elgamal(P192)
        clr = 7
        pub = el.generateKey()
        cipher = el.encrypt(clr, pub, P192.G, P192.N)
        decrypted = el.decrypt(cipher)
        clrpoint = P192.getNumberAsCurvePoint(clr)

        self.assertEqual(decrypted, clrpoint, "Should be point for 7")

    def test_mod(self):
        mod7 = Mod(7)
        result = mod7(3) + mod7(6)
        self.assertEqual(result, mod7(2), "Should be 2 mod 7")

    def test_inner(self):
        self.assertTrue(testInnerCircleDistance(), "Should be true")
        self.assertTrue(testInnerCircle(), "Should be true")


def testInnerCircleDistance():
    var = getInnerCircleVariables()

    result = var.inner.distance(var.px, var.py, var.px2, var.py2)

    dist = P192.getNumberAsCurvePoint(17) # the distance^2 between these points is 17

    return var.el.decrypt(result) == dist

def testInnerCircle():
    var = getInnerCircleVariables()
    result = var.inner.getDistanceList(var.px, var.py, var.px2, var.py2, 5)
    return any(P192.Zero == var.el.decrypt(r) for r in result)

def getInnerCircleVariables():
    el = Elgamal(P192)
    pub = el.generateKey()

    inner = InnerCircle(7, 5, el.publicKey)

    pointX = el.encrypt(3, pub, P192.G, P192.N)
    pointY = el.encrypt(6, pub, P192.G, P192.N)

    pointXSquare = multiplePointTuple(pointX, 3)
    pointYSquare = multiplePointTuple(pointY, 6)

    tup = namedtuple("inner_circle", ["inner", "px", "py", "px2", "py2", "el"])

    return tup(inner, pointX, pointY, pointXSquare, pointYSquare, el)

if __name__ == "__main__":
    unittest.main()