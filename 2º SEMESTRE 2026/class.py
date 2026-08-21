class Bolo:
  def __init__(self, sabor):
    self.sabor = sabor

# Criar o objeto
b1 = Bolo("chocolate")
b2 = Bolo("cenoura")

print(b1.sabor)
# Ao chamar o b1, estamos chamando sabor
print(b2.sabor)

-----------

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome  #criei variável nome
    self.idade = idade  #criei a varável idade

  #Método a ser criado *****  DEF - PERMITE CRIAR FUNÇÕES EM PYTHON
  def apresentar(self):
    return f"Meu nome é {self.nome} e tenho {self.idade} anos."

#Criar objeto
p1 = Pessoa ("Ana", 35)

print(p1.apresentar())
# Apresentar a informação, vms usar o método criado
# chamar: função()

print(p1.__dict__)
# Já com o objeto pronto, se dermos o nome do objeto e usar a função dict - ele transforma em dicionário

------------------


class Carro:
  def __init__(self, nome, carro, ano, modelo):
    self.nome = nome  #tem que ser igual
    self.carro = carro
    self.ano = ano
    self.modelo = modelo

#método criado
#DEF - PERMITE CRIAR FUNÇÕES EM PYTHON
  def apresentar (self):
      return f"Meu nome é {self.nome}, tenho o carro {self.carro} do ano {self.ano} e do modelo {self.modelo}"

#criar objeto - onde eu coloco INPUT
c1 = Carro (input("Nome: "), input("Carro: "), input("Ano: "), input("Modelo: "))

print(c1.apresentar())
# Apresentar a informação, vms usar o método criado
# chamar: função()

----

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  #criando método
  def calcular (self):
    return f"Para um retângulo de base {self.base} e altura {self.altura}, terei a área {(self.base * self.altura)} e o perímetro {(self.base * 2 + self.altura * 2)}"

r1 = Retangulo (float(input("Base: ")), float(input("Altura: ")))
print(r1.calcular())


-----

***ESTRUTURAÇÃO DE REPETIÇÃO FOR****

class Pessoa: 
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

# #Criando objeto com o código acima (somente, não é aplicável para os códigos a seguir)
# p1 = Pessoa ("Ana", 35)
# print(p1.apresentar())

#Criando lista de objetos. 
# Criar variavel pessoas para a lista
pessoas = [
    Pessoa("Laura", 25),
    Pessoa("Roberto", 26),
    Pessoa("Ana", 20)
    ]

#Usar estrutura de repetição no formato lista
# Para cada p, chamar a função apresentar (estrutura do texto)
for p in pessoas:
  print(p.apresentar())

-----

class Imc:
  def __init__(self, nome, peso, altura):
    self.nome = nome
    self.peso = peso
    self.altura = altura

  #Criar método
  def apresentar(self):
    return f"Meu nome é {self.nome}, peso {self.peso} e altura(metros) {self.altura}. Logo, eu tenho o IMC de {self.peso/self.altura**2} "

#Criando objeto - onde coloco input
# pessoa = Imc(input("Nome: "), float(input("Peso: ")), float(input("Altura: ")))

pessoa = [
    Imc(input("Nome:"), float(input("Peso: ")), float(input("Altura: "))),
    Imc(input("Nome:"), float(input("Peso: ")), float(input("Altura: "))),
    Imc(input("Nome:"), float(input("Peso: ")), float(input("Altura: "))),
    Imc(input("Nome:"), float(input("Peso: ")), float(input("Altura: "))),
    Imc(input("Nome:"), float(input("Peso: ")), float(input("Altura: ")))
]


#Criando lista, chamando a class do meu objeto QUANDO JÁ TENHO OS DADOS
# pessoa = [
#     Imc("Laura", 60, 1.50 ),
#     Imc("Roberto", 90, 1.70),
#     Imc("Ana", 64, 1.61),
#     Imc("Raul", 64, 1.65),
#     Imc("Maria", 80, 1.60)
#     ]


# Para cada p, chamar a função apresentar (estrutura do texto)
for p in pessoa:
  print(p.apresentar())