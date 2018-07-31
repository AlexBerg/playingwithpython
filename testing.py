import sys
sys.path.append('ecc')

from elgamal import Elgamal
from curves import P192
from fieldInts import FieldInts


def testElgamal():
    el = Elgamal(P192)
    clr = 7
    pub = el.generateKey()
    cipher = el.encrypt(clr, pub[0], pub[1], pub[2])
    decrypted = el.decrypt(cipher)
    if decrypted == clr:
        return True
    else:
        return False


def testField():
    mod7 = FieldInts(7)
    result = mod7(3) + mod7(6)
    if result == mod7(2):
        return True
    else:
        return False


if __name__ == "__main__":
    result = testField()
    if result:
        print("Field Success")
    else:
        print("Field Failed")

    result = testElgamal()
    if result:
        print("Elgamal Success")
    else:
        print("Elgamal Failed")
