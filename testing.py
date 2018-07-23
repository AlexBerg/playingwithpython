from elgamal import Elgamal
from curves import P192


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


if __name__ == "__main__":
    result = testElgamal()
    if result:
        print("Success")
    else:
        print("Failed")
