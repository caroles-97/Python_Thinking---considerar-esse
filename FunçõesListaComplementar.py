#Exercício 2 da aula 22: Nº natural é triangular se ele é produto de três números naturais consecutivos. Ex: 120 é triangular pois 4 * 5 * 6 =120. Fazer uma função que receba um número inteiro e retorne True se for um nº triangular e False, caso contrário. 

#Vamos definir uma função como triangular que vai receber um número
def triangular (numero):
    #Criar variável contador
    cont = 1

    while True:
        #Fazendo a verificação
        if cont*(cont+1)*(cont+2) == numero:
            return True

        elif cont*(cont+1)*(cont+2) > numero:
            return False
        cont += 1
#Main
N = int(input("Informe um número para verificar se é triangular: "))

#Ele só entra no if se a condição for verdade. Se o resultado disso for verdadeiro, será:
if triangular (N):
    print(f"O número {N} é triangular.")

#se não
else:
    print(f"O número {N} NÃO É triangular.")


##################################################################


#Exercício 3 - aula 22: Jogo de dados que pode ser sorteado qualquer número entre 1 a 6. Fazer função que simule 1 milhão de lançamentos de dados e mostre quantas vezes cada número foi sorteado

#Vamos mexer com nº aleatórios, logo precisamos importar uma biblioteca e iniciar função.

import random

def dados ():
    #Trabalharemos com lista chamada 'dado' em posição 0 vai receber a quantidade de nºx que cair. Logo vamos iniciar a lista na posição 0
    dado = [0,0,0,0,0,0]

    #Dado vai rodar 1 milhão de vezes:
    for i in range (1000000):
        #Aqui gerei nº randomico de 1 a 6:
        x = random.randint (1, 6)
        match x:
            case 1:
                dado [x - 1] += 1
            case 2:
                dado[x - 1] += 1
            case 3:
                dado[x - 1] += 1
            case 4:
                dado[x - 1] += 1
            case 5:
                dado[x - 1] += 1
            case 6:
                dado[x - 1] += 1
    return dado

#Main - aqui vamos chamar a função dados (dentro da função já vai ter gerada a lista)

dado = dados()
for i in range (len(dado)):
    print(f"O número {i+1} apareceu {dado[i]} vezes ")


###############################
### RESOLUÇÃO ARTHUR:
#Exercício 3 - aula 22: Jogo de dados que pode ser sorteado qualquer número entre 1 a 6. Fazer função que simule X de lançamentos de dados e mostre quantas vezes cada número foi sorteado

#Vamos mexer com nº aleatórios, logo precisamos importar uma biblioteca e iniciar função.

import random

def dados (num):
    #Trabalharemos com lista chamada 'dado' em posição 0 vai receber a quantidade de nºx que cair. Logo vamos iniciar a lista na posição 0
    dado = [0,0,0,0,0,0]

    #Dado vai rodar quantas vezes o usuário quiser:
    for i in range (num):
        #Aqui gerei nº randomico de 1 a 6:
        x = random.randint (1, 6)

        dado [x - 1] += 1

    for i in range(len(dado)):
       print(f"O número {i + 1} apareceu {dado[i]} vezes ")


#Main - aqui vamos chamar a função dados (dentro da função já vai ter gerada a lista)

n = int(input('Digite um número'))
dados(n)

