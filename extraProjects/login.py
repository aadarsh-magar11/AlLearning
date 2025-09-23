user_name="aadarsh magar"
password="@aadarsh11"
user=input("enter username:")
while user!=user_name:
    print("username doesn't exists")
    user=input("enter username again:")
    if user==user_name:
        i=1
        while i<=3:
            pw=input(f"enter password({3-i} attempts left):")
            if pw==password:
                print("LOGIN SUCCESSFULL")
                
            else:
                print("incorrect password")
        i+=1
        print("you have 0 attempts left try again later")
        
            