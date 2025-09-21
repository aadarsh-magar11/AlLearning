item = input("enter the name of item:")
price = input("enter the quantity of item:")
shoppingList={}
shoppingList.update({f"{item}":f"{price}"})

yesno=input("Do you want to add another item(yes/no)?:")#to add more items
while yesno.lower() == "yes":
    item = input("enter the name of item:")
    price = input("enter the quantity of item:")
    shoppingList.update({f"{item}":f"{price}"})
    yesno=input("Do you want to add another item(yes/no)?:")

print("The list of items in your shopping list:")#to display initial list without modification or removing
for item, price in shoppingList.items():
    print(f"Name:{item}, Price:{price}")
print("\n")

remod=input("do you want to remove or modify any item(yes/no)?:")#ask to either remove or modify an item
while remod.lower()=="yes":

    rem=input("do you want to remove?(yes/no):")#asks if user wants to remove
    while rem=="yes":
        to_rem=input("what do you want to remove?:")#asks what to remove
        shoppingList.pop(to_rem)
        rem=input("do you want to remove more?(yes/no):")#if user wants to remove other items
    
    mod=input("do you want to modify any item's quantity?(yes/no):")#asks if user wants to modify any item
    while mod.lower()=="yes":
        to_modify=input("what to modify?:")#asks what to modify
        quan=input("enter the quantity:")#asks how much to modify
        shoppingList[to_modify]=quan
        mod=input("do you want to modify any more item's quantity?(yes/no):")#asks is user wants to modify more items
    
    remod=input("do you want to remove or modify any item(yes/no)?:")#asks again

print("\n")
print("final shopping list:")#displays final list
for item, price in shoppingList.items():
    print(f"Name:{item}, Price:{price}")
