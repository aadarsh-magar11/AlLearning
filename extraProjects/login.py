user_name="puskar"
password="1234puskar"
user=input("enter the user name:")
while user!=user_name:
    print("username doesn't exists")
    user=input("enter username again:")
attempt=0
while attempt<3:
    pw=input(f"enter the password(you have {3-attempt} attempts left):")
    if pw==password:
        print("LOGIN SUCCESSFUL")
        break
    attempt+=1
else:
    print("you have no attempts left so try later")
