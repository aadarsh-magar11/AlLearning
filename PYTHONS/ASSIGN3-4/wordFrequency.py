with open("sample.txt") as file:
    get = file.read()

seperate = get.split()
count=0

word = input("to find frequency of :")

for x in seperate:
    if word == x:
        count+=1

print(f"'{word}' is repeated {count} times")

