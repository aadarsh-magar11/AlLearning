a = float(input("enter first number:"))
b = float(input("enter second number:"))
print("enter an option from + or - or * or /:")
sign = input()
match sign:
    case "+":
        print("the sum is ",a+b)
    case "-":
        if a > b :
            print("the difference is ",a-b)
        else:
            print("the difference is ",b-a)
    case "*":
        print("the product is ",a*b)
    case "/":
        div = float(a/b)
        print("the quotient is ",div)
    case _:
        print("enter a valid input")


