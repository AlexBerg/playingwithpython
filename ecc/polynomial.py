from utilities import *
from fractions import Fraction

#Remove all z from end of the list
def strip(L, z):
    if len(L) == 0:
        return L
    
    i = len(L) - 1
    while i >= 1 and L[i] == z:
        i -= 1
    
    return L[:i+1]

@memoize
def polynomials(field=Fraction):

    class Polynomial(DomainElement):
        operatorPrecedence = 2

        @classmethod
        def factory(cls, L):
            return Polynomial([cls.field(x) for x in L])

        def __init__(self, c):
            if type(c) is Polynomial:
                self.coefficients = c.coefficients
            elif isinstance(c, field):
                self.coefficients = [c]
            elif hasattr(c, '__iter__') and not hasattr(c, 'iter'):
                self.coefficients = [field(c)]
            else:
                self.coefficients = c

            self.coefficients = strip(self.coefficients, field(0))
        
        def isZero(self):
            return self.coefficients == []

    def Zero():
        return Polynomial([])

    Polynomial.field = field
    return Polynomial