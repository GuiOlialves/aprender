import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
# dataset clássico de gorjetas em restaurante
# colunas: total_bill, tip, sex, smoker, day, time, size
print(df.head())




