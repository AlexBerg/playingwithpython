from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod
from ecc.innercircle import InnerCircle


def testInnerCircle():
    el = Elgamal(P192)
    pub = el.generateKey()

    inner = InnerCircle(7, 5, el.publicKey)

    pointX = el.encrypt(3, pub, P192.G, P192.P)
    pointY = el.encrypt(6, pub, P192.G, P192.P)

    result = inner.getDistanceList(pointX, pointY, pointX * 3, pointY * 6, 5)

    return any(el.decrypt(r) == P192.Zero for r in result)



def testElgamal():
    el = Elgamal(P192)
    clr = 7
    pub = el.generateKey()
    cipher = el.encrypt(clr, pub, P192.G, P192.P)
    decrypted = el.decrypt(cipher)
    clrpoint = P192.getNumberAsCurvePoint(clr)
    if decrypted == clrpoint:
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

    result = testInnerCircle()
    if result:
        print("InnerCircle Success")
    else:
        print("InnerCircle Failed")
