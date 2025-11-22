class bankAccount:
    def __init__(self,account_holder,account_id,balance):
        self.account_holder=account_holder
        self.account_id=account_id
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"you deposited:{amount}\n new balance:{self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("no sufficient balance")
        else:
            print(f"withdraw amount:{amount}\n new balance:{self.balance-amount}")

    def showBalance(self):
        print(f"your balance is:{self.balance}")

holder=input("enter the name of the holder:\t")
id=input("enter the id of the holder:\t")
bal=int(input("initialize a balance:\t"))
h1=bankAccount(holder,id,bal)
while True:
    print("1. deposit money")
    print("2. withdraw money")
    print("3. balance inquiry")
    print("4. exit")
    print("\n")
    mod=int(input("choose an option from above:"))
    match mod:
        case 1:
            sum=int(input("enter the amount to deposit:\t"))
            h1.deposit(sum)
        case 2:
            sum=int(input("enter the amount to withdraw:\t"))
            h1.withdraw(sum)
        case 3:
            h1.showBalance()
        case 4:
            break
