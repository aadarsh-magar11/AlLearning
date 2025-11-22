c=0
for x in range(1000,3000,1):
    if(x%7==0 and x%5!=0):
        print(x)
        c+=1
print(c)  