#encapsulation means hiding the members and methods but display only those which are necessary
#class can be taken as encapsulation as it encapsulates all the methods and functions present in it
class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary#salary is now a protected attribute
        
    def show_salary(self):
        print("salary:",self._salary)

e1=employee("ram",20000)
print("name:",e1.name)
e1.show_salary()

print("\n")

class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#age is now private attribute
    
    def show_age(self):
        print("age:",self.__age)

p1=person("shyam","butwal")
print("name:",p1.name)
p1.show_age()

'''
single underscore(_) is used to create a protected attribute 
double underscore(__) is used to create a private attribute
'''
