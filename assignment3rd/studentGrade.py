class student:
    def __init__(self,mark1,mark2,mark3,mark4,mark5):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5
    
    def average(self):
        avg=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5
        return avg
    
    def grade(self,full):
        percent=(self.average()/(full*5))*100
        if percent>=90:
            print("your grade is A+")
        elif percent<90 and percent>=80:
            print("your grade is A")
        elif percent<80 and percent>=70:
            print("your grade is B+")
        elif percent<70 and percent>=60:
            print("your grade is B")
        elif percent<60 and percent>=50:
            print("your grade is C+")
        elif percent<50 and percent>=40:
            print("your garde is C+")
        else:
            print("you failed")

while True:
    fm=float(input("enter the full marks"))
    a=float(input("enter the marks in subject 1:"))
    b=float(input("enter the marks in subject 2:"))
    c=float(input("enter the marks in subject 3:"))
    d=float(input("enter the marks in subject 4:"))
    e=float(input("enter the marks in subject 5:"))
    s1=student(a,b,c,d,e)
    print("the average marks of the student is",s1.average())
    s1.grade(fm)
    print("\n")


