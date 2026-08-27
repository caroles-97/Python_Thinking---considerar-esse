# Algoritmo para calcular a área e perímetro de um retângulo utilizando a função class. Depois crie 5 objetos e insira em uma lista de objetos.
# Por fim, utilize for para inserir a lista de objetos em um dicionário

import pandas as pd

class Retangulo:
    def __init__(self, base, altura):
        self.base = base #criada variável base
        self.altura = altura  #criada variável altura

#Criar método  *  DEF - PERMITE CRIAR FUNÇÕES EM PYTHON

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2 + self.altura * 2)

    def apresentar(self):
        return f"Area é {self.area()}, Perimetro é {self.perimetro()}"

#Criando objeto
a1 = Retangulo(2,3)
a2 = Retangulo(5,6)
a3 = Retangulo(2,3)
a4 = Retangulo(8,9)
a5 = Retangulo(2,3)

#Lista de objetos
lista_retangulo = [a1, a2, a3, a4, a5] #lista cheia
dados = []

for i in lista_retangulo: #Um objeto por vez - estamos percorrendo a lista dos objetos 
    linha = {   #Monta dicionário
        "Base": i.base,     #chamando self . i chama a base
        "Altura" : i.altura,    #chama o self. i chama a altura
        "Area": i.area(),  #chamando função ()
        "Perimetro": i.perimetro(), #chamando função, precisamos usar ()
        "Calculo": i.apresentar(), 
        
    }
    dados.append (linha)    # guarda na lista 

print(pd.DataFrame(dados))



