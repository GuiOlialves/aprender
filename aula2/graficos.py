import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
# dataset clássico de gorjetas em restaurante
# colunas: total_bill, tip, sex, smoker, day, time, size
print(df.head())
# sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
# plt.title("Gorjeta vs Conta Total")
# plt.show()


