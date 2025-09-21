item = input("enter the name of item:")
price = input("enter the quantity of item:")
shoppingList={}
shoppingList.update({f"{item}":f"{price}"})

yesno=input("Do you want to add another item(yes/no)?:")
while yesno.lower() == "yes":
    item = input("enter the name of item:")
    price = input("enter the quantity of item:")
    shoppingList.update({f"{item}":f"{price}"})
    yesno=input("Do you want to add another item(yes/no)?:")

print("The list of items in your shopping list:")
for item, price in shoppingList.items():
    print(f"{item}:{price}")
print("\n")

remod=input("do you want to remove or modify any item(yes/no)?:")
while remod.lower()=="yes":

    rem=input("do you want to remove?(yes/no):")
    while rem=="yes":
        to_rem=input("what do you want to remove?:")
        shoppingList.pop(to_rem)
        rem=input("do you want to remove more?(yes/no):")
    
    mod=input("do you want to modify any item's quantity?(yes/no):")
    while mod.lower()=="yes":
        to_modify=input("what to modify?:")
        quan=input("enter the quantity:")
        shoppingList[to_modify]=quan
        mod=input("do you want to modify any more item's quantity?(yes/no):")
    
    remod=input("do you want to remove or modify any item(yes/no)?:")

print("\n")
print("final shopping list:")
for item, price in shoppingList.items():
    print(f"{item}:{price}")
