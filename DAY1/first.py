print("hello world")
x = 5
print(x)

fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

a = "hello"
b = "world"
print(a,b)
print(a + b)
print("hello","world")

m = 10
n = 20
print("the sum is", m+n)

#global variable
p = "awesome"

def myfunc():
    print("python is"+ p)

myfunc()

#to use random number need to import random
import random
print(random.randrange(0,10))

#conditional statements
e = 10
f = 10
if e > f:
    print("e is greater")
elif e<f:
    print("f is greater")
else:
    print("both are equal")


#multiline string- '''.....''' or """....."""
abc='''this is a multiline string 
used to print multiple lines'''
print(abc)

#string are array
w="this is an array of char"
print(w[1],w[2],w[9],w[11],w[12])

#loop through string
for r in "apple":
    print(r)

print(len(w))#len gives the length of string

#to check if a word lies in a string
xyz = "i am learning python"
print("python" in xyz)#gives boolean true/false

if("python" in xyz):
    print(xyz)

#to check not in a string
print("python" not in xyz)

#slicing
print(xyz[2:6])
#to slice from the beginning use 'print(xyz[:number])
#to slice to the end use 'print(xyz[number:])
#negative indexing ma pachhadi bata aauchha

#.lower() .upper()
#.strip() removes the blank space from the start and end

t = "Hello World!" 
print(t.replace("H","Y"))

'''
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
'''

#f-string means connecting two datatypes
e=10
txt=f"the number is {e}"
print(txt)

#to print with floating point
txt=f"the number after is {e:.2f}"
print(txt)


#evaluate values
print(bool())#empty string so returns false


