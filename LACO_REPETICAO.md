cont = 1

# Enquanto "cont" for maior ou igual a 10
while cont <= 10: 
    print (cont)
    cont += 1    #cont == cont +1

print ("Fim")
_____________________________________

Exercício: solicitar para o usuário um nº e imprimiremos uma tabuada

print ("Esta é a tabuada do número: \n")

n = int (input("Informe um número para ver a tabuada: "))

cont = 0
while cont <= 10: 
    print (f" {n} * {cont} = {n*cont}")
    cont += 1 

print("FIM")
_________________________________________

Exercício: escreva um algoritmo que solicite 15 números e informe o somatório de todos os números ímpares digitados. 

cont = 1

while cont <= 15: 

    N = int (input (f"Informe o {cont}º número: "))
    if N%2 != 0:
    # se o resto da divisão de N por 2 for diferente de 0.
        total += N

    cont += 1
print (f" A soma de todos os ímpares é {total} .")
____________________________________________________

Exercício: solicite vários números ao usuário (até que ele digite o número zero) e informe o somatório dos números digitados.

A condição para sair do laço de repetição é quando o N == 0, portanto: 

N = -1 
total = 0
cont = 1

while N != 0:
    N = int (input (f"Informe o {cont}º número: "))

    total += N
    cont += 1

print (f"A soma de tdos os números é {total} .")



