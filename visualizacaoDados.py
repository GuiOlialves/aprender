import matplotlib.pyplot as plt
import numpy as np

# meses= [1,2,3,4,5,6,7,8]
# vendas = [1200,1500,1100,1800,2000,1700,200,0]
# plt.plot(meses,vendas,color="steelblue",marker="o",linewidth=2)
# plt.title("Vendas por mês")
# plt.xlabel("mês") 
# plt.ylabel("Valor (R$)")
# plt.grid(True)
# #plt.show()


# produtos = ["notebook", "mouse", "teclado", "monitor"]
# quantidades = [5, 15, 10, 7]

# plt.bar(produtos, quantidades, color="steelblue", edgecolor="black")
# plt.title("Vendas por produto")
# plt.xlabel("Produto") 
# plt.ylabel("Valor (R$)")
# plt.grid(axis="y")
# #plt.show()


# idades = np.random.randint(0, 100, 200000)

# plt.hist(idades, bins=100, color="steelblue", edgecolor="black")
# plt.title("Distribuição de Idades")
# plt.xlabel("Idade")
# plt.ylabel("Frequência")
# plt.grid(axis="y")
# #plt.show()



# horas_estudo = [1, 2, 3, 4, 5, 6, 7, 8]
# nota = [37, 57, 63, 77, 88, 95, 85, 70]

# plt.scatter(horas_estudo, nota, color="coral", s=100, edgecolors="black")
# # s=100 é o tamanho dos pontos
# # edgecolors="black" borda preta em cada ponto

# plt.title("Horas de Estudo vs Nota")
# plt.xlabel("Horas")
# plt.ylabel("Nota")
# plt.grid(True)
# plt.show()




fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# 1 linha, 2 colunas de gráficos
# figsize=(largura, altura) em polegadas

# Gráfico 1 — linha
axes[0].plot([1,2,3,4,5], [100,150,120,180,200], color="steelblue", marker="o")
axes[0].set_title("Vendas")
axes[0].set_xlabel("Mês")
axes[0].grid(True)

# Gráfico 2 — barras
axes[1].bar(["SP","RJ","MG"], [500,300,200], color="coral", edgecolor="black")
axes[1].set_title("Vendas por Estado")
axes[1].set_xlabel("Estado")
axes[1].grid(axis="y")

plt.tight_layout()  # ajusta espaçamento automático entre os gráficos
plt.show()