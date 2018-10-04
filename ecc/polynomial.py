from utilities import *
from fractions import Fraction

@memoize
def polynomials(field=Fraction):
    class Polynomial(DomainElement):
        operatorPrecedence = 2
