# PARA DEIXAR AS INFORMAÇÕES = [[A,22.M],[B,40,F]]
lista_completa = []  #criando um armário para armazenar

for K in range (2):    #Repetir 2x
    nome = input("Digite o seu nome: ")  #entrada
    idade = int(input("Digite sua idade: ")) #entrada
    sexo = input("Digite M para masculino e F para feminino: ")   #entrada

    lista = [nome, idade, sexo] # criei um armário-filho (sublista) que tem as 3 informações da entrada
    lista_completa.append(lista) # Criado armário-pai (LISTA / LISTA COMPLETA) com os armários-filhos
    #APPEND. QUEM CONECTA PARA LISTA_COMPLETA

print (lista_completa) #mostrar o armário-pai


