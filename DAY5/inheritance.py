#inheritance allows to create a class that inherits the properties and methods
class school:
    def __init__(self,klas):
        self.klas=klas

    def printclass(self):
        print("class of the student:"+ self.klas)

c1=school("five")
print(c1.klas)