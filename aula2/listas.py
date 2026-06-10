import numpy as np
import pandas as pd

lista = [10,20,30,40]
del lista[0]
lista.pop()
print(lista)


df = pd.DataFrame({
    "nome": ["Ana", "Gui", "Leo", "Bob", "Mia"],
    "idade": [18, 15, 16, None, 20],
    "plano": ["pro", "pro", "free", "free", "pro"],
    "gasto": [120, None, 30, 45, None]
})

a = df.groupby("plano")["gasto"].mean()
b = df.groupby("plano")["nome"].count()
c = df.groupby("plano")["gasto"].agg(["mean", "min", "max","count", "sum"])
d = df.isnull()          # True/False pra cada célula
e = df.isnull().sum()    # quantidade de nulos por coluna
f = df.isnull().any()    # True se a coluna tem algum nulo
print(f)