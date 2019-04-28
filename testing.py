from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod
from ecc.innercircle import InnerCircle
import unittest

class Test(unittest.TestCase):    
    def test_elgamal(self):
        el = Elgamal(P192)
        clr = 7
        pub = el.generateKey()
        cipher = el.encrypt(clr, pub, P192.G, P192.P)
        decrypted = el.decrypt(cipher)
        clrpoint = P192.getNumberAsCurvePoint(clr)

        self.assertEqual(decrypted, clrpoint, "Should be point for 7")

    def test_mod(self):
        mod7 = Mod(7)
        result = mod7(3) + mod7(6)
        self.assertEqual(result, mod7(2), "Should be 2 mod 7")

    def test_inner(self):
        self.assertTrue(testInnerCircle(), "Should be true")


def testInnerCircle():
    el = Elgamal(P192)
    pub = el.generateKey()

    inner = InnerCircle(7, 5, el.publicKey)

    pointX = el.encrypt(3, pub, P192.G, P192.P)
    pointY = el.encrypt(6, pub, P192.G, P192.P)

    result = inner.getDistanceList(pointX, pointY, pointX * 3, pointY * 6, 5)

    return any(el.decrypt(r) == P192.Zero for r in result)



if __name__ == "__main__":
    unittest.main()