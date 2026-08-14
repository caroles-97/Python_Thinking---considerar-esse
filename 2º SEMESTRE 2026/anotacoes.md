****For - estrutura de repetição*** 

1º SEMESTRE 2026 : FOR, LISTAS [], APPEND. 

lista_nomes = []  - criando variavel lista "nomes" para armazenar cada variável. Criado lista para armazenar.
lista_idades = []
lista_sexo = []


Estrutura de repetição para solicitar esses dados 2x:

for i in range (2):    - REPETIÇÃO
    print(f"\nDados da {i+1}ª pessoa:")   ---SAÍDA
    nome = input("Digite o nome: ")   -------- ENTRADA (INPUT)
    lista_nomes.append(nome) ----- por meio do append. o NOME vai ser enviado para a lista NOMES

    IDADE = int(input("Digite sua idade: "))   -------- ENTRADA (INPUT)
    lista_idades.append(idade)

    sexo = input("Digite M para masculino e F para feminino: ")   -------- ENTRADA (INPUT)
    lista_sexo.append(sexo)  ---------- append. ARMAZENA NA LISTA    
print(lista_nomes)
print(lista_idades)
print(lista_sexo)

LISTA COM SUBLISTA COM TODAS AS INFORMAÇÕES DO USUÁRIO: 

****==================BASICAMENTE O PYTHON TEM 4 ESTRUTURAS: ====================****
- LISTA []
- TUPLA ()
- DICIONÁRIO {}
- **PANDAS (TABELAS)**

=========*** WHILE, APPEND E LISTA DENTRO DE LISTA ***===========  
*****************SITE PYTHON TUTOR depura a lógica do código ******************

dados = [[],[],[]]    -variavel chamada dados que tem uma LISTONA que tem sublistas vazias
contador = 0   **para limitar a quantidade de vezes que eu solicito ao usuario. Iniciarei como zero e vou repetir até a regra do while, ou seja, zero (1ª vez) e um (2ª vez repetição)**

while contador <2 :   ----- CONTADOR MENOR QUE 2
    print (f"\n Dados da (contador +1)ª pessoa:" )

    nome = input ("Digite o nome:")
    dados[0].append(nome)   ---- quando estamos colocando [0], estamos pegando o 1º valor do dados

    idade = int (input("Digite a idade:"))
    dados[1].append(idade) ---- estamos mandando o dado para a lista de dados no índice 1

    sexo=input("Digite o sexo da pessoa (M/F):").lower()
    dados[2].append(sexo)  ---- estamos mandando o dado para a lista de dados no índice 2

    contador += 1 ------------------limitando a quantidade de vezes que vamos executar

print (dados)


................................................

*Crie um algoritmo para solicitar:* 1 - marca de carro, 2-  versão do carro, 3- ano, 4 - cor, 5-IPVA pago. Solicite 4 dados para cada item. Deixa cada informação em uma sublista. 

Utiliza while ou for para solicitar as informações repetidas. 

**Abordagem 1 - resposta fica fragmentada**
lista = [[], [], [], [], []]    -- crio 5 sublistas para as informações
contador = 0 

while contador <=3 :     -- contando o 0 como nº inicial, vou ir até o número 3
    print (f"\n Dados do seu (contador +  1)º carro:")

    marca = input ("Digite a marca do seu carro:")
    versao = int (input("Digite a versão do carro:"))
    ano = int (input("Digite o ano do carro:"))
    cor = input ("Digite a cor do carro:")
    ipva = input ("IPVA foi pago? (S/N):")
    

    lista[0].append(marca) --- armazenar a marca na listona
    lista[1].append(versao)    ---- armazena a versão na listona
    lista[2].append(ano)    ----- armazena o ano do carro na listona
    lista[3].append(cor)    ---- armazena a cor na listona
    lista[4].append(ipva)   ---- armazena o ipva na listona

    contador += 1

print(lista)

**Abordagem 2 - com esse cód a resposta fica numa única sublista - gostei mais**
lista = [[], [], [], [], []]    -- crio 5 sublistas para as informações
contador = 0 

while contador < 4:     -- contando o 0 como nº inicial, vou ir até o número 3
    print (f"\n Dados do seu (contador +  1)º carro:")

    marca = input ("Digite a marca do seu carro:")
    versao = int (input("Digite a versão do carro:"))
    ano = int (input("Digite o ano do carro:"))
    cor = input ("Digite a cor do carro:")
    ipva = input ("IPVA foi pago? (S/N):")
    
    dados = [marca, versao, ano, cor, ipva]
    lista.append(dados)
    contador += 1

print(lista)

**DIFERENÇA ENTRE [] E (): as listas são mutáveis (você pode alterar, adicionar ou remover itens), enquanto as tuplas são imutáveis (não podem ser modificadas após a criação). Além disso, as listas usam colchetes [] e as tuplas usam parênteses ()**


*****DICIONÁRIO {} ou dict ***

**Contém várias informações dentro da variável. Ele é mais inteligente que a lista, tupla.*
*Contem uma chave que assemelha ao nome da coluna no excel. COLUNA = Chave.*
Os itens de cada chave podem ser: 
                Em lista []
                Em tupla ()
                Em dicionário {}

Exemplo 1: 

dicionario = { 
    'time': ['A', 'B', 'C'],
    'vitorias': ['10', '12', '8'],
    'Estado': ['RJ', 'CE', 'SP'],}
print (dicionario)

import pandas as pd
dados = pd.DataFrame(dicionario)  *#   . vai entrar uma função*
dado

Exemplo 2:
produto = dict(nome="Notebook", preco=300)
print(produto["nome"])

Exemplo 3:
cliente = {}
cliente['nome'] = input ('Nome:')
cliente['idade] = input ('Idade:')
print(f"Nome: {cliente['nome']}")

*Para corrigir o dado já registrado da idade dentro do dicionario:*
cliente['idade'] = 37 #aqui vai a idade
cliente.update({'tel': '56554'})  # *.update - adicionando nova variável*
print(cliente)

***PARA DELETAR VARIÁVEL NO DICIONÁRIO - del  ou  pop**
del *nome do dicionario com sua chave*

del cliente['idade']
print(cliente)

***Função útil em programação dinâmica - POP**
pop: retira deleta de forma inteligente as variáveis da lista.

**DICIONARIO e IF**  if nomedodicionario ["variaveldodicionario"]

*DICIONARIO E ESTRUTURA DE REPETIÇÃO (FOR, WHILE) - ESTRUTURA DO DICT: {CHAVE:VALOR, CHAVE:VALOR}*

estoque = {"maça": 10, "banana": 5, "laranja": 8}

for fruta in estoque:       # compreende somente as variáveis dentro das "", é diferente da lista []
    print(fruta)

OU

for fruta, qtd in estoque.items():      # qtd será para o VALOR
    print(f"(fruta): (qt) unidades")


OU 

*DICIONÁRIO ANINHADO (FOR DUPLO) - ESTRUTURA DE REPETIÇÃO DENTRO DE REPETIÇÃO*

alunos = {
    "Ana": {"n1": 8, "n2": 7},   # ÍNDICE 0
    "Bruno": {"n1": 5, "n2": 6}     # índice 1
}

for nome, notas in alunos.items():      # ele compreende o nome como CHAVE e notas como VALOR
    for prova, valor in notas.items():      #em ambos precisa usar a função .items()
        print(nome, prova, valor)


*for enumerated items*
for i, (nome, notas) in enumerate(alunos.items()):
    print (i, nome, notas)  # i de índice (se é zero, um etc), nome

*DICT E WHILE*

carrinho = {}   #DICT está vazio. Nome do DICT: carrinho
produto = ""    # Nome da chave:: produto

while produto != "sair":
    produto = input("Produto: ")
    if produto == "sair":
        break
    preco = float(input("Preço: "))
    carrinho[produto] = preco

print (carrinho)

