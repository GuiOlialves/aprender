
# frutas = ["maçã", "banana"]
# frutas.append("uva")  # No JS seria .push()
# print(frutas[2])      # Acesso por índice igual

# celular = {
#     "modelo":"samsung",
#     "cor":"azul"
# }
# numeros = [1,2,3,4, 5,6,7]
# # for numero in numeros:
# #     print(f"Numero: {numero}")
# # # print(celular["modelo"])

# # dobro = [n * 2 for n in numeros if n % 2 == 0]
# numeros = filter(lambda n: n >=5 , numeros)


# print(list(numeros))



# user = {
#     "nome": "Leo",
#     "idade": 30
# }

# # Acesso comum (se a chave não existir, dá ERRO/Exception)
# print(user["nome"]) 

# # Acesso seguro (se a chave não existir, retorna None - tipo o null do JS)
# print(user.get("email")) 

# # Adicionar nova chave
# user["stack"] = "Python"
# print(user)



# def criarPerfil(nome,cargo):
#     print(f"seu nome é {nome} seu cargo é {cargo}")
# criarPerfil(nome ="Guilherme", cargo= "editor")


# class celular:
#     def __init__(self,marca,modelo,cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.cor = cor
#     def adicionarCelular(marca,modelo,cor):
#         print(f"Seu modelo é {modelo} a marca dele é {marca} e a cor {cor}")
# celular.adicionarCelular(modelo = "A34", marca= "samsung", cor ="Azul")
# print(celular(modelo))

# class celular:
#     def __init__(self,marca,modelo,cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.cor = cor
#     def __str__(self):
#         return f"Seu modelo é {self.modelo} a marca dele é {self.marca} e a cor {self.cor}"
# meuCelular = celular(modelo = "A34", marca= "samsung", cor ="Azul")
# print(meuCelular)

# class Conta:
#     def __init__(self, saldo):
#         self._saldo = saldo 

#     @property
#     def saldo_disponivel(self):
#         return f"R$ {self._saldo:.2f}"

# conta = Conta(1000)
# print(conta.saldo_disponivel) # Você acessa sem os parênteses ()

# from pathlib import Path

# # Criar um objeto de caminho
# pasta = Path("meu_projeto/dados")

# # Criar a pasta (o exist_ok é como o recursive: true do Node)
# pasta.mkdir(parents=True, exist_ok=True)

# # Listar arquivos em uma pasta
# for arquivo in Path(".").iterdir():
#     print(arquivo.name)


# import json

# # String JSON (vindo de uma API, por exemplo)
# dados_json = '{"nome": "Leo", "ativo": true}'

# # JSON para Dicionário (JSON.parse)
# usuario = json.loads(dados_json)
# print(usuario["nome"])

# # Dicionário para JSON (JSON.stringify)
# string_pronta = json.dumps(usuario, indent=4)
# print(string_pronta)


# from datetime import datetime, timedelta

# # Data e hora agora
# agora = datetime.now()
# print(f"Data formatada: {agora.strftime('%d/%m/%Y %H:%M')}")

# # Somar dias (muito fácil!)
# amanha = agora + timedelta(days=1)
# print(f"Amanhã será: {amanha.day }")


# import json

# vendas_sujas = [
#     {"cliente": "ana", "valor": 1200, "produto": "Notebook"},
#     {"cliente": "pedro", "valor": 300, "produto": "Mouse"},
#     {"cliente": "carla", "valor": 850, "produto": "Monitor"},
#     {"cliente": "roberto", "valor": 150, "produto": "Teclado"}
# ]

# # 1 & 2 & 3. Filtrando e transformando usando List Comprehension
# # Note que estamos criando um novo dicionário e adicionando a chave 'categoria'


# numero = input("DIgite um Numero: ")
# try:    
#     numero = int(numero) * 2
#     print(f"O dobro do seu numero é {numero}")
# except:
#    print("digite um numero valido")


# TESTE = 10
# TESTE = 5
# print(TESTE)


# numeros = [1,2,3,4,5,6,7,8,9,10]
# numEscolhido = int(input("Escolha um number"))
# for n in numeros:
    
#     if n == numEscolhido:
#         print("chegou no numero")
#         break
#     print(n)

# a= [1,2]
# b = [1,2]
# c = a
# print(a is c)







