class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    def __add__(self,x):
        return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"
    
v=vector(2,4,5)
print(v)
v1=vector(1,2,3)
print(v1)
print(v+v1)


#to overload the equal == operator
class equal:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"x={self.x}, y={self.y}"
    
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
e1=equal(2,3)
e2=equal(3,4)
e3=equal(3,4)
print(e1==e2)
print(e2==e3)