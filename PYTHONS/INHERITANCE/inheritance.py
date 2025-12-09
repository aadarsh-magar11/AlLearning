#inheritance allows to create a class that inherits the properties and methods
class school:
    def __init__(self,klas):
        self.klas=klas

    def printclass(self):
        print("class of the student:"+ self.klas)

c1=school("five")
print(c1.klas)

class grade(school):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def display(self):
        print(f"name={self.name}, roll no={self.roll}")

g1=grade("puskar",11)
c1.printclass()
g1.display()
print("\n")

#parent class
class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):#this is child class
    def barks(self):
        print("dog barks")

a1=dog()#this is an object of child class that inherits the properties of its parent class
a1.sound()#child object accessing the parent function
a1.barks()#child object accessing its own function

#making a parent class named teacher and typist and making a child class coordinator that access the details of the parent class
class teacher:
    def __init__(self,subject):
        self.subject=subject

    def displayteacher(self):
        print("teacher's subject:"+self.subject)

class typist:
    def __init__(self,wpm):
        self.wpm=wpm

    def showtypist(self):
        print("the wpm of typist is"+self.wpm)

class coordinator(teacher,typist):
    def __init__(self,subject,wpm,faculty):
        teacher.__init__(self,subject)#calls teacher's constructor
        typist.__init__(self,wpm)#calls typist's conctructor
        self.faculty=faculty

    def show(self):
        print("faculty is:"+self.faculty)


co1=coordinator("math","120","science")
co1.displayteacher()
co1.showtypist()
co1.show()

print("\n\n\n")

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showEmp(self):
        print(f"the Employee is {self.name} aged {self.age}")

class Income(Employee):
    def __init__(self,name,age,income):
        super().__init__(name,age)#this called employee contructor
        self.income=income

    def showIncome(self):
        print(f"the income of {self.name} is {self.income}")

i1=Income("puskar",18,30000)
i1.showEmp()
i1.showIncome()
