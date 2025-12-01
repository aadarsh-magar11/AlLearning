import pandas as pd
import numpy as np
import csv
read=pd.read_csv("expense.csv")
day=np.array(["sunday","monday","tuesday","wednesday","thursday","firday","saturday"])

def add(x, y, z):
    with open("expense.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x, y, z])

n=0
for x in range(0,7):#for looping between days
    din=day[n]
    print(f"for {day[n]}")
    need=input("enter the cause:")
    expense=int(input("enter the cost:"))
    add(din,need,expense)
    more=(input(f"add more for {day[n]}?:")).lower()
    while more=="yes":
        need=input("enter the cause:")
        expense=int(input("enter the cost"))
        add(din,need,expense)
        more=(input(f"add more for {day[n]}?:")).lower()
        break
    n=n+1
    
#calculating total expense
def expense(rd):
    df=pd.DataFrame(rd)
    total_cost=df["cost"].sum()
    print(f"the total expense of the week is {total_cost}")

expense(read)