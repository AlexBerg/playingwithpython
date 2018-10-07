import itertools
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

        def __repr__(self):
            if self.isZero():
                return '0'

            return ' + '.join(['%s xˆ%d' % (a, i) if i > 0 else '%s' % a for a, i in enumerate(self.coefficients)])

        def __abs__(self): 
            return len(self.coefficients)
        def __len__(self):
            return len(self.coefficients)
        def __sub__(self, other):
            return self + (-other)
        def __iter__(self):
            return iter(self.coefficients)
        def __neg__(self):
            return Polynomial([-a for a in self.coefficients])

        def iter(self):
            return self.__iter__()
        def leadingCoefficient(self):
            return self.coefficients[-1]
        def degree(self):
            return abs(self) - 1

        @typecheck
        def __eq__(self, other):
            return self.degree == other.degree and all([x==y for x,y in zip(self, other)])
        @typecheck
        def __add__(self, other):
            newCoeffs = [sum(x) for x in itertools.zip_longest(self, other, fillvalue=self.field(0))]
            return Polynomial(newCoeffs)
        @typecheck
        def __mul__(self, other):
            if self.isZero() or other.isZero():
                return Zero()
            
            newCoeffs = [self.field(0) for _ in range(len(self) + len(other) - 1)]
            for i,a in enumerate(self):
                for j,b in enumerate(other):
                    newCoeffs[i+j] += a*b
            
            return Polynomial(newCoeffs)


    def Zero():
        return Polynomial([])

    Polynomial.field = field
    return Polynomial