'''
The 'try' block lets you test a block of code for errors.
The 'except' block lets you handle the error.
The 'else' block lets you execute code when there is no error.
The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("other error occured")

print("\n")

try:
    print("hello")
except:
    print("an error occured")
else:
    print("nothing is wrong")
finally:
    print("this works even if try or except works or not")

#raise is used to throw an exception even if there is no exception
'''
x = -2

if x < 0:
    raise Exception("only positive numbers are allowed")

'''
'''
x="hello"
if x is not int:
    raise TypeError("x is not a integer")
'''

'''
TypeError- used to give error for datatype
ValueError- used when the value given doesn't match the datatype
NameError- used when a variable's value is not defined
FileNotFoundError- used to give error when the file is not found
ZeroDivisionError- when a number is divided by zero
AttributeError- object ko value namilda
'''

