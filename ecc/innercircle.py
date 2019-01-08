from ecc.elgamal import Elgamal

class InnerCircle: 
    def __init__(self, qx, qy, pubKey):
        self.qx = qx
        self.qy = qy
        
        curve = pubKey[0]
        key = pubKey[1]
        elgamal = Elgamal(curve)
        self.qxPoint = elgamal.encrypt(qx, key, curve.G, curve.P)
        self.qyPoint = elgamal.encrypt(qy, key, curve.G, curve.P)
        

    def distance(self, px, py, pxSquared, pySquared):
        qxSquared = self.qxPoint * self.qx
        qySquared = self.qyPoint * self.qy

        xValues = pxSquared + qxSquared - ((px * self.qx) * 2) # pxˆ2 + qxˆ2 - 2pxqx
        yValues = pySquared + qySquared - ((py * self.qy) * 2) # pyˆ2 + qyˆ2 - 2pyqy

        return xValues + yValues



    
