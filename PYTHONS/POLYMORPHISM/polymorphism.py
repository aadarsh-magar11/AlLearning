#polymorphism means one having multiple forms or functions
#such as .len() function can be used to find the length of string,tuple,list,dictonary
x="hello whatsup"
tup=("hello","this","is","tuple")
lis=["this","is","list"]
dict={"name":"puskar","age":18}
print(f"length of string",len(x))
print(f"length of tuple",len(tup))
print(f"length of list",len(lis))
print(f"length of dictonary",len(dict))

#polymorphism can be used in class too where different classes have same function name
class animal:
    def __init__(self,name):
        self.name=name

    def sound():
        print("animal makes sound")
class dog:
    def __init__(self,breed):
        self.breed=breed

    def sound():
        print("dog barks")
class cat:
    def __init__(self,breed):
        self.breed=breed
    
    def sound():
        print("cat meows")

a1=animal("girrafe")
d1=dog("bully")
c1=cat("sphynx")
for x in (animal,dog,cat):
    x.sound()
print("\n\n")