#recursive function - it a function that calls itself until the condition is met
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#string formatting or f-string allows to format the strings printed in the diplay screen
name = input("enter your name:")
print(f"Hello, {name}")

#expressions can also be added in f-strings 
height = int(input("enter the height:"))
width = int(input("enter the width:"))
print(f"the area of the box is {height*width}")

#format specifiers (:) is used to format spaces, number of decimals displayed, padding, alignment
pi = 3.14159
number = 42
# Rounding a float 
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Padding an integer with zeros
print(f"Number padded with zeros: {number:04d}")

# Left-aligning text
fruit = "apple"
print(f"Fruit: {fruit:<10}")

#debugging the text with (=) shows the equals to sig useful for debugging
m, n = 3, 4
print(f"the values are: {m=}, {n=}")

#str.format() is older method of formatting the strings
#Positional arguments place the arguments based on their index
template = "The result is {} and {}."
result = template.format("good", "stable")
print(result)

#named arguments can be used to name the arguments that are used in the string
template = "the {food} is {taste}"
output = template.format(food="mo:mo", taste="delicious")
print(output)

# .format() can be used for unpacking dictionaries too
example = {"name":"Ram", "town":"Butwal"}
template = "NAME is {name} and lives in {town}"
print(template.format(**example))
