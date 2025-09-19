#functions are declared in python using 'def' keyword

def display():
    print("hello user")

display()


user=input("enter your name:")
#passing arguments in function
def greet(name):
    print("Hello",name)

greet(user)

#function with multiple arguments
first=input("enter your first name:")
last = input("enter your last name:")
def new(fname,lname):
    print("your name:",fname,lname)

new(first,last)

#arbitary arguments - when we dont know how many or which argument to use "*" before the argument
#we can pass a list or tuple then select the item using index
def my_function(*animal):
  print("you chose: " + animal[2])

my_function("chimpanzee", "elephant", "girrafe")


#keyword argument - can be used instead of using index in tuple or list just by assigning a name to the item
def my_function(animal1,animal2,animal3):
  print("The youngest child is " + animal1)

my_function(animal1="chimpanzee", animal2="rhino", animal3="human")

#arbitary keyword - it is combination of arbitary and keyword argument and such argument can be declared by **
def my_function(**animal):
  print("these are bigger cats " + animal["two"])

my_function(one = "lion", two = "tiger")


#default argument can be used in python too
def my_function(country = "Nepal"):
  print("I am from " + country)

my_function("bhutan")
my_function("India")
my_function()
my_function("china")


#we can send any datatypes of argument to a function 
def my_function(genre):
  for x in genre:
    print(x)

movie = ["comedy", "romance", "tragedy"]

my_function(movie)


#returning values using function 
def sum(a,b):
   return a+b

print(sum(2,3))


#pass statement can be used to skip the function or can be used if function is empty
def myfunction():
  pass 

#we can define positional only argument
def position(x, /):
  print(x)

position(3)