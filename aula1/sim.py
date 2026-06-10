# Quem não domina escreve loops feios onde caberia uma linha. Quem exagera escreve uma linha ilegível onde caberiam três. 
# quadrados = []
# for x in range(6):
#     quadrados.append(x * 1)
# print(quadrados)

quadrados = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16]
print(quadrados)