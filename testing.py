from ecc.elgamal import Elgamal
from ecc.curves import P192
from ecc.mods import Mod


def testElgamal():
    el = Elgamal(P192)
    print("Have curve!")
    clr = 7
    pub = el.generateKey()
    print("Generated key!")
    cipher = el.encrypt(clr, pub[0], pub[1], pub[2])
    decrypted = el.decrypt(cipher)
    if decrypted == clr:
        return True
    else:
        return False


def testField():
    mod7 = Mod(7)
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
