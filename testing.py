from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod


def testElgamal():
    el = Elgamal(P192)
    clr = 7
    pub = el.generateKey()
    cipher = el.encrypt(clr, pub, P192.G, P192.P)
    decrypted = el.decrypt(cipher)
    clrpoint = P192.getNumberAsCurvePoint(clr)
    if decrypted.x == clrpoint.x and decrypted.y == clrpoint.y:
        return True
    else:
        return False


def testMod():
    mod7 = Mod(7)
    result = mod7(3) + mod7(6)
    if result == mod7(2):
        return True
    else:
        return False


if __name__ == "__main__":
    result = testMod()
    if result:
        print("Mod Success")
    else:
        print("Mod Failed")

    result = testElgamal()
    if result:
        print("Elgamal Success")
    else:
        print("Elgamal Failed")
