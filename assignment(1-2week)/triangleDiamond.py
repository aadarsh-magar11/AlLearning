row = int(input("enter the rows : "))
print("\n")
print("diamond:\n")
for i in range(1,row+1):
    print(" "*(row-i) + "*"*(2*i-1))
for j in range(row-1,0,-1):
    print(" "*(row-j) + "*"*(2*j-1))

print("\n")
print("triangle:\n")
for i in range(1,row+1):
    print(" "*(row-i) + "*"*(2*i-1))



    