import numpy as np

# df = pd.read_csv("arquivo.csv")
# df2 = pd.read_excel("arquivo.xlsx")
# df.to_csv("novo.csv", index= False)
# df.to_excel("novo.xlsx", index = False)
import seaborn as sns
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head())

sns.barplot(data=df, x="day", y="total_bill", hue="sex")
plt.title("Conta média por dia e sexo")
plt.show()