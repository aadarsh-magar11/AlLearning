#Python is a object oriented programming in which almost everything is object and has properties and methods

#Class is declared in python using keyword 'class'
class first:
    x = "hello world!"

f1=first()
print(f"{f1.x}\n")

# __init__() is used to assign the values to the objects
class student:
    def __init__(std,name,roll):
        std.name=name
        std.roll=roll

    def __str__(new):# __str__() use garena bhane sidhai object ko memory location return garchha
        return f"{new.name}({new.roll})"
    
    def displayName(std):
        print("the name of the student is "+std.name)
    
s1=student("ram",1)
s2=student("shyam",2)
s2.roll = 4  #modifing property of an object
print(f"Name:{s1.name}, Rollno:{s1.roll}")
print(f"Name:{s2.name}, Rollno:{s2.roll}")
print(s1)
s1.displayName()

#generally 'self' is used as a access variable that belongs to a class

#create methods - we can make our own methods in class objects

#we can delete a property of an object using 'del' keyword

#class definition can't be empty so if by any case we just define the class we must use 'pass' 
class rectangle:
    pass
