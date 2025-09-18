number = int(input("enter a number to check whether it is prime or not:"))
if number == 0 or number == 1 :
    print (f"{number} is composite")
elif number == 2:
    print(" 2 is prime")
elif number % 2 == 0 :
    print(f"{number} is composite")
else:
    prime = True
    for x in range(3,(number//2+1),1):
        if number % x == 0 :
            prime = False
            break
    if prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is composite")
        
            