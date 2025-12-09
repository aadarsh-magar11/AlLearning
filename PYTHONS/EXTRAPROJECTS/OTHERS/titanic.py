import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
datas=pd.read_csv("titanic.csv")
# print(datas)
df=pd.DataFrame(datas)
datas=df.fillna({"survived":"1"}, inplace=True)
# print(df)
survived=((len(df[df["survived"]==1]))/df["survived"].count())*100
print(f"the survival rate is {survived:.2f}")
age=df["age"].median()
print(f"the people onboard were mostly of age {age}")
