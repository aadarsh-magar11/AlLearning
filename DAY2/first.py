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

