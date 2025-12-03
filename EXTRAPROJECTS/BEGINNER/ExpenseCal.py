import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
day=np.array(["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
 
 #for piechart
cause=np.array([])
kharcha=np.array([])

df_exists=pd.read_csv("expense.csv")#reading csv for the last week's number
if len(df_exists) == 0:
    week=1;
else:
    week= df_exists["week"].max() + 1;


def add(m, x, y, z):#function to add new data to csv file
    with open("expense.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([m, x, y, z])


n=0#initializing for array of week
for x in range(0,7):#for looping between days
    din=day[n]
    print(f"for week {week}")
    print(f"for {day[n]}")
    need=input("enter the cause:")
    expense=int(input("enter the cost:"))

    cause=np.append(cause,need)#appending in array
    kharcha=np.append(kharcha,expense)

    add(week,din,need,expense)
    more=(input(f"add more for {day[n]}?:")).lower()
    while more=="yes":
        need=input("enter the cause:")
        expense=int(input("enter the cost"))

        cause=np.append(cause,need)#appending in array
        kharcha=np.append(kharcha,expense)

        add(week,din,need,expense)
        more=(input(f"add more for {day[n]}?:")).lower()
        break
    n=n+1
    
#to print the sum of the week expense
df = pd.read_csv("expense.csv")
week_total = df[df["week"] == week]["cost"].sum()
print(f"\nTotal expense for Week {week}: {week_total}")

#plotting piechart
plt.pie(kharcha, labels=cause, autopct="%1.1f%%")
plt.show()