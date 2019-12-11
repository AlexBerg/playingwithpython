from ecc.elgamal import Elgamal
from ecc.point import Point
from ecc.utilities import multiplePointTuple

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

        self.qxTuple = elgamal.encrypt(qx, key, curve.G, curve.P)
        self.qyTuple = elgamal.encrypt(qy, key, curve.G, curve.P)
        

    def distance(self, px, py, pxSquared, pySquared):
        qxSquared = multiplePointTuple(self.qxTuple, self.qx)
        qySquared = multiplePointTuple(self.qyTuple, self.qy)

        combX = (pxSquared[0] + qxSquared[0], pxSquared[1] + qxSquared[1])
        combY = (pySquared[0] + qySquared[0], pySquared[1] + qySquared[1])

        pxqx = (px[0] * self.qx * 2, px[1] * self.qx * 2)
        pyqy = (py[0] * self.qy * 2, py[1] * self.qy * 2)

        xValues = (combX[0] - pxqx[0], combX[1] - pxqx[1]) # pxˆ2 + qxˆ2 - 2pxqx
        yValues = (combY[0] - pyqy[0], combY[1] - pyqy[1]) # pyˆ2 + qyˆ2 - 2pyqy

        return xValues + yValues

    def getDistanceList(self, px, py, pxSquared, pySquared, r):
        dist = self.distance(px, py, pxSquared, pySquared)
        squared = r * r
        d = 0
        result = []

        while d < squared:
            point = self.elgamal.encrypt(d, self.key, self.curve.G, self.curve.P)
            diff = (point[0] - dist[0], point[1] - dist[1])
            result.append(diff)
            d += 1
        
        return result



    
