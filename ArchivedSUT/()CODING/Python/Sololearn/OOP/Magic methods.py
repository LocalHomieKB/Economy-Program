#class Vector2D:
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y
#    def __add__(self,other):
#        return Vector2D(self.x+other.x,self.y+other.y)

#first=Vector2D(5,7)
#second=Vector2D(3,9)
#result=first+second
#print(result.x)
#print(result.y)

#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |

class SpecialString:
    def __init__(self,cont):
        self.cont=cont

#__lt__ for <
#__le__ for <=
#__eq__ for ==
#__ne__ for !=
#__gt__ for >
#__ge__ for >=

#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in

    def __truediv__(self,other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont,line,other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)