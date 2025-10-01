bill = 0
more="yes"
while True:
    print("enter any options:")
    print("1. see menu")
    print("2. order food")
    print("3. see total bill")
    print("4. exit")
    choice=int(input("enter you choice:"))
    match choice:
        case 1:
            print("OUR FOOD MENU:")
            print("DELICACIES\t\t\tPRICE")
            print("1. Jhol MOMO chicken\t\t150")
            print("2. Chicken Thuppa\t\t170")
            print("3. Chicken franky\t\t150")
            print("4. Chicken Samosa(2pcs)\t\t130")
        case 2:
            while more.lower()=="yes":
                print("OUR FOOD MENU:")
                print("DELICACIES\t\t\tPRICE")
                print("1. Jhol MOMO chicken\t\t150")
                print("2. Chicken Thuppa\t\t170")
                print("3. Chicken franky\t\t150")
                print("4. Chicken Samosa(2pcs)\t\t130")
                order=int(input("enter your order:"))
                match order:
                    case 1:
                        quantity=input("enter the qunatity of jhol momo:")
                        bill=150*quantity
                    case 2:
                        quantity=input("enter the qunatity of chicken thuppa:")
                        bill=170*quantity
                    case 3:
                        quantity=input("enter the quantity of chicken franky:")
                        bill=150*quantity
                    case 4:
                        quantity=input("enter the quantity of chicken samosa:")
                        bill=130*quantity
                    case _:
                        print("enter a valid option from the above")
                more=input("do you want to order more?(yes/no):")
        case 3:
            vat=(13/100)*float(bill)
            bill=float(vat)+float(bill)
            print(f"vat amount={vat:2f}")
            print(f"total bill={bill:2f}")
        case 4:
            print("exited")
            break
        case _:
            print("enter a valid option")

        
