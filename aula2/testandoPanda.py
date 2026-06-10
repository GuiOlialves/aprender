import numpy as np
import pandas as pd

# df = pd.read_csv("arquivo.csv")
# df2 = pd.read_excel("arquivo.xlsx")
# df.to_csv("novo.csv", index= False)
# df.to_excel("novo.xlsx", index = False)


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head())