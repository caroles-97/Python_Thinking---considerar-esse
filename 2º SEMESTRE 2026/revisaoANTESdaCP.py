#Revisão: crie um algoritmo com a função class para um problema que envolve carros. A classe deve conter a marca do carro, modelo, tipo de carro, cor, ano. 
# Retorne um dataframe com as respectivas informações de 3 objetos. 

#Criar uma função para classificar os carros emfunção do modelo e ano. Depois, criar uma nova coluna chamada Classificação utilizando a função apply.

class Carro:
    def __init__(self, marca, modelo, tipo, cor, ano):
        self.marca = marca  #variável marca
        self.modelo = modelo #criar variável modelo
        self.tipo = tipo    # criar variável tipo de carro
        self.cor = cor  #criar variável cor
        self.ano = ano  #criar variável ano

#Criar método usando DEF (criando função):
    def apresentar(self):
        return f"Meu carro é da marca {self.marca}, do modelo {self.modelo}, tipo de carro {self.tipo} da cor {self.cor} e do ano {self.ano}"

# lista_carro = []

# while True: 
#     marca = input("Marca:")

#     if marca == "nenhum":
#         break

#     modelo =  input("Modelo:")
#     tipo = input("Tipo de carro:")
#     cor = input("Cor do carro:")
#     ano = input(float("Ano do carro:"))

#     objeto = Carro(marca, modelo, tipo, cor, ano )
#     lista_carro.append(objeto)


# #Criando objeto - vou colocar input
carro1 = (input("Marca:"), input("Modelo:"), input("Tipo de carro:"), input("Cor do carro:"), int(input("Ano do carro:"))),
carro2 = (input("Marca:"), input("Modelo:"), input("Tipo de carro:"), input("Cor do carro:"), int(input("Ano do carro:"))),
carro3 = (input("Marca:"), input("Modelo:"), input("Tipo de carro:"), input("Cor do carro:"), int(input("Ano do carro:")))

# #Lista de objetos  - a partir daqui usamos para criar DataFrame (**SEMPRE EM DICT**)
lista_carro = [carro1, carro2, carro3]

dados = []#lista vazia para receber o dict {linha}

for i in lista_carro: #Um objeto por vez - estamos percorrendo a lista dos objetos 
    linha = {   #Monta dicionário
        "Marca": i.marca,     #chamando self . i (valor) da base
        "Modelo" : i.modelo,    #chama o self. i (valor) da altura
        "Tipo": i.tipo(),  #chamando função () area da posição i
        "Cor": i.cor(), #chamando função, precisamos usar ()
        "Ano": i.ano(), 
        
    }
    dados.append (linha)    # guarda na lista. Dados recebendo info do dict {linha}

import pandas as pd
print(pd.DataFrame(dados))  #Transformar o dict 'dados' em DataFrame/ Pandas

        
        