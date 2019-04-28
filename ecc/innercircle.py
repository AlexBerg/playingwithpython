from ecc.elgamal import Elgamal

class InnerCircle: 
    def __init__(self, qx, qy, pubKey):
        self.qx = qx
        self.qy = qy
        
        curve = pubKey[0]
        key = pubKey[1]
        elgamal = Elgamal(curve)
        self.elgamal = elgamal
        self.key = key
        self.curve = curve

        self.qxPoint = elgamal.encrypt(qx, key, curve.G, curve.P)
        self.qyPoint = elgamal.encrypt(qy, key, curve.G, curve.P)
        

    def distance(self, px, py, pxSquared, pySquared):
        qxSquared = self.qxPoint * self.qx
        qySquared = self.qyPoint * self.qy

        xValues = pxSquared + qxSquared - ((px * self.qx) * 2) # pxˆ2 + qxˆ2 - 2pxqx
        yValues = pySquared + qySquared - ((py * self.qy) * 2) # pyˆ2 + qyˆ2 - 2pyqy

        return xValues + yValues

    def getDistanceList(self, px, py, pxSquared, pySquared, r):
        dist = self.distance(px, py, pxSquared, pySquared)
        squared = r * r
        d = 0
        result = []

        while d < squared:
            point = self.elgamal.encrypt(d, self.key, self.curve.G, self.curve.P)
            diff = point - dist
            result.append(diff)
            d += 1
        
        return result



    
