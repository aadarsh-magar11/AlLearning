class user:
    def __init__(self,username,pin,balance):
        self.username=username
        self.pin=pin
        self.balance=balance

    def balance_inquiry(self):
        print("your balance is ",self.balance)
    
    def deposit(self,amount):
        self.balance+=amount
        print("you deposited ",amount)
    
    def withdraw(self,amount):
        self.balance-=amount
        print("you withdrew ",amount)

class ATM(user):
    def __init__(self,username,pin,balance):
        super().__init__(username,pin,balance)

    def login(self):
        success=False
        atm_user=ATM(username,pin,balance)
        with open("user.txt") as f:
            for line in f:
                line=line.strip()
                username,pin,balance=line.split(",")
                # user=input("enter the username: ")
                # while user!=atm_user.username:
                #     user=input("enter username again:")   
                print("enter your card")                     
                attempt=0
                while attempt<3:
                    pinn=int(input(f"enter the pin({3-attempt}attempts left):"))
                    if pinn==atm_user.pin:
                        print("login successful")
                        success=True
                print("you have no attempts left")    
                print("your account has been locked\n contact near branch or wait 24 hours")
        return success

    def menu(self,choice):
        print("1. balance inquiry")
        print("2. withdraw")
        print("3. desposit")
