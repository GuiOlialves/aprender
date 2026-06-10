# 1 - Identificar e tratar os nulos em vendas
# 2 - Fazer um merge pra juntar clientes com suas vendas
# 3 - Calcular o total gasto por cliente
# 4 - Calcular o total gasto por cidade
# 5 - Descobrir qual produto vendeu mais
# 6 - Filtrar só as vendas acima de R$200
import pandas as pd
import numpy as np

clientes = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "nome": ["Ana", "Gui", "Leo", "Bob", "Mia"],
    "cidade": ["SP", "SP", "RJ", "RJ", "SP"]
})

vendas = pd.DataFrame({
    "id": [1, 2, 2, 3, 5, 5, 5, None],
    "produto": ["notebook", "mouse", "teclado", "monitor", "mouse", "notebook", "teclado", "mouse"],
    "valor": [3500, 150, 280, 1200, 150, 3500, 280, None]
})


print("bem vindo ao nosso sistema de analise de vendads!")
print("-------------------------------------------------")
print("Oque gostaria de fazer hoje?")
print("1 - Identificar e tratar os nulos em vendas")
print("2 - Fazer um merge pra juntar clientes com suas venda")
print("3 - Calcular o total gasto por cliente")
print("4 - Calcular o total gasto por cidade")
print("5 - Descobrir qual produto vendeu mais")
print("6 - Filtrar só as vendas acima de R$200")
print("7 - Sair")
resp1 = int(input(""))
bd = pd.merge(clientes,vendas, on="id")
if resp1 == 1:
    vendas["id"] = vendas["id"].fillna(0)    
    vendas["valor"] = vendas["valor"].fillna(0)
if resp1 == 2:
    print(pd.merge(clientes,vendas, on="id"))
if resp1 == 3:  
    print(bd.groupby("nome")["valor"].sum())
if resp1 == 4:
    print(bd.groupby("cidade")["valor"].sum())
if resp1 == 5:
    contagem = bd.groupby("produto")["valor"].count()
    maisVendido = contagem.idxmax()
    print(f"Produto mais vendido: {maisVendido} ({contagem[maisVendido]}) vendas")    
if resp1 == 6:
    print(bd[bd["valor"] >= 200])





