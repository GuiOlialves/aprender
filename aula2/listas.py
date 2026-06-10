import numpy as np
import pandas as pd

# lista = [10,20,30,40]
# del lista[0]
# lista.pop()
# print(lista)


# df = pd.DataFrame({
#     "nome": ["Ana", "Gui", "Leo", "Bob", "Mia"],
#     "idade": [19, 16, 17, None, 20],
#     "plano": ["pro", "pro", "free", "free", "pro"],
#     "gasto": [120, None, 30, 45, None]
# })

# a = df.groupby("plano")["gasto"].mean()
# b = df.groupby("plano")["nome"].count()
# c = df.groupby("plano")["gasto"].agg(["mean", "min", "max","count", "sum"])
# d = df.isnull()          # True/False pra cada célula
# e = df.isnull().sum()    # quantidade de nulos por coluna
# f = df.isnull().any()    # True se a coluna tem algum nulo
# g = df["idade"].fillna(df["idade"].mean())
# print(g)


df1 = pd.DataFrame({
    "id":[1,2,3],
    "nome": ["Ana","Gui","Leo"]
})
df2 = pd.DataFrame({
    "id":[1,2,4],
    "plano": ["free","pro","Free"]
})
# print(df1)
# print(df2)
# df3 = pd.merge(df1,df2,on="id", how="outer")
# print(df3)
print(pd.concat([df1,df2]))
print()
print(pd.concat([df1,df2], axis=1))


