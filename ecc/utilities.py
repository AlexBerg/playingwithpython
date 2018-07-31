# A typechecker for trying to cast arguments to same class
def typecheck(f):
    def newF(self, other):
        if type(self) is not type(other):
            try:
                other = self.__class__(other)
            except TypeError:
                message = 'Not able to cast %s of type %s to %s'
                raise TypeError(message % (other, type(other).__name__, type(self).__name__))
            except Exception as e:
                message = 'Type error for %s due to %s'
                raise TypeError(message % (f.__name__, e))
        return f(self, other)

    return newF


# So we dont need to overload for all numbertypes
class DomainElement(object):
    def __radd__(self, other):
        return self + other
    def __rsub__(self, other):
        return self - other
    def __rmul__(self, other):
        return self * other


# Same as above, all field integers have the same overload
class FieldElement(DomainElement):
    def __truediv__(self, other):
        return self * other.inverse()
    def __rtruediv__(self, other):
        return self.inverse() * other
    def __div__(self, other):
        return self.__truediv__(other)
    def __rdiv__(self, other):
        return self.__rtruediv__(other)
