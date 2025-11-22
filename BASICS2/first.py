#while loop
i = 1
while i < 6 :
    print(i)
    if i == 4:
        break
    i+=1

#break - breaks the loop when a certain condition is met
#continue - continues the loop skipping the current loop

#for loop
veggies = ["potato", "spinach", "cabbage"]
for a in veggies:
    print(a)

#for loop with break and continue
for m in veggies:
    if m == "spinach" :
        continue #break is used prints potato only but in continue it skips the spinach printing
    print(m)


#range() in for loop
for y in range(6): #range goes from 0 to 5
    print(y)

print("\n")

for z in range(3,7):# first number denotes beginning and second number denotes upto which number to loop
    print(z)

print("\n")

for n in range(1,10,3):# here first=>initialization second=>ending point and third=>increment by ...... for default increments by 1
    print(n)

#nested loop
for i in range(1,5,1):
    for j in range (5,1,-1):
        print(i,j)

#list, tuples and set
veggies = ["potato", "spinach", "cabbage"]
#in the list the index starts from 0 so potato is index 0, spinach is index 1 and cabbage is index 2
print(veggies[1])

#List items can be accessed from the end too using -ve indexing 
#the last item's index is -1 
print(veggies[-1])

bird = ["kiwi" ,"hen", "peacock", "sparrow", "robin", "vulture", "crow"]
print(bird[2:4])
print(bird[:4])#4th item not included
print(bird[3:])#3rd item to last

#to check an item in a list we use keyword 'in'

#to change an item in list 
bird[3] = "eagle"
print(bird)

#to insert new items in a list
bird.insert(3,"duck")
print(bird)

#to add item at the end of the list use .append()
bird.append("parrot")
print(bird)

#to add elements from another list use .extend
animal = ["dog", "cat"]
bird.extend(animal)
print(bird)

#to remove an item use .remove
bird.remove("hen")
print(bird)

#to remove an item from specific index use .pop(index)
bird.pop(3)
print(bird)

#to delete an item we use del list_name[index]
del bird[3]
print(bird)

'''
#to clear the entire list we use .clear()
bird.clear()
print(bird)
'''

#.reverse() reverses the list items
bird.reverse()
print(bird)

# .sort() sorts the list items in alphabetical order and in ascending order for numbers

#to sort in descending order use:
bird.sort(reverse = True)
print(bird)

#tuple
new = ("hello", "world", "python")
print(new)

#can't add new items directly to tuple so convert tuple to list and add item then convert back to tuple
#or can create a tuple and add new tuple to existing one




#set - {......} it is unchangeable but items can be added and removed 
# .add() - it adds items to the set
# .update(iteratives) - any list,set,tuple can be added to the existing set
# to remove an item we use .remove() or .discard() but if the item doesnot exists then discard doesnot create error
# .pop() removes the first item in set
# .clear() empties the set but del deletes the set completely


#to add two sets we use union or |


# for taking input from  the user we use input keyword
print("enter the number:")
num = input()
#or




#MATCH in python is similar to switch case in C and C++
month = 3
match month:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case _:
        print("later to be added")

#combine match
#for the number entered above
num = int(input("enter the number:"))
match num:
    case 1 | 2 | 3 | 4 | 5 :
        print("first five whole numbers")
    case 6 | 7 | 8 | 9 | 10 :
        print("other whole number")
