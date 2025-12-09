while True:
    print("1. for adding contact")
    print("2. for removing contact")
    print("3. display contact list")
    print("4. exit")
    mode = int(input("enter any option from the above:"))

    match mode:
        case 1:
            name = input("enter the name:")
            phoneno=(input("enter the phone number:"))
            if len(phoneno)==10 and phoneno.isdigit():
                with open("contact.txt","a") as f:
                    f.write(f"Name: {name}, Phone no.: {phoneno}\n\n")
                print("----------successfully added----------\n")
            else:
                print("the phone number must be 10 digits")

        case 2:
            with open("contact.txt","r") as f:
                read = f.readlines()
                remove=input("enter the name to remove:")
                cont = []
                for x in read:
                    if not x.startswith("Name: "+ remove + ","):
                        cont.append(x)
            
            with open("contact.txt","w") as f:
                f.writelines(cont)

            print("----------removed successfully----------")

        case 3:
            with open("contact.txt") as f:
                print("the list of contacts:\n")
                print(f.read())

        case 4:
            print("----------you exited----------")
            break

        case _:
            print("---enter a valid option---")