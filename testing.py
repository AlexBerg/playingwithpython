from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod
from ecc.innercircle import InnerCircle
from ecc.utilities import multiplePointTuple
import unittest

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


def testInnerCircleDistance():
    el = Elgamal(P192)
    pub = el.generateKey()

    inner = InnerCircle(7, 5, el.publicKey)

    pointX = el.encrypt(3, pub, P192.G, P192.N)
    pointY = el.encrypt(6, pub, P192.G, P192.N)

    pointXSquare = multiplePointTuple(pointX, 3)
    pointYSquare = multiplePointTuple(pointY, 6)

    result = inner.distance(pointX, pointY, pointXSquare, pointYSquare)

    dist = P192.getNumberAsCurvePoint(17)

    return el.decrypt(result) == dist 



if __name__ == "__main__":
    unittest.main()