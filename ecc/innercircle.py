from ecc.elgamal import Elgamal
from ecc.point import Point
from ecc.utilities import multiplePointTuple, addTuple, substractTuple

# All encrypted points are actually two value tuples (v1, v2)
# This means all calculations need to be done as (p[0] + p[0], p[1] + p[1]) etc
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

        self.qxEncrypted = elgamal.encrypt(qx, key, curve.G, curve.P)
        self.qyEncrypted = elgamal.encrypt(qy, key, curve.G, curve.P)
        

    def distance(self, px, py, pxSquared, pySquared):
        qxSquared = multiplePointTuple(self.qxEncrypted, self.qx)
        qySquared = multiplePointTuple(self.qyEncrypted, self.qy)

        combX = addTuple(pxSquared, qxSquared)
        combY = addTuple(pySquared, qySquared)

        pxqx = multiplePointTuple(px, self.qx * 2)
        pyqy = multiplePointTuple(py, self.qy * 2)

        xValues = substractTuple(combX, pxqx) # pxˆ2 + qxˆ2 - 2pxqx
        yValues = substractTuple(combY, pyqy) # pyˆ2 + qyˆ2 - 2pyqy

        return addTuple(xValues, yValues)

    def getDistanceList(self, px, py, pxSquared, pySquared, r):
        dist = self.distance(px, py, pxSquared, pySquared)
        squared = r * r
        d = 0
        result = []

        while d < squared:
            point = self.elgamal.encrypt(d, self.key, self.curve.G, self.curve.P)
            diff = substractTuple(point, dist)
            result.append(diff)
            d += 1
        
        return result



    
