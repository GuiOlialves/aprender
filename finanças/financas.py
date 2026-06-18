import pandas as pd




df = pd.read_excel("financas.xlsx")
print(df.head())
print(df.dtypes)
print(df.shape)

total_receita = df[df["tipo"] == "receita"]["valor"].sum()
total_despesa = df[df["tipo"] == "gasto"]["valor"].sum()
saldo =  total_receita - total_despesa 
print(total_receita)
print(total_despesa)
print(saldo)
gastos_categoria = df[df["tipo"] == "gasto"].groupby("categoria")["valor"].sum().sort_values(ascending=False)
print(gastos_categoria)

