#wap to show the implementation of kbc
question=[['What is your country name?','Nepal','China','India','Pakistan',1],
          ['what is the capital of china?','wuhan','beijing','shanghai','hongkong',2],]
for i in range(0,len(question)):
    for j in range(0,len(question[i])-1):
        print(question[i][j]);
    user_input=int(input("Enter correct option: (1-4):"));
    if(user_input==question[i][len(question[i])-1]):
        print("congratulations!")
    else:
        print("your answer is incorrect")
        break

