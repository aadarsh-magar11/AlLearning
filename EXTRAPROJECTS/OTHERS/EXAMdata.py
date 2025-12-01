import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
datas=pd.read_csv("examPer.csv")
df=pd.DataFrame(datas)
def pass_std(data):#fn for students who passed maths exam
    math_pass=len(data[data["math score"]>=40])
    print(f"{math_pass} students passed in maths exam")

def reading_pass(data):#fn for students passing reading exam
    read_pass=len(data[data["reading score"]>=40])
    print(f"{read_pass} students passed in reading exam")

def writing_pass(data):#fn for students passing writing exam
    write_pass=len(data[data["writing score"]>=40])
    print(f"{write_pass} students passed in writing exam")

def prep_test_comp(data):
    total=len(data)
    prep=len(df[df["test preparation course"]=="completed"])
    print(f"out of {total} students, {prep} completed their test preparation course")

def piechart(data):
    sns.heatmap(data[["math score","reading score","writing score"]].corr(), annot=True, cmap="Reds")
    plt.show()

pass_std(df)
reading_pass(df)
writing_pass(df)
prep_test_comp(df)
piechart(df)
