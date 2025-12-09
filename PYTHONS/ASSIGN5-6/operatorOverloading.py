'''
operator overloading can be done in pyhton using dunder method (or magical methods) that defines how 
a operator works in a class
__add__(self, other): for +
__sub__(self, other): for -
__mul__(self, other): for *
__truediv__(self, other): for /
__floordiv__(self, other): for //
__mod__(self, other): for %
__pow__(self, other): for **
these are arithmetic dunder methods that overload the respective operator
'''
#to overload + to add two vectors
class vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def __str__(self):
        return (f"{self.i}i+{self.j}j")
    
    def __add__(self,v):
        return f"{self.i+v.i}i+{self.j+v.j}j"
    
    def __mul__(self,v):
        return f"{self.i*v.i}i,{self.j*v.j}j"


v1=vector(2,3)
v2=vector(1,4)
print("the vector sum is ",(v1+v2))
print("the vector multiplication is ",(v1*v2))
print("\n")

