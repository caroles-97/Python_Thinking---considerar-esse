#CAROLINA KIYOMI HADA - RM 571664

#DIFICULDADES: EXERCICIO 3: TRAVEI EM GERAR NOVA LISTA COM OS NUMEROS PRIMOS. EXERCICIO 4:TRAVEI AO ESCREVER A MULTIPLICAÇÃO COM A LISTA. EXERCICIO 5: GERAR TERCEIRA LISTA E COLOCAR OS VALORES INTERCALADOS DAS 2 OUTRAS LISTAS.

# 1. Preencha uma lista com 10 numeros aleatorios unicos (sorteados de 1 a 20), ou seja, sem elementos repetidos.
# Para embaralhar 'shuffle()', precisamos importar a bibilioteca 'random'. Para sortear os elementos, usamos o metodo 'choice'

import random #importa a biblioteca random para gerar numeros aleatorios

lista=[] #criei lista zerada
for i in range(10): #repetir 10x
    n=random.randint(1,20)  #- gera um numero aleatorio entre 1 e 20
    while n in lista:  # VERIFICA se o numero ja esta na lista, se estiver, gera outro numero
        n=random.randint(1,20) #- gera um NOVO numero aleatorio entre 1 e 20
    lista.append(n) #adicionar o numero sorteado na lista/ ARMAZENAR O NUMERO SORTEADO NA LISTA
# Exibir lista com todos os itens armazenados
print(f" Os 10 números aleatórios sorteados entre 1 a 20 são: {lista}")

OU

import random #importa a biblioteca random para gerar numeros aleatorios
lista = random.sample(range(1, 21), 10) #gera uma lista com 10 numeros aleatorios unicos entre 1 e 20
print(f" Os 10 números aleatórios sorteados entre 1 a 20 são: {lista}")

#2 Preencha uma lista com 30 numeros aleatorios (sorteados de 1 a 50). A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista. 

import random #importa a biblioteca random para gerar numeros aleatorios
lista = random.randint(range(1,51), 30) #gera uma lista com 30 numeros aleatorios entre 1 e 50

# ?????????????????????????????????????????????????????????????????  DIFICULDADE: TRAVEI PARA GERAR NOVA LISTA COM OS NUMEROS PRIMOS.

#3 Preencha uma lista com 30 numeros aleatorios (sorteados de 1 a 50). A seguir solicite um numero inteiro e multiplique todos os itens da lista por esse numero. 

import random #importa a biblioteca random para gerar numeros aleatorios

lista = []

for i in range(30):
    num = random.randint(1,50)
    lista.append(num)       

#gera uma lista com 30 numeros aleatorios entre 1 e 50

n=int(input("Digite um nº inteiro: "))

lista2 = [] #criamos nova lista para multiplicar com o nº informado

for i in range(len(lista)):
    num = lista[i]*n
    lista2.append(num)

print(f"Estes são os números sorteados de 1 a 50: {lista}")
print(f"Estes são os números multiplicados pelo valor informado: {lista2}")



# 4 Preencha uma lista com 10 itens e verifique se ela é um palíndrono, ou seja, se ela é igual quando lida da esquerda para a direita e da direita para a esquerda. 
# Lista P = lista do palindromo

P = []

for i in range (5):
    N = int(input("Informe um valor inteiro:"))

    # Vamos criar uma posição de memória na última posição da lista
    P.append(N)


print (P)

isPallindrome = True

for left in range (int(len(P) / 2)):
    right = len(P)-1-left
    if P [right] != P [left]:
        isPallindrome = False
        break

if isPallindrome:
    print ("Palindromo")





